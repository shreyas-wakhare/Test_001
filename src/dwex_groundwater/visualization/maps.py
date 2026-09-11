"""2D Hydrogeological Mapping Engine.

Generates hydraulic head contours, pumping drawdown surfaces,
and specific discharge groundwater flow vector quiver maps.
"""

from __future__ import annotations

from pathlib import Path
from typing import Any

import flopy
import matplotlib.pyplot as plt
import numpy as np

from dwex_groundwater.logging.logger import get_logger

logger = get_logger("visualization.maps")


class GroundwaterMapGenerator:
    """Generates high-resolution publication-quality 2D groundwater maps from MODFLOW outputs."""

    def __init__(self, workspace_dir: Path | str, conceptual_model: dict[str, Any]) -> None:
        self.workspace = Path(workspace_dir).resolve()
        self.conceptual_model = conceptual_model

        domain = conceptual_model.get("domain", {})
        bounds = domain.get("bounds", [500000.0, 2700000.0, 501000.0, 2701000.0])
        self.min_x, self.min_y, self.max_x, self.max_y = bounds[0], bounds[1], bounds[2], bounds[3]

    def _get_heads(self) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
        """Read binary head file and return baseline (period 0) and stressed heads (period 1)."""
        hds_files = list(self.workspace.glob("*.hds"))
        if not hds_files:
            raise FileNotFoundError(f"No .hds files found in {self.workspace}")

        hds_obj = flopy.utils.HeadFile(str(hds_files[0]))
        kstpkpers = hds_obj.get_kstpkper()

        # Baseline steady-state head (first record)
        head_steady = hds_obj.get_data(kstpkper=kstpkpers[0])
        # Final transient stressed head (last record)
        head_stressed = hds_obj.get_data(kstpkper=kstpkpers[-1])
        hds_obj.close()

        drawdown = head_steady - head_stressed
        return head_steady, head_stressed, drawdown

    def generate_head_contour_map(self, output_path: Path | str) -> Path:
        """Generate filled hydraulic head contour map with boundary and well overlays."""
        out = Path(output_path).resolve()
        out.parent.mkdir(parents=True, exist_ok=True)

        _, head_stressed, _ = self._get_heads()
        heads_lay0 = head_stressed[0, :, :]
        nrow, ncol = heads_lay0.shape

        x_coords = np.linspace(self.min_x, self.max_x, ncol)
        y_coords = np.linspace(self.max_y, self.min_y, nrow)
        X, Y = np.meshgrid(x_coords, y_coords)

        fig, ax = plt.subplots(figsize=(10, 8), dpi=200)

        # Filled contours
        levels = np.linspace(np.floor(heads_lay0.min()), np.ceil(heads_lay0.max()), 15)
        cf = ax.contourf(X, Y, heads_lay0, levels=levels, cmap="Blues_r", alpha=0.85)
        cbar = fig.colorbar(cf, ax=ax, shrink=0.8)
        cbar.set_label("Hydraulic Head (m a.s.l.)", fontsize=11, fontweight="bold")

        # Equipotential contour lines
        cl = ax.contour(X, Y, heads_lay0, levels=levels, colors="#1e293b", linewidths=0.8)
        ax.clabel(cl, inline=True, fontsize=8, fmt="%.1f m")

        # Boundaries
        ax.axvline(self.min_x, color="#2563eb", linewidth=4, label="Western Inflow (CHD)")
        ax.axvline(
            self.max_x,
            color="#0284c7",
            linewidth=4,
            linestyle="--",
            label="Eastern River Drainage (RIV)",
        )

        # Pumping well PW-01
        stresses = self.conceptual_model.get("boundary_conditions", {}).get("stresses", [])
        if stresses:
            pw = stresses[0]
            ax.plot(
                pw["x"],
                pw["y"],
                marker="o",
                markersize=9,
                color="#dc2626",
                markeredgecolor="white",
                markeredgewidth=1.5,
                label=f"Pumping Well ({pw['id']})",
            )

        # Observation wells
        for ow in self.conceptual_model.get("observation_targets", []):
            color = "#16a34a" if ow.get("use") == "calibration" else "#d97706"
            ax.plot(
                ow["x"],
                ow["y"],
                marker="^",
                markersize=7,
                color=color,
                markeredgecolor="white",
                label=f"Obs Well ({ow['well_id']}) [{ow.get('use')}]",
            )

        # Avoid duplicate legend entries
        handles, labels = ax.get_legend_handles_labels()
        by_label = dict(zip(labels, handles, strict=False))
        ax.legend(by_label.values(), by_label.keys(), loc="upper right", framealpha=0.9)

        ax.set_title(
            "Simulated Water Table Hydraulic Head Contours\nDWEX Synthetic Baseline Aquifer (Layer 1)",
            fontsize=13,
            fontweight="bold",
            pad=12,
        )
        ax.set_xlabel("Easting (UTM Zone 33N, m)", fontsize=10)
        ax.set_ylabel("Northing (UTM Zone 33N, m)", fontsize=10)
        ax.set_xlim(self.min_x, self.max_x)
        ax.set_ylim(self.min_y, self.max_y)
        ax.grid(True, linestyle=":", alpha=0.6)

        plt.tight_layout()
        fig.savefig(out)
        plt.close(fig)

        logger.info("Saved head contour map to %s", out)
        return out

    def generate_drawdown_map(self, output_path: Path | str) -> Path:
        """Generate drawdown map showing cone of depression around pumping wells."""
        out = Path(output_path).resolve()
        out.parent.mkdir(parents=True, exist_ok=True)

        _, _, drawdown = self._get_heads()
        dd_lay0 = np.clip(drawdown[0, :, :], 0.0, None)
        nrow, ncol = dd_lay0.shape

        x_coords = np.linspace(self.min_x, self.max_x, ncol)
        y_coords = np.linspace(self.max_y, self.min_y, nrow)
        X, Y = np.meshgrid(x_coords, y_coords)

        fig, ax = plt.subplots(figsize=(10, 8), dpi=200)

        dd_max = max(0.5, float(dd_lay0.max()))
        levels = np.linspace(0.0, dd_max, 12)
        cf = ax.contourf(X, Y, dd_lay0, levels=levels, cmap="YlOrRd", alpha=0.85)
        cbar = fig.colorbar(cf, ax=ax, shrink=0.8)
        cbar.set_label("Pumping Drawdown (meters)", fontsize=11, fontweight="bold")

        cl = ax.contour(X, Y, dd_lay0, levels=levels, colors="#7f1d1d", linewidths=0.8)
        ax.clabel(cl, inline=True, fontsize=8, fmt="%.2f m")

        # Pumping well
        stresses = self.conceptual_model.get("boundary_conditions", {}).get("stresses", [])
        if stresses:
            pw = stresses[0]
            ax.plot(
                pw["x"],
                pw["y"],
                marker="*",
                markersize=14,
                color="#b91c1c",
                markeredgecolor="black",
                label=f"Pumping Well ({pw['id']})",
            )

        ax.legend(loc="upper right", framealpha=0.9)
        ax.set_title(
            "Groundwater Drawdown Surface & Cone of Depression\n(Transient Pumping Stress = -500 m³/day)",
            fontsize=13,
            fontweight="bold",
            pad=12,
        )
        ax.set_xlabel("Easting (m)", fontsize=10)
        ax.set_ylabel("Northing (m)", fontsize=10)
        ax.set_xlim(self.min_x, self.max_x)
        ax.set_ylim(self.min_y, self.max_y)
        ax.grid(True, linestyle=":", alpha=0.6)

        plt.tight_layout()
        fig.savefig(out)
        plt.close(fig)

        logger.info("Saved drawdown map to %s", out)
        return out

    def generate_flow_vectors_map(self, output_path: Path | str) -> Path:
        """Generate groundwater specific discharge flow direction quiver vector map."""
        out = Path(output_path).resolve()
        out.parent.mkdir(parents=True, exist_ok=True)

        _, head_stressed, _ = self._get_heads()
        heads = head_stressed[0, :, :]
        nrow, ncol = heads.shape

        x_coords = np.linspace(self.min_x, self.max_x, ncol)
        y_coords = np.linspace(self.max_y, self.min_y, nrow)
        X, Y = np.meshgrid(x_coords, y_coords)

        # Darcy velocity gradients: qx = -K * dh/dx, qy = -K * dh/dy
        k = 20.0  # m/day
        grad_y, grad_x = np.gradient(
            heads, (self.max_y - self.min_y) / nrow, (self.max_x - self.min_x) / ncol
        )
        # Note: row index goes from north (max_y) to south (min_y), so dy is negative in spatial space
        qx = -k * grad_x
        qy = k * grad_y

        fig, ax = plt.subplots(figsize=(10, 8), dpi=200)

        # Background head field
        cf = ax.contourf(X, Y, heads, cmap="Blues_r", alpha=0.5)
        fig.colorbar(cf, ax=ax, shrink=0.8, label="Hydraulic Head (m a.s.l.)")

        # Quiver vectors (subsample for clarity)
        step = 2
        ax.quiver(
            X[::step, ::step],
            Y[::step, ::step],
            qx[::step, ::step],
            qy[::step, ::step],
            color="#0f172a",
            scale=15.0,
            width=0.003,
            label="Darcy Specific Discharge Vectors",
        )

        ax.set_title(
            "Groundwater Flow Vectors & Hydraulic Potential Field\n(West-to-East Regional Gradient)",
            fontsize=13,
            fontweight="bold",
            pad=12,
        )
        ax.set_xlabel("Easting (m)", fontsize=10)
        ax.set_ylabel("Northing (m)", fontsize=10)
        ax.set_xlim(self.min_x, self.max_x)
        ax.set_ylim(self.min_y, self.max_y)
        ax.legend(loc="upper right")
        ax.grid(True, linestyle=":", alpha=0.6)

        plt.tight_layout()
        fig.savefig(out)
        plt.close(fig)

        logger.info("Saved flow vectors map to %s", out)
        return out
