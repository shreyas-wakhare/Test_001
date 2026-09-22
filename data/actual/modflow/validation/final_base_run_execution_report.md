# FINAL BASE RUN EXECUTION REPORT — MODFLOW 6.7.0
**Project:** JVC15AMRM004 — Stonehenge 2, Dubai, UAE  
**Execution Date/Time (UTC):** 2026-09-21  
**MODFLOW Version:** 6.7.0  
**Status:** 🟢 BASE RUN — PASS

---

## 1. Executive Summary

The production BASE MODFLOW 6 simulation for **JVC15AMRM004 — Stonehenge 2** has successfully completed the full **150-day transient simulation** (150 time steps across 2 stress periods) with normal termination, zero numerical convergence failures, 0.00% water budget discrepancy, and complete output generation.

All three confirmed compatibility & hydrogeological fixes have been successfully validated:
1. **IMS Linear Solver:** `INNER_RCLOSE 1.00000000E-03` accepted cleanly by MODFLOW 6.7.0.
2. **IDOMAIN Computational Mask:** Header removal resulted in zero domain coordinate offset errors (0 domain errors, 0 HFB exclusions).
3. **CHD Boundary Assignment:** Assigned to saturated aquifer units (Layers 2 through 5: 196 cells per period), completely eliminating the vadose zone elevation conflict (`6.25 < 6.75 m DMD` in Layer 1).

---

## 2. Execution Metrics

| Parameter | Value |
| :--- | :--- |
| **MODFLOW Executable** | `tools/modflow6/mf6.exe` |
| **MODFLOW Engine Version** | `6.7.0` |
| **Working Directory** | `data/actual/modflow/input/` |
| **Execution Exit Code** | `0` (Normal Termination) |
| **Elapsed Runtime** | `0.130 Seconds` |
| **Total Stress Periods** | `2` (Period 1: 7 days, Period 2: 143 days) |
| **Total Time Steps** | `150` (P1: 7 steps, P2: 143 steps) |
| **Total Simulation Time** | `150.0 days` |
| **Solver Warnings / Errors** | `0` |

---

## 3. Package & Boundary Inventory

* **DIS (Discretization):** $5 \text{ layers} \times 28 \text{ rows} \times 26 \text{ columns}$, cell size $2.5\text{ m} \times 2.5\text{ m}$.
* **IDOMAIN:** 263 active cells per layer, 465 inactive cells per layer.
* **CHD (Constant Head):** Saturated boundary heads $+6.25\text{ m DMD}$ across Layers 2–5 ($49 \text{ cells/layer} \times 4 = 196\text{ records}$).
* **WEL (Dewatering Wells):** 6 wells in Layer 3 (DW-01 to DW-06).
  - Stress Period 1 (7 days): $-2,232\text{ m}^3/\text{day}$ ($-372\text{ m}^3/\text{day}$ per well).
  - Stress Period 2 (143 days): $-1,116\text{ m}^3/\text{day}$ ($-186\text{ m}^3/\text{day}$ per well).
* **HFB (Secant Pile Cutoff Wall):** 246 barriers active across Layers 1–3, open for underflow in Layers 4–5. 0 inactive exclusions.

---

## 4. Water Budget Summary

| Metric | Stress Period 1 ($t = 7.0\text{ d}$) | Stress Period 2 ($t = 150.0\text{ d}$) |
| :--- | :--- | :--- |
| **Total IN Rate** | $2,232.0000\text{ m}^3/\text{day}$ | $1,116.0000\text{ m}^3/\text{day}$ |
| **Total OUT Rate** | $2,232.0000\text{ m}^3/\text{day}$ | $1,116.0000\text{ m}^3/\text{day}$ |
| **CHD Inflow Rate** | $2,231.9986\text{ m}^3/\text{day}$ | $1,116.0000\text{ m}^3/\text{day}$ |
| **Storage Inflow Rate** | $0.0013789\text{ m}^3/\text{day}$ | $0.0000\text{ m}^3/\text{day}$ |
| **WEL Pumping Rate** | $-2,232.0000\text{ m}^3/\text{day}$ | $-1,116.0000\text{ m}^3/\text{day}$ |
| **Rate Residual (IN - OUT)** | $-1.9011 \times 10^{-6}\text{ m}^3/\text{day}$ | $2.3773 \times 10^{-7}\text{ m}^3/\text{day}$ |
| **Rate Percent Discrepancy** | **$0.00\%$** | **$0.00\%$** |
| **Cumulative Volume IN** | $15,623.9998\text{ m}^3$ | $175,233.6568\text{ m}^3$ |
| **Cumulative Volume OUT** | $15,624.0000\text{ m}^3$ | $175,233.6568\text{ m}^3$ |
| **Cumulative Percent Discrepancy** | **$0.00\%$** | **$0.00\%$** |

---

## 5. Output Verification

All required binary and text output files were successfully created and verified non-empty:
- `mfsim.lst` (140,090 bytes) — Solver and simulation log
- `Stonehenge2.lst` (192,168 bytes) — Complete model listing log
- `Stonehenge2.dis.grb` (113,780 bytes) — Binary grid output
- `Stonehenge2.hds` (58,760 bytes) — Binary hydraulic heads
- `Stonehenge2.cbc` (255,376 bytes) — Cell-by-cell water budget terms
