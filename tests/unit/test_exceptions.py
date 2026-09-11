"""Unit tests for domain exception hierarchy."""

from __future__ import annotations

from dwex_groundwater.exceptions.domain import (
    ConfigurationError,
    ConfigurationNotFoundError,
    ConfigurationValidationError,
    CrsValidationError,
    DataIntegrityError,
    DWEXError,
    EnvironmentError,
    ExecutionError,
    IncompatibleVersionError,
    MissingDependencyError,
    ModflowConvergenceError,
    ModflowError,
    ModflowExecutionError,
    ModflowNotFoundError,
    ValidationError,
)


def test_exception_hierarchy() -> None:
    """Verify all domain exceptions inherit from DWEXError."""
    assert issubclass(ConfigurationError, DWEXError)
    assert issubclass(ConfigurationNotFoundError, ConfigurationError)
    assert issubclass(ConfigurationValidationError, ConfigurationError)
    assert issubclass(EnvironmentError, DWEXError)
    assert issubclass(MissingDependencyError, EnvironmentError)
    assert issubclass(IncompatibleVersionError, EnvironmentError)
    assert issubclass(ModflowError, DWEXError)
    assert issubclass(ModflowNotFoundError, ModflowError)
    assert issubclass(ModflowExecutionError, ModflowError)
    assert issubclass(ModflowConvergenceError, ModflowError)
    assert issubclass(ValidationError, DWEXError)
    assert issubclass(CrsValidationError, ValidationError)
    assert issubclass(DataIntegrityError, ValidationError)
    assert issubclass(ExecutionError, DWEXError)


def test_exception_details_formatting() -> None:
    """Verify custom details dictionary is preserved and rendered in string representation."""
    err = ModflowNotFoundError("Binary missing", details={"path": "tools/modflow6/mf6.exe"})
    assert "Binary missing" in str(err)
    assert "tools/modflow6/mf6.exe" in str(err)
    assert err.details["path"] == "tools/modflow6/mf6.exe"


def test_exception_without_details() -> None:
    """Verify clean string representation when no details are provided."""
    err = ExecutionError("Generic failure")
    assert str(err) == "Generic failure"
