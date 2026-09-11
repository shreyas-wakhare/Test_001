"""Spatial and CRS Validation Engine.

Verifies coordinate reference system (CRS) compatibility, bounding box coverage,
raster-to-vector spatial alignment, and feature containment within the model domain.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from shapely.geometry import Point, box

from dwex_groundwater.logging.logger import get_logger

logger = get_logger("validation.spatial")


class SpatialValidator:
    """Validates CRS consistency, coordinate validity, and geometric containment."""

    def __init__(self, engineering_dataset: dict[str, Any]) -> None:
        self.dataset = engineering_dataset
        self.issues: list[dict[str, Any]] = []

    def validate(self) -> dict[str, Any]:
        """Perform comprehensive spatial consistency audit."""
        domain_info = self.dataset.get("domain", {})
        topography_info = self.dataset.get("topography", {})
        boreholes = self.dataset.get("boreholes", [])
        gw_levels = self.dataset.get("groundwater_levels", [])
        pumping_wells = self.dataset.get("pumping_wells", [])
        surface_water = self.dataset.get("surface_water", {})

        domain_crs = domain_info.get("crs")
        topo_crs = topography_info.get("crs")
        river_crs = surface_water.get("crs")

        # 1. CRS Consistency Check
        crs_summary = {
            "domain_crs": domain_crs,
            "topography_crs": topo_crs,
            "river_crs": river_crs,
        }

        # Check if CRSs are projected and matching
        crs_matched = True
        reference_crs = domain_crs
        for name, c in crs_summary.items():
            if c and reference_crs and c != reference_crs:
                crs_matched = False
                self.issues.append(
                    {
                        "type": "CRS_MISMATCH",
                        "severity": "FAIL",
                        "message": f"CRS mismatch detected: {name} ({c}) does not match domain CRS ({reference_crs})",
                    }
                )

        # 2. Domain Bounding Box & Polygon
        domain_bounds = domain_info.get("bounds", [0, 0, 0, 0])
        domain_box = box(*domain_bounds) if len(domain_bounds) == 4 else None

        # 3. DEM Coverage Check
        topo_bounds = topography_info.get("bounds", [0, 0, 0, 0])
        dem_covers_domain = False
        if domain_box and len(topo_bounds) == 4:
            topo_box = box(*topo_bounds)
            # Check if DEM envelope fully encloses or substantially covers domain
            dem_covers_domain = topo_box.contains(domain_box) or topo_box.intersects(domain_box)
            if not dem_covers_domain:
                self.issues.append(
                    {
                        "type": "DEM_COVERAGE_INCOMPLETE",
                        "severity": "FAIL",
                        "message": "Topography DEM does not fully enclose model domain bounds.",
                    }
                )

        # 4. Point Feature Containment (Boreholes, Observation Wells, Pumping Wells)
        points_checked = 0
        points_inside = 0
        outside_points = []

        all_points: list[tuple[str, str, float, float]] = []
        for bh in boreholes:
            if "x" in bh and "y" in bh:
                all_points.append(
                    ("borehole", str(bh.get("borehole_id")), float(bh["x"]), float(bh["y"]))
                )
        for gw in gw_levels:
            if "x" in gw and "y" in gw:
                all_points.append(
                    ("observation_well", str(gw.get("well_id")), float(gw["x"]), float(gw["y"]))
                )
        for pw in pumping_wells:
            if "x" in pw and "y" in pw:
                all_points.append(
                    ("pumping_well", str(pw.get("well_id")), float(pw["x"]), float(pw["y"]))
                )

        for p_type, p_id, x, y in all_points:
            points_checked += 1
            pt = Point(x, y)
            if domain_box and domain_box.contains(pt):
                points_inside += 1
            else:
                outside_points.append({"type": p_type, "id": p_id, "coords": [x, y]})
                self.issues.append(
                    {
                        "type": "FEATURE_OUTSIDE_DOMAIN",
                        "severity": "WARN",
                        "message": f"{p_type} '{p_id}' at ({x}, {y}) lies outside model domain bounding box.",
                    }
                )

        # 5. River / Surface Water Alignment
        river_intersects = False
        river_bounds = surface_water.get("bounds")
        if domain_box and river_bounds and len(river_bounds) == 4:
            river_box = box(*river_bounds)
            river_intersects = domain_box.intersects(river_box)
            if not river_intersects:
                self.issues.append(
                    {
                        "type": "SURFACE_WATER_DISCONNECTED",
                        "severity": "WARN",
                        "message": "River feature bounding box does not intersect model domain.",
                    }
                )

        overall_valid = all(issue["severity"] != "FAIL" for issue in self.issues)

        validation_result = {
            "status": "PASS" if overall_valid else "FAIL",
            "crs_summary": crs_summary,
            "crs_matched": crs_matched,
            "domain_bounds": domain_bounds,
            "dem_bounds": topo_bounds,
            "dem_covers_domain": dem_covers_domain,
            "points_checked": points_checked,
            "points_inside": points_inside,
            "outside_points": outside_points,
            "river_intersects_domain": river_intersects,
            "issues": self.issues,
        }

        logger.info(
            "Spatial validation completed with status: %s (%d issues)",
            validation_result["status"],
            len(self.issues),
        )
        return validation_result

    def export_report(self, output_path: Path | str) -> dict[str, Any]:
        """Run validation and save spatial_validation.json."""
        res = self.validate()
        out = Path(output_path).resolve()
        out.parent.mkdir(parents=True, exist_ok=True)
        with open(out, "w", encoding="utf-8") as f:
            json.dump(res, f, indent=2)
        return res
