# MODFLOW 6 Base Run Execution Report

## 1. Execution Overview
- **Project**: JVC15AMRM004 — Stonehenge 2 (Dubai, UAE)
- **Model Name**: `Stonehenge2`
- **MODFLOW Executable**: `tools/modflow6/mf6.exe` (Version 6.7.0, 02/05/2026)
- **Execution Working Directory**: `data/actual/modflow/input/`
- **Execution Date**: 2026-09-21
- **Exit Code**: `2` (Execution Failure)
- **Runtime Duration**: `0.0620 s`

## 2. Package Processing Sequence
1. `mfsim.nam` (NAM6) — Opened & Read successfully
2. `Stonehenge2.tdis` (TDIS6) — Opened & Read successfully (2 stress periods: 7d + 143d)
3. `Stonehenge2.nam` (GWF6) — Opened & Read successfully
4. `Stonehenge2.dis` (DIS6) — Opened & Read via `OPEN/CLOSE Stonehenge2_idomain_mask.dat`
5. `Stonehenge2.npf` (NPF6) — Opened & Read successfully
6. `Stonehenge2.sto` (STO6) — Opened & Read successfully
7. `Stonehenge2.ic` (IC6) — Opened & Read successfully
8. `Stonehenge2.oc` (OC6) — Opened & Read successfully
9. `Stonehenge2.wel` (WEL6) — Opened & Read successfully
10. `Stonehenge2.ims` (IMS6) — **PASSED** (Linear solver `INNER_RCLOSE` parsed with zero syntax errors)
11. `Stonehenge2.hfb` (HFB6) — 105 connections flagged as connecting inactive cells due to mask misalignment
12. `Stonehenge2.chd` (CHD6) — **FAILED** (110 errors: `Cell is outside active grid domain`)

## 3. Error Diagnosis & Root Cause
```text
ERROR REPORT:
    1.   Cell is outside active grid domain: (1,2,13)
    2.   Cell is outside active grid domain: (1,3,14)
    ...
  110.   Cell is outside active grid domain: (5,16,3)
  111.          110  errors encountered.

UNIT ERROR REPORT:
  1. ERROR OCCURRED WHILE READING FILE 'Stonehenge2.chd'
```

### Forensic Technical Root Cause:
- **File**: `data/actual/modflow/input/Stonehenge2_idomain_mask.dat`
- **Mechanism**: In MODFLOW 6 `OPEN/CLOSE` external array loading, line 1 of the file contains a header text comment:
  `# Approved-polygon computational mask: 28 rows x 26 columns; 263 active cells.`
- The Fortran free-format array reader read the ASCII characters of line 1 as integer data (`0x20232445 = 538985541`), shifting the entire 2D `IDOMAIN` array in memory by exactly 26 elements (one full row).
- As a consequence, valid boundary cells in `Stonehenge2.chd` and cell pairs in `Stonehenge2.hfb` were mapped against shifted inactive cells (`idomain = 0`), triggering 110 domain boundary errors.

## 4. Governance Action
Per strict Failure Governance rules, no input files were automatically altered during execution. Execution was halted immediately and documented.
