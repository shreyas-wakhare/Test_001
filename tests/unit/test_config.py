"""Unit tests for configuration system and loader."""

from __future__ import annotations

from pathlib import Path

import pytest

from dwex_groundwater.config.loader import ConfigurationLoader, find_project_root
from dwex_groundwater.config.settings import DWEXConfig
from dwex_groundwater.exceptions.domain import ConfigurationError, ConfigurationValidationError


def test_find_project_root(project_root: Path) -> None:
    """Verify project root discovery via pyproject.toml."""
    found = find_project_root(project_root / "src" / "dwex_groundwater")
    assert found == project_root


def test_load_default_config(test_config: DWEXConfig, project_root: Path) -> None:
    """Verify default configuration values and type constraints."""
    assert test_config.application.name == "DWEX AI Groundwater Modelling System"
    assert test_config.application.environment == "development"
    assert test_config.modflow.timeout_seconds >= 10
    assert test_config.project_root == project_root
    assert test_config.paths.raw_data.is_absolute()
    assert test_config.paths.raw_data == project_root / "data" / "raw"
    assert test_config.qa_qc.fail_on_missing_critical_data is True


def test_environment_variable_override(project_root: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    """Verify environment variables safely override file configuration."""
    monkeypatch.setenv("DWEX_ENVIRONMENT", "production")
    monkeypatch.setenv("DWEX_MODFLOW_EXECUTABLE", "custom/bin/mf6.exe")

    loader = ConfigurationLoader(project_root)
    cfg = loader.load()

    assert cfg.application.environment == "production"
    assert cfg.modflow.executable == "custom/bin/mf6.exe"


def test_missing_config_directory_uses_defaults(temp_workspace: Path) -> None:
    """Verify loading from an empty directory falls back to valid schema defaults."""
    loader = ConfigurationLoader(temp_workspace)
    cfg = loader.load(config_dir=temp_workspace)
    assert isinstance(cfg, DWEXConfig)
    assert cfg.application.environment == "development"


def test_invalid_yaml_raises_configuration_error(temp_workspace: Path) -> None:
    """Verify malformed YAML raises ConfigurationError."""
    bad_yaml = temp_workspace / "model_config.yaml"
    bad_yaml.write_text("application: [unclosed list", encoding="utf-8")

    loader = ConfigurationLoader(temp_workspace)
    with pytest.raises(ConfigurationError):
        loader.load(config_dir=temp_workspace)


def test_invalid_modflow_timeout_raises_validation_error(temp_workspace: Path) -> None:
    """Verify out-of-range timeout triggers Pydantic validation failure."""
    invalid_yaml = temp_workspace / "model_config.yaml"
    invalid_yaml.write_text("modflow:\n  timeout_seconds: 2\n", encoding="utf-8")

    loader = ConfigurationLoader(temp_workspace)
    with pytest.raises(ConfigurationValidationError):
        loader.load(config_dir=temp_workspace)
