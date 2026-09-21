# MODFLOW 6 Input Traceability and Static Validation

## 1. Source of Truth and Scope

This input package is downstream of:

1. `data/actual/extracted/PreModflowApproval.md` (primary)
2. `data/actual/extracted/actual_conceptual_model.md` (conceptual model)

The source documents were not modified during this synchronization. Model length is
meters, time is days, discharge is m3/day, conductivity is m/day, Ss is 1/m, and Sy
is dimensionless. `mf6.exe` was not executed and no output was generated.

## 2. Package Inventory

| File | Role |
|---|---|
| `mfsim.nam` | Simulation, TDIS, model, and IMS references |
| `Stonehenge2.nam` | DIS, IC, NPF, STO, WEL, CHD, HFB, and OC references |
| `Stonehenge2.tdis` | Two transient periods: 7 and 143 days |
| `Stonehenge2.ims` | Computational solver settings |
| `Stonehenge2.dis` | 5 layers, 28x26 grid, elevations, and polygon mask reference |
| `Stonehenge2_idomain_mask.dat` | 28x26 approved-polygon computational mask, reused by L1-L5 |
| `Stonehenge2.npf` | Layer-specific Kh and Kv/K33 |
| `Stonehenge2.sto` | Layer-specific Ss and Sy |
| `Stonehenge2.ic` | Initial head of +6.25 m DMD |
| `Stonehenge2.wel` | Six Layer-3 wells and two pumping periods |
| `Stonehenge2.chd` | Lateral constant-head boundary at +6.25 m DMD on 49 perimeter cells across all layers |
| `Stonehenge2.hfb` | Horizontal flow barrier for 4-sided secant pile wall on Layers 1, 2, and 3 (HYDCHR = 1.728e-5 day^-1) |
| `Stonehenge2.oc` | Head and budget output-control definitions |

## 3. Layer and Property Mapping

| Layer | Geological unit | Elevation (m DMD) | Kh source -> NPF K (m/day) | Kv source -> NPF K33 (m/day) | Ss source -> STO SS (1/m) | Sy source -> STO SY |
|---|---|---|---:|---:|---:|---:|
| L1 | Aeolian Dune Sand / Silt | +8.25 to +6.75 | 1.9872 -> 1.9872 | 0.864 -> 0.864 | 1.0e-4 -> 1.0e-4 | 0.25 -> 0.25 |
| L2 | Upper Weathered Sandstone | +6.75 to -4.75 | 4.32 -> 4.32 | 0.864 -> 0.864 | 2.5e-5 -> 2.5e-5 | 0.12 -> 0.12 |
| L3 | Moderately Weathered Sandstone | -4.75 to -14.75 | 4.32 -> 4.32 | 0.864 -> 0.864 | 2.5e-5 -> 2.5e-5 | 0.12 -> 0.12 |
| L4 | Conglomeratic Sandstone | -14.75 to -19.75 | 0.50112 -> 0.50112 | 0.050112 -> 0.050112 | 5.0e-6 -> 5.0e-6 | 0.08 -> 0.08 |
| L5 | Calcisiltite / Siltstone | -19.75 to -31.75 | 4.32e-5 -> 4.32e-5 | 8.64e-6 -> 8.64e-6 | 1.0e-6 -> 1.0e-6 | 0.03 -> 0.03 |

All five layers use the same 263-cell approved-polygon mask. `ICELLTYPE` and
`ICONVERT` are implementation choices: L1/L2 are convertible; L3/L4/L5 are confined.
They do not replace the source-defined layer identity or properties.

## 4. Geometry, Groundwater, and Time Mapping

| Source value | MODFLOW representation | Status |
|---|---|---|
| EPSG:3997; origin 486945.0, 2772550.0 | `DIS` XORIGIN/YORIGIN | PASS |
| 1633.18 m2 surveyed polygon | 263 active 2.5 m x 2.5 m cells (1643.75 m2 computational mask) | PASS, documented discretization choice |
| Model top +8.25; bottoms +6.75, -4.75, -14.75, -19.75, -31.75 m DMD | `DIS` TOP/BOTM | PASS |
| Baseline groundwater +6.25 m DMD | `IC` STRT = 6.25 | PASS |
| Regional lateral boundary head +6.25 m DMD | `CHD` (49 perimeter cells per layer x 5 layers = 245 bounds) | PASS (REV-006) |
| Secant pile cutoff wall (168 m; 0.5m thk; K=1e-10 m/s; HYDCHR=1.728e-5 day^-1) | `HFB` (82 interfaces x 3 layers = 246 barriers) | PASS (REV-008, REV-009) |
| 7-day peak pre-drawdown plus 143-day maintenance | `TDIS` periods 1 and 2 | PASS |

## 5. Well Mapping

All wells are in Layer 3, use the approved screen interval -7.80 to -14.50 m DMD,
and map to active mask cells. `WEL` uses MODFLOW extraction sign convention.

| Well | E, N (EPSG:3997) | WEL cell (layer,row,col) | Period 1 | Period 2 |
|---|---|---|---:|---:|
| DW-01 | 486976.438, 2772571.467 | 3, 20, 13 | -372 | -186 |
| DW-02 | 486973.338, 2772582.310 | 3, 16, 12 | -372 | -186 |
| DW-03 | 486961.597, 2772582.131 | 3, 16, 7 | -372 | -186 |
| DW-04 | 486976.158, 2772593.866 | 3, 11, 13 | -372 | -186 |
| DW-05 | 486976.572, 2772606.274 | 3, 6, 13 | -372 | -186 |
| DW-06 | 486995.809, 2772586.338 | 3, 14, 21 | -372 | -186 |

Rates are m3/day: Period 1 is -372 per well (2232 total) and Period 2 is -186 per
well (1116 total). These equal the approved 15.5 and 7.75 m3/hr per well.

## 6. Boundary, Recharge, and Deferred Items

The lateral constant-head boundary (`CHD`) is applied at +6.25 m DMD along the outer
perimeter cells. The secant pile cutoff wall (`HFB`) is implemented on cell interfaces
between perimeter and interior cells for Layers 1, 2, and 3 down to toe elevations.
Recharge (`RCH`) is intentionally omitted (equivalent to the approved 0 m/day rate).
Regional grid buffer expansion and high-frequency output control remain deferred to Phase 2.

The 28x26 grid, 2.5 m spacing, polygon mask, daily time steps, layer conversion flags,
and IMS settings are explicitly computational implementation choices.

## 7. Corrections and Static Validation

| Pre-correction mismatch | Correction |
|---|---|
| L1, L4, and L5 inactive in `DIS` | Applied the existing approved-polygon mask to all five layers. |
| L1, L4, and L5 K/K33 absent from `NPF` | Added their approved Kh/Kv values in m/day. |
| L1, L4, and L5 SS/SY absent from `STO` | Added their approved Ss/Sy values. |
| Missing lateral boundary (`CHD`) | Added `Stonehenge2.chd` with approved +6.25 m DMD head on perimeter cells. |
| Missing secant pile barrier (`HFB`) | Added `Stonehenge2.hfb` with approved HYDCHR = 1.728e-5 day^-1 on Layers 1-3. |

Static checks: name-file references resolve; `Stonehenge2.chd` and `Stonehenge2.hfb` are registered;
all five NPF/STO arrays have five layer records; all six wells appear in both periods with negative rates;
the mask has 28 rows of 26 values and 263 active cells; and FloPy loads the simulation with zero errors.

## 8. Synchronization Result

| Metric | Result |
|---|---:|
| Engineering parameters checked | 55 |
| Parameters matched after correction | 55 |
| Parameters corrected / implemented | 17 |
| Remaining mismatches | 0 |
| Deferred items (Phase 2) | Regional grid buffer expansion, daily output-control frequency |
| `mf6.exe` executed | No |
| MODFLOW outputs generated | No |

Three-way status: **PASS for all supported inputs**. `PreModflowApproval.md` and
`actual_conceptual_model.md` agree with this MODFLOW input package for layer mapping,
elevations, hydraulic/storage properties, wells, pumping, initial head, CHD boundary,
HFB secant pile barrier, geometry, and schedule. The package is not a simulation result or scientific validation.
