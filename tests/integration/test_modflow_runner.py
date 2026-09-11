"""Integration tests for MODFLOW 6 executable and runner abstraction."""

from __future__ import annotations

from pathlib import Path

import flopy
import numpy as np
import pytest

from dwex_groundwater.core.types import SimulationStatus
from dwex_groundwater.exceptions.domain import ModflowNotFoundError
from dwex_groundwater.modflow.executable import ModflowExecutable
from dwex_groundwater.modflow.runner import ModflowRunner


def test_modflow_executable_resolution(modflow_executable: ModflowExecutable) -> None:
    """Verify mf6.exe is located and version is retrieved."""
    exe_path = modflow_executable.resolve()
    assert exe_path.is_file()
    assert "mf6" in exe_path.name.lower()

    version = modflow_executable.get_version()
    assert "6." in version


def test_modflow_executable_non_existent_raises() -> None:
    """Verify invalid path raises ModflowNotFoundError."""
    with pytest.raises(ModflowNotFoundError):
        ModflowExecutable(Path("C:/non_existent_directory/mf6.exe")).resolve()


def test_modflow_runner_synthetic_execution(
    temp_workspace: Path, modflow_runner: ModflowRunner
) -> None:
    """Verify end-to-end synthetic simulation execution via ModflowRunner."""
    sim_name = "test_synthetic_sim"
    exe_path = modflow_runner.executable.resolve()

    sim = flopy.mf6.MFSimulation(
        sim_name=sim_name,
        version="mf6",
        exe_name=str(exe_path),
        sim_ws=str(temp_workspace),
    )

    flopy.mf6.ModflowTdis(sim, nper=1, perioddata=[(1.0, 1, 1.0)])
    flopy.mf6.ModflowIms(sim, pname="ims", complexity="SIMPLE")

    gwf = flopy.mf6.ModflowGwf(sim, modelname="gwf_test", save_flows=True)
    flopy.mf6.ModflowGwfdis(gwf, nlay=1, nrow=5, ncol=5, delr=10.0, delc=10.0, top=10.0, botm=0.0)
    flopy.mf6.ModflowGwfnpf(gwf, icelltype=1, k=5.0)
    flopy.mf6.ModflowGwfic(gwf, strt=10.0)

    # Boundaries: col 0 = 10.0, col 4 = 8.0
    chd_data = []
    for r in range(5):
        chd_data.append([(0, r, 0), 10.0])
        chd_data.append([(0, r, 4), 8.0])
    flopy.mf6.ModflowGwfchd(gwf, maxbound=len(chd_data), stress_period_data={0: chd_data})

    flopy.mf6.ModflowGwfoc(
        gwf,
        head_filerecord="gwf_test.hds",
        budget_filerecord="gwf_test.cbc",
        saverecord=[("HEAD", "ALL"), ("BUDGET", "ALL")],
    )

    sim.write_simulation()

    result = modflow_runner.run_simulation(temp_workspace, simulation_name=sim_name)

    assert result.status == SimulationStatus.CONVERGED
    assert result.converged is True
    assert result.exit_code == 0

    hds_path = temp_workspace / "gwf_test.hds"
    assert hds_path.is_file()

    hds = flopy.utils.HeadFile(str(hds_path))
    heads = hds.get_data()
    hds.close()

    assert heads.shape == (1, 5, 5)
    assert not np.isnan(heads).any()
    assert np.isclose(heads[0, :, 0].mean(), 10.0, atol=1e-3)
    assert np.isclose(heads[0, :, 4].mean(), 8.0, atol=1e-3)
