"""Hydrogeological Cross-Section Visualization Engine.

Generates vertical profile sections displaying hydrostratigraphic layering,
ground elevation, simulated water table, and well screen intervals.
"""

from __future__ import annotations

from pathlib import Path
from typing import Any

import flopy
import matplotlib.pyplot as plt
import numpy as np

from dwex_groundwater.logging.logger import get_logger

logger = get_logger("visualization.cross_section")


class CrossSectionGenerator:
    """Renders hydrogeological cross-sections from MODFLOW grid and simulated heads."""

    def __init__(self, workspace_dir: Path | str, conceptual_model: dict[str, Any]) -> None:
        self.workspace = Path(workspace_dir).resolve()
        self.conceptual_model = conceptual_model

    def generate_west_east_section(self, output_path: Path | str, row_index: int = 10) -> Path:
        """Generate a West-to-East vertical hydrogeological cross-section."""
        out = Path(output_path).resolve()
        out.parent.mkdir(parents=True, exist_ok=True)

        hds_files = list(self.workspace.glob("*.hds"))
        if not hds_files:
            raise FileNotFoundError(f"No .hds files found in {self.workspace}")

        hds_obj = flopy.utils.HeadFile(str(hds_files[0]))
        times = hds_obj.get_times()
        heads = hds_obj.get_data(totim=times[-1] if times else None)
        hds_obj.close()

        nlay, nrow, ncol = heads.shape
        x_dist = np.linspace(0, 1000.0, ncol)

        # Elevation profiles
        top_elevation = 32.0 - (6.0 * (np.arange(ncol) / (ncol - 1)))
        botm_layer1 = np.full(ncol, 10.0)
        botm_layer2 = np.full(ncol, -15.0)

        # Heads across row
        wt_head_l0 = heads[0, row_index, :]
        wt_head_l1 = heads[1, row_index, :]

        fig, ax = plt.subplots(figsize=(11, 6), dpi=200)

        # Fills for geological layers
        ax.fill_between(
            x_dist,
            botm_layer1,
            top_elevation,
            color="#fed7aa",
            alpha=0.6,
            label="Layer 1: Alluvial Sand & Gravel",
        )
        ax.fill_between(
            x_dist,
            botm_layer2,
            botm_layer1,
            color="#cbd5e1",
            alpha=0.6,
            label="Layer 2: Silty Sand & Fractured Rock",
        )

        # Layer contact lines
        ax.plot(
            x_dist,
            top_elevation,
            color="#78350f",
            linewidth=2.0,
            label="Ground Surface (Topography)",
        )
        ax.plot(
            x_dist,
            botm_layer1,
            color="#475569",
            linestyle="--",
            linewidth=1.5,
            label="Layer 1 / Layer 2 Contact (10 m)",
        )
        ax.plot(
            x_dist, botm_layer2, color="#0f172a", linewidth=2.0, label="Impermeable Base (-15 m)"
        )

        # Water Table Line
        ax.plot(
            x_dist,
            wt_head_l0,
            color="#0284c7",
            linewidth=2.5,
            label="Simulated Water Table (Layer 1 Head)",
        )
        ax.plot(
            x_dist,
            wt_head_l1,
            color="#0369a1",
            linestyle=":",
            linewidth=1.8,
            label="Piezometric Head (Layer 2)",
        )

        # Pumping well at center
        well_x = 500.0
        ax.vlines(
            well_x,
            ymin=5.0,
            ymax=29.0,
            color="#b91c1c",
            linewidth=3.5,
            label="Pumping Well (PW-01 Screen)",
        )
        ax.plot(well_x, 29.0, marker="v", color="#b91c1c", markersize=10)

        ax.set_title(
            "Hydrogeological West-East Cross-Section (Through Pumping Well PW-01)\nDWEX Baseline Aquifer Simulation",
            fontsize=13,
            fontweight="bold",
            pad=12,
        )
        ax.set_xlabel("Distance from Western Boundary (meters)", fontsize=11)
        ax.set_ylabel("Elevation (m a.s.l.)", fontsize=11)
        ax.set_xlim(0, 1000.0)
        ax.set_ylim(-20.0, 36.0)
        ax.legend(loc="lower right", framealpha=0.9, fontsize=9)
        ax.grid(True, linestyle=":", alpha=0.6)

        plt.tight_layout()
        fig.savefig(out)
        plt.close(fig)

        logger.info("Saved model cross-section to %s", out)
        return out
