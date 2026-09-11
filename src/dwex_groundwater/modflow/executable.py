"""MODFLOW 6 executable discovery, validation, and metadata inspection."""

from __future__ import annotations

import os
import shutil
import subprocess
from pathlib import Path

from dwex_groundwater.exceptions.domain import ModflowNotFoundError
from dwex_groundwater.logging.logger import get_logger

logger = get_logger("modflow.executable")


class ModflowExecutable:
    """Manages discovery, verification, and execution querying of the mf6 binary."""

    def __init__(self, explicit_path: Path | str | None = None) -> None:
        self.explicit_path = Path(explicit_path) if explicit_path else None
        self._resolved_path: Path | None = None
        self._version: str | None = None

    def resolve(self) -> Path:
        """Resolve the path to the mf6 binary or raise ModflowNotFoundError."""
        if self._resolved_path and self._resolved_path.is_file():
            return self._resolved_path

        candidates: list[Path] = []

        # 1. Explicit path passed in constructor
        if self.explicit_path:
            candidates.append(self.explicit_path.resolve())
        else:
            # 2. Environment variable
            env_exe = os.getenv("DWEX_MODFLOW_EXECUTABLE")
            if env_exe:
                candidates.append(Path(env_exe).resolve())

            # 3. Project-local tools/modflow6/mf6.exe
            project_root = Path(__file__).resolve().parent.parent.parent.parent
            candidates.append((project_root / "tools" / "modflow6" / "mf6.exe").resolve())
            candidates.append((project_root / "tools" / "modflow6" / "mf6").resolve())

            # 4. System PATH
            which_mf6 = shutil.which("mf6")
            if which_mf6:
                candidates.append(Path(which_mf6).resolve())

        for candidate in candidates:
            if candidate.is_file() and os.access(candidate, os.X_OK):
                self._resolved_path = candidate
                logger.debug("Resolved MODFLOW 6 executable at %s", candidate)
                return candidate

        raise ModflowNotFoundError(
            "MODFLOW 6 executable (mf6.exe) could not be found or is not executable.",
            details={"searched_locations": [str(c) for c in candidates]},
        )

    def get_version(self) -> str:
        """Query mf6 executable for its version string."""
        if self._version:
            return self._version

        exe = self.resolve()
        try:
            result = subprocess.run(
                [str(exe), "-v"],
                capture_output=True,
                text=True,
                timeout=10,
                check=False,
            )
            stdout = result.stdout.strip()
            # Expecting string like "mf6.exe: 6.7.0 02/05/2026"
            lines = [line.strip() for line in stdout.splitlines() if line.strip()]
            self._version = lines[0] if lines else "Unknown MODFLOW 6"
            return self._version
        except Exception as exc:
            logger.warning("Could not obtain MODFLOW 6 version: %s", exc)
            return "MODFLOW 6 (version unknown)"

    def is_available(self) -> bool:
        """Check if MODFLOW 6 is available without raising an exception."""
        try:
            self.resolve()
            return True
        except ModflowNotFoundError:
            return False
