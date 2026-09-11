"""Unit tests for calibrator and metrics computation."""

from __future__ import annotations

from dwex_groundwater.calibration.calibrator import ModelCalibrator, ObservationComparison


def test_calibrator_metrics_computation() -> None:
    """Verify RMSE, MAE, R-squared metric calculations."""
    calib = ModelCalibrator({}, "model/calib", "model/val")
    comps = [
        ObservationComparison(
            "W1",
            500200,
            2700800,
            1,
            observed_head=30.0,
            simulated_head=30.2,
            residual=0.2,
            abs_residual=0.2,
            use="calibration",
        ),
        ObservationComparison(
            "W2",
            500400,
            2700600,
            1,
            observed_head=28.0,
            simulated_head=27.9,
            residual=-0.1,
            abs_residual=0.1,
            use="calibration",
        ),
        ObservationComparison(
            "W3",
            500600,
            2700400,
            1,
            observed_head=26.0,
            simulated_head=26.1,
            residual=0.1,
            abs_residual=0.1,
            use="calibration",
        ),
    ]
    metrics = calib.compute_metrics(comps)

    assert metrics["rmse"] > 0.0
    assert metrics["mae"] > 0.0
    assert metrics["r_squared"] > 0.9
    assert metrics["max_abs_residual"] == 0.2
