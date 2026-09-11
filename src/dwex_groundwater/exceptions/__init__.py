"""Exception package exports."""

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

__all__ = [
    "DWEXError",
    "ConfigurationError",
    "ConfigurationNotFoundError",
    "ConfigurationValidationError",
    "EnvironmentError",
    "MissingDependencyError",
    "IncompatibleVersionError",
    "ModflowError",
    "ModflowNotFoundError",
    "ModflowExecutionError",
    "ModflowConvergenceError",
    "ValidationError",
    "CrsValidationError",
    "DataIntegrityError",
    "ExecutionError",
]
