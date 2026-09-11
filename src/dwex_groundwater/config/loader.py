"""Configuration loader implementation supporting YAML cascading and environment overrides."""

from __future__ import annotations

import os
from pathlib import Path
from typing import Any

import yaml
from pydantic import ValidationError as PydanticValidationError

from dwex_groundwater.config.settings import (
    ApplicationSettings,
    DWEXConfig,
    ModflowSettings,
    PathsSettings,
    ProjectSettings,
    QaQcSettings,
)
from dwex_groundwater.exceptions.domain import (
    ConfigurationError,
    ConfigurationNotFoundError,
    ConfigurationValidationError,
)


def find_project_root(start_path: Path | None = None) -> Path:
    """Traverse parent directories to locate project root by pyproject.toml."""
    env_root = os.getenv("DWEX_PROJECT_ROOT")
    if env_root and os.path.exists(env_root):
        return Path(env_root).resolve()

    current = (start_path or Path.cwd()).resolve()
    for parent in [current, *current.parents]:
        if (parent / "pyproject.toml").is_file():
            return parent
    return current


class ConfigurationLoader:
    """Loads and validates DWEX configuration files."""

    def __init__(self, project_root: Path | None = None) -> None:
        self.project_root = find_project_root(project_root)

    def _load_yaml(self, path: Path) -> dict[str, Any]:
        if not path.is_file():
            raise ConfigurationNotFoundError(
                f"Required configuration file not found: {path}",
                details={"path": str(path)},
            )
        try:
            with open(path, encoding="utf-8") as f:
                data = yaml.safe_load(f)
                return data if isinstance(data, dict) else {}
        except yaml.YAMLError as exc:
            raise ConfigurationError(
                f"Error parsing YAML file: {path}",
                details={"error": str(exc), "path": str(path)},
            ) from exc

    def load(self, config_dir: Path | None = None) -> DWEXConfig:
        """Load and merge configuration from paths.yaml, model_config.yaml, and validation_rules.yaml."""
        cfg_dir = config_dir or (self.project_root / "config")

        paths_file = cfg_dir / "paths.yaml"
        model_cfg_file = cfg_dir / "model_config.yaml"
        val_rules_file = cfg_dir / "validation_rules.yaml"

        paths_dict = self._load_yaml(paths_file) if paths_file.exists() else {}
        model_cfg_dict = self._load_yaml(model_cfg_file) if model_cfg_file.exists() else {}
        val_rules_dict = self._load_yaml(val_rules_file) if val_rules_file.exists() else {}

        # Environment variable overrides
        env_exe = os.getenv("DWEX_MODFLOW_EXECUTABLE")
        if env_exe:
            if "modflow" not in model_cfg_dict:
                model_cfg_dict["modflow"] = {}
            model_cfg_dict["modflow"]["executable"] = env_exe

        env_env = os.getenv("DWEX_ENVIRONMENT")
        if env_env:
            if "application" not in model_cfg_dict:
                model_cfg_dict["application"] = {}
            model_cfg_dict["application"]["environment"] = env_env

        try:
            raw_paths = PathsSettings(**paths_dict.get("paths", {}))
            resolved_paths = raw_paths.resolve_paths(self.project_root)

            application_cfg = ApplicationSettings(**model_cfg_dict.get("application", {}))
            modflow_cfg = ModflowSettings(**model_cfg_dict.get("modflow", {}))
            project_cfg = ProjectSettings(**model_cfg_dict.get("project", {}))
            qa_qc_cfg = QaQcSettings(**val_rules_dict.get("qa_qc", {}))

            return DWEXConfig(
                project_root=self.project_root,
                application=application_cfg,
                modflow=modflow_cfg,
                project=project_cfg,
                paths=resolved_paths,
                qa_qc=qa_qc_cfg,
            )
        except PydanticValidationError as exc:
            raise ConfigurationValidationError(
                f"Configuration validation failed: {exc}",
                details={"errors": exc.errors()},
            ) from exc
        except Exception as exc:
            raise ConfigurationError(
                f"Unexpected error constructing DWEXConfig: {exc}",
                details={"error": str(exc)},
            ) from exc


def load_config(project_root: Path | None = None) -> DWEXConfig:
    """Convenience helper to load default project configuration."""
    loader = ConfigurationLoader(project_root=project_root)
    return loader.load()
