# Repository Guidelines

## Project Structure & Module Organization

Application code lives in `src/dwex_groundwater/`. Keep domain logic in its existing
area: `config/` for settings and YAML loading, `ingestion/` and `extraction/` for
source data, `validation/` for QA checks, `modflow/` for FloPy/MODFLOW execution,
and `visualization/` and `reporting/` for deliverables. Use `scripts/` for
executable workflows, such as `scripts/actual/build_actual_engineering_dataset.py`.

Configuration belongs in `config/`; do not hard-code paths or physics settings.
Project data is organized by dataset under `data/` (for example, `data/actual/`).
Treat files in `data/*/raw/` as immutable source evidence. Bundled MODFLOW binaries
are in `tools/modflow6/`; do not modify or commit generated model outputs.

## Setup, Build, and Development Commands

Use Python 3.11+ in a virtual environment:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
pip install -e . --no-deps
.\.venv\Scripts\python scripts\verify_environment.py
```

Run `.\.venv\Scripts\python scripts\smoke_test_modflow.py` to exercise FloPy and
the local `mf6.exe`. Run `.\.venv\Scripts\pytest -v --cov=dwex_groundwater` for
the test suite and coverage, `.\.venv\Scripts\ruff check .` for linting,
`.\.venv\Scripts\ruff format --check .` for formatting, and
`.\.venv\Scripts\mypy src` for type checking.

## Coding Style & Naming Conventions

Use four-space indentation, type annotations on functions, `snake_case` for modules,
functions, and variables, and `PascalCase` for classes. Keep lines within the
configured 100-character target where practical. Ruff enforces the project’s import,
bugbear, modernization, and style rules; format changed Python before review. Prefer
`pathlib.Path`, domain exceptions, and the existing structured logger over ad-hoc
paths, generic errors, or `print` statements.

## Testing Guidelines

Place tests in `tests/unit/` or `tests/integration/`, named `test_<feature>.py`, with
functions named `test_<behavior>`. Use fixtures and temporary workspaces so tests do
not alter raw data or persistent model folders. Run the full suite after changes to
configuration, model execution, or data validation; run the smoke test when changing
MODFLOW integration.

## Commits & Pull Requests

The repository currently has only an initial commit, so no established commit format
exists. Use short, imperative subjects such as `Add spatial validation checks`.
Keep commits focused. PRs should explain the engineering impact, list validation
commands run, link the relevant issue or dataset, and include screenshots or sample
outputs when reports, maps, or visualizations change.
