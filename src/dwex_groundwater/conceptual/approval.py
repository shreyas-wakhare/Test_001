"""Mandatory Project Engineer Approval Gate.

Enforces governance verification before proceeding from conceptual hydrogeology
to numerical FloPy MODFLOW 6 model generation.
"""

from __future__ import annotations

import json
from datetime import UTC, datetime
from pathlib import Path
from typing import Any

from dwex_groundwater.exceptions.domain import ValidationError
from dwex_groundwater.logging.logger import get_logger

logger = get_logger("conceptual.approval")


class ApprovalGate:
    """Manages validation and recording of engineer approval for model generation."""

    def __init__(self, approval_dir: Path | str) -> None:
        self.approval_dir = Path(approval_dir).resolve()
        self.approval_file = self.approval_dir / "conceptual_model_approval.json"

    def is_approved(self) -> bool:
        """Check if a valid approval certificate exists."""
        if not self.approval_file.is_file():
            return False

        try:
            with open(self.approval_file, encoding="utf-8") as f:
                data = json.load(f)
                status = data.get("status", "")
                return status in {"APPROVED", "APPROVED_FOR_SYNTHETIC_TEST"}
        except Exception as exc:
            logger.warning("Error reading approval file: %s", exc)
            return False

    def require_approval(self) -> dict[str, Any]:
        """Ensure approval is granted, or raise ValidationError."""
        if not self.is_approved():
            raise ValidationError(
                "Mandatory Engineer Approval Gate failed: Numerical model compilation cannot proceed without approved conceptual model.",
                details={"approval_file": str(self.approval_file)},
            )
        with open(self.approval_file, encoding="utf-8") as f:
            data: dict[str, Any] = json.load(f)
            return data

    def grant_approval(
        self,
        approved_by: str = "AUTOMATED_TEST_ENGINEER_GATE",
        comments: str = "Approved for synthetic end-to-end software validation testing.",
        is_synthetic: bool = True,
    ) -> dict[str, Any]:
        """Record formal engineer approval artifact."""
        self.approval_dir.mkdir(parents=True, exist_ok=True)
        approval_record = {
            "status": "APPROVED_FOR_SYNTHETIC_TEST",
            "approved_by": approved_by,
            "timestamp_utc": datetime.now(UTC).isoformat(),
            "synthetic": is_synthetic,
            "comments": comments,
        }
        with open(self.approval_file, "w", encoding="utf-8") as f:
            json.dump(approval_record, f, indent=2)

        logger.info("Engineer approval gate successfully recorded at %s", self.approval_file)
        return approval_record
