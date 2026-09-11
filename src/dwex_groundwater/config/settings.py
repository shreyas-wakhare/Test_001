"""Pydantic configuration models for DWEX Groundwater Modelling platform."""

from __future__ import annotations

from pathlib import Path
from typing import Any

from pydantic import BaseModel, Field, field_validator


class ApplicationSettings(BaseModel):
    """Application metadata and runtime mode."""

    name: str = Field(default="DWEX AI Groundwater Modelling System")
    environment: str = Field(default="development")
    version: str = Field(default="0.1.0")


class ModflowSettings(BaseModel):
    """MODFLOW 6 engine settings."""

    executable: str = Field(default="tools/modflow6/mf6.exe")
    timeout_seconds: int = Field(default=300, ge=10)
    double_precision: bool = Field(default=True)
    verbose: bool = Field(default=True)

    @field_validator("executable")
    @classmethod
    def validate_executable_name(cls, v: str) -> str:
        if not v or not v.strip():
            raise ValueError("MODFLOW executable path cannot be empty")
        return v.strip()


class ProjectSettings(BaseModel):
    """Groundwater modeling project domain settings."""

    name: str = Field(default="DWEX Synthetic Baseline Model")
    length_unit: str = Field(default="meters")
    time_unit: str = Field(default="days")
    coordinate_reference_system: str | None = Field(
        default=None,
        description="EPSG code or WKT. None until project data defines CRS.",
    )


class PathsSettings(BaseModel):
    """Directory paths for the groundwater modeling platform."""

    raw_data: Path = Field(default=Path("data/raw"))
    processed_data: Path = Field(default=Path("data/processed"))
    validated_data: Path = Field(default=Path("data/validated"))
    model_input: Path = Field(default=Path("model/input"))
    model_output: Path = Field(default=Path("model/output"))
    model_calibration: Path = Field(default=Path("model/calibration"))
    model_scenarios: Path = Field(default=Path("model/scenarios"))
    reports: Path = Field(default=Path("reports"))
    logs: Path = Field(default=Path("logs"))
    maps: Path = Field(default=Path("outputs/maps"))
    graphs: Path = Field(default=Path("outputs/graphs"))
    viz_3d: Path = Field(default=Path("outputs/3d"))
    qa_qc: Path = Field(default=Path("outputs/qa_qc"))
    tools_modflow6: Path = Field(default=Path("tools/modflow6"))

    def resolve_paths(self, root: Path) -> PathsSettings:
        """Resolve all relative paths against the project root."""
        resolved: dict[str, Any] = {}
        for field_name in type(self).model_fields:
            val = getattr(self, field_name)
            if isinstance(val, Path):
                if not val.is_absolute():
                    resolved[field_name] = (root / val).resolve()
                else:
                    resolved[field_name] = val.resolve()
            else:
                resolved[field_name] = val
        return PathsSettings(**resolved)


class QaQcSettings(BaseModel):
    """Quality assurance and quality control thresholds."""

    fail_on_missing_critical_data: bool = Field(default=True)
    fail_on_crs_mismatch: bool = Field(default=True)
    fail_on_modflow_error: bool = Field(default=True)
    water_balance_tolerance_percent: float = Field(default=0.1, ge=0.0, le=5.0)
    max_solver_head_change: float = Field(default=1e-4, gt=0.0)


class DWEXConfig(BaseModel):
    """Complete, unified configuration container for DWEX platform."""

    project_root: Path
    application: ApplicationSettings = Field(default_factory=ApplicationSettings)
    modflow: ModflowSettings = Field(default_factory=ModflowSettings)
    project: ProjectSettings = Field(default_factory=ProjectSettings)
    paths: PathsSettings = Field(default_factory=PathsSettings)
    qa_qc: QaQcSettings = Field(default_factory=QaQcSettings)

    def get_resolved_modflow_executable(self) -> Path:
        """Return the resolved absolute path to mf6.exe."""
        raw_exe = Path(self.modflow.executable)
        if raw_exe.is_absolute():
            return raw_exe
        return (self.project_root / raw_exe).resolve()
