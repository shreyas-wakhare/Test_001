# SCENARIO 1 — VERTICAL CROSS-SECTION QA/QC REPORT
**Project:** JVC15AMRM004 — Stonehenge 2  
**Location:** Al Barsha South Fourth, Dubai, UAE  
**Scenario:** Scenario 1 — Base / No Pumping  
**Deliverable Path:** `data/actual/Visualizations/Scenario1(Base No pumping)/Vertical Cross Section/visualization/`  
**Report Date:** 2026-09-21  
**Status:** 🟢 PASS (Full Engineering QA/QC Verification Completed)

---

## 1. Project & Scenario Context

* **Project Title:** 4B+G+10 Residential Building (Stonehenge -2)
* **Plot Number:** `JVC15AMRM004`
* **Scenario:** Scenario 1 — Baseline Hydrogeological Cross-Section (No Pumping)
* **Primary Objective:** Answer the engineering question: *"What is happening below the ground under static baseline conditions?"*

---

## 2. Approved Source-of-Truth Hierarchy

All parameters, layer boundaries, properties, well depths, and engineering levels were extracted exclusively from the four approved project repositories:
1. **Source 1:** [actual_conceptual_model.md](file:///C:/Users/Shreyas-Wakhare/Desktop/TEST_001/data/actual/extracted/actual_conceptual_model.md) (Approved Stratigraphy, Hydrogeology, Geometry)
2. **Source 2:** [PreModflowApproval.md](file:///C:/Users/Shreyas-Wakhare/Desktop/TEST_001/data/actual/extracted/PreModflowApproval.md) (Approved Baseline Parameters & Review Table)
3. **Source 3:** `data/actual/modflow/input/` (`Stonehenge2.dis`, `Stonehenge2.npf`, `Stonehenge2.sto`, `Stonehenge2.wel`, `Stonehenge2.hfb`)
4. **Source 4:** `data/actual/modflow/Scenario1(Base No pumping)/output/` (`Stonehenge2.hds`, `Stonehenge2.cbc`, `Stonehenge2.lst`)

---

## 3. Section Orientation & Generation Methodology

* **Section Classification:** **Hydrostratigraphic Engineering Cross-Section** (Derived from MODFLOW conceptual model geometry, excavation drawings, and wellfield layout; not an unconstrained generic geological sketch).
* **Section Orientation:** Representative West $\to$ East transverse profile ($X = 0.0\text{ m}$ to $X = 70.0\text{ m}$) traversing the excavation footprint ($X = 12.5\text{ m}$ to $X = 57.5\text{ m}$, width $45.0\text{ m}$).
* **Well Projection:** Deepwells DW-01 to DW-06 are projected orthogonally onto the section profile preserving relative spacing and spatial distribution inside the shoring box.
* **Vertical Exaggeration:** $\approx 1.8\times$ (Applied to ensure geological layers and engineering interfaces remain clearly legible without distorting true elevation labels).

---

## 4. Hydrostratigraphic Layer Audit & Properties

All 5 approved hydrostratigraphic layers are vertically delineated and characterized:

| Layer # | Geological / Material Description | Top (m DMD) | Bottom (m DMD) | Thickness (m) | $K_h$ (m/d) | $K_v$ (m/d) | $S_s$ ($1/\text{m}$) | $S_y$ | Hydrogeological Function |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| **L1** | Aeolian Dune Sand / Silt | $+8.25$ | $+6.75$ | $1.5$ | $1.9872$ | $0.8640$ | $1.0 \times 10^{-4}$ | $0.25$ | Unsaturated Vadose Zone Cover |
| **L2** | Upper Weathered Sandstone | $+6.75$ | $-4.75$ | $11.5$ | $4.3200$ | $0.8640$ | $2.5 \times 10^{-5}$ | $0.12$ | Upper Aquifer / Phreatic Water Table |
| **L3** | Moderately Weathered Sandstone | $-4.75$ | $-14.75$ | $10.0$ | $4.3200$ | $0.8640$ | $2.5 \times 10^{-5}$ | $0.12$ | Screened Aquifer / Production Horizon |
| **L4** | Conglomeratic Sandstone | $-14.75$ | $-19.75$ | $5.0$ | $0.50112$ | $0.050112$ | $5.0 \times 10^{-6}$ | $0.08$ | Transition Unit / Open Underflow Bed |
| **L5** | Calcisiltite / Siltstone | $-19.75$ | $-31.75$ | $12.0$ | $4.32 \times 10^{-5}$ | $8.64 \times 10^{-6}$ | $1.0 \times 10^{-6}$ | $0.03$ | Regional Basal Aquitard / Confining Bed |

---

## 5. Engineering & Dewatering Levels Verification

* **Natural Ground / Model Surface:** $+8.25\text{ m DMD}$ ($0.00\text{ m bgl}$)
* **Baseline Static GWL:** $+6.25\text{ m DMD}$ ($2.00\text{ m bgl}$)
* **Scenario 1 Simulated Head:** $+6.2500\text{ m DMD}$ (Horizontal hydrostatic baseline; zero pumping drawdown)
* **General Excavation Level:** $-6.10\text{ m DMD}$ ($14.35\text{ m bgl}$)
* **Deepest Excavation Level:** $-8.00\text{ m DMD}$ ($16.25\text{ m bgl}$, Level 08 elevator/sump pit)
* **Target Dewatering Level:** **$-8.50\text{ m DMD}$** ($16.75\text{ m bgl}$, includes $+0.50\text{ m}$ buffer below deepest formation)
  - *Note:* Labeled explicitly as a **Design Target Reference** — **NOT** an achieved water level under Scenario 1 ($Q=0$).

---

## 6. Shoring & Deepwell Verification

### Secant Pile Cutoff Wall:
- **Location:** 4 sides enclosing excavation pit ($X = 12.5\text{ m}$ West Wall, $X = 57.5\text{ m}$ East Wall).
- **Wall Thickness:** $0.60\text{ m}$ (600 mm diameter interlocking piles).
- **Toe Elevations:** Structural design toes vary by segment ($-9.30, -10.00, -11.65\text{ m DMD}$). In MODFLOW, the cutoff wall (HFB) penetrates completely through Layers 1–3 down to $-14.75\text{ m DMD}$, leaving Layer 4 open for underflow. Both are clearly annotated.

### Dewatering Wellfield (DW-01 to DW-06):
- **Total Depth:** $22.75\text{ m}$ ($+8.25\text{ m}$ to $-14.50\text{ m DMD}$).
- **Blank Casing:** $+8.25\text{ m}$ down to $-7.80\text{ m DMD}$ (Unscreened solid pipe).
- **Intake Screen:** $-7.80\text{ m}$ to $-14.50\text{ m DMD}$ ($6.70\text{ m}$ slotted screen in Layer 3).
- **Pumping Status:** **All 6 deepwells are INACTIVE ($Q = 0.0\text{ m}^3/\text{day}$)**.

---

## 7. QA/QC Compliance Checklist

| Check # | Verification Item | Status | Verification Evidence |
| :---: | :--- | :---: | :--- |
| **1** | All 5 hydrostratigraphic layers represented | **PASS** | Layers 1 to 5 with distinct fills and borders |
| **2** | Layer elevations match approved model | **PASS** | $+8.25, +6.75, -4.75, -14.75, -19.75, -31.75\text{ m DMD}$ |
| **3** | Layer thicknesses match approved geometry | **PASS** | $1.5\text{ m}, 11.5\text{ m}, 10.0\text{ m}, 5.0\text{ m}, 12.0\text{ m}$ |
| **4** | Hydraulic conductivities ($K_h, K_v$) verified | **PASS** | Exact values displayed in legend and annotations |
| **5** | Storage parameters ($S_s, S_y$) verified | **PASS** | Exact values displayed in legend and metadata |
| **6** | Baseline GWL matches source ($+6.25\text{ m DMD}$) | **PASS** | Displayed as horizontal static surface at $+6.25\text{ m}$ |
| **7** | Scenario 1 simulated head matches `.hds` output | **PASS** | Uniform $+6.2500\text{ m DMD}$ across saturated domain |
| **8** | Unsaturated vadose zone delineated | **PASS** | Hatched from $+8.25\text{ m}$ to $+6.25\text{ m DMD}$ |
| **9** | All 6 deepwells shown with screen intervals | **PASS** | DW-01 to DW-06 shown with casing and screen |
| **10** | Deepwells marked as $Q = 0\text{ m}^3/\text{day}$ | **PASS** | Boldly annotated "INACTIVE — Q = 0" |
| **11** | Excavation levels verified | **PASS** | General $-6.10\text{ m}$, Deepest $-8.00\text{ m DMD}$ |
| **12** | Target dewatering level displayed as design reference | **PASS** | Labeled "Design Reference Only — NOT Achieved (Q=0)" |
| **13** | Secant wall geometry & toe levels verified | **PASS** | Structural toes ($-9.3$ to $-11.65\text{ m}$) & MODFLOW toe ($-14.75\text{ m}$) |
| **14** | Open underflow bed in Layer 4 identified | **PASS** | Open horizon annotated beneath shoring toe |
| **15** | Dual Y-axes (Elevation m DMD & Depth m bgl) | **PASS** | Elevation left, Depth right |
| **16** | Zero pumping drawdown / cone shown | **PASS** | Static hydrostatic baseline; no cones or flow vectors |
| **17** | Complete metadata JSON generated | **PASS** | [Scenario1_Vertical_Cross_Section_Metadata.json](file:///C:/Users/Shreyas-Wakhare/Desktop/TEST_001/data/actual/Visualizations/Scenario1%28Base%20No%20pumping%29/Vertical%20Cross%20Section/visualization/Scenario1_Vertical_Cross_Section_Metadata.json) |
| **18** | Zero external / invented values introduced | **PASS** | 100% parameter traceability preserved |

---

## 8. Limitations & Engineering Disclaimers

1. **Hydrostratigraphic Model Representation:** This cross-section illustrates the MODFLOW conceptual model layering and engineering geometry. It represents the idealized layer-cake numerical grid architecture implemented in MODFLOW 6.
2. **Scenario Specificity:** This deliverable represents **Scenario 1 (No-Pumping Static Baseline)**. Dynamic drawdown cones, wellfield interference, and underflow seepage develop only under operational pumping scenarios (Scenario 2).
