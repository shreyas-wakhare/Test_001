"""Unit tests for spatial, quality, and unit validation."""

from __future__ import annotations

from pathlib import Path

from dwex_groundwater.extraction.extractor import DataExtractor
from dwex_groundwater.validation.quality import DataQualityValidator
from dwex_groundwater.validation.spatial import SpatialValidator
from dwex_groundwater.validation.units import UnitValidator


def test_unit_validator() -> None:
    """Verify explicit unit conversion and audit records."""
    uv = UnitValidator()
    val_m = uv.convert_length(3.28084, "ft", "meters", parameter_name="depth")
    assert round(val_m, 2) == 1.0

    k_m_d = uv.convert_conductivity(0.01, "cm/s", "m/day", parameter_name="k_sand")
    assert round(k_m_d, 2) == 8.64
    assert len(uv.get_audit_trail()) == 2


def test_spatial_and_quality_validators(project_root: Path, temp_workspace: Path) -> None:
    """Verify spatial CRS checking and tabular QA/QC validation."""
    raw_dir = project_root / "data" / "synthetic_test" / "raw"
    extractor = DataExtractor(raw_dir)
    eng_dataset = extractor.build_engineering_dataset(temp_workspace / "dataset.json")

    # Spatial
    sv = SpatialValidator(eng_dataset)
    s_res = sv.validate()
    assert s_res["status"] == "PASS"
    assert s_res["dem_covers_domain"] is True
    assert s_res["points_inside"] == s_res["points_checked"]

    # Quality
    qv = DataQualityValidator(eng_dataset)
    q_res = qv.run_all()
    assert q_res["overall_status"] == "PASS"
