"""Data Ingestion & Inventory Module.

Discovers raw files, calculates cryptographic fingerprints (SHA-256),
classifies datasets by technical category, and exports a structured data inventory.
"""

from __future__ import annotations

import hashlib
import json
import os
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any

from dwex_groundwater.logging.logger import get_logger

logger = get_logger("ingestion.inventory")


@dataclass
class FileInventoryItem:
    """Metadata record for a discovered raw project file."""

    file_name: str
    relative_path: str
    size_bytes: int
    sha256: str
    category: str
    extension: str
    is_duplicate: bool
    groundwater_relevance: str


class DataInventoryManager:
    """Scans and catalogs raw project files into a canonical inventory."""

    CATEGORY_MAPPING = {
        ".geojson": "Spatial Vector",
        ".shp": "Spatial Vector",
        ".gpkg": "Spatial Vector",
        ".tif": "Spatial Raster",
        ".tiff": "Spatial Raster",
        ".csv": "Tabular",
        ".xlsx": "Tabular",
        ".xls": "Tabular",
        ".pdf": "Document",
        ".docx": "Document",
        ".doc": "Document",
        ".yaml": "Configuration",
        ".yml": "Configuration",
        ".json": "Structured Data",
        ".md": "Documentation",
    }

    RELEVANCE_MAPPING = {
        "boundary": "Model Domain",
        "dem": "Ground Elevation",
        "borehole": "Stratigraphy & Lithology",
        "hydraulic": "Aquifer Properties",
        "level": "Monitoring Heads",
        "water_level": "Monitoring Heads",
        "pumping": "Well Stresses",
        "recharge": "Hydrological Inflow",
        "river": "Surface Water Boundary",
        "requirement": "Model Specification",
        "note": "Site Documentation",
    }

    def __init__(self, raw_data_dir: Path | str) -> None:
        self.raw_data_dir = Path(raw_data_dir).resolve()

    def _compute_sha256(self, file_path: Path) -> str:
        sha256 = hashlib.sha256()
        with open(file_path, "rb") as f:
            for chunk in iter(lambda: f.read(65536), b""):
                sha256.update(chunk)
        return sha256.hexdigest()

    def _determine_relevance(self, filename: str) -> str:
        name_lower = filename.lower()
        for key, relevance in self.RELEVANCE_MAPPING.items():
            if key in name_lower:
                return relevance
        return "General Project Reference"

    def scan(self) -> list[FileInventoryItem]:
        """Discover all files in raw_data_dir and generate inventory records."""
        if not self.raw_data_dir.is_dir():
            raise FileNotFoundError(f"Raw data directory does not exist: {self.raw_data_dir}")

        items: list[FileInventoryItem] = []
        seen_hashes: set[str] = set()

        # Deterministic sorting of files
        for root, _, files in os.walk(self.raw_data_dir):
            for file in sorted(files):
                file_path = Path(root) / file
                if not file_path.is_file():
                    continue

                rel_path = file_path.relative_to(self.raw_data_dir).as_posix()
                size = file_path.stat().st_size
                ext = file_path.suffix.lower()
                sha256 = self._compute_sha256(file_path)

                is_dup = sha256 in seen_hashes
                seen_hashes.add(sha256)

                category = self.CATEGORY_MAPPING.get(ext, "Unclassified")
                relevance = self._determine_relevance(file)

                item = FileInventoryItem(
                    file_name=file,
                    relative_path=rel_path,
                    size_bytes=size,
                    sha256=sha256,
                    category=category,
                    extension=ext,
                    is_duplicate=is_dup,
                    groundwater_relevance=relevance,
                )
                items.append(item)

        logger.info("Scanned %d files in %s", len(items), self.raw_data_dir)
        return items

    def export_inventory(self, output_json_path: Path | str) -> dict[str, Any]:
        """Scan raw directory and export data_inventory.json."""
        items = self.scan()
        out_path = Path(output_json_path).resolve()
        out_path.parent.mkdir(parents=True, exist_ok=True)

        inventory_data = {
            "total_files": len(items),
            "raw_directory": str(self.raw_data_dir),
            "files": [asdict(item) for item in items],
        }

        with open(out_path, "w", encoding="utf-8") as f:
            json.dump(inventory_data, f, indent=2)

        logger.info("Saved data inventory to %s", out_path)
        return inventory_data
