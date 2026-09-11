#!/usr/bin/env python
"""Environment verification CLI script for DWEX Groundwater Modelling platform.

Executes all Phase 0 technical checks, package audits, filesystem permissions,
MODFLOW 6 binary responsiveness, and produces a structured manifest.
"""

from __future__ import annotations

import sys
from pathlib import Path

# Ensure src is in python path
project_root = Path(__file__).resolve().parent.parent
src_dir = project_root / "src"
if str(src_dir) not in sys.path:
    sys.path.insert(0, str(src_dir))

from dwex_groundwater.environment.checker import EnvironmentChecker
from dwex_groundwater.logging.logger import setup_logger


def main() -> int:
    """Main verification CLI entry point."""
    setup_logger(name="dwex", log_file="environment_verification.log")
    checker = EnvironmentChecker(project_root=project_root)
    checker.run_all()

    report = checker.format_report()
    print(report)

    checker.generate_manifest()
    manifest_path = project_root / "config" / "environment_manifest.json"
    print(f"\nEnvironment manifest saved to: {manifest_path}")

    return 0 if checker.is_ready() else 1


if __name__ == "__main__":
    sys.exit(main())
