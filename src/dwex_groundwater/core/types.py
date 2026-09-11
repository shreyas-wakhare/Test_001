"""Core domain types, enums, and protocols for groundwater modelling."""

from __future__ import annotations

from dataclasses import dataclass
from enum import StrEnum
from pathlib import Path
from typing import Any


class LengthUnit(StrEnum):
    """Supported physical length units in groundwater simulations."""

    METERS = "meters"
    FEET = "feet"
    CENTIMETERS = "centimeters"


class TimeUnit(StrEnum):
    """Supported physical time units in groundwater simulations."""

    SECONDS = "seconds"
    MINUTES = "minutes"
    HOURS = "hours"
    DAYS = "days"
    YEARS = "years"


class SimulationStatus(StrEnum):
    """MODFLOW simulation completion states."""

    NOT_STARTED = "not_started"
    RUNNING = "running"
    CONVERGED = "converged"
    FAILED = "failed"
    NON_CONVERGENT = "non_convergent"


@dataclass(frozen=True)
class SimulationResult:
    """Immutable result container from a MODFLOW numerical simulation run."""

    simulation_name: str
    workspace: Path
    status: SimulationStatus
    exit_code: int
    execution_time_seconds: float
    converged: bool
    output_files: list[Path]
    stdout_summary: str
    stderr_summary: str
    metadata: dict[str, Any]
