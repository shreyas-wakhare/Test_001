"""Unit Conversion and Validation Engine.

Ensures all length, elevation, conductivity, and flow units are validated
and explicitly converted without silent assumptions.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from dwex_groundwater.logging.logger import get_logger

logger = get_logger("validation.units")


@dataclass
class UnitConversionRecord:
    """Audit record for an explicit unit conversion."""

    parameter: str
    original_value: float
    original_unit: str
    converted_value: float
    converted_unit: str
    conversion_factor: float
    source: str


class UnitValidator:
    """Validates and explicitly converts physical hydrogeological units."""

    # Standard conversion to meters and days (MODFLOW standard SI engineering units)
    LENGTH_TO_METERS = {
        "m": 1.0,
        "meter": 1.0,
        "meters": 1.0,
        "ft": 0.3048,
        "feet": 0.3048,
        "cm": 0.01,
        "centimeter": 0.01,
    }

    TIME_TO_DAYS = {
        "d": 1.0,
        "day": 1.0,
        "days": 1.0,
        "s": 1.0 / 86400.0,
        "sec": 1.0 / 86400.0,
        "seconds": 1.0 / 86400.0,
        "hr": 1.0 / 24.0,
        "hour": 1.0 / 24.0,
        "hours": 1.0 / 24.0,
    }

    def __init__(self) -> None:
        self.conversion_records: list[UnitConversionRecord] = []

    def convert_length(
        self,
        value: float,
        from_unit: str,
        target_unit: str = "meters",
        parameter_name: str = "length",
        source: str = "unknown",
    ) -> float:
        """Explicitly convert length dimension to target unit."""
        norm_from = from_unit.lower().strip()
        norm_to = target_unit.lower().strip()

        if norm_from == norm_to:
            return value

        if norm_from not in self.LENGTH_TO_METERS or norm_to not in self.LENGTH_TO_METERS:
            raise ValueError(f"Unsupported length conversion from '{from_unit}' to '{target_unit}'")

        factor = self.LENGTH_TO_METERS[norm_from] / self.LENGTH_TO_METERS[norm_to]
        converted = value * factor

        record = UnitConversionRecord(
            parameter=parameter_name,
            original_value=value,
            original_unit=from_unit,
            converted_value=converted,
            converted_unit=target_unit,
            conversion_factor=factor,
            source=source,
        )
        self.conversion_records.append(record)
        return converted

    def convert_conductivity(
        self,
        value: float,
        from_unit: str,
        target_unit: str = "m/day",
        parameter_name: str = "hydraulic_conductivity",
        source: str = "unknown",
    ) -> float:
        """Convert hydraulic conductivity (e.g. cm/s, m/s, m/day) to target unit."""
        norm_from = from_unit.lower().strip()
        norm_to = target_unit.lower().strip()

        if norm_from == norm_to:
            return value

        # Known rates to m/day
        rate_factors = {
            "m/day": 1.0,
            "m/d": 1.0,
            "m/s": 86400.0,
            "m/sec": 86400.0,
            "cm/s": 864.0,
            "cm/sec": 864.0,
            "ft/day": 0.3048,
        }

        if norm_from not in rate_factors or norm_to not in rate_factors:
            raise ValueError(
                f"Unsupported conductivity conversion from '{from_unit}' to '{target_unit}'"
            )

        factor = rate_factors[norm_from] / rate_factors[norm_to]
        converted = value * factor

        self.conversion_records.append(
            UnitConversionRecord(
                parameter=parameter_name,
                original_value=value,
                original_unit=from_unit,
                converted_value=converted,
                converted_unit=target_unit,
                conversion_factor=factor,
                source=source,
            )
        )
        return converted

    def get_audit_trail(self) -> list[dict[str, Any]]:
        """Return audit trail of all performed conversions."""
        return [
            {
                "parameter": r.parameter,
                "original": f"{r.original_value} {r.original_unit}",
                "converted": f"{r.converted_value} {r.converted_unit}",
                "factor": r.conversion_factor,
                "source": r.source,
            }
            for r in self.conversion_records
        ]
