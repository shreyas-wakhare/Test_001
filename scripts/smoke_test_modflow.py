#!/usr/bin/env python
"""MODFLOW 6 Smoke Test - Synthetic Numerical Simulation Verification.

Creates a minimal, synthetic steady-state groundwater simulation using FloPy,
writes MODFLOW 6 input files, executes mf6.exe, reads binary head outputs,
and verifies numerical convergence and physical head gradients.
"""

from __future__ import annotations

import shutil
import sys
import tempfile
from pathlib import Path

# Ensure src is in python path
project_root = Path(__file__).resolve().parent.parent
src_dir = project_root / "src"
if str(src_dir) not in sys.path:
    sys.path.insert(0, str(src_dir))

import flopy
import numpy as np

from dwex_groundwater.config.loader import load_config
from dwex_groundwater.logging.logger import setup_logger
from dwex_groundwater.modflow.executable import ModflowExecutable
from dwex_groundwater.modflow.runner import ModflowRunner


def run_modflow_smoke_test(verbose: bool = True) -> bool:
    """Build, run, and numerically validate a synthetic MODFLOW 6 model."""
    logger = setup_logger(name="dwex.smoke_test", log_file="smoke_test_modflow.log")

    print("=" * 64)
    print("DWEX GROUNDWATER - MODFLOW 6 NUMERICAL SMOKE TEST")
    print("=" * 64)

    # 1. Resolve mf6.exe
    config = load_config(project_root)
    mf_exe = ModflowExecutable(config.get_resolved_modflow_executable())
    try:
        exe_path = mf_exe.resolve()
        version_str = mf_exe.get_version()
        print(f"[STEP 1] MODFLOW 6 Executable: {exe_path} ({version_str})")
    except Exception as exc:
        print(f"[FAIL] Could not locate or execute MODFLOW 6 binary: {exc}")
        return False

    # 2. Setup temporary simulation workspace
    temp_dir = Path(tempfile.mkdtemp(prefix="dwex_mf6_smoke_"))
    print(f"[STEP 2] Temporary Workspace: {temp_dir}")

    try:
        # 3. Create synthetic FloPy simulation
        sim_name = "mf6_smoke_test"
        sim = flopy.mf6.MFSimulation(
            sim_name=sim_name,
            version="mf6",
            exe_name=str(exe_path),
            sim_ws=str(temp_dir),
            memory_print_option="SUMMARY",
        )

        # Time discretization (1 steady-state stress period)
        flopy.mf6.ModflowTdis(
            sim,
            time_units="DAYS",
            nper=1,
            perioddata=[(1.0, 1, 1.0)],
        )

        # Iterative Model Solver (IMS)
        flopy.mf6.ModflowIms(
            sim,
            pname="ims",
            complexity="SIMPLE",
            inner_maximum=100,
            outer_maximum=50,
            inner_dvclose=1e-5,
            outer_dvclose=1e-5,
        )

        # Groundwater Flow (GWF) Model
        model_name = "gwf_smoke"
        gwf = flopy.mf6.ModflowGwf(
            sim,
            modelname=model_name,
            model_nam_file=f"{model_name}.nam",
            save_flows=True,
        )

        # Discretization (DIS): 1 layer, 10 rows, 10 cols (1000m x 1000m domain)
        nlay = 1
        nrow = 10
        ncol = 10
        delr = 100.0  # meters
        delc = 100.0  # meters
        top = 50.0  # m a.s.l.
        botm = 0.0  # m a.s.l.

        flopy.mf6.ModflowGwfdis(
            gwf,
            nlay=nlay,
            nrow=nrow,
            ncol=ncol,
            delr=delr,
            delc=delc,
            top=top,
            botm=botm,
        )

        # Node Property Flow (NPF): hydraulic conductivity = 10 m/day
        flopy.mf6.ModflowGwfnpf(
            gwf,
            icelltype=1,  # unconfined
            k=10.0,
            k33=1.0,
            save_flows=True,
        )

        # Initial Conditions (IC): starting head = 45.0 m
        flopy.mf6.ModflowGwfic(gwf, strt=45.0)

        # Constant Head Boundaries (CHD):
        # West boundary (col 0) = 45.0 m, East boundary (col 9) = 40.0 m
        chd_data = []
        for r in range(nrow):
            chd_data.append([(0, r, 0), 45.0])  # West
            chd_data.append([(0, r, ncol - 1), 40.0])  # East

        flopy.mf6.ModflowGwfchd(
            gwf,
            maxbound=len(chd_data),
            stress_period_data={0: chd_data},
            pname="chd",
        )

        # Output Control (OC): save heads and budget
        head_file_name = f"{model_name}.hds"
        budget_file_name = f"{model_name}.cbc"
        flopy.mf6.ModflowGwfoc(
            gwf,
            head_filerecord=head_file_name,
            budget_filerecord=budget_file_name,
            saverecord=[("HEAD", "ALL"), ("BUDGET", "ALL")],
            printrecord=[("HEAD", "LAST"), ("BUDGET", "LAST")],
        )

        print("[STEP 3] Writing MODFLOW 6 input files...")
        sim.write_simulation()

        # 4. Execute simulation via ModflowRunner
        print("[STEP 4] Executing mf6.exe via ModflowRunner...")
        runner = ModflowRunner(executable=mf_exe, timeout_seconds=60)
        sim_result = runner.run_simulation(workspace=temp_dir, simulation_name=sim_name)

        print(f"[STEP 5] Process terminated normally in {sim_result.execution_time_seconds:.3f}s")
        print(f"         Simulation Status: {sim_result.status.value}")

        # 5. Read and validate binary head output
        head_path = temp_dir / head_file_name
        if not head_path.is_file():
            print(f"[FAIL] Expected binary head file '{head_file_name}' was not created.")
            return False

        head_obj = flopy.utils.HeadFile(str(head_path))
        heads = head_obj.get_data(kstpkper=(0, 0))
        head_obj.close()

        print("[STEP 6] Validating numerical heads...")
        print(f"         Head array shape: {heads.shape}")
        print(
            f"         West boundary head (col 0): min={heads[0, :, 0].min():.2f}, max={heads[0, :, 0].max():.2f}"
        )
        print(
            f"         East boundary head (col 9): min={heads[0, :, -1].min():.2f}, max={heads[0, :, -1].max():.2f}"
        )
        print(f"         Domain head range: [{heads.min():.2f}, {heads.max():.2f}] m")

        # Numerical sanity checks
        if np.isnan(heads).any() or np.isinf(heads).any():
            print("[FAIL] Output heads contain NaN or Infinite values.")
            return False

        if not np.isclose(heads[0, :, 0].mean(), 45.0, atol=1e-3):
            print("[FAIL] West constant head mismatch.")
            return False

        if not np.isclose(heads[0, :, -1].mean(), 40.0, atol=1e-3):
            print("[FAIL] East constant head mismatch.")
            return False

        # Gradient check: head should decrease monotonically from west to east
        row_gradients = np.diff(heads[0, 5, :])
        if not (row_gradients < 0).all():
            print("[FAIL] Hydraulic gradient is non-monotonic along flow path.")
            return False

        print("[STEP 7] Hydraulic gradient is physically consistent and monotonic.")
        print("-" * 64)
        print("MODFLOW 6 SMOKE TEST: PASSED")
        print("=" * 64)
        return True

    except Exception as exc:
        print(f"[FAIL] Smoke test encountered an error: {exc}")
        logger.exception("Smoke test failed with exception")
        return False

    finally:
        # Safe cleanup
        if temp_dir.exists():
            try:
                shutil.rmtree(temp_dir)
                print(f"[CLEANUP] Removed temporary workspace {temp_dir.name}")
            except Exception as e:
                logger.warning("Could not clean up temp directory %s: %s", temp_dir, e)


def main() -> int:
    """Entry point for smoke test CLI."""
    success = run_modflow_smoke_test()
    return 0 if success else 1


if __name__ == "__main__":
    sys.exit(main())
