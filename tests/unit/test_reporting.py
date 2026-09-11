"""Unit tests for reporting and manifest generation."""

from __future__ import annotations

from pathlib import Path

from dwex_groundwater.reporting.test_report import TestReportGenerator


def test_test_report_generator(project_root: Path, temp_workspace: Path) -> None:
    """Verify artifact recording, manifest export, and markdown report compilation."""
    gen = TestReportGenerator(project_root)

    dummy_file = temp_workspace / "dummy.txt"
    dummy_file.write_text("Test", encoding="utf-8")
    gen.record_artifact("dummy.txt", "text", "unit test", dummy_file)

    manifest_json = temp_workspace / "manifest.json"
    manifest = gen.export_manifest(manifest_json)
    assert manifest["total_artifacts"] == 1
    assert manifest_json.is_file()

    report_md = temp_workspace / "REPORT.md"
    gen.generate_markdown_report(report_md, pipeline_data={})
    assert report_md.is_file()
    content = report_md.read_text(encoding="utf-8")
    assert "END-TO-END SYNTHETIC PROJECT TEST REPORT" in content
