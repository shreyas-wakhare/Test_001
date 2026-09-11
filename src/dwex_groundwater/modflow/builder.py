"""FloPy MODFLOW 6 Numerical Model Builder.

Converts approved conceptual hydrogeological models into native, verified MODFLOW 6 packages.
"""

from __future__ import annotations

from pathlib import Path
from typing import Any

import flopy
import numpy as np

from dwex_groundwater.logging.logger import get_logger
from dwex_groundwater.modflow.executable import ModflowExecutable

logger = get_logger("modflow.builder")


class Modflow6ModelBuilder:
    """Constructs complete, native MODFLOW 6 simulations from conceptual specifications."""

    def __init__(
        self,
        conceptual_model: dict[str, Any],
        workspace_dir: Path | str,
        executable: ModflowExecutable | None = None,
        simulation_name: str = "dwex_gwf_sim",
    ) -> None:
        self.conceptual_model = conceptual_model
        self.workspace_dir = Path(workspace_dir).resolve()
        self.executable = executable or ModflowExecutable()
        self.simulation_name = simulation_name

    def build_and_write(
        self,
        nlay: int = 2,
        nrow: int = 20,
        ncol: int = 20,
        k1_override: float | None = None,
        recharge_override: float | None = None,
        riv_cond_override: float | None = None,
    ) -> flopy.mf6.MFSimulation:
        """Construct FloPy objects and write all MODFLOW 6 input files."""
        self.workspace_dir.mkdir(parents=True, exist_ok=True)
        exe_path = self.executable.resolve()

        domain = self.conceptual_model.get("domain", {})
        bounds = domain.get("bounds", [500000.0, 2700000.0, 501000.0, 2701000.0])
        x_min, y_min, x_max, y_max = bounds[0], bounds[1], bounds[2], bounds[3]
        delr = (x_max - x_min) / ncol  # 50m
        delc = (y_max - y_min) / nrow  # 50m

        layers_info = self.conceptual_model.get("hydrostratigraphy", {}).get("layers", [])
        k1 = (
            k1_override
            if k1_override is not None
            else float(layers_info[0].get("k_horizontal", 20.0))
        )
        k2 = float(layers_info[1].get("k_horizontal", 6.0)) if len(layers_info) > 1 else 5.0

        rch_rate = (
            recharge_override
            if recharge_override is not None
            else float(
                self.conceptual_model.get("boundary_conditions", {})
                .get("surface_recharge", {})
                .get("rate_m_day", 0.0005)
            )
        )
        riv_cond = (
            riv_cond_override
            if riv_cond_override is not None
            else float(
                self.conceptual_model.get("boundary_conditions", {})
                .get("east", {})
                .get("conductance", 50.0)
            )
        )

        logger.info(
            "Building MODFLOW 6 model in %s (K1=%.2f m/d, RCH=%.6f m/d, RivCond=%.1f)",
            self.workspace_dir,
            k1,
            rch_rate,
            riv_cond,
        )

        # 1. MFSimulation Container
        sim = flopy.mf6.MFSimulation(
            sim_name=self.simulation_name,
            version="mf6",
            exe_name=str(exe_path),
            sim_ws=str(self.workspace_dir),
            memory_print_option="SUMMARY",
        )

        # 2. TDIS (Time Discretization) - 1 Steady-state period followed by 1 transient period (10 days)
        flopy.mf6.ModflowTdis(
            sim,
            time_units="DAYS",
            nper=2,
            perioddata=[
                (1.0, 1, 1.0),  # Period 1: Steady-state
                (
                    10.0,
                    10,
                    1.2,
                ),  # Period 2: Transient (10 days, 10 steps, time step multiplier 1.2)
            ],
        )

        # 3. IMS (Iterative Model Solver)
        flopy.mf6.ModflowIms(
            sim,
            pname="ims",
            complexity="MODERATE",
            inner_maximum=150,
            outer_maximum=100,
            inner_dvclose=1e-5,
            outer_dvclose=1e-5,
            linear_acceleration="BICGSTAB",
        )

        # 4. GWF Model
        model_name = "gwf_dwex"
        gwf = flopy.mf6.ModflowGwf(
            sim,
            modelname=model_name,
            model_nam_file=f"{model_name}.nam",
            save_flows=True,
        )

        # 5. DIS (Structured Grid Discretization)
        # West to East sloping ground top
        top_grid = np.zeros((nrow, ncol), dtype=float)
        for c in range(ncol):
            top_grid[:, c] = 32.0 - (6.0 * (c / (ncol - 1)))  # 32m west -> 26m east

        botm_layer1 = np.full((nrow, ncol), 10.0, dtype=float)
        botm_layer2 = np.full((nrow, ncol), -15.0, dtype=float)
        botm_grid = np.stack([botm_layer1, botm_layer2], axis=0)

        flopy.mf6.ModflowGwfdis(
            gwf,
            nlay=nlay,
            nrow=nrow,
            ncol=ncol,
            delr=delr,
            delc=delc,
            top=top_grid,
            botm=botm_grid,
            xorigin=x_min,
            yorigin=y_min,
        )

        # 6. NPF (Node Property Flow)
        k_array = np.array([k1, k2])
        k33_array = np.array([k1 * 0.1, k2 * 0.1])
        flopy.mf6.ModflowGwfnpf(
            gwf,
            icelltype=[1, 0],  # Layer 1 unconfined (convertible), Layer 2 confined
            k=k_array,
            k33=k33_array,
            save_flows=True,
            save_specific_discharge=True,
        )

        # 7. STO (Storage) for transient period
        flopy.mf6.ModflowGwfsto(
            gwf,
            pname="sto",
            save_flows=True,
            iconvert=[1, 0],
            sy=[0.20, 0.10],
            ss=[1e-4, 1e-5],
            steady_state={0: True},
            transient={1: True},
        )

        # 8. IC (Initial Conditions)
        strt_head = np.zeros((nlay, nrow, ncol), dtype=float)
        for c in range(ncol):
            strt_head[:, :, c] = 31.0 - (6.0 * (c / (ncol - 1)))
        flopy.mf6.ModflowGwfic(gwf, strt=strt_head)

        # 9. CHD (Constant Head Boundary - Western Inflow)
        west_head = float(
            self.conceptual_model.get("boundary_conditions", {})
            .get("west", {})
            .get("head_elevation", 32.0)
        )
        chd_data = []
        for r in range(nrow):
            chd_data.append([(0, r, 0), west_head])  # Layer 0 (1st layer), row r, col 0
        flopy.mf6.ModflowGwfchd(
            gwf,
            maxbound=len(chd_data),
            stress_period_data={0: chd_data, 1: chd_data},
            pname="chd_west",
        )

        # 10. RIV (River Drainage Boundary - Eastern Edge)
        east_stage = float(
            self.conceptual_model.get("boundary_conditions", {}).get("east", {}).get("stage", 24.0)
        )
        east_rbot = float(
            self.conceptual_model.get("boundary_conditions", {})
            .get("east", {})
            .get("riverbed_bottom", 22.5)
        )
        riv_data = []
        for r in range(nrow):
            # cellid: (lay, row, col), stage, conductance, rbot
            riv_data.append([(0, r, ncol - 1), east_stage, riv_cond, east_rbot])
        flopy.mf6.ModflowGwfriv(
            gwf,
            maxbound=len(riv_data),
            stress_period_data={0: riv_data, 1: riv_data},
            pname="riv_east",
        )

        # 11. RCH (Areal Infiltration)
        flopy.mf6.ModflowGwfrcha(
            gwf,
            recharge=rch_rate,
            pname="rch",
        )

        # 12. WEL (Pumping Stress)
        # Well PW-01 at center: row 10, col 10 in Layer 0
        pw_rate = -500.0
        stresses = self.conceptual_model.get("boundary_conditions", {}).get("stresses", [])
        if stresses:
            pw_rate = float(stresses[0].get("pumping_rate_m3_day", -500.0))

        well_row = nrow // 2
        well_col = ncol // 2
        wel_spd = {
            0: [
                [(0, well_row, well_col), 0.0]
            ],  # Steady-state: no pumping (baseline pre-development)
            1: [[(0, well_row, well_col), pw_rate]],  # Transient: pumping active
        }
        flopy.mf6.ModflowGwfwel(
            gwf,
            maxbound=1,
            stress_period_data=wel_spd,
            pname="wel",
        )

        # 13. OC (Output Control)
        flopy.mf6.ModflowGwfoc(
            gwf,
            head_filerecord=f"{model_name}.hds",
            budget_filerecord=f"{model_name}.cbc",
            saverecord=[("HEAD", "ALL"), ("BUDGET", "ALL")],
            printrecord=[("HEAD", "LAST"), ("BUDGET", "LAST")],
        )

        logger.info("Writing MODFLOW 6 simulation files to %s", self.workspace_dir)
        sim.write_simulation()
        return sim
