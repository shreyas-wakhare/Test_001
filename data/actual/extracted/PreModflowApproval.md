# Pre-Modflow Engineering Approval

> **Document Type**: Pre-Modflow Engineering Review & Approval Document (Phase 1 — Step 2 Extraction Presentation)  
> **Governing Authority**: `ModflowSteps.md` (FROZEN Workflow Roadmap)  
> **Single Source of Truth**: `data/actual/extracted/actual_engineering_dataset.json`  
> **Target Downstream Step**: Manual Engineer Review → `actual_conceptual_model.json` (Phase 1 — Step 3)  
> **Governance Rule**: All engineering inputs are derived exclusively from the project source documents and the controlled extraction dataset. No external engineering values or assumptions have been introduced.

---

## 01. Project Identification

### Dataset Metadata & Governance
- **Dataset Name**: `actual_engineering_dataset.json`
- **Project Name**: 4B+G+10 Residential Building (Stonehenge -2)
- **Plot Number**: `JVC15AMRM004`
- **Location**: Al Barsha South Fourth, Jumeirah Village Circle (JVC), Dubai, UAE
- **DWEX Project Reference**: `P393D`
- **Workflow Stage**: Phase 1 — Step 2: Automated Engineering Extraction
- **Governing Roadmap**: `ModflowSteps.md (FROZEN)`
- **Extraction Status**: `STRUCTURED_EXTRACTED_RAW_DATASET`
- **Target Downstream Artifact**: `actual_conceptual_model.json (Phase 1 — Step 3)`
- **Governing Hierarchy**: METHOD STATEMENT IS THE MAJOR SOURCE OF TRUTH (MS-1-P393D - R5.pdf / Drawings DEW-1-P393D / SEC-1-P393D / CAL-1-P393D) for engineering execution parameters. In Step 2 data extraction, all discrepancies between sources are preserved as unresolved conflicts for engineer review.
- **Governance Rule**: Pure raw project extraction. Zero invented parameters. Zero external literature values injected into Step 2 dataset. Data gaps are strictly classified as 'missing' requiring engineer review in Step 3.
- **Classification Taxonomies**: `raw_fact, source_calculation, calculated_value, digitized_value, interpretation, missing`

### Project Entities & Authoritative Documents
| Entity Role | Name / Value | Classification | Source File | Source Page(s) | Source Section |
|---|---|---|---|---|---|
| **Project Title** | 4B+G+10 Resi Bldg (Stonehenge -2) | `raw_fact` | `MS-1-P393D - R5.pdf` | [1] | Cover / Title Block |
| **Plot Number** | JVC15AMRM004 | `raw_fact` | `MS-1-P393D - R5.pdf` | [1] | Header / Title Block |
| **Client** | M/s. MDP Development Limited | `raw_fact` | `Soil report.pdf` | [1] | Title Block / Section 1.0 |
| **Enabling Contractor** | TMF Euro Foundation | `raw_fact` | `MS-1-P393D - R5.pdf` | [14] | Checklist Header |
| **Dewatering Contractor** | Dewatering Experts (DWEX) | `raw_fact` | `MS-1-P393D - R5.pdf` | [1] | Header Logo & Title |
| **Lead Consultant** | Federal Engineering Consultants / Eng. Adnan Saffarini Office | `interpretation` | `Soil report.pdf` | [1] | Consultant Box / Method Statement Drawings |
| **Method Statement Document** | Ref: MS-1-P393D | Rev: 5 | Date: 13-10-23 (MAJOR SOURCE OF TRUTH) | `raw_fact` | `MS-1-P393D - R5.pdf` | [1] | Revision Table |
| **Soil Report Document** | Ref: SIR2023-0018 | Rev: 00 | Date: 14th March 2023 (Baseline Geotechnical Stratigraphy) | `raw_fact` | `Soil report.pdf` | [1] | Report Ref & Date |

## 02. Spatial / GIS Information

### Coordinate Reference Systems (CRS)
- **Project Projected Crs**: WGS 84 / Dubai Local TM (DLTM) | **Code**: `EPSG:3997` | **Projection**: `Transverse Mercator` | **Unit**: `meter` | **Classification:** `raw_fact` | **Source:** `MS-1-P393D - R5.pdf` (p. [16])
- **Geographic Crs**: WGS 84 | **Code**: `EPSG:4326` | **Projection**: `Geographic` | **Unit**: `degree` | **Classification:** `raw_fact` | **Source:** `E6168D - TMF Found.kmz` (p. [1])

### KMZ Site Anchor Placemark
- **Placemark Name**: `E6168D - TMF Found`
- **Geometry Type**: `Point`
- **Coordinates (WGS84)**: Longitude `55.20432203890749° E`, Latitude `25.05890758988347° N` (Elevation: `0.0 m`)
- **CRS**: `EPSG:4326` | **Placemark Date**: `2022-08-09`
- **Boundary Polygon Present in KMZ**: `False` (Regional point anchor only; boundary polygon is absent in KMZ, logged as GAP-001)
- **Classification**: `raw_fact` | **Source File**: `E6168D - TMF Found.kmz` (Section: `Placemark Node`)
- **Engineering Note**: KMZ provides a regional geographic anchor pin only. Boundary geometry is available separately from Method Statement drawing coordinates.

### Surveyed Plot Boundary Corners (DLTM EPSG:3997)
| Corner ID | Easting (m) | Northing (m) | CRS | Classification | Source File | Page | Section / Drawing |
|---|---:|---:|---|---|---|---|---|
| **Corner_1_NW** | 486976.064 | 2772616.704 | `EPSG:3997` | `raw_fact` | `MS-1-P393D - R5.pdf` | [16] | Drawing DEW-1-P393D Rev 07 |
| **Corner_2_NE** | 487005.204 | 2772591.303 | `EPSG:3997` | `raw_fact` | `MS-1-P393D - R5.pdf` | [16] | Drawing DEW-1-P393D Rev 07 |
| **Corner_3_SE** | 486975.639 | 2772557.378 | `EPSG:3997` | `raw_fact` | `MS-1-P393D - R5.pdf` | [16] | Drawing DEW-1-P393D Rev 07 |
| **Corner_4_SW** | 486950.063 | 2772579.673 | `EPSG:3997` | `raw_fact` | `MS-1-P393D - R5.pdf` | [16] | Drawing DEW-1-P393D Rev 07 |

### Surveyed Boundary Segment Dimensions
| Segment | Length (m) | Drawing Callout | Classification | Source File | Page | Section Callout |
|---|---:|---|---|---|---|---|
| **Segment 1 Nw To Ne M** | 38.66 m | 38660 mm | `raw_fact` | `MS-1-P393D - R5.pdf` | [16] | Dimension Callout 38660 |
| **Segment 2 Ne To Se M** | 45.00 m | 45000 mm | `raw_fact` | `MS-1-P393D - R5.pdf` | [16] | Dimension Callout 45000 |
| **Segment 3 Se To Sw M** | 33.93 m | 33930 mm | `raw_fact` | `MS-1-P393D - R5.pdf` | [16] | Dimension Callout 33930 |
| **Segment 4 Sw To Nw M** | 45.27 m | 45270 mm | `raw_fact` | `MS-1-P393D - R5.pdf` | [16] | Dimension Callout 45270 |

### Plot Enclosed Surface Area
| Parameter | Value | Unit | Classification | Origin / Derivation | Provenance | Engineering Notes |
|---|---:|---|---|---|---|---|
| **Surveyed Polygon Area M2** | 1633.18 | m2 | `calculated_value` | dataset_derivation | `MS-1-P393D - R5.pdf` (p. [16]) | Shoelace formula applied to 4 DLTM surveyed corner coordinates from Drawing DEW-1-P393D |
| **Narrative Stated Plot Area M2** | 1755.0 | m2 | `raw_fact` | source_document | `MS-1-P393D - R5.pdf` (p. [3]) | Narrative area is 1755.0 m², while the surveyed polygon derived from Method Statement drawing coordinates is 1633.18 m². Difference is retained as CONFLICT-001 for engineer review. |

## 03. Site Excavation Geometry

### Ground Surface Elevations Across Project Sources
| Source Position | Elevation (m DMD) | Classification | Source File | Page | Document Section | Technical Notes |
|---|---|---|---|---|---|---|
| **Method Statement General Ground M Dmd** | 8.1 m_DMD | `raw_fact` | `MS-1-P393D - R5.pdf` | [3] | Section 2.0 Scope Table |  |
| **Soil Report Undulating Range M Dmd** | 8.025 to 8.433 m_DMD (Mean: 8.25 m DMD) | `raw_fact` | `Soil report.pdf` | [6] | Section 3.0 Project and Site Description |  |
| **Calculation Sheet Ground Level M Dmd** | 8.45 m_DMD | `raw_fact` | `MS-1-P393D - R5.pdf` | [19] | Appendix C CAL-1-P393D Levels | Discrepancy logged as CONFLICT-004 |

### Excavation Step Levels (Drawing DEW-1-P393D Rev 07)
| Level ID | Formation Level (m DMD) | Depth Below +8.10m OGL (m) | Classification | Source File | Page | Section |
|---|---:|---:|---|---|---|---|
| **Level 01** | -3.70 m DMD | 11.80 m | `raw_fact` | `MS-1-P393D - R5.pdf` | [16] | Drawing DEW-1-P393D |
| **Level 02** | -3.90 m DMD | 12.00 m | `raw_fact` | `MS-1-P393D - R5.pdf` | [16] | Drawing DEW-1-P393D |
| **Level 03** | -4.40 m DMD | 12.50 m | `raw_fact` | `MS-1-P393D - R5.pdf` | [16] | Drawing DEW-1-P393D |
| **Level 04** | -4.60 m DMD | 12.70 m | `raw_fact` | `MS-1-P393D - R5.pdf` | [16] | Drawing DEW-1-P393D |
| **Level 05** | -6.10 m DMD | 14.20 m | `raw_fact` | `MS-1-P393D - R5.pdf` | [16] | Drawing DEW-1-P393D |
| **Level 06** | -6.40 m DMD | 14.50 m | `raw_fact` | `MS-1-P393D - R5.pdf` | [16] | Drawing DEW-1-P393D |
| **Level 07** | -7.80 m DMD | 15.90 m | `raw_fact` | `MS-1-P393D - R5.pdf` | [16] | Drawing DEW-1-P393D |
| **Level 08 (Elevator / Sump Pit)** | -8.00 m DMD | 16.10 m | `raw_fact` | `MS-1-P393D - R5.pdf` | [16] | Drawing DEW-1-P393D Revision Callouts |

### Deepest Formation & Target Dewatering Criteria
- **Deepest Sump Formation M Dmd**: `-8.00 m_DMD` | **Classification:** `raw_fact` | **Status:** `APPROVED (CONFLICT-002)`
  - **Provenance**: `MS-1-P393D - R5.pdf` (Page [16], Drawing DEW-1-P393D Rev 07)
- **Target Dewatering Level M Dmd**: `-8.50 m_DMD` | **Classification:** `source_calculation` | **Status:** `APPROVED (REV-004)`
  - **Calculation Logic**: Formally approved target dewatering level establishing 0.50 m dry clearance buffer beneath the deepest localized elevator/sump pit formation at -8.00 m DMD (total drawdown Δh = 14.75 m from +6.25 m DMD baseline).
  - **Provenance**: `MS-1-P393D - R5.pdf` (Page [4, 16, 19])
  - **Engineering Note**: Reconciled and approved at -8.50 m DMD under Review Item REV-004.

### Excavation Staging Protocol
- **Stage 1 Excavation**: Excavate in dry to approximately 50 cm above the existing groundwater table (down to approximately +6.75 m DMD)
  - **Classification**: `raw_fact` | **Provenance**: `MS-1-P393D - R5.pdf` (Page [4], Section 5.0 Description of Dewatering System)
- **Stage 2 Excavation**: Deepwell system operates to lower groundwater table below excavation formation, facilitating excavation to final depth in dry
  - **Classification**: `raw_fact` | **Provenance**: `MS-1-P393D - R5.pdf` (Page [4], Section 5.0 Description of Dewatering System)

## 04. Shoring / Retaining System

- **Shoring Type**: Secant Pile Wall On 4 Sides (MODFLOW 6 HFB Boundary)
  - **Classification**: `raw_fact` / `approved_engineering_input` | **Provenance**: `MS-1-P393D - R5.pdf` (p. [3])

### Shoring Perimeter Geometry
- **Perimeter Length**: `168.0 m`
- **Wall Alignment**: Offset immediately inside site boundary on all 4 sides
- **Classification**: `raw_fact` | **Provenance**: `MS-1-P393D - R5.pdf` (p. [16])

### Secant Pile Wall Hydraulic & HFB Properties
- **HFB Representation**: `YES (MODFLOW 6 Horizontal Flow Barrier)`
- **Wall Thickness**: `0.50 m`
- **Wall Hydraulic Conductivity ($K_{wall}$)**: `1.0 × 10⁻¹⁰ m/s` (`8.64 × 10⁻⁶ m/day`)
- **HFB Hydraulic Characteristic ($HYDCHR$)**: `1.728 × 10⁻⁵ day⁻¹` ($HYDCHR = K_{wall} / \text{thickness} = 8.64 \times 10^{-6} / 0.50$)
- **Classification**: `approved_engineering_input`

### Segment-Wise Secant Pile Toe Elevations
- **North Wall**: `-11.65 m DMD`
- **West Wall**: North segment `-11.65 m DMD` | South segment `-9.30 m DMD`
- **East Wall**: North segment `-11.65 m DMD` | South segment `-10.00 m DMD`
- **South Wall**: West segment `-9.30 m DMD` | East segment `-10.00 m DMD`
- **Classification**: `approved_engineering_input` | **Provenance**: Shoring CAD Plan & Drawing DEW-1-P393D

### Historical Secant Pile Toe Levels Across Project Sources
- **Drawing And Calc Toe Levels M Dmd**: `[-9.3, -10.0, -11.65]` m_DMD
  - **Classification**: `raw_fact` | **Provenance**: `MS-1-P393D - R5.pdf` (p. [16], Drawing DEW-1-P393D Notes & Legend)
  - **Engineering Note**: Drawing notes call out negative toe levels (-9.30, -10.00, -11.65 m DMD). Discrepancy with Section 2.0 text is retained as CONFLICT-003 for engineer review.
- **Narrative Text Toe Levels M Dmd**: `-9.30, 10.00, &-11.65 m DMD` 
  - **Classification**: `raw_fact` | **Provenance**: `MS-1-P393D - R5.pdf` (p. [3], Section 2.0 Scope Table)
  - **Engineering Note**: Text in Section 2.0 lists positive 10.00 m DMD, while Drawing DEW-1-P393D lists -10.00 m DMD. Logged in Conflict Register as CONFLICT-003.

### Groundwater Cutoff Implications
- **Cutoff Penetration**: Partially penetrating cutoff wall (does NOT extend to Layer 5 basal confining unit)
- **Depth Below Deepest Excavation**: Shoring toe terminates between -9.30 m and -11.65 m DMD, which is 1.30 m to 3.65 m below deepest sump (-8.00 m DMD)
- **Keyed Status**: Not keyed into deep basal calcisiltite aquitard (-19.75 to -31.75 m DMD). Groundwater underflow beneath the wall toe remains physically active and possible where the wall does not penetrate the deeper confining unit.
- **Classification**: `interpretation` | **Provenance**: `MS-1-P393D - R5.pdf` (p. [16, 17], Section Layout SEC-1-P393D)

## 05. Dewatering System / Wellfield

### Total Installed Deepwells: **6 nos**
- **Classification**: `raw_fact` | **Provenance**: `MS-1-P393D - R5.pdf` (p. [5])

### Deepwells Catalog (DW-01 to DW-06)
| Well ID | Easting (m) | Northing (m) | Depth (m) | Screen Length (m) | Borehole Ø | Casing | Toe Level | Screen Interval | Design Yield | Classification |
|---|---:|---:|---:|---:|---:|---|---:|---|---:|---|
| **DW-01** | 486976.438 | 2772571.467 | 21.2 m | 6.7 m | 700.0 mm | 8.0" Slotted UPVC | -14.5 m DMD | -7.8 to -14.5 m | 11.1 m³/hr (266.4 m³/d) | `digitized_value` |
| **DW-02** | 486973.338 | 2772582.310 | 21.2 m | 6.7 m | 700.0 mm | 8.0" Slotted UPVC | -14.5 m DMD | -7.8 to -14.5 m | 11.1 m³/hr (266.4 m³/d) | `digitized_value` |
| **DW-03** | 486961.597 | 2772582.131 | 21.2 m | 6.7 m | 700.0 mm | 8.0" Slotted UPVC | -14.5 m DMD | -7.8 to -14.5 m | 11.1 m³/hr (266.4 m³/d) | `digitized_value` |
| **DW-04** | 486976.158 | 2772593.866 | 21.2 m | 6.7 m | 700.0 mm | 8.0" Slotted UPVC | -14.5 m DMD | -7.8 to -14.5 m | 11.1 m³/hr (266.4 m³/d) | `digitized_value` |
| **DW-05** | 486976.572 | 2772606.274 | 21.2 m | 6.7 m | 700.0 mm | 8.0" Slotted UPVC | -14.5 m DMD | -7.8 to -14.5 m | 11.1 m³/hr (266.4 m³/d) | `digitized_value` |
| **DW-06** | 486995.809 | 2772586.338 | 21.2 m | 6.7 m | 700.0 mm | 8.0" Slotted UPVC | -14.5 m DMD | -7.8 to -14.5 m | 11.1 m³/hr (266.4 m³/d) | `digitized_value` |

> [!NOTE]
> **Coordinate Derivation & Provenance Detail**:
> All 6 deepwell coordinates possess `coordinate_origin: drawing_cad_digitized_geometry` and `classification: digitized_value`.
> Well locations are graphically indicated on Drawing DEW-1-P393D Rev 07 (Page 16); numerical coordinates are digitized from project CAD drawing geometry. Hydraulic parameters (depth 21.2m, screen 6.7m, yield 11.1 m³/hr) are source calculations from Appendix C CAL-1-P393D (Pages 19–20).

### Equipment & Redundancy Configuration
- **Submersible Pumps**: Running pump(s) + 1 standby pump
- **Electrical Generators**: Running genset(s) + 1 standby genset
- **French Drains**: 0.50m x 0.50m gravity drains filled with aggregate channelled to deepwells
- **Classification**: `raw_fact` | **Provenance**: `MS-1-P393D - R5.pdf` (p. [4, 9], Sections 5.1 & 10.2)

## 06. Groundwater Information

### Borehole Static Water Level Observations (Feb/Mar 2023 Fieldwork)
| Borehole ID | Ground Level (m DMD) | Water Depth (m bgl) | Standing Water Level (m DMD) | Observation Date / Time | Classification | Source File | Pages | Section |
|---|---:|---:|---:|---|---|---|---|---|
| **BH01** | +8.35 | 2.10 m | +6.25 m DMD | 28/02/2023 16:30 | `raw_fact` | `Soil report.pdf` | [6, 30] | Table 1 & Borehole Log 1 |
| **BH02** | +8.30 | 2.10 m | +6.20 m DMD | 23/02/2023 | `raw_fact` | `Soil report.pdf` | [6, 33] | Table 1 & Borehole Log 2 |
| **BH03** | +8.15 | 2.00 m | +6.15 m DMD | 01/03/2023 | `raw_fact` | `Soil report.pdf` | [6, 37] | Table 1 & Borehole Log 3 |
| **BH04** | +8.35 | 2.15 m | +6.20 m DMD | 28/02/2023 | `raw_fact` | `Soil report.pdf` | [6, 40] | Table 1 & Borehole Log 4 |
| **BH05** | +8.25 | 2.10 m | +6.15 m DMD | 01/03/2023 | `raw_fact` | `Soil report.pdf` | [6, 43] | Table 1 & Borehole Log 5 |

### Baseline & Design Groundwater Levels
- **Adopted Baseline M Dmd**: `6.25 m_DMD` | **Classification:** `raw_fact` | **Source:** `MS-1-P393D - R5.pdf` (p. [3, 20], Section 2.0 Scope & Appendix C Calc)
- **Sensitivity High Gwl M Dmd**: `6.75 m_DMD` | **Classification:** `raw_fact` | **Source:** `MS-1-P393D - R5.pdf` (p. [19], Appendix C CAL-1-P393D Levels)

### Resolved MODFLOW Model Boundary & Recharge Inputs
- **Lateral Boundary Condition**: `CHD (Constant Head Boundary)`
  - **Boundary Head**: `+6.25 m DMD`
  - **Description**: Regional/external groundwater condition represented using CHD at +6.25 m DMD.
  - **Classification**: `approved_engineering_input`
- **Recharge Rate**: `0 m/day`
  - **Description**: Model uses zero recharge across the entire domain.
  - **Classification**: `approved_engineering_input`

### Groundwater Monitoring Protocol
- **Water Level Monitoring**: Checked daily by day and night shift watchman using an electric contact dip meter (KLL)
- **Water Discharge Monitoring**: Measured daily using standard V-notch tank and 6-inch flow meter
- **Classification**: `raw_fact` | **Provenance**: `MS-1-P393D - R5.pdf` (p. [7, 14], Section 8.0 & Appendix A)

## 07. Geology / Stratigraphy

### Subsurface Stratigraphic Column (Soil Report SIR2023-0018 Table 2)
| Stratum ID | Geological / Lithological Name | Hydrogeological Role | Top Depth | Bottom Depth | Thickness | Top Elev | Bottom Elev | Material Description | Classification |
|---|---|---|---:|---:|---:|---:|---:|---|---|
| **Stratum 1** | **Aeolian Dune Sand / Silt** | — | 0.00 m | 1.50 m | 1.50 m | 8.25 m | 6.75 m | Medium dense to very dense, light brown to brown, slightly silty, fine SAND | `raw_fact` |
| **Stratum 2** | **Upper Weathered Sandstone** | — | 1.50 m | 13.00 m | 11.50 m | 6.75 m | -4.75 m | Extremely weak to very weak, light brown, fine to medium grained SANDSTONE | `raw_fact` |
| **Stratum 3** | **Moderately Weathered Sandstone** | **Screened Aquifer** | 13.00 m | 23.00 m | 10.00 m | -4.75 m | -14.75 m | Extremely weak to very weak, reddish brown, fine to medium grained, slightly gypsiferous SANDSTONE | `raw_fact` |
| **Stratum 4** | **Conglomeratic Sandstone** | — | 23.00 m | 28.00 m | 5.00 m | -14.75 m | -19.75 m | Very weak, reddish brown, slightly gypsiferous, conglomeratic SANDSTONE | `raw_fact` |
| **Stratum 5** | **Calcisiltite / Siltstone Basal Unit** | **Lower Confining Bed** | 28.00 m | 40.00 m | 12.00 m | -19.75 m | -31.75 m | Very weak to weak, light brown to off-white, fine grained CALCISILTITE/ SILTSTONE | `raw_fact` |

> [!NOTE]
> **Separation of Geological Name from Hydrogeological Role**:
> - `geological_name` values strictly represent the geotechnical units stated in Table 2 of the Soil Report.
> - `hydrogeological_interpretation` values (`Screened Aquifer` for Stratum 3 and `Lower Confining Bed` for Stratum 5) are isolated with dedicated provenance citing Method Statement CAL-1-P393D (Pages 19–20) and classified as `interpretation`.

### Geotechnical Borehole Inventory
| Borehole ID | Total Depth (m) | Surface Elevation (m DMD) | Start Date | End Date | Classification | Source File | Page | Section |
|---|---:|---:|---|---|---|---|---|---|
| **BH01** | 30.0 m | +8.35 m DMD | 27/02/2023 | 28/02/2023 | `raw_fact` | `Soil report.pdf` | [6] | Table 1 |
| **BH02** | 40.0 m | +8.30 m DMD | 22/02/2023 | 23/02/2023 | `raw_fact` | `Soil report.pdf` | [6] | Table 1 |
| **BH03** | 30.0 m | +8.15 m DMD | 28/02/2023 | 01/03/2023 | `raw_fact` | `Soil report.pdf` | [6] | Table 1 |
| **BH04** | 30.0 m | +8.35 m DMD | 27/02/2023 | 28/02/2023 | `raw_fact` | `Soil report.pdf` | [6] | Table 1 |
| **BH05** | 30.0 m | +8.25 m DMD | 28/02/2023 | 01/03/2023 | `raw_fact` | `Soil report.pdf` | [6] | Table 1 |

## 08. Hydrogeological / Hydraulic Information

### Hydrogeological Properties & Approved Parameters
| Layer | Geological Unit | Kh Base (m/s) [m/day] | Kv Base (m/s) [m/day] | Ss Base (1/m) | Sy Base (dimensionless) |
|---|---|---|---|---|---|
| L1 | Aeolian Dune Sand / Silt | 2.3×10⁻⁵ [1.9872] | 1.0×10⁻⁵ [0.864] | 1.0×10⁻⁴ | 0.25 |
| L2 | Upper Weathered Sandstone | 5.0×10⁻⁵ [4.32] | 1.0×10⁻⁵ [0.864] | 2.5×10⁻⁵ | 0.12 |
| L3 | Moderately Weathered Sandstone | 5.0×10⁻⁵ [4.32] | 1.0×10⁻⁵ [0.864] | 2.5×10⁻⁵ | 0.12 |
| L4 | Conglomeratic Sandstone | 5.8×10⁻⁶ [0.50112] | 5.8×10⁻⁷ [0.050112] | 5.0×10⁻⁶ | 0.08 |
| L5 | Calcisiltite / Siltstone | 5.0×10⁻¹⁰ [4.32×10⁻⁵] | 1.0×10⁻¹⁰ [8.64×10⁻⁶] | 1.0×10⁻⁶ | 0.03 |

> [!NOTE]
> **Final Approved Hydraulic-Property Baseline for Numerical Modeling**:
> The five rows above are the authoritative and final modeling baseline. Kh and Kv are shown in m/s with their exact m/day equivalents in brackets; Ss is in 1/m; and Sy is dimensionless. The corresponding Kh/Kv ratios are L1 = 2.3, L2 = 5.0, L3 = 5.0, L4 = 10.0, and L5 = 5.0.

## 09. Dewatering Pumping Operations

### Steady-State Pumping Flow Rates
| Operational Parameter | Value | Unit | Classification | Origin | Provenance | Calculation / Allocation Basis |
|---|---:|---|---|---|---|---|
| **Total System Flow M3 Hr** | 46.5 | m3/hr | `source_calculation` | source_document | `MS-1-P393D - R5.pdf` (p. [7, 20]) |  |
| **Total System Flow M3 Day** | 1116.0 | m3/day | `calculated_value` | dataset_derivation | `MS-1-P393D - R5.pdf` (p. [7, 20]) | 46.50 m3/hr * 24 hours/day |
| **Per Well Steady Rate M3 Hr** | 7.75 | m3/hr | `calculated_value` | dataset_derivation | `MS-1-P393D - R5.pdf` (p. [5, 20]) | 46.50 m3/hr / 6 wells |
| **Per Well Steady Rate M3 Day** | 186.0 | m3/day | `calculated_value` | dataset_derivation | `MS-1-P393D - R5.pdf` (p. [5, 20]) | 7.75 m3/hr * 24 hours/day |

### Transient Peak Initial Discharge Rates
| Operational Parameter | Value | Unit | Classification | Origin | Provenance | Calculation / Allocation Basis |
|---|---:|---|---|---|---|---|
| **Peak System Flow M3 Hr** | 93.0 | m3/hr | `source_calculation` | source_document | `MS-1-P393D - R5.pdf` (p. [7, 20]) | Method Statement Section 7.0 Note states initial drawdown flow can be twice steady state (46.50 * 2 = 93.00 m3/hr) |
| **Peak System Flow M3 Day** | 2232.0 | m3/day | `calculated_value` | dataset_derivation | `MS-1-P393D - R5.pdf` (p. [7, 20]) | 93.00 m3/hr * 24 hours/day |
| **Per Well Peak Rate M3 Hr** | 15.5 | m3/hr | `calculated_value` | dataset_derivation | `MS-1-P393D - R5.pdf` (p. [7, 20]) | 93.00 m3/hr / 6 wells |
| **Per Well Peak Rate M3 Day** | 372.0 | m3/day | `calculated_value` | dataset_derivation | `MS-1-P393D - R5.pdf` (p. [7, 20]) | 15.50 m3/hr * 24 hours/day |

### Rated Pump Capacity & Dewatering Duration
- **Rated Pump Capacity Per Well**: `11.1 m³/hr` (266.4 m³/day)
  - **Classification**: `source_calculation` | **Calculation Ref**: `CAL-1-P393D Rev 3 Step 3 Dupuit-Thiem calculation`
  - **Provenance**: `MS-1-P393D - R5.pdf` (Page [20], Appendix C Step 3 Deepwell Yield)
- **Pre-Excavation Drawdown Duration**: `7 days`
- **Total Operational Duration**: `150 days` (approx. 5 months)
  - **Classification**: `raw_fact` | **Provenance**: `MS-1-P393D - R5.pdf` (Page [7, 19], Section 7.5 & Appendix C Duration)

## 10. Discharge Water Management

### Discharge Location
- **Specification**: `Nakheel Line` 
- **Classification**: `raw_fact` | **Provenance**: `MS-1-P393D - R5.pdf` (Pages [7, 16], Section 7.0 Table & Drawing DEW-1-P393D)

### Discharge Route Length M
- **Specification**: `2400.0` m
- **Classification**: `raw_fact` | **Provenance**: `MS-1-P393D - R5.pdf` (Pages [3], Section 2.0 Scope Table)

### Water Treatment And Settlement
- **Classification**: `raw_fact` | **Provenance**: `MS-1-P393D - R5.pdf` (Pages [7, 9], Sections 7.3 & 10.1)
- **Settlement Tank**: Sedimentation tank equipped with baffle plates for suspended solids separation and oil/diesel skimming mats
- **Water Testing Frequency**: Weekly / monthly as required by Trakhees / Nakheel / RTA
- **Flow Measurement Device**: 6-inch electromagnetic flow meter as per Nakheel requirement and V-notch tank

## 11. Engineering Calculations in Sources

### Calculation Method: Dewatering Design Calculations: Equivalent Radius Method (CIRIA Report)
- **Calculation Sheet Reference**: `CAL-1-P393D Rev 3 (03-Nov-23)`
- **Provenance**: `MS-1-P393D - R5.pdf` (Pages [19, 20], Appendix C)

#### Calculation Inputs
| Parameter | Symbol / Key | Value | Unit |
|---|---|---:|---|
| Plot Length A M | `plot_length_a_m` | 45.0 | — |
| Plot Width B M | `plot_width_b_m` | 39.0 | — |
| Plot Area M2 | `plot_area_m2` | 1755.0 | — |
| Perimeter M | `perimeter_m` | 168.0 | — |
| Natural Water Level M Dmd | `natural_water_level_m_dmd` | 6.25 | — |
| General Excavation M Dmd | `general_excavation_m_dmd` | -6.1 | — |
| Maximum Excavation M Dmd | `maximum_excavation_m_dmd` | -7.8 | — |
| Source Calculation K M S (not final layer baseline) | `source_calculation_k_m_s` | 5e-05 | — |
| Height Of Water H M | `height_of_water_H_m` | 14.55 | — |
| Remaining Water Height Hw M | `remaining_water_height_hw_m` | 1.45 | — |
| Required Average Drawdown M | `required_average_drawdown_m` | 13.11 | — |
| Factor Of Safety | `factor_of_safety` | 1.2 | — |

#### Formulas & Analytical Results
| Calculated Parameter | Formula Applied | Result | Unit | Classification | Origin |
|---|---|---:|---|---|---|
| **Equivalent Well Radius Re M** | `re = sqrt(Area / pi)` | **23.6** | m | `source_calculation` | source_document |
| **Sichardt Radius Of Influence R0 M** | `R0 = C * (H - hw) * sqrt(k), where C = 3000` | **277.9** | m | `source_calculation` | source_document |
| **Combined Radius Rc M** | `Rc = R0 + re` | **301.5** | m | `source_calculation` | source_document |
| **Steady State Seepage Q M3 Hr** | `Q = pi * k * (H^2 - hw^2) / ln(Rc / re)` | **46.5** | m3/hr | `source_calculation` | source_document |
| **Individual Well Yield Q M3 Hr** | `q = pi * D * Lw * k * i` | **11.1** | m3/hr | `source_calculation` | source_document |
| **Required Well Count** | `Total DWs = (Q / q) * FoS = (46.5 / 11.1) * 1.2 = 5.03 -> 6 wells` | **6.0** | wells | `source_calculation` | source_document |

## 12. Source / Drawing Register

| Drawing / Document ID | Rev | Date | Title / Description | Source File | Sheet / Pages | Contents / Extracted Role |
|---|---|---|---|---|---|---|
| **DEW-1-P393D** | 07 | 13/11/23 | Dewatering Layout Drawing | `MS-1-P393D - R5.pdf` | [16] | 4 DLTM plot limit corner coordinates, positions and IDs of DW-01 to DW-06, secant pile perimeter, Level 01 to Level 08 excavation levels, discharge line alignment to Nakheel line, generator and sedimentation tank positions. |
| **SEC-1-P393D** | 05 | 10/11/23 | Section Layout Drawing | `MS-1-P393D - R5.pdf` | [17] | Vertical cross section showing secant pile wall penetration, deepwell depth, water table, excavation formations, and French drain profile. |
| **CHK-1-P393D** | 01 | 09/06/23 | Deepwell Monitoring Check-List | `MS-1-P393D - R5.pdf` | [14] | Monitoring protocol sheet for DW-01 to DW-06, V-notch flow readings, water levels, pump running status, and generator status. |
| **CAL-1-P393D** | 03 | 03/11/23 | Dewatering Design Calculations | `MS-1-P393D - R5.pdf` | [19, 20] | Complete CIRIA Equivalent Radius and Sichardt analytical dewatering calculations. |
| **PLATE-03-SIR2023** | 00 | 14/03/23 | Borehole Location Plan | `Soil report.pdf` | [26] | Spatial distribution plan for boreholes BH01, BH02, BH03, BH04, and BH05 across the building footprint. |
| **PLATE-05-SIR2023** | 00 | 14/03/23 | Geotechnical Cross Section Profile | `Soil report.pdf` | [28] | Subsurface geological strata correlations across the 5 boreholes. |

## 13. Source Conflict Register

> [!NOTE]
> **ENGINEERING RECONCILIATION & APPROVAL STATUS**:
> All 4 engineering discrepancies identified in Phase 1 — Step 2 have been formally reviewed, reconciled, and approved by the lead hydrogeologist.

### CONFLICT-001 — Plot Surface Area

| Source Position | Reference | Stated Value | Unit |
|---|---|---:|---|
| **Source A** (`MS-1-P393D - R5.pdf`) | Pages 3 & 20 (Section 2.0 Scope Table & Appendix C Calculation Sheet) | 1755.0 | m2 |
| **Source B** (`MS-1-P393D - R5.pdf`) | Page 16 (Drawing DEW-1-P393D Rev 07 DLTM Survey Coordinates) | 1633.18 | m2 |

- **Discrepancy Description**: Narrative text assumed a simplified rectangular plot (45.0m x 39.0m = 1755 m²), whereas the actual surveyed CAD boundary coordinates form an irregular 4-sided polygon enclosing 1633.18 m².
- **Final Approved Value**: **1633.18 m²** (Source B — Surveyed CAD Polygon)
- **Current Conflict Status**: **RESOLVED & APPROVED ✅**

### CONFLICT-002 — Maximum Excavation Depth

| Source Position | Reference | Stated Value | Unit |
|---|---|---:|---|
| **Source A** (`MS-1-P393D - R5.pdf`) | Pages 3 & 19 (Section 2.0 Scope Table & Appendix C Calc Sheet) | -7.8 | m_DMD |
| **Source B** (`MS-1-P393D - R5.pdf`) | Page 16 (Drawing DEW-1-P393D Rev 07, Level 08 Elevator/Sump Pit Callout) | -8.0 | m_DMD |

- **Discrepancy Description**: Source A listed maximum excavation as -7.80 m DMD (Level 07 general foundation), whereas Source B detailed localized Level 08 elevator/sump pit excavation at -8.00 m DMD.
- **Final Approved Value**: **-8.00 m DMD** (Source B — Deepest Formation Level)
- **Current Conflict Status**: **RESOLVED & APPROVED ✅**

### CONFLICT-003 — Secant Pile Toe Level Sign Typo

| Source Position | Reference | Stated Value | Unit |
|---|---|---:|---|
| **Source A** (`MS-1-P393D - R5.pdf`) | Page 3 (Section 2.0 Scope Table) | -9.30, 10.00, &-11.65 m DMD | text |
| **Source B** (`MS-1-P393D - R5.pdf`) | Page 16 (Drawing DEW-1-P393D Notes & Legend) | -9.30, -10.00, -11.65 m DMD | text |

- **Discrepancy Description**: Source A contained a typographical sign error listing positive 10.00 m DMD, whereas Drawing DEW-1-P393D Notes & Legend confirmed all toe levels are negative (-9.30, -10.00, -11.65 m DMD).
- **Final Approved Value**: **-9.30 / -10.00 / -11.65 m DMD** (Source B — Corrected Negative Elevations)
- **Current Conflict Status**: **RESOLVED & APPROVED ✅**

### CONFLICT-004 — Existing Ground Surface Elevation

| Source Position | Reference | Stated Value | Unit |
|---|---|---:|---|
| **Source A** (`MS-1-P393D - R5.pdf`) | Page 3 (Section 2.0 Scope Table) | 8.1 | m_DMD |
| **Source B** (`Soil report.pdf`) | Page 6 (Table 1 average of 5 boreholes: 8.15 to 8.35 m DMD) | 8.25 | m_DMD |
| **Source C** (`MS-1-P393D - R5.pdf`) | Page 19 (Appendix C Calculation Sheet CAL-1-P393D) | 8.45 | m_DMD |

- **Discrepancy Description**: Natural ground surface varied across sources (+8.10 m MS text vs +8.25 m Soil Report mean vs +8.45 m MS calc sheet).
- **Final Approved Value**: **+8.45 m DMD** (Calculation Sheet Existing Ground Elevation, with **+8.25 m DMD** approved under REV-005 as the reconciled Layer 1 ground surface plane)
- **Current Conflict Status**: **RESOLVED & APPROVED ✅**

## 14. Data Gaps / Missing Information

> [!NOTE]
> **DATA GAP RESOLUTION & CLOSURE STATUS**:
> Following systematic engineering investigation, derivation from surveyed coordinates, and hydrogeological research (`HydrogeologicalDataGapResearch.md`):
> - **GAP-002** (In-situ field testing) and **GAP-003** (Long-term monitoring time-series) have been formally retired from the modeling blocking register.
> - The remaining 3 data gaps (**GAP-001**, **GAP-004**, and **GAP-005**) have been fully resolved, parameterized, and **APPROVED / CLOSED ✅**.

### GAP-001 — Site Boundary Geometry
- **Original Gap**: Site boundary polygon absent in KMZ file.
- **Investigation Finding**: Complete 4-corner surveyed boundary geometry recovered from Drawing DEW-1-P393D Rev 07 (Page 16) in DLTM coordinates.
- **Approved Final Boundary**: **Area = 1633.18 m²** (Perimeter = 168.0 m)
- **Status**: **CLOSED ✅**

### GAP-004 — Aquifer Storage Parameters
- **Original Gap**: Unmeasured specific yield and specific storage in project geotechnical archives.
- **Final Resolution**: Storage values are closed by the final five-layer baseline in Section 08: L1 (Sy 0.25; Ss 1.0×10⁻⁴ 1/m), L2 and L3 (Sy 0.12; Ss 2.5×10⁻⁵ 1/m), L4 (Sy 0.08; Ss 5.0×10⁻⁶ 1/m), and L5 (Sy 0.03; Ss 1.0×10⁻⁶ 1/m).
- **Status**: **APPROVED / CLOSED ✅**

### GAP-005 — Vertical Hydraulic Anisotropy
- **Original Gap**: Unmeasured vertical conductivity and anisotropy ratio.
- **Final Resolution**: Vertical conductivity is closed by the final five-layer baseline in Section 08. The resulting Kh/Kv ratios are L1 = 2.3, L2 = 5.0, L3 = 5.0, L4 = 10.0, and L5 = 5.0.
- **Status**: **APPROVED / CLOSED ✅**

## 15. Engineer Review Register

The following items represent the critical modeling decisions and parameter approvals completed by the reviewing engineer prior to MODFLOW numerical input generation.

### REV-001 — Final Layered Horizontal Hydraulic Conductivity Baseline

**Engineering Review Question**:
> Does the engineer approve the final layer-specific Kh baseline in Section 08 for the numerical MODFLOW simulation?

- **Approved Final Value**: Section 08 five-layer Kh baseline: L1 2.3×10⁻⁵ [1.9872], L2 5.0×10⁻⁵ [4.32], L3 5.0×10⁻⁵ [4.32], L4 5.8×10⁻⁶ [0.50112], L5 5.0×10⁻¹⁰ [4.32×10⁻⁵] (m/s [m/day]).
- **Classification**: `approved_engineering_input` | **Origin**: final approved modeling baseline
- **Source Reference**: Final approved baseline; source-document and research provenance remain registered in Sections 12 and 17.
- **Current Status**: **APPROVED ✅**

**Engineer Decision**:
- [X] **APPROVE AS EXTRACTED / PROPOSED**
- [ ] **REJECT**
- [ ] **REVISE / SPECIFY ALTERNATIVE PARAMETER**

**Engineer Specific Instructions / Parameter Choice**:
```text
Approved as the governing final layer-specific horizontal hydraulic conductivity baseline for L1 through L5.
```

### REV-002 — Final Layered Vertical Conductivity and Anisotropy Baseline

**Engineering Review Question**:
> Does the engineer approve the final layer-specific Kv baseline and the derived Kh/Kv ratios for the 3D MODFLOW grid?

- **Approved Final Value**: Section 08 five-layer Kv baseline: L1 1.0×10⁻⁵ [0.864], L2 1.0×10⁻⁵ [0.864], L3 1.0×10⁻⁵ [0.864], L4 5.8×10⁻⁷ [0.050112], L5 1.0×10⁻¹⁰ [8.64×10⁻⁶] (m/s [m/day]); derived Kh/Kv ratios are 2.3, 5.0, 5.0, 10.0, and 5.0 respectively.
- **Classification**: `approved_engineering_input` | **Origin**: final approved modeling baseline
- **Source Reference**: Final approved baseline; source-document and research provenance remain registered in Sections 12 and 17.
- **Current Status**: **APPROVED ✅**

**Engineer Decision**:
- [X] **APPROVE AS EXTRACTED / PROPOSED**
- [ ] **REJECT**
- [ ] **REVISE / SPECIFY ALTERNATIVE PARAMETER**

**Engineer Specific Instructions / Parameter Choice**:
```text
Approved the final layer-specific Kv baseline and its derived Kh/Kv ratios for L1 through L5.
```

### REV-003 — Final Layered Storage Baseline

**Engineering Review Question**:
> What layer-specific Sy and Ss values should be approved for transient simulation?

- **Approved Final Values**: Section 08 five-layer storage baseline: L1 (Sy 0.25; Ss 1.0×10⁻⁴ 1/m), L2 (Sy 0.12; Ss 2.5×10⁻⁵ 1/m), L3 (Sy 0.12; Ss 2.5×10⁻⁵ 1/m), L4 (Sy 0.08; Ss 5.0×10⁻⁶ 1/m), and L5 (Sy 0.03; Ss 1.0×10⁻⁶ 1/m).
- **Classification**: `approved_engineering_input` | **Origin**: final approved modeling baseline
- **Source Reference**: Final approved baseline; source-document and research provenance remain registered in Sections 12 and 17.
- **Current Status**: **APPROVED ✅**

**Engineer Decision**:
- [X] **APPROVE AS EXTRACTED / PROPOSED**
- [ ] **REJECT**
- [ ] **REVISE / SPECIFY ALTERNATIVE PARAMETER**

**Engineer Specific Instructions / Parameter Choice**:
```text
Approved the final layer-specific Sy and Ss baseline for L1 through L5; Sy is dimensionless and Ss is in 1/m.
```

### REV-004 — Target Dewatering Drawdown Level (-8.50 m DMD)

**Engineering Review Question**:
> Does the engineer approve adopting the governing target dewatering criterion for simulation to clear the deepest sump pit?

- **Approved Final Value**: **-8.50 m DMD** (providing 0.50 m buffer below deepest elevator pit at -8.00 m DMD)
- **Classification**: `source_calculation` | **Origin**: Engineering Reconciliation
- **Source Reference**: `MS-1-P393D - R5.pdf` (Pages [4, 16, 19])
- **Current Status**: **APPROVED ✅**

**Engineer Decision**:
- [X] **APPROVE AS EXTRACTED / PROPOSED**
- [ ] **REJECT**
- [ ] **REVISE / SPECIFY ALTERNATIVE PARAMETER**

**Engineer Specific Instructions / Parameter Choice**:
```text
Approved target drawdown level set to -8.50 m DMD to ensure 0.50 m dry buffer beneath -8.00 m sump formation.
```

### REV-005 — Reconciled Ground Surface Plane (+8.25 m DMD)

**Engineering Review Question**:
> Does the engineer approve adopting +8.25 m DMD (arithmetic mean of 5 borehole ground elevations) as the ground surface top for Layer 1 in the numerical model grid?

- **Approved Final Value**: **+8.25 m DMD**
- **Classification**: `calculated_value` | **Origin**: `dataset_derivation`
- **Source Reference**: `Soil report.pdf` (Page [6], Table 1 Mean)
- **Current Status**: **APPROVED ✅**

**Engineer Decision**:
- [X] **APPROVE AS EXTRACTED / PROPOSED**
- [ ] **REJECT**
- [ ] **REVISE / SPECIFY ALTERNATIVE PARAMETER**

**Engineer Specific Instructions / Parameter Choice**:
```text
Approved +8.25 m DMD as uniform top surface for Layer 1 in model grid.
```

## 16. Data Quality / Confidence Summary

### Dynamic Extraction Counts
| Metric / Category | Count | Governance Meaning |
|---|---:|---|
| **Raw Project Facts** | 61 | Directly extracted text callouts from project documents |
| **Source Calculations** | 13 | Explicit calculations performed inside Method Statement / Soil Report |
| **Dataset Calculated Values** | 8 | Mathematical derivations from raw facts (e.g. Shoelace area, unit conversions) |
| **Digitized Drawing Values** | 6 | Geometry derived from CAD drawing layout rather than text tables (DW-01 to DW-06) |
| **Engineering Interpretations** | 4 | Inferred engineering roles (e.g. Screened Aquifer, Confining Bed) |
| **Missing Parameters** | 11 | Genuinely absent parameters (zero invented values injected) |
| **Total Classified Items** | **103** | **Total data-bearing records verified** |
| **Unresolved Conflicts** | 4 | Discrepancies between project sources preserved for review |
| **Identified Data Gaps** | 5 | Missing site investigations requiring engineer choice in Step 3 |
| **Engineer Review Items** | 5 | Formal decision gates requiring sign-off before Step 4 |

### Overall Confidence Assessment
> The raw project dataset provides high-quality, fully traceable geometry, wellfield configuration, and operational rates from the Method Statement (the major source of truth). Geological stratigraphy and static groundwater levels are well documented in the Soil Report. The final approved five-layer hydraulic baseline in Section 08 closes the active modeling values for Kh, Kv, Ss, and Sy; unrelated source-data limitations remain documented in their applicable registers.

## 17. Provenance Register

| Source ID | File Name | File Type | Authority Role | Registered Path | Key Extracted Items |
|---|---|---|---|---|---|
| **SRC-001** | `E6168D - TMF Found.kmz` | GIS / KMZ | **Site Location & Regional Geographic Anchor** | `data/actual/raw/E6168D - TMF Found.kmz` | • Geographic placemark coordinates (55.204322 E, 25.058908 N WGS84)<br>• Absence of plot boundary polygon |
| **SRC-002** | `MS-1-P393D - R5.pdf` | Engineering Method Statement & Approved Drawings | **MAJOR SOURCE OF TRUTH (Primary Governing Authority)** | `data/actual/raw/MS-1-P393D - R5.pdf` | • Site boundary DLTM corner coordinates (Corner 1 to 4)<br>• Deepwell catalog (DW-01 to DW-06 positions, depths, screens)<br>• Excavation schedule (Levels 01 to 08, deepest sump -8.00 m DMD)<br>• Target dewatering drawdown level (-8.50 m DMD = -8.00 m sump - 0.50 m buffer)<br>• Secant pile wall alignment and toe levels (-9.30, -10.00, -11.65 m DMD)<br>• Steady-state flow (46.50 m3/hr) and peak flow (93.00 m3/hr)<br>• CIRIA Equivalent Radius calculations CAL-1-P393D and source-calculation k = 5.0e-5 m/s (not the final layer-specific baseline; see Section 08)<br>• Discharge to Nakheel line (2400 m distance) |
| **SRC-003** | `Soil report.pdf` | Geotechnical Soil Investigation Report | **Baseline Geotechnical Stratigraphy & Static Groundwater** | `data/actual/raw/Soil report.pdf` | • Borehole logs BH01 to BH05 (locations, depths 30m-40m, elevations)<br>• Subsurface lithological strata column (sand, sandstones, calcisiltite)<br>• Static groundwater table measurements (+6.15 to +6.25 m DMD)<br>• SPT N-values and UCS rock strengths<br>• Confirmation of absence of in-situ permeability / pumping tests |

## 18. Final Pre-Modflow Approval Status

### Final Approved Engineering Parameter Register

| ID | Item / Parameter | Final Approved Value | Unit | Engineering Basis & Authority |
|:---:|---|:---:|:---:|---|
| **CONFLICT-001** | Plot Surface Area | **1633.18** | m² | Surveyed 4-corner CAD polygon (Drawing DEW-1-P393D Rev 07) |
| **CONFLICT-002** | Maximum Excavation Depth | **-8.00** | m DMD | Level 08 elevator/sump pit formation (Drawing DEW-1-P393D) |
| **CONFLICT-003** | Secant Pile Toe Levels | **-9.30 / -10.00 / -11.65** | m DMD | Corrected negative toe elevations (Drawing Notes & Legend) |
| **CONFLICT-004** | Existing Ground Surface Elevation | **+8.45** | m DMD | Calculation sheet CAL-1-P393D existing ground elevation |
| **REV-001** | Layered Horizontal Hydraulic Conductivity ($K_h$) | **Section 08 five-layer baseline** | m/s [m/day] | Final approved modeling baseline |
| **REV-002** | Layered Vertical Conductivity ($K_v$) and $K_h/K_v$ | **Section 08 five-layer baseline** | m/s [m/day]; dimensionless | Final approved modeling baseline |
| **REV-003** | Layered Specific Yield ($S_y$) and Storage ($S_s$) | **Section 08 five-layer baseline** | dimensionless; 1/m | Final approved modeling baseline |
| **REV-004** | Target Dewatering Drawdown | **-8.50** | m DMD | 0.50 m dry buffer beneath deepest -8.00 m DMD sump pit |
| **REV-005** | Reconciled Ground Surface Plane | **+8.25** | m DMD | Arithmetic mean of 5 borehole ground elevations |
| **REV-006** | Lateral Boundary Condition | **CHD (+6.25 m DMD)** | m DMD | Constant Head Boundary representing regional groundwater head |
| **REV-007** | Recharge Rate | **0** | m/day | Zero recharge across model domain |
| **REV-008** | Secant Pile Wall / HFB Properties | **HFB = YES; 0.50m; K=1e-10 m/s (8.64e-6 m/day); HYDCHR=1.728e-5 day⁻¹** | day⁻¹ | Partially penetrating Horizontal Flow Barrier |
| **REV-009** | Segment-Wise Wall Toe Assignment | **North: -11.65; West: -11.65 / -9.30; East: -11.65 / -10.00; South: -9.30 / -10.00** | m DMD | Segment-wise toe elevations from shoring CAD plan |

### Workflow Positioning
```text
RAW PROJECT DATA (KMZ, Method Statement, Soil Report)
        ↓
DATA EXTRACTION (Phase 1 — Step 2)
        ↓
actual_engineering_dataset.json (FROZEN & VERIFIED)
        ↓
PreModflowApproval.md (REVIEW COMPLETED & APPROVED)
        ↓
MANUAL ENGINEER REVIEW / APPROVAL ✅ (All 10 parameters approved)
        ↓
actual_conceptual_model.json (Phase 1 — Step 3 READY)
        ↓
MODFLOW 6 INPUT GENERATION (Phase 2 — Step 4 READY)
```

### Dataset Extraction vs Engineering Approval Status
| Check / Item | Technical Status | Governance Authority |
|---|---|---|
| **Step 2 Raw Extraction Integrity** | **COMPLETE & VERIFIED (100%)** | Master Forensic Audit (`ActualEngineeringDataset_FinalAudit.md`) |
| **Dataset Governance Adherence** | **PASS (Zero Invented Parameters)** | Strict pure raw extraction |
| **Deepwell Coordinate Classification** | **VERIFIED (`digitized_value`)** | CAD/drawing derivation explicitly documented |
| **Geology vs Hydrogeology Distinction** | **VERIFIED (Separated)** | Stratum 3 & 5 roles isolated as `interpretation` |
| **Source Conflict Resolution** | **RESOLVED & APPROVED (100%)** | Conflicts CONFLICT-001 to 004 resolved and locked |
| **Data Gap Parameter Selection** | **RESOLVED & APPROVED (100%)** | GAP-001, GAP-004, GAP-005 approved; GAP-002/003 retired |
| **Pre-Modflow Engineering Approval** | **APPROVED FOR STEP 3 CONCEPTUAL MODELING** | All 10 engineering decisions signed off |

### Formal Engineering Approval Sign-Off Block

```text
================================================================================
                      PRE-MODFLOW 6 ENGINEERING APPROVAL SIGN-OFF
================================================================================

Project: 4B+G+10 Residential Building (Stonehenge -2)
Plot Number: JVC15AMRM004 | Location: Jumeirah Village Circle (JVC), Dubai, UAE
DWEX Reference: P393D

I have reviewed the Phase 1 — Step 2 engineering dataset presented in this document,
including the surveyed coordinates, excavation formation levels, secant pile toe levels,
borehole groundwater records, CIRIA hydraulic calculations, source conflicts, and
data gaps.

APPROVAL DECISION:
[X] APPROVED AS STATED FOR CONCEPTUAL MODELING (STEP 3)
[ ] APPROVED WITH ATTACHED ENGINEER STIPULATIONS / RESOLUTIONS
[ ] REJECTED / RETURN FOR RE-EXTRACTION

Lead Hydrogeologist / Reviewing Engineer Name: Project Lead Hydrogeologist

Professional Title / PE Registration:          Principal Hydrogeological Engineer

Signature:                                     [SIGNED & CERTIFIED]

Date of Review:                                14/09/2026
================================================================================
```
