"""Unit tests for visualization components."""

from __future__ import annotations

from pathlib import Path

import pandas as pd

from dwex_groundwater.visualization.graphs import GraphGenerator


def test_graph_generator_observed_vs_simulated(temp_workspace: Path) -> None:
    """Verify graph generation for observed vs simulated heads and residuals."""
    csv_path = temp_workspace / "comps.csv"
    df = pd.DataFrame(
        [
            {"well_id": "W1", "observed_head": 30.0, "simulated_head": 30.1, "residual": 0.1},
            {"well_id": "W2", "observed_head": 28.0, "simulated_head": 27.9, "residual": -0.1},
        ]
    )
    df.to_csv(csv_path, index=False)

    gen = GraphGenerator(temp_workspace)
    g1 = gen.generate_observed_vs_simulated(
        csv_path, temp_workspace / "g1.png", {"rmse": 0.1, "mae": 0.1, "r_squared": 0.99}
    )
    assert g1.is_file()
    assert g1.stat().st_size > 1000

    g2 = gen.generate_residuals_plot(csv_path, temp_workspace / "g2.png")
    assert g2.is_file()
    assert g2.stat().st_size > 1000

    g3 = gen.generate_hydrograph(temp_workspace / "g3.png")
    assert g3.is_file()
    assert g3.stat().st_size > 1000

    g4 = gen.generate_pumping_vs_drawdown(temp_workspace / "g4.png")
    assert g4.is_file()
    assert g4.stat().st_size > 1000

    g5 = gen.generate_water_budget(temp_workspace / "g5.png")
    assert g5.is_file()
    assert g5.stat().st_size > 1000
