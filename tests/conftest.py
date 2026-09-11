"""Shared pytest fixtures and configuration."""

from __future__ import annotations

import tempfile
from collections.abc import Generator
from pathlib import Path

import pytest

from dwex_groundwater.config.loader import load_config
from dwex_groundwater.config.settings import DWEXConfig
from dwex_groundwater.modflow.executable import ModflowExecutable
from dwex_groundwater.modflow.runner import ModflowRunner


@pytest.fixture
def project_root() -> Path:
    """Return project root directory."""
    return Path(__file__).resolve().parent.parent


@pytest.fixture
def test_config(project_root: Path) -> DWEXConfig:
    """Return loaded test configuration."""
    return load_config(project_root)


@pytest.fixture
def temp_workspace() -> Generator[Path, None, None]:
    """Provide an isolated temporary workspace that is safely removed after test."""
    with tempfile.TemporaryDirectory(prefix="dwex_test_") as tmp:
        yield Path(tmp)


@pytest.fixture
def modflow_executable() -> ModflowExecutable:
    """Return initialized ModflowExecutable instance."""
    return ModflowExecutable()


@pytest.fixture
def modflow_runner(modflow_executable: ModflowExecutable) -> ModflowRunner:
    """Return initialized ModflowRunner instance."""
    return ModflowRunner(executable=modflow_executable)
