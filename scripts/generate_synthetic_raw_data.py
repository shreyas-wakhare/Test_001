"""Synthetic Raw Project Data Generator.

Creates an internally consistent, physically plausible hydrogeological raw dataset
in data/synthetic_test/raw/ strictly tagged as SYNTHETIC TEST DATA.
"""

from __future__ import annotations

import json
from pathlib import Path

import numpy as np
import pandas as pd
import rasterio
import yaml
from docx import Document
from rasterio.transform import from_bounds


def generate_synthetic_package(target_dir: Path | str) -> dict[str, Path]:
    """Generate all 10 synthetic project input files in target_dir."""
    raw_dir = Path(target_dir).resolve()
    raw_dir.mkdir(parents=True, exist_ok=True)

    crs_str = "EPSG:32633"  # UTM Zone 33N
    min_x, max_x = 500000.0, 501000.0
    min_y, max_y = 2700000.0, 2701000.0

    generated_files: dict[str, Path] = {}

    # 1. project_boundary.geojson
    boundary_path = raw_dir / "project_boundary.geojson"
    boundary_geo = {
        "type": "FeatureCollection",
        "crs": {"type": "name", "properties": {"name": "urn:ogc:def:crs:EPSG::32633"}},
        "features": [
            {
                "type": "Feature",
                "properties": {
                    "project_name": "DWEX Baseline Synthetic Site",
                    "area_m2": 1000000.0,
                    "status": "SYNTHETIC TEST DATA",
                },
                "geometry": {
                    "type": "Polygon",
                    "coordinates": [
                        [
                            [min_x, min_y],
                            [max_x, min_y],
                            [max_x, max_y],
                            [min_x, max_y],
                            [min_x, min_y],
                        ]
                    ],
                },
            }
        ],
    }
    boundary_path.write_text(json.dumps(boundary_geo, indent=2), encoding="utf-8")
    generated_files["project_boundary"] = boundary_path

    # 2. dem.tif (Topography GeoTIFF)
    dem_path = raw_dir / "dem.tif"
    width, height = 40, 40
    # Gentle slope from West (34m) to East (26m)
    x_grid = np.linspace(0, 1, width)
    y_grid = np.linspace(0, 1, height)
    X, Y = np.meshgrid(x_grid, y_grid)
    elevation_data = (34.0 - 8.0 * X + 1.5 * np.sin(Y * np.pi)).astype(np.float32)

    transform = from_bounds(min_x, min_y, max_x, max_y, width, height)
    with rasterio.open(
        dem_path,
        "w",
        driver="GTiff",
        height=height,
        width=width,
        count=1,
        dtype=np.float32,
        crs=crs_str,
        transform=transform,
        nodata=-9999.0,
    ) as dst:
        dst.write(elevation_data, 1)
    generated_files["dem"] = dem_path

    # 3. boreholes.csv
    bh_path = raw_dir / "boreholes.csv"
    bh_records = [
        {
            "borehole_id": "BH-01",
            "x": 500150.0,
            "y": 2700850.0,
            "ground_elevation": 33.2,
            "total_depth": 50.0,
            "layer": 1,
            "lithology": "Alluvial Sand & Gravel",
            "top_elevation": 33.2,
            "bottom_elevation": 10.0,
        },
        {
            "borehole_id": "BH-01",
            "x": 500150.0,
            "y": 2700850.0,
            "ground_elevation": 33.2,
            "total_depth": 50.0,
            "layer": 2,
            "lithology": "Silty Sand & Sandstone",
            "top_elevation": 10.0,
            "bottom_elevation": -15.0,
        },
        {
            "borehole_id": "BH-02",
            "x": 500850.0,
            "y": 2700850.0,
            "ground_elevation": 27.1,
            "total_depth": 45.0,
            "layer": 1,
            "lithology": "Fine Alluvial Sand",
            "top_elevation": 27.1,
            "bottom_elevation": 10.0,
        },
        {
            "borehole_id": "BH-02",
            "x": 500850.0,
            "y": 2700850.0,
            "ground_elevation": 27.1,
            "total_depth": 45.0,
            "layer": 2,
            "lithology": "Fractured Sandstone",
            "top_elevation": 10.0,
            "bottom_elevation": -15.0,
        },
        {
            "borehole_id": "BH-03",
            "x": 500500.0,
            "y": 2700500.0,
            "ground_elevation": 30.0,
            "total_depth": 48.0,
            "layer": 1,
            "lithology": "Medium to Coarse Sand",
            "top_elevation": 30.0,
            "bottom_elevation": 10.0,
        },
        {
            "borehole_id": "BH-03",
            "x": 500500.0,
            "y": 2700500.0,
            "ground_elevation": 30.0,
            "total_depth": 48.0,
            "layer": 2,
            "lithology": "Silty Sand",
            "top_elevation": 10.0,
            "bottom_elevation": -15.0,
        },
        {
            "borehole_id": "BH-04",
            "x": 500200.0,
            "y": 2700200.0,
            "ground_elevation": 32.5,
            "total_depth": 50.0,
            "layer": 1,
            "lithology": "Coarse Sand",
            "top_elevation": 32.5,
            "bottom_elevation": 10.0,
        },
        {
            "borehole_id": "BH-04",
            "x": 500200.0,
            "y": 2700200.0,
            "ground_elevation": 32.5,
            "total_depth": 50.0,
            "layer": 2,
            "lithology": "Bedrock / Sandstone",
            "top_elevation": 10.0,
            "bottom_elevation": -15.0,
        },
        {
            "borehole_id": "BH-05",
            "x": 500800.0,
            "y": 2700200.0,
            "ground_elevation": 26.8,
            "total_depth": 44.0,
            "layer": 1,
            "lithology": "Alluvial Silt & Sand",
            "top_elevation": 26.8,
            "bottom_elevation": 10.0,
        },
        {
            "borehole_id": "BH-05",
            "x": 500800.0,
            "y": 2700200.0,
            "ground_elevation": 26.8,
            "total_depth": 44.0,
            "layer": 2,
            "lithology": "Fractured Sandstone",
            "top_elevation": 10.0,
            "bottom_elevation": -15.0,
        },
    ]
    pd.DataFrame(bh_records).to_csv(bh_path, index=False)
    generated_files["boreholes"] = bh_path

    # 4. hydraulic_properties.xlsx
    hp_path = raw_dir / "hydraulic_properties.xlsx"
    with pd.ExcelWriter(hp_path, engine="openpyxl") as writer:
        df_props = pd.DataFrame(
            [
                {
                    "layer_id": 1,
                    "name": "Alluvial Sand & Gravel",
                    "k_horizontal": 20.0,
                    "k_vertical": 2.0,
                    "specific_yield": 0.20,
                    "specific_storage": 0.0001,
                    "classification": "MEASURED_ESTIMATE",
                    "confidence": "HIGH",
                },
                {
                    "layer_id": 2,
                    "name": "Silty Sand & Sandstone",
                    "k_horizontal": 6.0,
                    "k_vertical": 0.6,
                    "specific_yield": 0.10,
                    "specific_storage": 0.00001,
                    "classification": "ASSUMED",
                    "confidence": "MEDIUM",
                },
            ]
        )
        df_props.to_excel(writer, sheet_name="aquifer_layers", index=False)
    generated_files["hydraulic_properties"] = hp_path

    # 5. groundwater_levels.csv
    gw_path = raw_dir / "groundwater_levels.csv"
    gw_records = [
        {
            "well_id": "OW-01",
            "x": 500200.0,
            "y": 2700800.0,
            "date": "2026-09-01",
            "groundwater_elevation": 30.5,
            "screen_top": 25.0,
            "screen_bottom": 12.0,
            "layer": 1,
            "use": "calibration",
        },
        {
            "well_id": "OW-02",
            "x": 500400.0,
            "y": 2700600.0,
            "date": "2026-09-01",
            "groundwater_elevation": 28.2,
            "screen_top": 24.0,
            "screen_bottom": 11.0,
            "layer": 1,
            "use": "calibration",
        },
        {
            "well_id": "OW-03",
            "x": 500600.0,
            "y": 2700400.0,
            "date": "2026-09-01",
            "groundwater_elevation": 26.5,
            "screen_top": 23.0,
            "screen_bottom": 10.5,
            "layer": 1,
            "use": "calibration",
        },
        {
            "well_id": "OW-04",
            "x": 500800.0,
            "y": 2700200.0,
            "date": "2026-09-01",
            "groundwater_elevation": 24.8,
            "screen_top": 22.0,
            "screen_bottom": 10.0,
            "layer": 1,
            "use": "calibration",
        },
        {
            "well_id": "OW-05",
            "x": 500300.0,
            "y": 2700300.0,
            "date": "2026-09-01",
            "groundwater_elevation": 29.1,
            "screen_top": 24.0,
            "screen_bottom": 11.0,
            "layer": 1,
            "use": "validation",
        },
        {
            "well_id": "OW-06",
            "x": 500700.0,
            "y": 2700700.0,
            "date": "2026-09-01",
            "groundwater_elevation": 25.9,
            "screen_top": 23.0,
            "screen_bottom": 10.5,
            "layer": 1,
            "use": "validation",
        },
    ]
    pd.DataFrame(gw_records).to_csv(gw_path, index=False)
    generated_files["groundwater_levels"] = gw_path

    # 6. pumping_wells.csv
    pw_path = raw_dir / "pumping_wells.csv"
    pw_records = [
        {
            "well_id": "PW-01",
            "x": 500500.0,
            "y": 2700500.0,
            "screen_top": 20.0,
            "screen_bottom": 5.0,
            "pumping_rate": -500.0,
            "unit": "m3/day",
            "start_date": "2026-09-01",
            "end_date": "2026-09-11",
            "layer": 1,
        }
    ]
    pd.DataFrame(pw_records).to_csv(pw_path, index=False)
    generated_files["pumping_wells"] = pw_path

    # 7. recharge.csv
    rch_path = raw_dir / "recharge.csv"
    rch_records = [
        {
            "date": "2026-09-01",
            "recharge_rate": 0.0005,
            "unit": "m/day",
            "notes": "Estimated 182.5 mm/year effective net infiltration",
        }
    ]
    pd.DataFrame(rch_records).to_csv(rch_path, index=False)
    generated_files["recharge"] = rch_path

    # 8. river.geojson
    riv_path = raw_dir / "river.geojson"
    river_geo = {
        "type": "FeatureCollection",
        "crs": {"type": "name", "properties": {"name": "urn:ogc:def:crs:EPSG::32633"}},
        "features": [
            {
                "type": "Feature",
                "properties": {
                    "river_name": "East Regional Canal",
                    "stage_m": 24.0,
                    "riverbed_bottom_m": 22.5,
                    "conductance_m2_day": 50.0,
                },
                "geometry": {
                    "type": "LineString",
                    "coordinates": [
                        [500980.0, 2700000.0],
                        [500990.0, 2700500.0],
                        [500985.0, 2701000.0],
                    ],
                },
            }
        ],
    }
    riv_path.write_text(json.dumps(river_geo, indent=2), encoding="utf-8")
    generated_files["river"] = riv_path

    # 9. project_notes.docx
    doc_path = raw_dir / "project_notes.docx"
    doc = Document()
    doc.add_heading("DWEX Synthetic Baseline Groundwater Project Notes", level=1)
    doc.add_paragraph("SYNTHETIC TEST PROJECT — NOT FIELD MEASURED DATA")
    doc.add_paragraph(
        "This project represents a synthetic 1 km x 1 km alluvial aquifer site. "
        "The ground slopes gently from 34 m a.s.l. in the west to 26 m in the east. "
        "Groundwater flow is regionally driven towards the eastern drainage canal. "
        "A dewatering extraction well PW-01 operates at 500 m3/day in Layer 1."
    )
    doc.save(str(doc_path))
    generated_files["project_notes"] = doc_path

    # 10. model_requirements.yaml
    req_path = raw_dir / "model_requirements.yaml"
    requirements = {
        "model_metadata": {
            "name": "DWEX Synthetic Baseline Model",
            "type": "Groundwater Flow Simulation (GWF)",
            "engine": "MODFLOW 6",
            "crs": crs_str,
            "units": {"length": "meters", "time": "days"},
        },
        "simulation": {
            "steady_state": True,
            "transient_period_days": 10.0,
            "solver": {"outer_dvclose": 1e-5, "inner_dvclose": 1e-5, "complexity": "MODERATE"},
        },
        "qa_qc_thresholds": {
            "max_water_balance_discrepancy_percent": 0.1,
            "target_calibration_rmse_m": 0.5,
        },
    }
    with open(req_path, "w", encoding="utf-8") as f:
        yaml.dump(requirements, f, indent=2)
    generated_files["model_requirements"] = req_path

    # 11. SYNTHETIC_TEST_README.md
    readme_path = raw_dir / "SYNTHETIC_TEST_README.md"
    readme_text = """# Synthetic Groundwater Project Data Package

> **Status:** SYNTHETIC TEST DATA — NOT FIELD MEASURED
> **Coordinate Reference System:** EPSG:32633 (UTM Zone 33N)
> **Units:** Meters, Days, m³/day, m a.s.l.

## Package Inventory
1. `project_boundary.geojson`: 1000m x 1000m model domain polygon
2. `dem.tif`: Ground topography GeoTIFF (34m to 26m a.s.l.)
3. `boreholes.csv`: 5 geological borehole logs defining stratigraphy
4. `hydraulic_properties.xlsx`: Hydrostratigraphic K and storage parameters
5. `groundwater_levels.csv`: 6 monitoring well targets (4 calibration, 2 validation)
6. `pumping_wells.csv`: Dewatering well PW-01 (-500 m³/day)
7. `recharge.csv`: Areal recharge infiltration (0.0005 m/day)
8. `river.geojson`: East canal boundary line
9. `project_notes.docx`: Technical site narrative and notes
10. `model_requirements.yaml`: Simulation configuration specifications
"""
    readme_path.write_text(readme_text, encoding="utf-8")
    generated_files["readme"] = readme_path

    return generated_files


if __name__ == "__main__":
    base_dir = Path(__file__).resolve().parent.parent / "data" / "synthetic_test" / "raw"
    files = generate_synthetic_package(base_dir)
    print(f"Successfully generated {len(files)} synthetic project files in {base_dir}")
