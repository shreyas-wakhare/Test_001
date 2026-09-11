"""MODFLOW 6 execution engine with process control and result inspection."""

from __future__ import annotations

import subprocess
import time
from pathlib import Path

from dwex_groundwater.core.types import SimulationResult, SimulationStatus
from dwex_groundwater.exceptions.domain import (
    ModflowConvergenceError,
    ModflowExecutionError,
)
from dwex_groundwater.logging.logger import get_logger
from dwex_groundwater.modflow.executable import ModflowExecutable

logger = get_logger("modflow.runner")


class ModflowRunner:
    """Orchestrates MODFLOW 6 execution in a specified simulation workspace."""

    def __init__(
        self,
        executable: ModflowExecutable | None = None,
        timeout_seconds: int = 300,
    ) -> None:
        self.executable = executable or ModflowExecutable()
        self.timeout_seconds = timeout_seconds

    def run_simulation(
        self,
        workspace: Path,
        simulation_name: str = "simulation",
        check_convergence: bool = True,
    ) -> SimulationResult:
        """Execute mf6.exe inside the designated simulation workspace."""
        workspace = Path(workspace).resolve()
        if not workspace.is_dir():
            raise FileNotFoundError(f"Simulation workspace directory does not exist: {workspace}")

        mf6_path = self.executable.resolve()
        logger.info("Executing MODFLOW 6 simulation '%s' in %s", simulation_name, workspace)

        start_time = time.perf_counter()
        try:
            process = subprocess.run(
                [str(mf6_path)],
                cwd=str(workspace),
                capture_output=True,
                text=True,
                timeout=self.timeout_seconds,
                check=False,
            )
            elapsed_time = time.perf_counter() - start_time
        except subprocess.TimeoutExpired as exc:
            elapsed_time = time.perf_counter() - start_time
            logger.error("Simulation timed out after %s seconds", self.timeout_seconds)
            raise ModflowExecutionError(
                f"MODFLOW 6 execution timed out after {self.timeout_seconds} seconds.",
                details={"workspace": str(workspace), "elapsed_seconds": elapsed_time},
            ) from exc

        stdout = process.stdout
        stderr = process.stderr
        exit_code = process.returncode

        # Identify generated output files
        output_files = [
            p
            for p in workspace.iterdir()
            if p.is_file() and p.suffix.lower() in {".hds", ".cbc", ".cbb", ".lst", ".csv"}
        ]

        # Verify normal termination
        # MODFLOW 6 standard normal completion output includes "Normal termination of simulation."
        normal_termination = (exit_code == 0) and (
            "Normal termination of simulation." in stdout or "normal termination" in stdout.lower()
        )

        if not normal_termination:
            logger.error(
                "MODFLOW simulation '%s' failed with exit code %s", simulation_name, exit_code
            )
            status = SimulationStatus.FAILED
            raise ModflowExecutionError(
                f"MODFLOW 6 simulation failed with exit code {exit_code}.",
                details={
                    "simulation_name": simulation_name,
                    "workspace": str(workspace),
                    "exit_code": exit_code,
                    "stdout_tail": "\n".join(stdout.splitlines()[-10:]),
                    "stderr": stderr,
                },
            )

        converged = True
        if check_convergence:
            # Check listing files or stdout for solver failure messages
            if "FAILED TO CONVERGE" in stdout.upper():
                converged = False
                logger.warning("Simulation finished but failed solver convergence criteria.")
                status = SimulationStatus.NON_CONVERGENT
                raise ModflowConvergenceError(
                    "MODFLOW 6 solver did not converge.",
                    details={"simulation_name": simulation_name, "workspace": str(workspace)},
                )
            status = SimulationStatus.CONVERGED
        else:
            status = SimulationStatus.CONVERGED

        logger.info(
            "MODFLOW 6 simulation '%s' converged successfully in %.2f seconds.",
            simulation_name,
            elapsed_time,
        )

        return SimulationResult(
            simulation_name=simulation_name,
            workspace=workspace,
            status=status,
            exit_code=exit_code,
            execution_time_seconds=elapsed_time,
            converged=converged,
            output_files=output_files,
            stdout_summary="\n".join(stdout.splitlines()[-5:]),
            stderr_summary=stderr,
            metadata={"mf6_version": self.executable.get_version()},
        )
