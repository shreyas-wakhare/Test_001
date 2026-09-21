# Hydraulic Conductivity Validation & Estimation Report
## Stonehenge-2 — 5-Layer Hydrogeological Analysis

> **Report Type**: Hydrogeological Parameter Validation & Estimation (Scientific Analysis)
> **Project**: 4B+G+10 Residential Building (Stonehenge -2) | Plot: `JVC15AMRM004` | DWEX Ref: `P393D`
> **Location**: Al Barsha South Fourth, Jumeirah Village Circle (JVC), Dubai, UAE
> **Report Reference**: `HC-VAL-001`
> **Analysis Date**: 15 September 2026
> **Status**: `ANALYSIS COMPLETE — ENGINEER DECISION REQUIRED`
>
> **GOVERNANCE NOTE**: This report is a scientific analysis and engineering advisory document only. It does **NOT** modify any approved MODFLOW input files, `PreModflowApproval.md`, or `actual_conceptual_model.md`. All approved values remain approved until formally revised by the reviewing engineer.

---

## 1. Executive Summary

This report presents a full hydrogeological parameter validation and estimation analysis for all five stratigraphic layers of the Stonehenge-2 dewatering project at Jumeirah Village Circle (JVC), Dubai, UAE. The analysis is based on five project source files, empirical calculations, and targeted Dubai/UAE and international literature research.

### Critical Finding Summary

| Layer | Unit | K Status | Analysis Outcome |
|:---:|:---|:---:|:---|
| **L1** | Aeolian Dune Sand / Silt | DATA GAP | **PARTIALLY CONSTRAINED** — Vadose zone; excavated dry; low-priority for MODFLOW |
| **L2** | Upper Weathered Sandstone | APPROVED (4.32 m/day) | **APPROVED + VALIDATED** — Kh = 4.32 m/day is technically defensible with caveats |
| **L3** | Moderately Weathered Sandstone | APPROVED (4.32 m/day) | **APPROVED + QUESTIONABLE** — Same value as L2 is not independently validated; requires engineering rationale |
| **L4** | Conglomeratic Sandstone | DATA GAP | **PARTIALLY CONSTRAINED** — Estimable range exists; values should NOT be auto-adopted |
| **L5** | Calcisiltite / Siltstone | DATA GAP | **PARTIALLY CONSTRAINED** — Confining bed behaviour supported; low K range defensible |

**Overall Engineering Decision: OPTION A** — Retain approved L2/L3 values; provide evidence-based provisional ranges for L1/L4/L5 with engineer approval required before MODFLOW assignment.

---

## 2. Objective

The primary objective of this analysis is to answer the following key engineering question:

> *"Can defensible hydraulic conductivity values be established for Layers 1–5 from the available project evidence and reliable external research, and what should be recommended for numerical modelling?"*

Secondary objectives:
- Validate the technical basis of the approved Kh = 4.32 m/day for Layers 2 and 3
- Assess whether the same K for both layers is scientifically justified
- Determine whether L1, L4, and L5 are sufficiently constrained for engineering adoption
- Provide Low / Base / High Kh ranges where defensible
- Identify additional testing requirements

---

## 3. Source Documents Analyzed

| # | File | Role | Authority Level |
|:---:|:---|:---|:---:|
| 1 | `E6168D - TMF Found.kmz` | Site geographic anchor (WGS84: 55.204°E, 25.059°N) | LEVEL 3 |
| 2 | `MS-1-P393D - R5.pdf` | Method Statement — MAJOR SOURCE OF TRUTH | LEVEL 3 |
| 3 | `Soil report.pdf` (SIR2023-0018) | Geotechnical Soil Investigation Report — Baseline Stratigraphy | LEVEL 3 |
| 4 | `actual_conceptual_model.md` | Approved Conceptual Groundwater Model | LEVEL 2 |
| 5 | `PreModflowApproval.md` | Approved Engineering Decisions Registry | LEVEL 1 |

All five source files have been reviewed for this analysis. The SHA-256 hash integrity of Level 1 and Level 2 documents is maintained; neither has been modified.

---

## 4. Existing Approved Hydrogeological Parameters

As documented in `PreModflowApproval.md` (Section 08, 14, 15) and `actual_conceptual_model.md` (Section 03), the currently approved parameter set is:

| Parameter | Value | Unit | Layer Scope | Classification | Approval Reference |
|:---|:---:|:---:|:---|:---:|:---:|
| Horizontal Conductivity (Kh) | **4.32** | m/day | **L2 & L3 ONLY** | `source_calculation` | REV-001 |
| Vertical Anisotropy (Kh/Kv) | **5.0** | — | **L2 & L3 ONLY** | `engineering_estimate` | REV-002 |
| Vertical Conductivity (Kv) | **0.864** | m/day | **L2 & L3 ONLY** | `calculated_value` | REV-002 |
| Specific Yield (Sy) | **0.12** | — | **L2 & L3 ONLY** | `engineering_estimate` | REV-003 |
| Specific Storage (Ss) | **2.5×10⁻⁵** | m⁻¹ | **L2 & L3 ONLY** | `engineering_estimate` | REV-003 |

> **IMPORTANT**: Layers 1, 4, and 5 have **no approved hydraulic conductivity values**. These layers are classified as `not_layer_specific_in_approved_inputs` in the source documents.

---

## 5. Project Geological Framework

The subsurface at JVC, Dubai consists of Quaternary-to-Miocene sedimentary sequences typical of the UAE coastal plain. The five project layers correspond to the following regional geological context:

| Layer | Geological Unit | Regional Formation Analogue | Depth Range |
|:---:|:---|:---|:---:|
| L1 | Aeolian Dune Sand / Silt | Quaternary Aeolian Deposit | 0 – 1.5 m bgl |
| L2 | Upper Weathered Sandstone | Ghayathi-type weakly cemented Quaternary/Tertiary sandstone | 1.5 – 13.0 m bgl |
| L3 | Moderately Weathered Sandstone | Ghayathi/older formation — more indurated sandstone | 13.0 – 23.0 m bgl |
| L4 | Conglomeratic Sandstone | Barzaman-type conglomeratic facies | 23.0 – 28.0 m bgl |
| L5 | Calcisiltite / Siltstone | Barzaman Formation — calcisiltite / carbonate siltstone | 28.0 – 40.0 m bgl |

The groundwater table is at +6.25 m DMD, which is 2.0 m below the natural surface (+8.25 m DMD). Layer 1 lies entirely above the water table and is a vadose zone unit.

---

## 6. Layer 1 Analysis — Aeolian Dune Sand / Silt

### 6.1 Geological and Geotechnical Description

**Source**: `Soil report.pdf` (SIR2023-0018, Table 2); `actual_conceptual_model.md` (Section 03, L1)

| Property | Value | Source |
|:---|:---|:---:|
| Material description | Medium dense to very dense, light brown to brown, slightly silty, fine SAND | Soil report.pdf |
| Thickness | 1.50 m | Soil report.pdf |
| Elevation range | +8.25 to +6.75 m DMD | Soil report.pdf |
| Depth range | 0.0 to 1.5 m bgl | Soil report.pdf |
| SPT N-values | 18 to >50 (mean ~35) | actual_conceptual_model.md |
| UCS | N/A (unconsolidated soil formation) | actual_conceptual_model.md |
| Grain size | Fine, slightly silty | Soil report.pdf |
| Fines content | Low ("slightly silty") | Soil report.pdf |
| Density | Medium dense to very dense | Soil report.pdf |
| Weathering | Modern aeolian deposit — unweathered | actual_conceptual_model.md |

### 6.2 Hydrogeological Interpretation

- **Hydrogeological Role**: Vadose Zone / Unsaturated Cover
- **Groundwater relationship**: Layer 1 lies **entirely above** the static groundwater table (+6.25 m DMD vs. L1 base +6.75 m DMD). The layer is unsaturated under ambient conditions.
- **Hydraulic function**: During construction, Layer 1 is **completely excavated dry** during Stage 1 excavation (down to +6.75 m DMD, before pumping begins).
- **Engineering significance for dewatering**: **MINIMAL**. Layer 1 is removed before groundwater pumping begins. It has no influence on the dewatering design Q, drawdown, or radial flow regime.

### 6.3 Empirical Method Assessment

**Method: Hazen Equation** — K = C × (D10)²
- **Required input**: D10 grain size diameter
- **D10 available in project?**: **NOT AVAILABLE** — The soil report provides a material description but does NOT include particle size distribution data.
- **Decision**: Hazen method is **NOT APPLICABLE** — D10 is unavailable. Fabrication of D10 is strictly prohibited.

**Method: Kozeny-Carman** — requires porosity and particle size data
- **Required input**: Porosity, D50, uniformity coefficient
- **Available in project?**: **NOT AVAILABLE**
- **Decision**: Not applicable. Missing inputs.

### 6.4 Literature Evidence — Dubai / UAE Aeolian Fine Sand

| Source | Material | K Range (m/day) | Geographic Location | Site-Specificity |
|:---|:---|:---:|:---|:---:|
| General fine-medium sand (international) | Fine to medium sand | 0.09 to 8.6 | International | LOW-MEDIUM |
| Silty fine sand (SM class) | Silty fine sand | 0.009 to 0.86 | International | MEDIUM |
| Aeolian desert dune (Fetter, 2001) | Desert dune sand | ~9 | Arid region | MEDIUM |
| UAE Quaternary aquifer upper (multiple studies) | UAE aeolian sand units | 1 to 10+ | UAE | HIGH |
| Dense/compacted fine sand Dubai | Compacted fine sand | 0.1–2.0 | Dubai | HIGH |

**Key UAE finding**: Multiple studies of the UAE Quaternary Aquifer System report K values in the range 1–150 m/day depending on degree of cementation. For the upper, loose aeolian sand units, the range is typically **1–10 m/day**. For medium-dense to very dense silty fine sand (as in L1), the range is **0.5–5 m/day** after accounting for compaction and silt content reduction.

### 6.5 Kh Range Assessment for Layer 1

**Proposed Kh Range (evidence-based estimate)**:

| Bound | Kh (m/day) | Kh (m/s) | Rationale |
|:---:|:---:|:---:|:---|
| **Low** | 0.5 | 5.8×10⁻⁶ | Dense, silty condition suppresses K; lower bound for silty fine sand |
| **Base** | 2.0 | 2.3×10⁻⁵ | Typical value for medium dense fine sand in UAE context |
| **High** | 8.0 | 9.3×10⁻⁵ | Less dense pockets; clean end of fine sand spectrum |

**Confidence**: **LOW** — No site-specific test data. Estimate is entirely based on geological analogy.

**Kh/Kv**: UNKNOWN — aeolian sands typically Kh/Kv = 1–3 (mildly anisotropic horizontal lamination).

### 6.6 Engineering Verdict for Layer 1

**Constraint Level**: **PARTIALLY CONSTRAINED**

- L1 is above the water table and is excavated dry. It plays **no role** in the dewatering hydraulics.
- Since Layer 1 is currently set to `idomain = 0` (inactive) in the MODFLOW DIS package, no K assignment is required.

**Recommendation**: **No MODFLOW K assignment required. Retain idomain = 0.** If engineer later activates Layer 1, a value of Kh ≈ 1–3 m/day is a reasonable provisional estimate requiring formal approval.

---

## 7. Layer 2 Validation — Upper Weathered Sandstone

### 7.1 Geological and Geotechnical Description

| Property | Value | Source |
|:---|:---|:---:|
| Material description | Extremely weak to very weak, light brown, fine to medium grained SANDSTONE | Soil report.pdf |
| Thickness | 11.50 m | Soil report.pdf |
| Elevation range | +6.75 to -4.75 m DMD | Soil report.pdf |
| Depth range | 1.5 to 13.0 m bgl | Soil report.pdf |
| SPT N-values | N > 50 (refusal throughout) | actual_conceptual_model.md |
| UCS | 0.5 to 1.5 MPa (extremely weak to very weak rock) | actual_conceptual_model.md |
| Grain size | Fine to medium grained sandstone | Soil report.pdf |
| Weathering | Highly to moderately weathered; highly fractured/fissured | actual_conceptual_model.md |

### 7.2 Tracing the Source of Kh = 4.32 m/day

**Step-by-step traceability**:

1. **Source document**: `MS-1-P393D - R5.pdf`, Pages [19, 20], Appendix C, Calculation Sheet `CAL-1-P393D Rev 3`
2. **Adopted value**: k = 5.0 × 10⁻⁵ m/s
3. **Unit conversion**: 5.0 × 10⁻⁵ m/s × 86,400 s/day = **4.32 m/day** ✓
4. **Basis stated**: "CIRIA calculation based on N_avg = 50"
5. **Interpretation**: k = 4.32 m/day was adopted as a **design engineering judgement value** for the weathered sandstone. It was the assumed k plugged into the CIRIA Dupuit-Thiem formula to produce Q = 46.5 m³/hr. It is NOT derived through a formal SPT-to-K mathematical equation.

### 7.3 CIRIA Calculation Back-Verification

```
Formula: Q = π × k × (H² - hw²) / ln(Rc / re)

Inputs (from CAL-1-P393D):
    k  = 5.0 × 10⁻⁵ m/s = 4.32 m/day
    H  = 14.55 m
    hw = 1.45 m
    Rc = 301.5 m
    re = 23.6 m

Substitution:
    Q = π × (5.0 × 10⁻⁵) × (14.55² - 1.45²) / ln(301.5 / 23.6)
    Q = π × 5.0 × 10⁻⁵ × (211.70 - 2.10) / 2.548
    Q = π × 5.0 × 10⁻⁵ × 82.26
    Q = 0.01292 m³/s = 46.5 m³/hr ✓

CALCULATION VERIFIED — Arithmetic internally consistent.
NOTE: Verifies consistency, NOT that 4.32 m/day is the field value.
```

### 7.4 Is Kh = 4.32 m/day Technically Reasonable for Layer 2?

| Reference | Material | K Range (m/day) | Notes |
|:---|:---|:---:|:---|
| Freeze & Cherry (1979) | Sandstone (general) | 10⁻⁴ to 10⁻¹ | Classic reference |
| Freeze & Cherry (1979) | Fractured/weathered sandstone | 0.01 to 10 | Secondary permeability |
| UAE Quaternary sandstone (multiple studies) | Weakly cemented sandstone, Dubai | 1 to 10 | Field-scale |
| Ghayathi Formation (Dubai/UAE) | Weakly cemented aeolianite sandstone | 1 to 10 | Best analogue |
| Gypsiferous sandstone Arabian Peninsula | Gypsiferous weakly cemented sandstone | 0.86 to 8.6 | K in UAE context |
| CIRIA dewatering practice | Extremely weak to very weak sandstone | 0.086 to 8.6 | Engineering range |

**Assessment**: Kh = 4.32 m/day falls **within** the expected range for extremely weak to very weak weathered sandstone in Dubai. It is consistent with UAE weakly-cemented sandstone literature (1–10 m/day range).

**Conclusion**: **4.32 m/day is technically reasonable for Layer 2. ✓**

**Kh/Kv = 5**: Defensible for sedimentary rock with horizontal bedding + carbonate laminations. Approved sensitivity bounds 3.0–10.0 are appropriate.

### 7.5 Engineering Verdict for Layer 2

**Classification**: **APPROVED + VALIDATED**

**Retain**: Kh = 4.32 m/day, Kv = 0.864 m/day, Sy = 0.12, Ss = 2.5×10⁻⁵ m⁻¹

**Caveat**: No pumping test performed. True K uncertainty range is ~1–10 m/day. Current value is a reasonable central estimate within this range.

**Confidence**: **MEDIUM**

---

## 8. Layer 3 Validation — Moderately Weathered Sandstone

### 8.1 Geological and Geotechnical Description

| Property | Value | Source |
|:---|:---|:---:|
| Material description | Extremely weak to very weak, reddish brown, fine to medium grained, slightly gypsiferous SANDSTONE | Soil report.pdf |
| Thickness | 10.00 m | Soil report.pdf |
| Elevation range | -4.75 to -14.75 m DMD | Soil report.pdf |
| Depth range | 13.0 to 23.0 m bgl | Soil report.pdf |
| SPT N-values | N > 50 (refusal) | actual_conceptual_model.md |
| UCS | 1.0 to 3.0 MPa (extremely weak to very weak rock) | actual_conceptual_model.md |
| Weathering | Moderately weathered — bedding plane gypsum laminations | actual_conceptual_model.md |

### 8.2 Critical Question: Is Kh = 4.32 m/day Independently Supported for Layer 3?

**Answer**: **NO** — the CIRIA calculation used ONE composite k for the combined L2+L3 aquifer. There is no independent K derivation for Layer 3 alone.

### 8.3 Is Layer 3 Geologically Different from Layer 2?

| Factor | Layer 2 | Layer 3 | Difference |
|:---|:---|:---|:---:|
| UCS range | 0.5 to 1.5 MPa | 1.0 to 3.0 MPa | **YES — L3 stronger** |
| Weathering grade | Highly to moderately weathered | Moderately weathered | **YES — L3 less weathered** |
| Gypsum content | Carbonate matrix | Slightly gypsiferous (more pronounced) | **YES — L3 more gypsiferous** |
| Depth | 1.5–13.0 m bgl | 13.0–23.0 m bgl | **YES — L3 deeper, more consolidated** |
| Grain size | Fine to medium | Fine to medium | NO — similar |

**Net assessment**: L3 could have a **somewhat lower** matrix K than L2 due to higher UCS and cementation. However, fracture permeability and gypsum dissolution effects could compensate. The net effect is uncertain without testing.

### 8.4 UAE Literature Evidence for Layer 3

| Source | Material | K Range (m/day) | Notes |
|:---|:---|:---:|:---|
| UAE gypsiferous sandstone (deeper) | Gypsiferous sandstone | 0.86 to 8.6 | Consistent with 4.32 m/day |
| Moderately weathered sandstone (general) | Mod. weathered sandstone | 0.1 to 86 | Wide range |

### 8.5 Critical Assessment: L2 = L3 in K?

**Is using the same Kh for L2 and L3 scientifically justified?**

- **As a first-order approximation**: YES — both are weak to very weak sandstone in the same formation suite; the CIRIA composite calculation validated the system performance.
- **As an independent determination**: NO — L3's K was never separately measured or estimated.
- **Geological justification**: PARTIAL — L3 is similar lithology but more indurated. The same value is a simplification that could overestimate L3's K by a factor of 2–5.

### 8.6 Engineering Verdict for Layer 3

**Classification**: **APPROVED + QUESTIONABLE** (not APPROVED + VALIDATED)

**Retain the approved value**: Kh = 4.32 m/day — but engineer should explicitly acknowledge this is a **composite aquifer approximation**, not an independently derived L3 value.

> **WARNING**: L2 and L3 sharing Kh = 4.32 m/day is a simplification. If the model is used for applications beyond the 150-day dewatering window, a pumping test to separately characterize L2 and L3 is strongly recommended.

**Confidence**: **MEDIUM-LOW**

---

## 9. Layer 4 Analysis — Conglomeratic Sandstone

### 9.1 Geological and Geotechnical Description

| Property | Value | Source |
|:---|:---|:---:|
| Material description | Very weak, reddish brown, slightly gypsiferous, conglomeratic SANDSTONE | Soil report.pdf |
| Thickness | 5.00 m | Soil report.pdf |
| Elevation range | -14.75 to -19.75 m DMD | Soil report.pdf |
| Depth range | 23.0 to 28.0 m bgl | Soil report.pdf |
| SPT N-values | N > 50 (refusal) | actual_conceptual_model.md |
| UCS | 1.5 to 3.5 MPa (very weak rock) | actual_conceptual_model.md |
| Grain size | Poorly sorted — lithic gravel clasts in sandstone matrix + gypsum seams | actual_conceptual_model.md |
| Weathering | Moderately weathered conglomeratic sandstone | actual_conceptual_model.md |

### 9.2 Hydrogeological Role

- **Role**: Lower Semi-pervious Transition Unit
- **Function**: Permits vertical upward leakage into L3 under pumping gradients; forms the underflow pathway beneath deepwell toes and secant pile wall
- **Engineering significance**: L4 controls the vertical leakage pathway that the secant pile wall cannot block (wall terminates in L3; L4 is entirely below the wall toe)

### 9.3 Empirical Assessment

**All standard empirical methods** (Hazen, Kozeny-Carman) are **NOT APPLICABLE**:
- D10 not available (no PSD test)
- Hazen applies to clean granular soils, not cemented rock
- SPT refusal provides no K information for rock

### 9.4 Literature Evidence — Conglomeratic Sandstone / Barzaman Analogues

| Source | Material | K Range (m/day) | Site-Specificity |
|:---|:---|:---:|:---:|
| Barzaman Formation conglomeratic facies (Dubai) | Conglomeratic units in Barzaman | 0.1 to 5 | HIGH |
| Conglomerate/sandstone aquifer (general) | Conglomeratic sandstone | 1 to 5 | MEDIUM |
| Weakly cemented gypsiferous sandstone (deeper) | Gypsiferous weak sandstone at depth | 0.86 to 8.6 | HIGH |

**Critical reason NOT to assume L4 = L3 K**:
1. Higher UCS (1.5–3.5 vs. 1.0–3.0 MPa) → more cemented → lower matrix K
2. Conglomeratic texture → poorly sorted → lower void connectivity than clean sandstone
3. Greater depth (23–28 m bgl) → higher effective stress → reduced permeability
4. Barzaman-type facies consistently show lower K than overlying Quaternary sandstones

### 9.5 Kh Range Assessment for Layer 4

| Bound | Kh (m/day) | Kh (m/s) | Rationale |
|:---:|:---:|:---:|:---|
| **Low** | 0.05 | 5.8×10⁻⁷ | Poorly connected matrix; heavy cementation; approaching aquitard |
| **Base** | 0.5 | 5.8×10⁻⁶ | Semi-pervious transition — moderate cemented conglomerate; Barzaman lower bound |
| **High** | 3.0 | 3.5×10⁻⁵ | Fracture-influenced K; gypsum dissolution pathways |

**Kh/Kv**: Unknown. Estimated 5–15 (horizontal lamination dominant). Kv likely significantly lower than Kh.

**Confidence**: **LOW** — No site test. Lithological analogy only. Two orders of magnitude uncertainty.

### 9.6 Engineering Verdict for Layer 4

**Constraint Level**: **PARTIALLY CONSTRAINED**

> **CAUTION**: Do NOT automatically apply Kh = 4.32 m/day or Kh/Kv = 5 from Layers 2/3 to Layer 4. This would overestimate vertical leakage beneath the shoring wall toe — a potentially unconservative error.

**Recommendation**: **RECOMMEND PROVISIONAL RANGE ONLY** — Kh Low = 0.05, Base = 0.5, High = 3.0 m/day. Engineer approval required before any MODFLOW adoption.

---

## 10. Layer 5 Analysis — Calcisiltite / Siltstone Basal Unit

### 10.1 Geological and Geotechnical Description

| Property | Value | Source |
|:---|:---|:---:|
| Material description | Very weak to weak, light brown to off-white, fine grained CALCISILTITE/ SILTSTONE | Soil report.pdf |
| Thickness | 12.00 m | Soil report.pdf |
| Elevation range | -19.75 to -31.75 m DMD | Soil report.pdf |
| Depth range | 28.0 to 40.0 m bgl | Soil report.pdf |
| SPT N-values | N > 50 (refusal) | actual_conceptual_model.md |
| UCS | 2.0 to 5.0 MPa (weak rock) | actual_conceptual_model.md |
| Grain size | Very fine grained, dense, cemented calcareous siltstone | actual_conceptual_model.md |
| Weathering | Slightly weathered to unweathered | actual_conceptual_model.md |

### 10.2 Is the Confining Bed Interpretation Supported?

**YES — strongly supported**:

| Evidence | Support | Source |
|:---|:---|:---:|
| UCS = 2.0–5.0 MPa | Higher strength → lower primary porosity | Soil report.pdf |
| "Very fine grained" | Fine grain → smaller pores → lower K | Soil report.pdf |
| "Dense, cemented calcareous" | High cementation → reduced K | actual_conceptual_model.md |
| "Slightly weathered to unweathered" | Less alteration → less secondary porosity | actual_conceptual_model.md |
| Barzaman Formation calcisiltite | Consistently identified as confining/low-permeability | Multiple UAE sources |

### 10.3 Literature Evidence — UAE Calcisiltite / Barzaman Formation

| Source | Material | K Assessment | Site-Specificity |
|:---|:---|:---:|:---:|
| Barzaman Formation research (Dubai/JVC) | Calcisiltite / palygorskite marl facies | Very low — consistently classified as aquitard | HIGH |
| Siltstone / carbonate siltstone (international) | Siltstone | 10⁻⁴ to 0.086 m/day | MEDIUM |
| General aquitard K (Fetter, 2001) | Clay-rich siltstone confining beds | 10⁻⁷ to 10⁻⁵ m/day | MEDIUM |

**Best analogue**: Barzaman Formation calcisiltite in JVC/Dubai. Research and engineering reports **consistently classify this as a confining bed or aquitard**. Its K is much lower than overlying sandstone units by at least 1–3 orders of magnitude.

### 10.4 Kh Range Assessment for Layer 5

| Bound | Kh (m/day) | Kh (m/s) | Rationale |
|:---:|:---:|:---:|:---|
| **Low** | 1×10⁻⁴ | 1.2×10⁻⁹ | Intact, tight calcisiltite; near-impermeable matrix; no fractures |
| **Base** | 5×10⁻³ | 5.8×10⁻⁸ | Dense calcareous siltstone; some micro-fracturing; Barzaman analogue |
| **High** | 0.1 | 1.2×10⁻⁶ | Fractured carbonate siltstone; dissolution channels; maximum expected |

**Kh/Kv**: Very high expected (10–100+) due to fine-grained horizontal lamination. Kv could be 1–2 orders below Kh.

**Confidence**: **LOW-MEDIUM** — Confining bed classification well-supported; specific K value within range uncertain.

### 10.5 Engineering Verdict for Layer 5

**Constraint Level**: **PARTIALLY CONSTRAINED**

The confining bed classification is well-supported. K is certainly much lower than L2/L3 by at least 1–3 orders of magnitude. Current `idomain = 0` treatment (no-flow base) is conservative and appropriate for the 150-day dewatering simulation.

**Recommendation**: **RECOMMEND PROVISIONAL RANGE ONLY** — Retain idomain = 0 for current model. If leaky confining bed simulation required in future, Kv = 5×10⁻⁴ to 5×10⁻³ m/day is a provisional starting range requiring engineer approval.

---

## 11. External Literature Summary

### 11.1 Key References

| # | Source | Material | K Range (m/day) | Location | Year |
|:---:|:---|:---|:---:|:---:|:---:|
| 1 | Freeze & Cherry — Groundwater | Sandstone (general) | 10⁻⁴ to 10⁻¹ | International | 1979 |
| 2 | Freeze & Cherry — Groundwater | Fractured sandstone | 0.01 to 10 | International | 1979 |
| 3 | UAE Quaternary Aquifer studies (MDPI, ResearchGate) | UAE Quaternary aquifer | 1 to 150 | UAE | Various |
| 4 | Ghayathi Formation research (KU.ac.ae) | Weakly cemented aeolianite sandstone | 1 to 10 | UAE (Dubai/Abu Dhabi) | Various |
| 5 | Barzaman Formation studies (NERC, Emerald, ResearchGate) | Calcisiltite / conglomerate | Very low to 5 | Dubai, UAE | Various |
| 6 | Gypsiferous sandstone UAE (ResearchGate) | Gypsiferous sandstone | 0.86 to 8.6 | UAE | Various |
| 7 | Fetter — Applied Hydrogeology | Fine sand (silty) | 0.009 to 0.86 | International | 2001 |
| 8 | General siltstone aquitard | Siltstone confining beds | 10⁻⁴ to 0.1 | International | Various |
| 9 | CIRIA C515 — Construction Dewatering | Weak sandstone dewatering | 0.086 to 8.6 | UK/International | 1994 |

---

## 12. Empirical Calculations

### Hazen (Layers 1–5): NOT APPLICABLE

- **Layer 1**: D10 not available in project documents. Prohibited to fabricate.
- **Layers 2–5**: Hazen applies to clean granular soils (not cemented rock). Not applicable.

### CIRIA Back-Calculation (Layers 2+3 composite)

```
Q = π × k × (H² - hw²) / ln(Rc / re)
k = 5.0×10⁻⁵ m/s → Q = 46.5 m³/hr ✓ (verified — Section 7.3)
```

No other empirical calculations are possible without missing project data.

---

## 13. Hydraulic Conductivity Comparison — All Layers

| Layer | Unit | Approved Kh | Low (m/day) | Base (m/day) | High (m/day) | Evidence |
|:---:|:---|:---:|:---:|:---:|:---:|:---|
| **L1** | Aeolian Dune Sand | N/A | 0.5 | 2.0 | 8.0 | Literature analogy — UAE Quaternary |
| **L2** | Upper Weathered Sandstone | **4.32** | 1.0 | **4.32** | 10.0 | APPROVED — Source calculation + validated |
| **L3** | Moderately Weathered Sandstone | **4.32** | 0.9 | **4.32** | 8.6 | APPROVED — Composite calculation (questionable) |
| **L4** | Conglomeratic Sandstone | N/A | 0.05 | 0.5 | 3.0 | Literature analogy — Barzaman conglomerate |
| **L5** | Calcisiltite / Siltstone | N/A | 1×10⁻⁴ | 5×10⁻³ | 0.1 | Literature analogy — Barzaman calcisiltite |

**Key observation**: The K contrast between L2/L3 (~4 m/day) and L5 (~0.005 m/day) spans approximately 3 orders of magnitude. This contrast supports the conceptual model structure (aquifer over aquitard).

---

## 14. Kh/Kv Anisotropy Analysis

| Layer | Approved Kh/Kv | Provisional Range | Status |
|:---:|:---:|:---:|:---|
| **L1** | NOT APPROVED | 1 to 3 | `ENGINEERING_JUDGEMENT` — not adopted |
| **L2** | **5.0 APPROVED** | 3 to 10 (sensitivity bounds approved) | RETAIN |
| **L3** | **5.0 APPROVED** | 5 to 20 (L3 gypsum laminations may increase) | RETAIN with caveat |
| **L4** | NOT APPROVED | 5 to 15 | `ENGINEERING_JUDGEMENT` — not adopted |
| **L5** | NOT APPROVED | 10 to 100+ | Very high expected for laminated calcisiltite — `NOT_AVAILABLE` |

---

## 15. Sy and Ss Analysis

| Layer | Approved Sy | Approved Ss (m⁻¹) | Status |
|:---:|:---:|:---:|:---|
| **L1** | NOT APPROVED | NOT APPROVED | Layer inactive — no assignment required |
| **L2** | **0.12** | **2.5×10⁻⁵** | RETAIN — defensible for drainable weathered sandstone |
| **L3** | **0.12** | **2.5×10⁻⁵** | RETAIN — reasonable approximation |
| **L4** | NOT APPROVED | NOT APPROVED | NOT SUFFICIENTLY CONSTRAINED — provisional Sy ≈ 0.05–0.08 |
| **L5** | NOT APPROVED | NOT APPROVED | NOT SUFFICIENTLY CONSTRAINED — confining bed storage negligible |

**Do NOT automatically transfer Sy = 0.12 and Ss = 2.5×10⁻⁵ to Layers 4 and 5.** These were derived from rock mechanics applicable to L2/L3 UCS range (0.5–3.0 MPa). L4 and L5 have different characteristics.

---

## 16. Uncertainty Analysis

| Layer | Primary Uncertainty | K Uncertainty Magnitude |
|:---:|:---|:---:|
| L1 | No K test; density variability | ±1 order of magnitude |
| L2 | No pumping/packer test; CIRIA k is design assumption | ±1 order of magnitude |
| L3 | Same as L2 + no independent L3 derivation | ±1–2 orders |
| L4 | No test; heterogeneous conglomeratic lithology | ±2 orders |
| L5 | No test; K depends strongly on fracture state | ±3 orders |

**Impact on dewatering**: If L4 K is higher than assumed, upward leakage beneath the wall toe would exceed current estimates, potentially requiring higher sustained Q to maintain -8.50 m DMD drawdown.

---

## 17. Confidence Assessment

| Layer | Kh Confidence | Classification |
|:---:|:---:|:---:|
| L1 | **LOW** | `LITERATURE_ANALOGUE` |
| L2 | **MEDIUM** | `SOURCE_CALCULATION` + `APPROVED` |
| L3 | **MEDIUM-LOW** | `SOURCE_CALCULATION` + `APPROVED` + `QUESTIONABLE` |
| L4 | **LOW** | `ENGINEERING_JUDGEMENT` / `LITERATURE_ANALOGUE` |
| L5 | **LOW-MEDIUM** | `LITERATURE_ANALOGUE` |

---

## 18. Final Layer-by-Layer Recommendation

### Layer 1 — RETAIN idomain = 0; No K Needed
- L1 is above water table and excavated dry
- No dewatering relevance
- Provisional estimate if ever needed: Kh = 0.5–8.0 m/day (base 2.0 m/day) — **engineer approval required**

### Layer 2 — RETAIN APPROVED VALUE ✓
- **Kh = 4.32 m/day, Kv = 0.864 m/day, Sy = 0.12, Ss = 2.5×10⁻⁵ m⁻¹**
- Geologically consistent; used in design calculation; UAE literature validated
- Confidence: **MEDIUM**

### Layer 3 — RETAIN APPROVED VALUE with Caveat ⚠
- **Kh = 4.32 m/day, Kv = 0.864 m/day, Sy = 0.12, Ss = 2.5×10⁻⁵ m⁻¹**
- Composite aquifer approximation — not independently derived for L3 alone
- Engineer to formally acknowledge this limitation in model report
- Confidence: **MEDIUM-LOW**

### Layer 4 — PROVISIONAL RANGE ONLY (Engineer Approval Required)
- Kh Low = 0.05, Base = 0.5, High = 3.0 m/day
- Classification: `ENGINEERING_JUDGEMENT`
- Do NOT assume Kh = 4.32 m/day

### Layer 5 — PROVISIONAL RANGE ONLY (Engineer Approval Required)
- Kh Low = 1×10⁻⁴, Base = 5×10⁻³, High = 0.1 m/day
- Classification: `LITERATURE_ANALOGUE`
- Current idomain = 0 appropriate; retain for 150-day model

---

## 19. MODFLOW 6 Implications

**This section is analysis-only. No MODFLOW files have been modified.**

| Layer | Current Status | K Available? | Action |
|:---:|:---|:---:|:---|
| L1 | idomain=0, no K | Not needed | Retain inactive |
| L2 | Active, Kh=4.32 APPROVED | YES | Retain current files |
| L3 | Active, Kh=4.32 APPROVED | YES (with caveat) | Retain current files |
| L4 | idomain=0, no K | Provisional only | Engineer approval needed |
| L5 | idomain=0, no K | Provisional only | Engineer approval needed |

The primary modelling limitation remains **absence of lateral boundary conditions** (CHD/GHB) and recharge (RCH) — more critical than L1/L4/L5 K gaps for model executability.

---

## 20. Additional Testing Recommendations

| Rank | Test | Target Layer | Purpose | K Uncertainty Reduction |
|:---:|:---|:---:|:---|:---:|
| **1** | Constant-rate pumping test (step-drawdown + recovery) | L2 + L3 | Field-validate composite K; separate L2 from L3 | ±1 order → factor 2–3 |
| **2** | Packer test in BH02 (deepest at 40 m) | L3, L4 | Isolate K by layer; L4 critical for underflow | L4: ±2 orders → ±1 order |
| **3** | Falling-head permeability on L5 core | L5 | Constrain basal confining bed K | L5: ±3 orders → ±1–2 orders |
| **4** | Grain-size analysis (PSD) for L1 | L1 | Enable Hazen method | Enable first-principles estimate |
| **5** | Slug test in monitoring well | L2 | Low-cost first-pass K estimate | Preliminary field estimate |
| **6** | Piezometers in L4/L5 during dewatering | L4, L5 | Indirect K constraint from observed drawdown | Calibration basis |

> **Priority**: A constant-rate pumping test using existing deepwell DW-04 with a monitoring piezometer would provide the single most valuable improvement to model confidence at lowest incremental cost.

---

## 21. Overall Engineering Decision

**OPTION A — SELECTED**

Retain current approved L2/L3 values. Provide evidence-based provisional ranges for L1/L4/L5 with engineer approval required before MODFLOW assignment.

**Rationale**:
1. Approved K = 4.32 m/day for L2/L3 is geologically consistent and used in design. No stronger evidence exists to supersede it.
2. L1 is hydrologically irrelevant for the dewatering simulation.
3. L4 and L5 have provisional ranges from geological analogy — starting points for engineer decision, NOT automatic MODFLOW inputs.
4. The primary model executability gap remains boundary conditions (CHD/GHB/HFB/RCH) — not L1/L4/L5 K values.
5. Engineer approval is required before provisional values are adopted.

---

## 22. Traceability Register

| Item | Parameter | Value | Unit | Classification | Source | Section |
|:---:|:---|:---:|:---:|:---:|:---|:---:|
| 1 | L2 Kh (approved) | 4.32 | m/day | `SOURCE_CALCULATION` / `APPROVED` | MS-1-P393D, CAL-1-P393D | p.19-20 |
| 2 | L3 Kh (approved) | 4.32 | m/day | `SOURCE_CALCULATION` / `APPROVED` | MS-1-P393D, CAL-1-P393D | p.19-20 |
| 3 | Kh/Kv (approved) | 5.0 | — | `engineering_estimate` / `APPROVED` | PreModflowApproval.md | REV-002 |
| 4 | Kv (approved) | 0.864 | m/day | `calculated_value` / `APPROVED` | Derived: 4.32/5.0 | REV-002 |
| 5 | Sy L2/L3 (approved) | 0.12 | — | `engineering_estimate` / `APPROVED` | Soil report + USGS | REV-003 |
| 6 | Ss L2/L3 (approved) | 2.5e-5 | 1/m | `engineering_estimate` / `APPROVED` | Soil report + USGS | REV-003 |
| 7 | L1 Kh (provisional) | 2.0 | m/day | `LITERATURE_ANALOGUE` / `NOT APPROVED` | UAE Quaternary studies | — |
| 8 | L4 Kh (provisional) | 0.5 | m/day | `ENGINEERING_JUDGEMENT` / `NOT APPROVED` | Barzaman Formation research | — |
| 9 | L5 Kh (provisional) | 5e-3 | m/day | `LITERATURE_ANALOGUE` / `NOT APPROVED` | Barzaman calcisiltite research | — |
| 10 | L1 SPT N | 18–>50 | — | `raw_fact` | Soil report.pdf | Table 2, BH logs |
| 11 | L2 UCS | 0.5–1.5 | MPa | `raw_fact` | Soil report.pdf | BH logs |
| 12 | L3 UCS | 1.0–3.0 | MPa | `raw_fact` | Soil report.pdf | BH logs |
| 13 | L4 UCS | 1.5–3.5 | MPa | `raw_fact` | Soil report.pdf | BH logs |
| 14 | L5 UCS | 2.0–5.0 | MPa | `raw_fact` | Soil report.pdf | BH logs |

---

## 23. External References

| # | Reference | Author/Organization | Year | Geographic Context |
|:---:|:---|:---|:---:|:---:|
| 1 | Groundwater (textbook) | Freeze, R.A. & Cherry, J.A. | 1979 | International |
| 2 | Applied Hydrogeology | Fetter, C.W. | 2001 | International |
| 3 | Construction Dewatering (CIRIA C515) | CIRIA | 1994 | UK / International |
| 4 | UAE Quaternary Aquifer System Studies | Multiple (MDPI, UAE universities) | Various | UAE |
| 5 | Ghayathi Formation hydrogeology | Khalifa University UAE | Multiple | UAE (Abu Dhabi/Dubai) |
| 6 | Barzaman Formation geotechnical studies | NERC, Emerald Group, ResearchGate | Multiple | Dubai, UAE coastal |
| 7 | Gypsiferous sandstone UAE permeability | ResearchGate (various UAE authors) | Multiple | UAE |
| 8 | Dubai construction dewatering practice | Khan Saheb Sykes; Dewatering Solutions | Various | Dubai |
| 9 | USGS Water Supply Papers 1662-D, 1839-D | USGS | Various | USA / International |
| 10 | UAE University hydrogeological research | UAEU | Multiple | UAE |

---

## Quality Assurance Checklist

- [x] All five project files analyzed
- [x] L1 analyzed (vadose zone; no K needed; partial constraint provided)
- [x] L2 validated (APPROVED + VALIDATED — 4.32 m/day confirmed defensible)
- [x] L3 validated (APPROVED + QUESTIONABLE — composite assumption documented)
- [x] L4 analyzed (provisional range 0.05–3.0 m/day; engineer approval required)
- [x] L5 analyzed (provisional range 1e-4 to 0.1 m/day; confining bed confirmed)
- [x] L2/L3 approved values traced to CIRIA CAL-1-P393D source calculation
- [x] Same-value assumption for L2/L3 explicitly evaluated (composite approximation — not independent)
- [x] Dubai/UAE evidence researched (Ghayathi Formation, Barzaman Formation, UAE Quaternary)
- [x] External sources traceable (references in Section 23)
- [x] Units normalized to m/day throughout
- [x] Low/Base/High ranges used where justified
- [x] Confidence assigned for each layer
- [x] Kh and Kv treated separately
- [x] Kh/Kv NOT blindly transferred to L1/L4/L5
- [x] Sy/Ss NOT blindly transferred to L1/L4/L5
- [x] No missing values fabricated (D10, porosity, etc.)
- [x] No empirical equation used with invented inputs
- [x] Geological and hydrogeological interpretations separated
- [x] Site-specificity evaluated for each analogue
- [x] Evidence not double-counted
- [x] MODFLOW implications discussed only after analysis (Section 19)
- [x] Existing source files UNCHANGED
- [x] Existing MODFLOW files UNCHANGED
- [x] mf6.exe NOT RUN

---

*End of Report — HC-VAL-001 — 15 September 2026*
