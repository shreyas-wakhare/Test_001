"""Data Extraction Engine.

Extracts spatial, tabular, raster, and document datasets into a canonical
structured engineering dataset preserving complete provenance and source traceability.
"""

from __future__ import annotations

import json
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any, cast

import geopandas as gpd
import numpy as np
import pandas as pd
import rasterio
import yaml
from docx import Document

from dwex_groundwater.logging.logger import get_logger

logger = get_logger("extraction.extractor")


@dataclass
class EngineeringParameter:
    """Canonical parameter container preserving engineering provenance."""

    parameter: str
    value: Any
    unit: str
    source_file: str
    source_record: str
    status: str = "SYNTHETIC"
    classification: str = "MEASURED"
    confidence: str = "HIGH"
    derived: bool = False


class DataExtractor:
    """Extracts raw multi-format datasets into a canonical engineering dataset."""

    def __init__(self, raw_dir: Path | str) -> None:
        self.raw_dir = Path(raw_dir).resolve()

    def extract_vector(self, file_path: Path) -> dict[str, Any]:
        """Extract spatial vector features and metadata."""
        gdf = gpd.read_file(file_path)
        bounds = gdf.total_bounds.tolist()  # [minx, miny, maxx, maxy]
        crs = str(gdf.crs) if gdf.crs else None

        features = []
        for idx, row in gdf.iterrows():
            props = {k: v for k, v in row.items() if k != "geometry"}
            geom_type = row.geometry.geom_type if row.geometry else "None"
            features.append(
                {
                    "record_id": f"{file_path.stem}_{idx}",
                    "geometry_type": geom_type,
                    "properties": props,
                }
            )

        return {
            "source_file": file_path.name,
            "crs": crs,
            "feature_count": len(gdf),
            "bounds": bounds,
            "features": features,
        }

    def extract_raster(self, file_path: Path) -> dict[str, Any]:
        """Extract spatial raster metadata and elevation statistics."""
        with rasterio.open(file_path) as src:
            data = src.read(1)
            valid_mask = (
                data != src.nodata if src.nodata is not None else np.ones_like(data, dtype=bool)
            )
            valid_data = data[valid_mask]

            return {
                "source_file": file_path.name,
                "crs": str(src.crs) if src.crs else None,
                "width": src.width,
                "height": src.height,
                "bounds": [src.bounds.left, src.bounds.bottom, src.bounds.right, src.bounds.top],
                "resolution": [src.res[0], src.res[1]],
                "min_value": float(np.min(valid_data)) if len(valid_data) > 0 else None,
                "max_value": float(np.max(valid_data)) if len(valid_data) > 0 else None,
                "mean_value": float(np.mean(valid_data)) if len(valid_data) > 0 else None,
            }

    def extract_csv(self, file_path: Path) -> list[dict[str, Any]]:
        """Extract tabular records from CSV."""
        df = pd.read_csv(file_path)
        records = cast(list[dict[str, Any]], df.to_dict(orient="records"))
        return records

    def extract_excel(self, file_path: Path) -> dict[str, list[dict[str, Any]]]:
        """Extract sheets and tabular records from Excel."""
        excel_file = pd.ExcelFile(file_path)
        sheets: dict[str, list[dict[str, Any]]] = {}
        for sheet_name in excel_file.sheet_names:
            df = pd.read_excel(excel_file, sheet_name=sheet_name)
            sheets[sheet_name] = cast(list[dict[str, Any]], df.to_dict(orient="records"))
        return sheets

    def extract_docx(self, file_path: Path) -> dict[str, Any]:
        """Extract text and metadata from Word documents."""
        doc = Document(str(file_path))
        paragraphs = [p.text.strip() for p in doc.paragraphs if p.text.strip()]
        return {
            "source_file": file_path.name,
            "paragraphs": paragraphs,
        }

    def extract_yaml(self, file_path: Path) -> dict[str, Any]:
        """Extract structured YAML specifications."""
        with open(file_path, encoding="utf-8") as f:
            data = yaml.safe_load(f)
            return data if isinstance(data, dict) else {}

    def build_engineering_dataset(self, output_path: Path | str) -> dict[str, Any]:
        """Orchestrate multi-format extraction and export structured engineering dataset."""
        logger.info("Extracting engineering dataset from %s", self.raw_dir)

        dataset: dict[str, Any] = {
            "metadata": {
                "project_name": "DWEX Synthetic Baseline Validation Project",
                "status": "SYNTHETIC TEST DATA",
                "source_directory": str(self.raw_dir),
            },
            "domain": {},
            "topography": {},
            "boreholes": [],
            "hydraulic_properties": [],
            "groundwater_levels": [],
            "pumping_wells": [],
            "recharge": [],
            "surface_water": {},
            "specifications": {},
            "provenance_parameters": [],
        }

        # 1. Project Boundary
        boundary_file = self.raw_dir / "project_boundary.geojson"
        if boundary_file.is_file():
            dataset["domain"] = self.extract_vector(boundary_file)

        # 2. Topography DEM
        dem_file = self.raw_dir / "dem.tif"
        if dem_file.is_file():
            dataset["topography"] = self.extract_raster(dem_file)

        # 3. Boreholes
        bh_file = self.raw_dir / "boreholes.csv"
        if bh_file.is_file():
            bh_records = self.extract_csv(bh_file)
            dataset["boreholes"] = bh_records
            for rec in bh_records:
                dataset["provenance_parameters"].append(
                    asdict(
                        EngineeringParameter(
                            parameter="borehole_layer_contact",
                            value={
                                "lithology": rec.get("lithology"),
                                "bottom_elevation": rec.get("bottom_elevation"),
                            },
                            unit="meters a.s.l.",
                            source_file=bh_file.name,
                            source_record=str(rec.get("borehole_id")),
                            classification="MEASURED",
                        )
                    )
                )

        # 4. Hydraulic Properties
        hp_file = self.raw_dir / "hydraulic_properties.xlsx"
        if hp_file.is_file():
            hp_sheets = self.extract_excel(hp_file)
            dataset["hydraulic_properties"] = hp_sheets
            for sheet, records in hp_sheets.items():
                for rec in records:
                    layer_id = rec.get("layer_id", sheet)
                    dataset["provenance_parameters"].append(
                        asdict(
                            EngineeringParameter(
                                parameter="hydraulic_conductivity_horizontal",
                                value=rec.get("k_horizontal"),
                                unit="m/day",
                                source_file=hp_file.name,
                                source_record=f"{sheet}_{layer_id}",
                                classification=rec.get("classification", "ASSUMED"),
                            )
                        )
                    )

        # 5. Groundwater Monitoring Levels
        gw_file = self.raw_dir / "groundwater_levels.csv"
        if gw_file.is_file():
            gw_records = self.extract_csv(gw_file)
            dataset["groundwater_levels"] = gw_records
            for rec in gw_records:
                dataset["provenance_parameters"].append(
                    asdict(
                        EngineeringParameter(
                            parameter="observed_hydraulic_head",
                            value=rec.get("groundwater_elevation"),
                            unit="meters a.s.l.",
                            source_file=gw_file.name,
                            source_record=str(rec.get("well_id")),
                            classification="MEASURED",
                        )
                    )
                )

        # 6. Pumping Wells
        pw_file = self.raw_dir / "pumping_wells.csv"
        if pw_file.is_file():
            pw_records = self.extract_csv(pw_file)
            dataset["pumping_wells"] = pw_records
            for rec in pw_records:
                dataset["provenance_parameters"].append(
                    asdict(
                        EngineeringParameter(
                            parameter="well_pumping_rate",
                            value=rec.get("pumping_rate"),
                            unit="m3/day",
                            source_file=pw_file.name,
                            source_record=str(rec.get("well_id")),
                            classification="DESIGN_SPECIFICATION",
                        )
                    )
                )

        # 7. Recharge
        rch_file = self.raw_dir / "recharge.csv"
        if rch_file.is_file():
            dataset["recharge"] = self.extract_csv(rch_file)

        # 8. Surface Water / River
        river_file = self.raw_dir / "river.geojson"
        if river_file.is_file():
            dataset["surface_water"] = self.extract_vector(river_file)

        # 9. Model Requirements
        req_file = self.raw_dir / "model_requirements.yaml"
        if req_file.is_file():
            dataset["specifications"] = self.extract_yaml(req_file)

        out_path = Path(output_path).resolve()
        out_path.parent.mkdir(parents=True, exist_ok=True)
        with open(out_path, "w", encoding="utf-8") as f:
            json.dump(dataset, f, indent=2)

        logger.info(
            "Saved structured engineering dataset to %s (%d parameters)",
            out_path,
            len(dataset["provenance_parameters"]),
        )
        return dataset
