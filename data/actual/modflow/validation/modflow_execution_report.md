# MODFLOW 6 Execution Report

## Simulation Execution Summary
- **Project**: JVC15AMRM004 — Stonehenge 2 (Dubai, UAE)
- **Model Name**: `Stonehenge2`
- **Executable**: `tools/modflow6/mf6.exe` (Version 6.7.0, 02/05/2026)
- **CWD**: `data/actual/modflow/input/`
- **Timestamp**: 2026-09-21
- **Exit Code**: `2` (Execution Failure)
- **Duration**: `0.0606` seconds

## Package Parsing Sequence
1. `mfsim.nam` (NAM6) — Opened & Read successfully
2. `Stonehenge2.tdis` (TDIS6) — Opened & Read successfully (2 stress periods: 7d + 143d)
3. `Stonehenge2.nam` (GWF6) — Opened & Read successfully
4. `Stonehenge2.dis` (DIS6) — Opened & Read successfully (5 layers, 28x26 grid, mask link)
5. `Stonehenge2.npf` (NPF6) — Opened & Read successfully (5-layer Kh/Kv)
6. `Stonehenge2.hfb` (HFB6) — Opened & Read successfully (246 barriers across Layers 1-3)
7. `Stonehenge2.sto` (STO6) — Opened & Read successfully (5-layer Ss/Sy, transient)
8. `Stonehenge2.ic` (IC6) — Opened & Read successfully (STRT = +6.25 m DMD)
9. `Stonehenge2.oc` (OC6) — Opened & Read successfully
10. `Stonehenge2.wel` (WEL6) — Opened & Read successfully (6 wells in Layer 3)
11. `Stonehenge2.chd` (CHD6) — Opened & Read successfully (245 perimeter bounds per period)
12. `Stonehenge2.ims` (IMS) — **FAILED during processing of LINEAR block**

## Error Diagnosis
```text
ERROR REPORT:
  1. Unknown IMSLINEAR keyword (RCLOSE).

UNIT ERROR REPORT:
  1. Error occurred while reading file
     'C:\Users\Shreyas-Wakhare\Desktop\TEST_001\data\actual\modflow\input\Stonehenge2.ims'
```

- **Root Cause**: In MODFLOW 6.7.0, the residual convergence tolerance parameter in the `linear` block of the Iterative Model Solver (IMS) is named `INNER_RCLOSE` (or `RCLOSE_0`), whereas `Stonehenge2.ims` specifies `RCLOSE 1.00000000E-03`.
- **Governance Action**: In accordance with the Master Prompt Failure Handling protocol, model inputs were NOT modified during execution. Execution stopped immediately and this failure report was generated.
