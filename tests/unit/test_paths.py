"""Unit tests for path management and resolution."""

from __future__ import annotations

from pathlib import Path

from dwex_groundwater.config.settings import PathsSettings


def test_paths_relative_resolution(project_root: Path) -> None:
    """Verify relative paths resolve properly to absolute paths under project root."""
    paths = PathsSettings()
    resolved = paths.resolve_paths(project_root)

    assert resolved.raw_data.is_absolute()
    assert resolved.raw_data == project_root / "data" / "raw"
    assert resolved.processed_data == project_root / "data" / "processed"
    assert resolved.model_output == project_root / "model" / "output"
    assert resolved.tools_modflow6 == project_root / "tools" / "modflow6"


def test_paths_preserve_existing_absolute_paths(project_root: Path, temp_workspace: Path) -> None:
    """Verify pre-existing absolute paths are untouched during resolution."""
    custom_abs = temp_workspace / "custom_raw"
    paths = PathsSettings(raw_data=custom_abs)
    resolved = paths.resolve_paths(project_root)

    assert resolved.raw_data == custom_abs.resolve()
