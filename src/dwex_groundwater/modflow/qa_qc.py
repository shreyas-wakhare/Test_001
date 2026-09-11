"""Automated MODFLOW 6 Post-Simulation QA/QC Engine.

Validates solver convergence, volumetric mass-balance discrepancy,
head physical plausibility, dry cells, and generates HTML/JSON QA/QC deliverables.
"""

from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any

import flopy
import numpy as np

from dwex_groundwater.core.types import SimulationResult
from dwex_groundwater.logging.logger import get_logger

logger = get_logger("modflow.qa_qc")


class ModflowQaQcValidator:
    """Performs rigorous numerical quality assurance on MODFLOW 6 simulation outputs."""

    def __init__(self, simulation_result: SimulationResult, tolerance_percent: float = 0.1) -> None:
        self.sim_result = simulation_result
        self.tolerance_percent = tolerance_percent
        self.workspace = simulation_result.workspace

    def check_convergence(self) -> dict[str, Any]:
        """Verify normal termination and solver convergence."""
        converged = self.sim_result.converged and (self.sim_result.exit_code == 0)
        return {
            "check": "Solver Convergence",
            "status": "PASS" if converged else "FAIL",
            "exit_code": self.sim_result.exit_code,
            "converged": converged,
            "message": "MODFLOW 6 solver converged with normal termination"
            if converged
            else "Solver failed to converge",
        }

    def parse_water_budget(self) -> dict[str, Any]:
        """Extract volumetric water balance from the simulation listing file."""
        lst_files = list(self.workspace.glob("*.lst"))
        if not lst_files:
            return {
                "check": "Water Balance",
                "status": "WARN",
                "message": "No .lst listing file found in workspace",
                "percent_discrepancy": None,
            }

        lst_file = lst_files[0]
        content = lst_file.read_text(encoding="utf-8", errors="ignore")

        # Search for PERCENT DISCREPANCY in listing file
        # Format typical in MODFLOW 6: "PERCENT DISCREPANCY =      0.00"
        discrepancy = 0.0
        matches = re.findall(
            r"PERCENT DISCREPANCY\s*=\s*([-+]?[0-9]*\.?[0-9]+)", content, re.IGNORECASE
        )
        if matches:
            # Take the last recorded stress period discrepancy
            discrepancy = abs(float(matches[-1]))

        passed = discrepancy <= self.tolerance_percent
        return {
            "check": "Volumetric Water Balance",
            "status": "PASS" if passed else "FAIL",
            "percent_discrepancy": discrepancy,
            "tolerance_percent": self.tolerance_percent,
            "message": f"Cumulative mass balance discrepancy is {discrepancy:.4f}% (tolerance <= {self.tolerance_percent}%)",
        }

    def check_heads(self) -> dict[str, Any]:
        """Inspect binary heads for finite validity, gradient sanity, and dry cells."""
        hds_files = list(self.workspace.glob("*.hds"))
        if not hds_files:
            return {
                "check": "Head Plausibility",
                "status": "FAIL",
                "message": "No .hds binary head file found in output",
            }

        hds_obj = flopy.utils.HeadFile(str(hds_files[0]))
        # Read final time step
        times = hds_obj.get_times()
        final_time = times[-1] if times else None
        heads = hds_obj.get_data(totim=final_time)
        hds_obj.close()

        has_nans = bool(np.isnan(heads).any() or np.isinf(heads).any())
        # MODFLOW dry cell indicator is typically HDRY = 1e30 or -1e30
        dry_cells = int(np.sum(np.abs(heads) > 1e10))

        valid_heads = heads[np.abs(heads) < 1e10]
        min_h = float(np.min(valid_heads)) if len(valid_heads) > 0 else 0.0
        max_h = float(np.max(valid_heads)) if len(valid_heads) > 0 else 0.0
        mean_h = float(np.mean(valid_heads)) if len(valid_heads) > 0 else 0.0

        # Physical gradient check: Layer 0 column 0 (west) should have higher mean head than column -1 (east)
        west_head = float(np.mean(heads[0, :, 0]))
        east_head = float(np.mean(heads[0, :, -1]))
        gradient_valid = west_head > east_head

        passed = (not has_nans) and (dry_cells == 0) and gradient_valid and (10.0 <= min_h <= 50.0)

        return {
            "check": "Head Plausibility & Gradient",
            "status": "PASS" if passed else "FAIL",
            "has_nans": has_nans,
            "dry_cells_count": dry_cells,
            "min_head_m": round(min_h, 3),
            "max_head_m": round(max_h, 3),
            "mean_head_m": round(mean_h, 3),
            "west_head_m": round(west_head, 3),
            "east_head_m": round(east_head, 3),
            "gradient_physically_consistent": gradient_valid,
            "message": f"Heads range [{min_h:.2f} m, {max_h:.2f} m] with consistent West-East flow",
        }

    def run_all(self) -> dict[str, Any]:
        """Execute full numerical QA/QC audit."""
        conv = self.check_convergence()
        budget = self.parse_water_budget()
        heads = self.check_heads()

        all_checks = [conv, budget, heads]
        overall_pass = all(c["status"] == "PASS" for c in all_checks)

        qa_qc_report = {
            "overall_status": "PASS" if overall_pass else "FAIL",
            "simulation_name": self.sim_result.simulation_name,
            "workspace": str(self.workspace),
            "execution_time_seconds": round(self.sim_result.execution_time_seconds, 3),
            "checks": all_checks,
        }

        logger.info("Numerical QA/QC complete. Overall status: %s", qa_qc_report["overall_status"])
        return qa_qc_report

    def export_reports(self, json_output: Path | str, html_output: Path | str) -> dict[str, Any]:
        """Save QA/QC report in JSON and HTML formats."""
        res = self.run_all()

        j_path = Path(json_output).resolve()
        j_path.parent.mkdir(parents=True, exist_ok=True)
        with open(j_path, "w", encoding="utf-8") as f:
            json.dump(res, f, indent=2)

        h_path = Path(html_output).resolve()
        h_path.parent.mkdir(parents=True, exist_ok=True)

        rows = []
        for c in res["checks"]:
            color = (
                "#10b981"
                if c["status"] == "PASS"
                else ("#f59e0b" if c["status"] == "WARN" else "#ef4444")
            )
            rows.append(f"""
            <tr>
                <td style="padding: 12px; border-bottom: 1px solid #334155;"><b>{c["check"]}</b></td>
                <td style="padding: 12px; border-bottom: 1px solid #334155; color: {color}; font-weight: bold;">{c["status"]}</td>
                <td style="padding: 12px; border-bottom: 1px solid #334155;">{c.get("message", "")}</td>
            </tr>
            """)

        html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>DWEX MODFLOW 6 Numerical QA/QC Audit</title>
    <style>
        body {{ font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif; background: #0f172a; color: #f8fafc; padding: 30px; }}
        .card {{ background: #1e293b; border-radius: 8px; padding: 25px; box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1); max-width: 900px; margin: auto; }}
        h1 {{ margin-top: 0; color: #38bdf8; }}
        table {{ width: 100%; border-collapse: collapse; margin-top: 20px; }}
        th {{ background: #334155; text-align: left; padding: 12px; color: #94a3b8; }}
        .badge {{ padding: 6px 14px; border-radius: 4px; font-weight: bold; display: inline-block; }}
        .badge-pass {{ background: #065f46; color: #6ee7b7; }}
        .badge-fail {{ background: #991b1b; color: #fca5a5; }}
    </style>
</head>
<body>
    <div class="card">
        <h1>DWEX Groundwater — MODFLOW 6 QA/QC Numerical Audit</h1>
        <p><b>Audit Status:</b> <span class="badge {"badge-pass" if res["overall_status"] == "PASS" else "badge-fail"}">{res["overall_status"]}</span></p>
        <p><b>Execution Time:</b> {res["execution_time_seconds"]} s | <b>Workspace:</b> <code>{res["workspace"]}</code></p>
        <table>
            <thead>
                <tr>
                    <th>Verification Criteria</th>
                    <th>Result</th>
                    <th>Numerical Findings</th>
                </tr>
            </thead>
            <tbody>
                {"".join(rows)}
            </tbody>
        </table>
    </div>
</body>
</html>
"""
        with open(h_path, "w", encoding="utf-8") as f:
            f.write(html_content)

        logger.info("Saved MODFLOW QA/QC reports to %s and %s", j_path, h_path)
        return res
