"""Comprehensive environment and dependency verification engine."""

from __future__ import annotations

import importlib
import json
import os
import platform
import shutil
import sys
import time
from datetime import UTC, datetime
from pathlib import Path

from dwex_groundwater.config.loader import load_config
from dwex_groundwater.environment.models import CheckResult, CheckStatus
from dwex_groundwater.logging.logger import get_logger
from dwex_groundwater.modflow.executable import ModflowExecutable

logger = get_logger("environment.checker")


class EnvironmentChecker:
    """Verifies all Phase 0 technical requirements, packages, configuration, and tools."""

    def __init__(self, project_root: Path | None = None) -> None:
        self.project_root = (
            project_root or Path(__file__).resolve().parent.parent.parent.parent
        ).resolve()
        self.results: list[CheckResult] = []

    def check_python(self) -> CheckResult:
        """Check Python version and 64-bit runtime architecture."""
        t0 = time.perf_counter()
        version_info = sys.version_info
        is_compatible = version_info.major == 3 and version_info.minor >= 11
        is_64bit = sys.maxsize > 2**32
        arch = platform.architecture()[0]

        details = {
            "version": platform.python_version(),
            "executable": sys.executable,
            "architecture": arch,
            "is_64bit": is_64bit,
        }

        if is_compatible and is_64bit:
            status = CheckStatus.PASS
            msg = f"Python {platform.python_version()} ({arch})"
        elif not is_compatible:
            status = CheckStatus.FAIL
            msg = f"Incompatible Python version {platform.python_version()} (requires >= 3.11)"
        else:
            status = CheckStatus.WARN
            msg = f"Python {platform.python_version()} is not 64-bit ({arch})"

        duration = time.perf_counter() - t0
        res = CheckResult(
            name="Python Runtime",
            category="Runtime",
            status=status,
            message=msg,
            duration_seconds=duration,
            details=details,
        )
        self.results.append(res)
        return res

    def _check_package(
        self, package_name: str, import_name: str | None = None, category: str = "Packages"
    ) -> CheckResult:
        t0 = time.perf_counter()
        target_import = import_name or package_name
        try:
            mod = importlib.import_module(target_import)
            ver = getattr(mod, "__version__", "unknown")
            duration = time.perf_counter() - t0
            res = CheckResult(
                name=package_name,
                category=category,
                status=CheckStatus.PASS,
                message=f"{package_name} {ver}",
                duration_seconds=duration,
                details={"version": str(ver), "module_path": getattr(mod, "__file__", "")},
            )
        except ImportError as exc:
            duration = time.perf_counter() - t0
            res = CheckResult(
                name=package_name,
                category=category,
                status=CheckStatus.FAIL,
                message=f"Failed to import {package_name}: {exc}",
                duration_seconds=duration,
                details={"error": str(exc)},
            )
        self.results.append(res)
        return res

    def check_scientific_stack(self) -> list[CheckResult]:
        """Verify core scientific computing packages."""
        return [
            self._check_package("NumPy", "numpy", "Scientific Stack"),
            self._check_package("Pandas", "pandas", "Scientific Stack"),
            self._check_package("SciPy", "scipy", "Scientific Stack"),
        ]

    def check_modflow_stack(self) -> list[CheckResult]:
        """Verify FloPy library and MODFLOW 6 binary engine."""
        results = [self._check_package("FloPy", "flopy", "MODFLOW Stack")]

        t0 = time.perf_counter()
        mf_exe = ModflowExecutable()
        try:
            exe_path = mf_exe.resolve()
            version_str = mf_exe.get_version()
            duration = time.perf_counter() - t0
            res = CheckResult(
                name="MODFLOW 6 Executable",
                category="MODFLOW Stack",
                status=CheckStatus.PASS,
                message=f"{version_str} ({exe_path.name})",
                duration_seconds=duration,
                details={"path": str(exe_path), "version": version_str},
            )
        except Exception as exc:
            duration = time.perf_counter() - t0
            res = CheckResult(
                name="MODFLOW 6 Executable",
                category="MODFLOW Stack",
                status=CheckStatus.FAIL,
                message=f"mf6.exe not found or failed execution: {exc}",
                duration_seconds=duration,
                details={"error": str(exc)},
            )
        results.append(res)
        self.results.append(res)
        return results

    def check_gis_stack(self) -> list[CheckResult]:
        """Verify spatial and GIS packages."""
        return [
            self._check_package("GeoPandas", "geopandas", "GIS Stack"),
            self._check_package("Pyogrio", "pyogrio", "GIS Stack"),
            self._check_package("Shapely", "shapely", "GIS Stack"),
            self._check_package("PyProj", "pyproj", "GIS Stack"),
            self._check_package("Rasterio", "rasterio", "GIS Stack"),
        ]

    def check_visualization_stack(self) -> list[CheckResult]:
        """Verify charting, mapping, and 3D visualization libraries."""
        return [
            self._check_package("Matplotlib", "matplotlib", "Visualization"),
            self._check_package("Plotly", "plotly", "Visualization"),
            self._check_package("PyVista", "pyvista", "Visualization"),
        ]

    def check_document_stack(self) -> list[CheckResult]:
        """Verify document and raw data extraction packages."""
        return [
            self._check_package("openpyxl", "openpyxl", "Document Stack"),
            self._check_package("python-docx", "docx", "Document Stack"),
            self._check_package("pypdf", "pypdf", "Document Stack"),
        ]

    def check_validation_and_config(self) -> list[CheckResult]:
        """Verify Pydantic, PyYAML, and project configuration integrity."""
        results = [
            self._check_package("Pydantic", "pydantic", "Configuration"),
            self._check_package("PyYAML", "yaml", "Configuration"),
        ]

        t0 = time.perf_counter()
        try:
            config = load_config(self.project_root)
            exe_path = config.get_resolved_modflow_executable()
            duration = time.perf_counter() - t0
            res = CheckResult(
                name="Project Configuration",
                category="Configuration",
                status=CheckStatus.PASS,
                message="Loaded paths.yaml, model_config.yaml, and validation_rules.yaml",
                duration_seconds=duration,
                details={
                    "project_name": config.project.name,
                    "resolved_mf6": str(exe_path),
                    "raw_data_dir": str(config.paths.raw_data),
                },
            )
        except Exception as exc:
            duration = time.perf_counter() - t0
            res = CheckResult(
                name="Project Configuration",
                category="Configuration",
                status=CheckStatus.FAIL,
                message=f"Configuration error: {exc}",
                duration_seconds=duration,
                details={"error": str(exc)},
            )
        results.append(res)
        self.results.append(res)
        return results

    def check_filesystem_and_directories(self) -> CheckResult:
        """Verify presence and writeability of all designated directory paths."""
        t0 = time.perf_counter()
        required_dirs = [
            self.project_root / "data" / "raw",
            self.project_root / "data" / "processed",
            self.project_root / "data" / "validated",
            self.project_root / "model" / "input",
            self.project_root / "model" / "output",
            self.project_root / "model" / "calibration",
            self.project_root / "model" / "scenarios",
            self.project_root / "outputs" / "maps",
            self.project_root / "outputs" / "graphs",
            self.project_root / "outputs" / "3d",
            self.project_root / "outputs" / "qa_qc",
            self.project_root / "reports",
            self.project_root / "logs",
            self.project_root / "tools" / "modflow6",
        ]

        missing = []
        not_writable = []
        for d in required_dirs:
            if not d.is_dir():
                missing.append(str(d.relative_to(self.project_root)))
            elif not os.access(d, os.W_OK):
                not_writable.append(str(d.relative_to(self.project_root)))

        duration = time.perf_counter() - t0
        if not missing and not not_writable:
            res = CheckResult(
                name="Filesystem Directories",
                category="Filesystem",
                status=CheckStatus.PASS,
                message=f"All {len(required_dirs)} required directories present and writable",
                duration_seconds=duration,
            )
        else:
            res = CheckResult(
                name="Filesystem Directories",
                category="Filesystem",
                status=CheckStatus.FAIL,
                message=f"Missing: {missing} | Not writable: {not_writable}",
                duration_seconds=duration,
                details={"missing": missing, "not_writable": not_writable},
            )
        self.results.append(res)
        return res

    def check_dev_tools(self) -> list[CheckResult]:
        """Verify Ruff and Mypy development utilities."""
        results = []
        for tool in ["ruff", "mypy", "pytest"]:
            t0 = time.perf_counter()
            found = shutil.which(tool) is not None
            # Also check if installed in current python virtualenv scripts
            venv_script = self.project_root / ".venv" / "Scripts" / f"{tool}.exe"
            if venv_script.is_file():
                found = True
            duration = time.perf_counter() - t0

            if found:
                res = CheckResult(
                    name=tool,
                    category="Development Tools",
                    status=CheckStatus.PASS,
                    message=f"{tool} executable available",
                    duration_seconds=duration,
                )
            else:
                res = CheckResult(
                    name=tool,
                    category="Development Tools",
                    status=CheckStatus.WARN,
                    message=f"{tool} executable not in PATH",
                    duration_seconds=duration,
                )
            results.append(res)
            self.results.append(res)
        return results

    def run_all(self) -> list[CheckResult]:
        """Execute all environment verification checks."""
        self.results.clear()
        self.check_python()
        self.check_scientific_stack()
        self.check_modflow_stack()
        self.check_gis_stack()
        self.check_visualization_stack()
        self.check_document_stack()
        self.check_validation_and_config()
        self.check_filesystem_and_directories()
        self.check_dev_tools()
        return self.results

    def is_ready(self) -> bool:
        """Return True if no checks resulted in FAIL."""
        return all(r.status != CheckStatus.FAIL for r in self.results)

    def generate_manifest(self, output_path: Path | None = None) -> dict:
        """Export machine-readable environment manifest."""
        manifest_file = output_path or (self.project_root / "config" / "environment_manifest.json")

        mf_exe = ModflowExecutable()
        mf_version = mf_exe.get_version() if mf_exe.is_available() else "Not Found"
        mf_path = str(mf_exe.resolve()) if mf_exe.is_available() else None

        manifest = {
            "timestamp_utc": datetime.now(UTC).isoformat(),
            "environment_status": "READY" if self.is_ready() else "NOT READY",
            "system": {
                "os": platform.system(),
                "os_release": platform.release(),
                "os_version": platform.version(),
                "architecture": platform.architecture()[0],
                "processor": platform.processor(),
                "python_version": platform.python_version(),
                "python_executable": sys.executable,
            },
            "modflow": {
                "executable_path": mf_path,
                "version": mf_version,
            },
            "checks": [
                {
                    "name": r.name,
                    "category": r.category,
                    "status": r.status.value,
                    "message": r.message,
                    "duration_seconds": round(r.duration_seconds, 4),
                    "details": r.details,
                }
                for r in self.results
            ],
        }

        manifest_file.parent.mkdir(parents=True, exist_ok=True)
        with open(manifest_file, "w", encoding="utf-8") as f:
            json.dump(manifest, f, indent=2)

        return manifest

    def format_report(self) -> str:
        """Render formatted terminal verification report."""
        lines = [
            "=" * 64,
            "DWEX AI GROUNDWATER MODELLING - ENVIRONMENT VERIFICATION",
            "=" * 64,
        ]

        current_cat = None
        for r in self.results:
            if r.category != current_cat:
                current_cat = r.category
                lines.append(f"\n{current_cat}:")
            lines.append(f"  [{r.status.value:4}] {r.name:<26} {r.message}")

        lines.append("\n" + "-" * 64)
        if self.is_ready():
            lines.append("ENVIRONMENT STATUS: READY")
        else:
            lines.append("ENVIRONMENT STATUS: NOT READY (Action required)")
        lines.append("-" * 64)

        return "\n".join(lines)
