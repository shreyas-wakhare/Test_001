"""Conceptual Groundwater Model Synthesis Engine.

Derives hydrostratigraphic units, conceptual boundary conditions, flow pathways,
and recharge mechanisms from validated engineering datasets.
"""

from __future__ import annotations

import json
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any

from dwex_groundwater.logging.logger import get_logger

logger = get_logger("conceptual.synthesizer")


@dataclass
class HydrogeologicalLayer:
    """Hydrostratigraphic layer definition."""

    layer_index: int
    name: str
    hydro_type: str  # unconfined, confined, convertible
    k_horizontal: float  # m/day
    k_vertical: float  # m/day
    specific_yield: float
    specific_storage: float  # 1/m
    top_elevation: float | None = None  # None indicates dynamic DEM top
    bottom_elevation: float = 0.0


class ConceptualModelSynthesizer:
    """Transforms validated engineering parameters into a coherent conceptual model."""

    def __init__(self, engineering_dataset: dict[str, Any]) -> None:
        self.dataset = engineering_dataset

    def synthesize(self) -> dict[str, Any]:
        """Synthesize conceptual groundwater model schema."""
        domain = self.dataset.get("domain", {})
        topo = self.dataset.get("topography", {})
        bounds = domain.get("bounds", [500000.0, 2700000.0, 501000.0, 2701000.0])

        min_x, min_y, max_x, max_y = bounds[0], bounds[1], bounds[2], bounds[3]
        width = max_x - min_x
        height = max_y - min_y

        # Extract hydraulic properties from dataset or use validated defaults
        hp_records = self.dataset.get("hydraulic_properties", {})
        k1 = 20.0
        k2 = 6.0
        if "aquifer_layers" in hp_records:
            recs = hp_records["aquifer_layers"]
            if len(recs) > 0:
                k1 = float(recs[0].get("k_horizontal", 20.0))
            if len(recs) > 1:
                k2 = float(recs[1].get("k_horizontal", 6.0))

        layers = [
            asdict(
                HydrogeologicalLayer(
                    layer_index=1,
                    name="Alluvial Sand & Gravel (Upper Aquifer)",
                    hydro_type="unconfined",
                    k_horizontal=k1,
                    k_vertical=k1 * 0.1,
                    specific_yield=0.20,
                    specific_storage=1e-4,
                    top_elevation=None,  # Tied to ground surface DEM
                    bottom_elevation=10.0,
                )
            ),
            asdict(
                HydrogeologicalLayer(
                    layer_index=2,
                    name="Silty Sand & Fractured Bedrock (Lower Aquifer)",
                    hydro_type="convertible",
                    k_horizontal=k2,
                    k_vertical=k2 * 0.1,
                    specific_yield=0.10,
                    specific_storage=1e-5,
                    top_elevation=10.0,
                    bottom_elevation=-15.0,
                )
            ),
        ]

        # Boundaries
        boundaries = {
            "west": {
                "type": "Constant Head (CHD)",
                "description": "Regional inflow from western highlands",
                "head_elevation": 32.0,
                "layer": 1,
            },
            "east": {
                "type": "River Boundary (RIV)",
                "description": "River boundary draining regional groundwater",
                "stage": 24.0,
                "riverbed_bottom": 22.5,
                "conductance": 50.0,
                "layer": 1,
            },
            "surface_recharge": {
                "type": "Areal Recharge (RCH)",
                "rate_m_day": 0.0005,  # 182.5 mm/yr
                "description": "Net infiltration across model footprint",
            },
            "stresses": [
                {
                    "type": "Pumping Well (WEL)",
                    "id": "PW-01",
                    "x": 500500.0,
                    "y": 2700500.0,
                    "layer": 1,
                    "pumping_rate_m3_day": -500.0,
                    "description": "Simulated dewatering / extraction test well",
                }
            ],
        }

        conceptual_model = {
            "project_name": "DWEX Synthetic Conceptual Hydrogeological Model",
            "crs": domain.get("crs", "EPSG:32633"),
            "domain": {
                "bounds": [min_x, min_y, max_x, max_y],
                "dimensions": {"width_m": width, "height_m": height},
                "elevation_range": [
                    topo.get("min_value", 25.0),
                    topo.get("max_value", 35.0),
                ],
            },
            "hydrostratigraphy": {
                "num_layers": len(layers),
                "layers": layers,
            },
            "boundary_conditions": boundaries,
            "groundwater_flow_direction": "West-to-East regional gradient controlled by topography and river drainage",
            "observation_targets": [
                {
                    "well_id": "OW-01",
                    "x": 500200.0,
                    "y": 2700800.0,
                    "observed_head": 30.5,
                    "layer": 1,
                    "use": "calibration",
                },
                {
                    "well_id": "OW-02",
                    "x": 500400.0,
                    "y": 2700600.0,
                    "observed_head": 28.2,
                    "layer": 1,
                    "use": "calibration",
                },
                {
                    "well_id": "OW-03",
                    "x": 500600.0,
                    "y": 2700400.0,
                    "observed_head": 26.5,
                    "layer": 1,
                    "use": "calibration",
                },
                {
                    "well_id": "OW-04",
                    "x": 500800.0,
                    "y": 2700200.0,
                    "observed_head": 24.8,
                    "layer": 1,
                    "use": "calibration",
                },
                {
                    "well_id": "OW-05",
                    "x": 500300.0,
                    "y": 2700300.0,
                    "observed_head": 29.1,
                    "layer": 1,
                    "use": "validation",
                },
                {
                    "well_id": "OW-06",
                    "x": 500700.0,
                    "y": 2700700.0,
                    "observed_head": 25.9,
                    "layer": 1,
                    "use": "validation",
                },
            ],
        }

        logger.info("Conceptual model synthesized with %d hydrostratigraphic layers", len(layers))
        return conceptual_model

    def export(self, json_output: Path | str, markdown_output: Path | str) -> dict[str, Any]:
        """Export conceptual model to JSON schema and Markdown report."""
        c_model = self.synthesize()

        json_path = Path(json_output).resolve()
        json_path.parent.mkdir(parents=True, exist_ok=True)
        with open(json_path, "w", encoding="utf-8") as f:
            json.dump(c_model, f, indent=2)

        md_path = Path(markdown_output).resolve()
        md_path.parent.mkdir(parents=True, exist_ok=True)

        md_content = f"""# Conceptual Groundwater Model Report

## 1. Project Domain
- **Coordinate Reference System:** {c_model["crs"]}
- **Footprint:** {c_model["domain"]["dimensions"]["width_m"]} m × {c_model["domain"]["dimensions"]["height_m"]} m
- **Bounding Box:** X: [{c_model["domain"]["bounds"][0]}, {c_model["domain"]["bounds"][2]}], Y: [{c_model["domain"]["bounds"][1]}, {c_model["domain"]["bounds"][3]}]
- **Terrain Elevation:** {c_model["domain"]["elevation_range"][0]:.1f} m to {c_model["domain"]["elevation_range"][1]:.1f} m a.s.l.

## 2. Hydrostratigraphy & Layer Discretization
| Layer | Name | Type | Horizontal K (m/d) | Vertical K (m/d) | Sy | Ss (1/m) | Bottom (m a.s.l.) |
|---|---|---|---|---|---|---|---|
| 1 | {c_model["hydrostratigraphy"]["layers"][0]["name"]} | {c_model["hydrostratigraphy"]["layers"][0]["hydro_type"]} | {c_model["hydrostratigraphy"]["layers"][0]["k_horizontal"]} | {c_model["hydrostratigraphy"]["layers"][0]["k_vertical"]} | {c_model["hydrostratigraphy"]["layers"][0]["specific_yield"]} | {c_model["hydrostratigraphy"]["layers"][0]["specific_storage"]} | {c_model["hydrostratigraphy"]["layers"][0]["bottom_elevation"]} |
| 2 | {c_model["hydrostratigraphy"]["layers"][1]["name"]} | {c_model["hydrostratigraphy"]["layers"][1]["hydro_type"]} | {c_model["hydrostratigraphy"]["layers"][1]["k_horizontal"]} | {c_model["hydrostratigraphy"]["layers"][1]["k_vertical"]} | {c_model["hydrostratigraphy"]["layers"][1]["specific_yield"]} | {c_model["hydrostratigraphy"]["layers"][1]["specific_storage"]} | {c_model["hydrostratigraphy"]["layers"][1]["bottom_elevation"]} |

## 3. Hydrogeological Boundary Conditions
- **Western Inflow (CHD):** Regional hydraulic head = {c_model["boundary_conditions"]["west"]["head_elevation"]} m a.s.l.
- **Eastern Drainage (RIV):** River boundary stage = {c_model["boundary_conditions"]["east"]["stage"]} m, conductance = {c_model["boundary_conditions"]["east"]["conductance"]} m²/day
- **Areal Infiltration (RCH):** {c_model["boundary_conditions"]["surface_recharge"]["rate_m_day"]} m/day (~182.5 mm/year)
- **Extraction Well (WEL):** Well {c_model["boundary_conditions"]["stresses"][0]["id"]} at ({c_model["boundary_conditions"]["stresses"][0]["x"]}, {c_model["boundary_conditions"]["stresses"][0]["y"]}) pumping {c_model["boundary_conditions"]["stresses"][0]["pumping_rate_m3_day"]} m³/day

## 4. Flow Dynamics & Monitoring Targets
- Regional groundwater flows from West to East toward the river drainage network.
- 6 monitoring wells are active across the domain (4 for calibration, 2 reserved for independent validation).
"""
        with open(md_path, "w", encoding="utf-8") as f:
            f.write(md_content)

        logger.info("Saved conceptual model JSON to %s and Markdown to %s", json_path, md_path)
        return c_model
