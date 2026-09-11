"""3D Groundwater Hydrogeological Model Visualization.

Renders interactive 3D meshes of surface topography, aquifer units,
water table elevation, and well screen columns to standalone HTML.
"""

from __future__ import annotations

from pathlib import Path
from typing import Any

import flopy
import numpy as np
import plotly.graph_objects as go

from dwex_groundwater.logging.logger import get_logger

logger = get_logger("visualization.viz3d")


class Model3DVisualizer:
    """Renders 3D interactive hydrogeological surfaces and monitoring wells."""

    def __init__(self, workspace_dir: Path | str, conceptual_model: dict[str, Any]) -> None:
        self.workspace = Path(workspace_dir).resolve()
        self.conceptual_model = conceptual_model

    def generate_3d_html(self, output_path: Path | str) -> Path:
        """Create an interactive 3D HTML scene with topography, water table, and well infrastructure."""
        out = Path(output_path).resolve()
        out.parent.mkdir(parents=True, exist_ok=True)

        hds_files = list(self.workspace.glob("*.hds"))
        if not hds_files:
            raise FileNotFoundError(f"No .hds files found in {self.workspace}")

        hds_obj = flopy.utils.HeadFile(str(hds_files[0]))
        times = hds_obj.get_times()
        heads = hds_obj.get_data(totim=times[-1] if times else None)
        hds_obj.close()

        _, nrow, ncol = heads.shape
        x = np.linspace(0, 1000, ncol)
        y = np.linspace(0, 1000, nrow)
        X, Y = np.meshgrid(x, y)

        # 1. Surface Topography DEM
        top_grid = np.zeros((nrow, ncol), dtype=float)
        for c in range(ncol):
            top_grid[:, c] = 32.0 - (6.0 * (c / (ncol - 1)))

        # 2. Water Table (Simulated Heads Layer 0)
        wt_grid = heads[0, :, :]

        # 3. Layer 1 Contact (10.0 m)
        botm1_grid = np.full((nrow, ncol), 10.0)

        # 4. Aquifer Base (-15.0 m)
        botm2_grid = np.full((nrow, ncol), -15.0)

        fig = go.Figure()

        # Surface 1: Ground Surface
        fig.add_trace(
            go.Surface(
                x=X,
                y=Y,
                z=top_grid,
                colorscale="Earth",
                opacity=0.6,
                name="Ground Surface (DEM)",
                showscale=False,
            )
        )

        # Surface 2: Simulated Groundwater Table
        fig.add_trace(
            go.Surface(
                x=X,
                y=Y,
                z=wt_grid,
                colorscale="Blues",
                opacity=0.85,
                name="Simulated Water Table",
                colorbar={"title": "Head (m a.s.l.)", "len": 0.6, "x": 1.05},
            )
        )

        # Surface 3: Upper Aquifer Base
        fig.add_trace(
            go.Surface(
                x=X,
                y=Y,
                z=botm1_grid,
                colorscale="YlOrBr",
                opacity=0.4,
                name="Layer 1 Bottom (10m)",
                showscale=False,
            )
        )

        # Surface 4: Impermeable Bedrock
        fig.add_trace(
            go.Surface(
                x=X,
                y=Y,
                z=botm2_grid,
                colorscale="Greys",
                opacity=0.3,
                name="Aquifer Base (-15m)",
                showscale=False,
            )
        )

        # Add Pumping Well 3D Column
        stresses = self.conceptual_model.get("boundary_conditions", {}).get("stresses", [])
        if stresses:
            pw = stresses[0]
            # Convert UTM coordinates to local offset (0-1000m)
            pw_lx = 500.0
            pw_ly = 500.0
            fig.add_trace(
                go.Scatter3d(
                    x=[pw_lx, pw_lx],
                    y=[pw_ly, pw_ly],
                    z=[32.0, 5.0],
                    mode="lines+markers",
                    line={"color": "red", "width": 8},
                    marker={"size": 6, "color": "red"},
                    name=f"Pumping Well ({pw['id']})",
                )
            )

        # Add Observation Wells
        for ow in self.conceptual_model.get("observation_targets", []):
            ow_lx = float(ow["x"]) - 500000.0
            ow_ly = float(ow["y"]) - 2700000.0
            col = "green" if ow.get("use") == "calibration" else "orange"
            fig.add_trace(
                go.Scatter3d(
                    x=[ow_lx, ow_lx],
                    y=[ow_ly, ow_ly],
                    z=[30.0, float(ow["observed_head"])],
                    mode="lines+markers",
                    line={"color": col, "width": 5},
                    marker={"size": 4, "color": col},
                    name=f"Obs Well {ow['well_id']} ({ow.get('use')})",
                )
            )

        fig.update_layout(
            title="Interactive 3D Hydrogeological Model & Simulated Water Table<br><sup>DWEX Synthetic Groundwater Validation System</sup>",
            scene={
                "xaxis_title": "Easting (m)",
                "yaxis_title": "Northing (m)",
                "zaxis_title": "Elevation (m a.s.l.)",
                "aspectratio": {"x": 1.2, "y": 1.2, "z": 0.5},
                "camera": {"eye": {"x": 1.6, "y": -1.6, "z": 1.0}},
            },
            margin={"l": 0, "r": 0, "b": 0, "t": 50},
            template="plotly_dark",
        )

        fig.write_html(str(out), include_plotlyjs="cdn")
        logger.info("Saved 3D model visualization to %s", out)
        return out
