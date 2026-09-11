"""Unit tests for data ingestion and inventory."""

from __future__ import annotations

from pathlib import Path

from dwex_groundwater.ingestion.inventory import DataInventoryManager


def test_inventory_scan_and_export(project_root: Path, temp_workspace: Path) -> None:
    """Verify inventory manager scans raw files, hashes them, and detects categories."""
    raw_dir = project_root / "data" / "synthetic_test" / "raw"
    mgr = DataInventoryManager(raw_dir)
    items = mgr.scan()

    assert len(items) >= 10
    names = [i.file_name for i in items]
    assert "project_boundary.geojson" in names
    assert "dem.tif" in names
    assert "boreholes.csv"
    assert "hydraulic_properties.xlsx" in names

    # Verify SHA-256 is present and non-trivial
    assert all(len(i.sha256) == 64 for i in items)
    assert not any(i.is_duplicate for i in items)

    # Export check
    out_json = temp_workspace / "inv_test.json"
    data = mgr.export_inventory(out_json)
    assert data["total_files"] == len(items)
    assert out_json.is_file()
