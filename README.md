# DWEX AI-Assisted Groundwater Modelling System

[![Environment Status](https://img.shields.io/badge/Environment-READY-brightgreen.svg)]()
[![MODFLOW 6](https://img.shields.io/badge/MODFLOW-6.7.0-blue.svg)]()
[![FloPy](https://img.shields.io/badge/FloPy-3.11.0-blue.svg)]()
[![Code Style](https://img.shields.io/badge/code%20style-ruff-black.svg)]()
[![Type Checked](https://img.shields.io/badge/type%20checked-mypy-blue.svg)]()

> **Phase 0: Production-Grade Environment Setup, Configuration & Verification**

An AI-assisted groundwater modelling and environmental engineering platform built on modern scientific Python and the official USGS MODFLOW 6 numerical groundwater physics engine.

---

## 1. System Architecture

```text
Raw Project Data (Borehole logs, Pumping tests, GIS, Water levels)
        │
        ▼
AI Data Inventory & Extraction Engine
        │
        ▼
Structured Engineering Dataset (SQLite / GeoPackage)
        │
        ▼
GIS / CRS Spatial Validation
        │
        ▼
Conceptual Groundwater Model (Layering, Boundary Conditions)
        │
        ▼
Hydrogeologist / Engineer Approval Gate
        │
        ▼
Python Orchestration & FloPy Model Generator
        │
        ▼
MODFLOW 6 Numerical Physics Engine (mf6.exe)
        │
        ▼
Output Simulation Files (.hds binary heads, .cbc cell budgets)
        │
        ▼
Automated QA/QC & Calibration (PEST / Residual Analysis)
        │
        ▼
Visualization & Engineering Deliverables (Contour maps, 3D meshes, Reports)
```

> [!IMPORTANT]
> **Separation of Concerns**: The AI agent orchestrates data extraction, model formulation, QA/QC, and visualization. It **never** fakes or replaces the USGS MODFLOW 6 numerical groundwater physics engine.

---

## 2. Directory Structure

```text
DWEX_AI_Groundwater_Model/
│
├── data/
│   ├── raw/                 # Immutable source files (DOC-20260910-WA0008.pdf, borehole sheets)
│   ├── processed/           # Extracted structured tabular & spatial files
│   └── validated/           # Engineer-approved datasets
│
├── model/
│   ├── input/               # Generated MODFLOW 6 input packages
│   ├── output/              # MODFLOW heads (.hds), budgets (.cbc), listings (.lst)
│   ├── calibration/         # Observation residuals and calibration runs
│   └── scenarios/           # Predictive scenario runs
│
├── src/
│   └── dwex_groundwater/
│       ├── config/          # Pydantic v2 settings & YAML loader
│       ├── core/            # Domain models, units, constants, and types
│       ├── exceptions/      # Hierarchical custom domain exceptions
│       ├── logging/         # Rotating structured file & console logging
│       ├── environment/     # Verification engine & check models
│       ├── modflow/         # ModflowExecutable & ModflowRunner abstraction
│       ├── ingestion/       # [Phase 1] Raw data inventory & hashing
│       ├── extraction/      # [Phase 1] PDF, Word, Excel data extraction
│       ├── validation/      # [Phase 1] CRS and spatial validation
│       ├── conceptual/      # [Phase 2] Hydrostratigraphy & conceptual synthesis
│       ├── calibration/     # [Phase 4] Automated residual & calibration analysis
│       ├── visualization/   # [Phase 5] 2D maps & 3D mesh rendering
│       └── reporting/       # [Phase 6] Technical report compilation
│
├── config/
│   ├── model_config.yaml    # Application & MODFLOW physics settings
│   ├── paths.yaml           # Centralized relative-to-root directory paths
│   ├── validation_rules.yaml# QA/QC tolerance thresholds
│   └── environment_manifest.json # Machine-readable environment stamp
│
├── scripts/
│   ├── verify_environment.py   # Comprehensive environment audit CLI
│   └── smoke_test_modflow.py   # FloPy + mf6.exe synthetic model runner
│
├── tests/
│   ├── conftest.py          # Pytest fixtures and temporary workspaces
│   ├── unit/                # Config, environment, exceptions, and path tests
│   ├── integration/         # MODFLOW 6 synthetic simulation tests
│   └── fixtures/
│
├── outputs/
│   ├── maps/                # Groundwater contour & hydraulic gradient maps
│   ├── graphs/              # Hydrographs & scatter plots
│   ├── 3d/                  # 3D PyVista/VTK hydrogeological meshes
│   └── qa_qc/               # Water balance and solver audit summaries
│
├── reports/                 # Compiled engineering documents
├── logs/                    # Rotating log files
├── tools/
│   └── modflow6/            # Official USGS mf6.exe and companion binaries
│
├── .env.example
├── .gitignore
├── pyproject.toml
├── requirements.txt
└── README.md
```

---

## 3. Installation & Setup

### Prerequisites
- Python 3.11, 3.12, 3.13, or 3.14 (64-bit)
- Windows 10/11 or Windows Server

### Quick Start

1. **Clone/Open repository**:
   ```powershell
   cd DWEX_AI_Groundwater_Model
   ```

2. **Create and activate dedicated virtual environment**:
   ```powershell
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1
   ```

3. **Install dependencies**:
   ```powershell
   pip install -r requirements.txt
   pip install -e . --no-deps
   ```

4. **MODFLOW 6 Binary Setup**:
   The official USGS 64-bit binaries are located under `tools/modflow6/mf6.exe`.
   If downloading on a fresh system, run:
   ```powershell
   python -c "import flopy; flopy.utils.get_modflow(bindir='tools/modflow6')"
   ```

---

## 4. Verification & Testing

### A. Environment Verification
Executes audit of Python runtime, scientific libraries, GIS packages, MODFLOW binaries, filesystem permissions, and configuration loading:

```powershell
.\.venv\Scripts\python scripts\verify_environment.py
```

Expected terminal output:
```text
================================================================
DWEX AI GROUNDWATER MODELLING - ENVIRONMENT VERIFICATION
================================================================
Runtime:
  [PASS] Python Runtime             Python 3.14.3 (64bit)
Scientific Stack:
  [PASS] NumPy                      NumPy 2.5.3
  [PASS] Pandas                     Pandas 3.0.5
  [PASS] SciPy                      SciPy 1.18.1
MODFLOW Stack:
  [PASS] FloPy                      FloPy 3.11.0
  [PASS] MODFLOW 6 Executable       mf6.exe: 6.7.0 02/05/2026 (mf6.exe)
GIS Stack:
  [PASS] GeoPandas                  GeoPandas 1.1.4
  [PASS] Pyogrio                    Pyogrio 0.13.0
  [PASS] Shapely                    Shapely 2.1.2
  [PASS] PyProj                     PyProj 3.8.0
  [PASS] Rasterio                   Rasterio 1.5.1
Visualization:
  [PASS] Matplotlib                 Matplotlib 3.11.1
  [PASS] Plotly                     Plotly 7.0.0
  [PASS] PyVista                    PyVista 0.49.0
Document Stack:
  [PASS] openpyxl                   openpyxl 3.1.5
  [PASS] python-docx                python-docx 1.2.0
  [PASS] pypdf                      pypdf 6.18.0
Configuration:
  [PASS] Pydantic                   Pydantic 2.13.5
  [PASS] PyYAML                     PyYAML 6.0.3
  [PASS] Project Configuration      Loaded paths.yaml, model_config.yaml, and validation_rules.yaml
Filesystem:
  [PASS] Filesystem Directories     All 14 required directories present and writable
Development Tools:
  [PASS] ruff                       ruff executable available
  [PASS] mypy                       mypy executable available
  [PASS] pytest                     pytest executable available
----------------------------------------------------------------
ENVIRONMENT STATUS: READY
----------------------------------------------------------------
```

### B. MODFLOW 6 Numerical Smoke Test
Builds a synthetic 10x10 unconfined aquifer simulation with FloPy, executes `mf6.exe`, reads the binary `.hds` file, and validates the physical hydraulic gradient:

```powershell
.\.venv\Scripts\python scripts\smoke_test_modflow.py
```

Expected output:
```text
================================================================
DWEX GROUNDWATER - MODFLOW 6 NUMERICAL SMOKE TEST
================================================================
[STEP 1] MODFLOW 6 Executable: tools\modflow6\mf6.exe (mf6.exe: 6.7.0 02/05/2026)
[STEP 2] Temporary Workspace: ...
[STEP 3] Writing MODFLOW 6 input files...
[STEP 4] Executing mf6.exe via ModflowRunner...
[STEP 5] Process terminated normally in 0.137s
         Simulation Status: converged
[STEP 6] Validating numerical heads...
         Head array shape: (1, 10, 10)
         West boundary head (col 0): min=45.00, max=45.00
         East boundary head (col 9): min=40.00, max=40.00
         Domain head range: [40.00, 45.00] m
[STEP 7] Hydraulic gradient is physically consistent and monotonic.
----------------------------------------------------------------
MODFLOW 6 SMOKE TEST: PASSED
================================================================
```

### C. Automated Pytest Suite & Coverage
```powershell
.\.venv\Scripts\pytest -v --cov=dwex_groundwater
```

### D. Static Analysis & Linting
```powershell
.\.venv\Scripts\ruff check .
.\.venv\Scripts\ruff format --check .
.\.venv\Scripts\mypy src
```

---

## 5. Configuration Architecture

All paths and physics parameters are managed centrally without hardcoding:

- **`config/paths.yaml`**: Relative project directories (automatically resolved to absolute paths relative to root).
- **`config/model_config.yaml`**: Application mode, MODFLOW solver settings, units, and timeout.
- **`config/validation_rules.yaml`**: Water balance tolerances and strictness flags.
- **`.env` / Environment variables**:
  - `DWEX_ENVIRONMENT`: `development` | `staging` | `production`
  - `DWEX_LOG_LEVEL`: `DEBUG` | `INFO` | `WARNING` | `ERROR`
  - `DWEX_MODFLOW_EXECUTABLE`: Optional custom path to `mf6.exe`
  - `DWEX_PROJECT_ROOT`: Optional override for workspace root directory

---

## 6. Next Recommended Phase

```text
Phase 1 — Raw DWEX Project Data Ingestion, Inventory & MODFLOW-Relevant Data Extraction
```
In Phase 1, we will ingest `DOC-20260910-WA0008.pdf` (and subsequent field documents), cataloging lithological layers, hydraulic conductivity measurements, pumping rates, and observation well heads into a structured SQLite/GeoPackage dataset.
