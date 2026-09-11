"""Unit tests for environment verification engine."""

from __future__ import annotations

from pathlib import Path

from dwex_groundwater.environment.checker import EnvironmentChecker
from dwex_groundwater.environment.models import CheckStatus


def test_environment_checker_python(project_root: Path) -> None:
    """Verify python runtime checker produces PASS on supported interpreter."""
    checker = EnvironmentChecker(project_root)
    res = checker.check_python()
    assert res.status == CheckStatus.PASS
    assert "Python" in res.message


def test_environment_checker_packages(project_root: Path) -> None:
    """Verify package checkers detect installed scientific and modflow libraries."""
    checker = EnvironmentChecker(project_root)
    sci_results = checker.check_scientific_stack()
    assert len(sci_results) == 3
    assert all(r.status == CheckStatus.PASS for r in sci_results)

    modflow_results = checker.check_modflow_stack()
    assert len(modflow_results) == 2
    assert all(r.status == CheckStatus.PASS for r in modflow_results)


def test_environment_checker_filesystem(project_root: Path) -> None:
    """Verify all designated directory paths pass verification."""
    checker = EnvironmentChecker(project_root)
    res = checker.check_filesystem_and_directories()
    assert res.status == CheckStatus.PASS


def test_environment_checker_full_run_and_manifest(
    project_root: Path, temp_workspace: Path
) -> None:
    """Verify full environment audit run and manifest export."""
    checker = EnvironmentChecker(project_root)
    results = checker.run_all()
    assert len(results) > 10
    assert checker.is_ready() is True

    manifest_file = temp_workspace / "test_manifest.json"
    manifest = checker.generate_manifest(manifest_file)
    assert manifest["environment_status"] == "READY"
    assert manifest_file.is_file()
