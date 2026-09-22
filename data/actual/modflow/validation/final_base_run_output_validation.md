# FINAL BASE RUN OUTPUT VALIDATION REPORT — MODFLOW 6.7.0
**Project:** JVC15AMRM004 — Stonehenge 2, Dubai, UAE  
**MODFLOW Version:** 6.7.0  
**Status:** 🟢 PASS

---

## 1. Output Package Audit

| Output File | Generated | Size (Bytes) | Readable | Status |
| :--- | :--- | :--- | :--- | :--- |
| `mfsim.lst` | YES | 140,090 | YES | 0 errors, 0 warnings, Normal Termination |
| `Stonehenge2.lst` | YES | 192,168 | YES | Complete budget tables & iteration reports |
| `Stonehenge2.dis.grb` | YES | 113,780 | YES | Grid definition valid ($5 \times 28 \times 26$) |
| `Stonehenge2.hds` | YES | 58,760 | YES | Binary heads for $t = 7.0\text{ d}$ and $t = 150.0\text{ d}$ |
| `Stonehenge2.cbc` | YES | 255,376 | YES | Complete cell-by-cell budget terms |

---

## 2. Head & Drawdown Validation

### Domain Layer-Wise Statistics ($t = 150.0\text{ days}$)

* **Layer 1 (Aeolian Dune Sand Vadose Zone):**
  - Saturated Cells: $0 / 263$ active cells (Unsaturated cover above water table $+6.25\text{ m DMD}$).
* **Layer 2 (Upper Sandstone):**
  - Saturated Cells: $49 / 263$ (49 perimeter boundary cells held at $+6.25\text{ m DMD}$; interior cells dewatered into Layer 3).
  - Head Range: Min $= +6.2500\text{ m}$, Max $= +6.2500\text{ m}$.
* **Layer 3 (Screened Aquifer — Pumping Horizon):**
  - Saturated Cells: $263 / 263$ ($100\%$ saturated).
  - Head Range: Min $= -59.4860\text{ m DMD}$, Max $= +6.2500\text{ m DMD}$, Mean $= -45.0005\text{ m DMD}$.
  - Drawdown: Min $= 0.0000\text{ m}$, Max $= 65.7360\text{ m}$, Mean $= 51.2505\text{ m}$.
* **Layer 4 (Conglomerate Sandstone):**
  - Saturated Cells: $263 / 263$ ($100\%$ saturated).
  - Head Range: Min $= -23.5736\text{ m DMD}$, Max $= +6.2500\text{ m DMD}$, Mean $= -7.2760\text{ m DMD}$.
  - Drawdown: Min $= 0.0000\text{ m}$, Max $= 29.8236\text{ m}$, Mean $= 13.5260\text{ m}$.
* **Layer 5 (Basal Confining Bed):**
  - Saturated Cells: $263 / 263$ ($100\%$ saturated).
  - Head Range: Min $= +0.6554\text{ m DMD}$, Max $= +6.2500\text{ m DMD}$, Mean $= +4.1118\text{ m DMD}$.
  - Drawdown: Min $= 0.0000\text{ m}$, Max $= 5.5946\text{ m}$, Mean $= 2.1382\text{ m}$.

---

## 3. Pumping Well Final Heads & Drawdowns

All 6 dewatering wells are screened in Layer 3 ($k = 3$).

| Well ID | Grid Coordinate (L, R, C) | P1 Head ($t=7\text{d}$) | P1 Drawdown | P2 Head ($t=150\text{d}$) | P2 Drawdown | Simulated Rate P1 | Simulated Rate P2 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **DW-01** | (3, 10, 14) | $-120.10\text{ m}$ | $126.35\text{ m}$ | $-56.93\text{ m}$ | $63.18\text{ m}$ | $-372.0\text{ m}^3/\text{d}$ | $-186.0\text{ m}^3/\text{d}$ |
| **DW-02** | (3, 12, 18) | $-118.59\text{ m}$ | $124.84\text{ m}$ | $-56.17\text{ m}$ | $62.42\text{ m}$ | $-372.0\text{ m}^3/\text{d}$ | $-186.0\text{ m}^3/\text{d}$ |
| **DW-03** | (3, 16, 18) | $-118.47\text{ m}$ | $124.72\text{ m}$ | $-56.11\text{ m}$ | $62.36\text{ m}$ | $-372.0\text{ m}^3/\text{d}$ | $-186.0\text{ m}^3/\text{d}$ |
| **DW-04** | (3, 18, 14) | $-119.81\text{ m}$ | $126.06\text{ m}$ | $-56.78\text{ m}$ | $63.03\text{ m}$ | $-372.0\text{ m}^3/\text{d}$ | $-186.0\text{ m}^3/\text{d}$ |
| **DW-05** | (3, 16, 9) | $-120.46\text{ m}$ | $126.71\text{ m}$ | $-57.10\text{ m}$ | $63.35\text{ m}$ | $-372.0\text{ m}^3/\text{d}$ | $-186.0\text{ m}^3/\text{d}$ |
| **DW-06** | (3, 12, 9) | $-119.23\text{ m}$ | $125.48\text{ m}$ | $-56.49\text{ m}$ | $62.74\text{ m}$ | $-372.0\text{ m}^3/\text{d}$ | $-186.0\text{ m}^3/\text{d}$ |
| **Total** | — | — | — | — | — | **$-2,232.0\text{ m}^3/\text{d}$** | **$-1,116.0\text{ m}^3/\text{d}$** |

---

## 4. Water Budget & Mass Balance

* **Stress Period 1 ($t = 7.0\text{ d}$):**
  - Inflow: $\text{CHD} = 2,231.9986\text{ m}^3/\text{d}$, $\text{Storage} = 0.0013789\text{ m}^3/\text{d}$
  - Outflow: $\text{Pumping} = 2,232.0000\text{ m}^3/\text{d}$
  - Net Residual: $-1.9011 \times 10^{-6}\text{ m}^3/\text{d}$ ($0.00\%$ Discrepancy)
* **Stress Period 2 ($t = 150.0\text{ d}$):**
  - Inflow: $\text{CHD} = 1,116.0000\text{ m}^3/\text{d}$
  - Outflow: $\text{Pumping} = 1,116.0000\text{ m}^3/\text{d}$
  - Net Residual: $2.3773 \times 10^{-7}\text{ m}^3/\text{d}$ ($0.00\%$ Discrepancy)

---

## 5. Horizontal Flow Barrier (HFB) Audit

* **Barrier Count:** 246 secant pile wall elements.
* **Vertical Extent:** Layers 1–3 active, Layers 4–5 open.
* **Inactive Exclusions:** 0 exclusions.
* **Hydrogeological Behavior:** Maintained steep hydraulic head gradient between exterior regional aquifer ($+6.25\text{ m DMD}$) and interior dewatered excavation pit.
