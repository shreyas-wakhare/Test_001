"""Unit tests for data extraction engine."""

from __future__ import annotations

from pathlib import Path

from dwex_groundwater.extraction.extractor import DataExtractor


def test_data_extractor_multi_format(project_root: Path, temp_workspace: Path) -> None:
    """Verify extraction of vector, raster, CSV, Excel, and docx with provenance."""
    raw_dir = project_root / "data" / "synthetic_test" / "raw"
    extractor = DataExtractor(raw_dir)

    out_json = temp_workspace / "eng_dataset_test.json"
    dataset = extractor.build_engineering_dataset(out_json)

    assert "metadata" in dataset
    assert dataset["domain"]["feature_count"] == 1
    assert dataset["topography"]["width"] == 40
    assert len(dataset["boreholes"]) >= 5
    assert len(dataset["groundwater_levels"]) >= 6
    assert len(dataset["provenance_parameters"]) >= 10

    # Provenance audit
    param0 = dataset["provenance_parameters"][0]
    assert "source_file" in param0
    assert "source_record" in param0
    assert param0["status"] == "SYNTHETIC"
