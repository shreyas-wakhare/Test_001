"""Verification data models and result schemas."""

from __future__ import annotations

from dataclasses import dataclass, field
from enum import StrEnum
from typing import Any


class CheckStatus(StrEnum):
    """Result status for an individual verification check."""

    PASS = "PASS"
    WARN = "WARN"
    FAIL = "FAIL"
    SKIPPED = "SKIPPED"


@dataclass
class CheckResult:
    """Detailed outcome of a single environment verification item."""

    name: str
    category: str
    status: CheckStatus
    message: str
    duration_seconds: float = 0.0
    details: dict[str, Any] = field(default_factory=dict)
