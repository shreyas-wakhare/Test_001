"""Unit tests for conceptual model synthesis and engineer approval gate."""

from __future__ import annotations

from pathlib import Path

import pytest

from dwex_groundwater.conceptual.approval import ApprovalGate
from dwex_groundwater.conceptual.synthesizer import ConceptualModelSynthesizer
from dwex_groundwater.exceptions.domain import ValidationError
from dwex_groundwater.extraction.extractor import DataExtractor


def test_conceptual_synthesizer_and_approval_gate(project_root: Path, temp_workspace: Path) -> None:
    """Verify conceptual model generation and mandatory approval gate enforcement."""
    raw_dir = project_root / "data" / "synthetic_test" / "raw"
    extractor = DataExtractor(raw_dir)
    eng_dataset = extractor.build_engineering_dataset(temp_workspace / "ds.json")

    synthesizer = ConceptualModelSynthesizer(eng_dataset)
    c_model = synthesizer.synthesize()

    assert c_model["hydrostratigraphy"]["num_layers"] == 2
    assert "west" in c_model["boundary_conditions"]
    assert "east" in c_model["boundary_conditions"]

    # Test Gate: unapproved
    gate_dir = temp_workspace / "approval"
    gate = ApprovalGate(gate_dir)
    assert not gate.is_approved()
    with pytest.raises(ValidationError):
        gate.require_approval()

    # Test Gate: approved
    gate.grant_approval(approved_by="LEAD_HYDROGEOLOGIST")
    assert gate.is_approved()
    cert = gate.require_approval()
    assert cert["status"] == "APPROVED_FOR_SYNTHETIC_TEST"
    assert cert["approved_by"] == "LEAD_HYDROGEOLOGIST"
