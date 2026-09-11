"""Domain exception hierarchy for DWEX Groundwater Modelling platform."""

from typing import Any


class DWEXError(Exception):
    """Base exception for all domain errors within DWEX groundwater platform."""

    def __init__(self, message: str, details: dict[str, Any] | None = None) -> None:
        super().__init__(message)
        self.message = message
        self.details = details or {}

    def __str__(self) -> str:
        if self.details:
            return f"{self.message} | Details: {self.details}"
        return self.message


class ConfigurationError(DWEXError):
    """Raised when configuration loading, schema validation, or parsing fails."""


class ConfigurationNotFoundError(ConfigurationError):
    """Raised when an expected configuration file cannot be found."""


class ConfigurationValidationError(ConfigurationError):
    """Raised when configuration values fail type or boundary constraints."""


class EnvironmentError(DWEXError):
    """Raised when runtime environment, directory, or platform checks fail."""


class MissingDependencyError(EnvironmentError):
    """Raised when a required external package or library is not installed."""


class IncompatibleVersionError(EnvironmentError):
    """Raised when an installed dependency version does not satisfy requirements."""


class ModflowError(DWEXError):
    """Base exception for MODFLOW execution, binary resolution, and simulation issues."""


class ModflowNotFoundError(ModflowError):
    """Raised when mf6.exe cannot be located in PATH or configured paths."""


class ModflowExecutionError(ModflowError):
    """Raised when mf6.exe terminates with a non-zero exit code or fatal error."""


class ModflowConvergenceError(ModflowError):
    """Raised when MODFLOW 6 fails to converge within solver iteration limits."""


class ValidationError(DWEXError):
    """Raised when raw or processed data fails domain validation rules."""


class CrsValidationError(ValidationError):
    """Raised when spatial datasets have missing, ambiguous, or mismatched CRS."""


class DataIntegrityError(ValidationError):
    """Raised when data completeness, null-checks, or boundary limits fail."""


class ExecutionError(DWEXError):
    """Raised when general workflow execution fails unexpectedly."""
