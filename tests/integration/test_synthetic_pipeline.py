"""Integration test verifying synthetic pipeline components end-to-end."""

from __future__ import annotations

from pathlib import Path

from dwex_groundwater.conceptual.approval import ApprovalGate
from dwex_groundwater.conceptual.synthesizer import ConceptualModelSynthesizer
from dwex_groundwater.extraction.extractor import DataExtractor
from dwex_groundwater.ingestion.inventory import DataInventoryManager
from dwex_groundwater.modflow.builder import Modflow6ModelBuilder
from dwex_groundwater.modflow.qa_qc import ModflowQaQcValidator
from dwex_groundwater.modflow.runner import ModflowRunner


def test_synthetic_flow_integration(project_root: Path, temp_workspace: Path) -> None:
    """Verify ingestion -> extraction -> conceptual -> approval -> FloPy -> simulation -> QA/QC."""
    raw_dir = project_root / "data" / "synthetic_test" / "raw"

    # Ingestion
    inv_mgr = DataInventoryManager(raw_dir)
    items = inv_mgr.scan()
    assert len(items) >= 10

    # Extraction
    extractor = DataExtractor(raw_dir)
    dataset = extractor.build_engineering_dataset(temp_workspace / "ds.json")
    assert len(dataset["provenance_parameters"]) >= 10

    # Conceptual
    synthesizer = ConceptualModelSynthesizer(dataset)
    c_model = synthesizer.synthesize()

    # Approval
    gate = ApprovalGate(temp_workspace / "approval")
    gate.grant_approval(approved_by="TEST_ENGINEER")
    assert gate.is_approved()

    # Model build & run
    sim_ws = temp_workspace / "sim_ws"
    builder = Modflow6ModelBuilder(c_model, sim_ws, simulation_name="test_integration_sim")
    builder.build_and_write(nlay=2, nrow=10, ncol=10)

    runner = ModflowRunner(timeout_seconds=60)
    result = runner.run_simulation(sim_ws, simulation_name="test_integration_sim")
    assert result.converged is True
    assert result.exit_code == 0

    # QA/QC
    qa = ModflowQaQcValidator(result, tolerance_percent=0.1)
    qa_res = qa.run_all()
    assert qa_res["overall_status"] == "PASS"
