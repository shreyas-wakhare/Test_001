# Stonehenge-2 Dewatering Conceptual Groundwater Model

> **Purpose**: BASE CONCEPTUAL GROUNDWATER / DEWATERING MODEL  
> **Project**: 4B+G+10 Residential Building (Stonehenge -2) (Plot: `JVC15AMRM004`)  
> **Workflow Stage**: Phase 1 — Step 3: Conceptual Model Creation  
> **Status**: `GENERATED_PENDING_ENGINEER_APPROVAL`  
> **Ultimate Source of Truth**: `data/actual/extracted/PreModflowApproval.md`  
> **Supporting Source**: `data/actual/extracted/actual_engineering_dataset.json`  

---

## 01. Model Metadata

| Metadata Property | Specification / Value |
|:---|:---|
| **model_name** | `Stonehenge-2 Dewatering Conceptual Groundwater Model` |
| **project_name** | `4B+G+10 Residential Building (Stonehenge -2)` |
| **project_reference** | `P393D` |
| **plot_reference** | `JVC15AMRM004` |
| **location** | `Al Barsha South Fourth, Jumeirah Village Circle (JVC), Dubai, UAE` |
| **country** | `United Arab Emirates` |
| **city** | `Dubai` |
| **purpose** | `BASE CONCEPTUAL GROUNDWATER / DEWATERING MODEL` |
| **model_type** | `Three-Dimensional Hydrogeological Conceptual Dewatering Model` |
| **workflow_phase** | `Phase 1 — Step 3: Conceptual Model Creation` |
| **workflow_step** | `Step 3` |
| **model_status** | `actual_conceptual_model.json` |
| **conceptual_model_status** | `GENERATED_PENDING_ENGINEER_APPROVAL` |
| **governing_workflow** | `ModflowSteps.md (FROZEN)` |
| **ultimate_source_of_truth** | `data/actual/extracted/PreModflowApproval.md` |
| **supporting_source** | `data/actual/extracted/actual_engineering_dataset.json` |
| **research_source** | `data/actual/extracted/HydrogeologicalParameterResearch.md` |
| **data_gap_source** | `data/actual/extracted/HydrogeologicalDataGapResearch.md` |
| **CRS** | `WGS 84 / Dubai Local TM (DLTM) (EPSG:3997)` |
| **model_scope** | `BASE_CONCEPTUAL_MODEL_ONLY` |
| **scenario_policy** | `SINGLE_BASE_CONCEPTUAL_MODEL (No alternative scenarios, no sensitivity cases in active parameters)` |
| **modflow_generation_status** | `NOT_PERFORMED (Conceptual modeling phase only; native MODFLOW 6 package generation deferred to Phase 2 — Step 4 following manual engineer sign-off)` |
| **mf6_execution_status** | `NOT_EXECUTED` |
| **governance_notes** | `This artifact represents the proposed conceptual groundwater model synthesized exclusively from the approved engineering decisions in PreModflowApproval.md. It is NOT approved_conceptual_model.json, which requires formal manual human engineering sign-off.` |

### Governing Units

| Physical Dimension | Prescribed Engineering Unit |
|:---|:---|
| **length** | `meter` |
| **time** | `day` |
| **discharge** | `m3/day` |
| **discharge_hourly** | `m3/hr` |
| **hydraulic_conductivity** | `m/day` |
| **specific_yield** | `dimensionless` |
| **specific_storage** | `1/meter` |
| **elevation** | `m DMD (Dubai Mining Datum)` |

> **Governance Note**: This artifact represents the proposed conceptual groundwater model synthesized exclusively from the approved engineering decisions in PreModflowApproval.md. It is NOT approved_conceptual_model.json, which requires formal manual human engineering sign-off.

---

## 02. Model Domain & Geometry

### Domain Distinction
- **Engineering Domain**: Physical site boundary defined by surveyed CAD coordinates enclosing 1633.18 m² with a perimeter of 168.0 m.
- **Future Numerical Model Grid**: Numerical discretization (cell sizes, row/column counts, regional buffer extent) is strictly deferred to Phase 2 (FloPy / MODFLOW 6 input file generation) and is NOT invented in this conceptual model.

### Coordinate Reference System (CRS)
- **Name**: WGS 84 / Dubai Local TM (DLTM)
- **Code**: `EPSG:3997`
- **Projection Type**: Transverse Mercator
- **Unit**: meter
- **Central Meridian**: 55.3333333333333°
- **Latitude of Origin**: 0.0°
- **False Easting**: 500000.0 m
- **False Northing**: 0.0 m
- **Provenance**: Source ID `SRC-002`, `MS-1-P393D - R5.pdf` (p. [16], Drawing DEW-1-P393D Coordinate Callouts)

### Approved Plot Boundary & Geometry
- **Approved Plot Surface Area**: **1633.18 m2** (`APPROVED`, `approved_engineering_input`, Ref: `CONFLICT-001`)
  - *Derivation Logic*: Shoelace formula applied to 4 DLTM surveyed corner coordinates from Drawing DEW-1-P393D Rev 07
  - *Rejected Alternative*: 1755.0 m² narrative rectangular approximation rejected under CONFLICT-001
  - *Provenance*: Primary `PreModflowApproval.md (Section 02, 13 CONFLICT-001, 18)`, Supporting `MS-1-P393D - R5.pdf (Page 16, Drawing DEW-1-P393D Rev 07)`
- **Approved Perimeter**: **168.0 m** (`APPROVED`, `approved_engineering_input`)
- **Boundary Geometry Source**: MS-1-P393D - R5.pdf (Page 16, Drawing DEW-1-P393D Rev 07)
- **Spatial Interpretation**: The model domain is defined by an irregular quadrilateral polygon enclosing 1633.18 m² with four distinct perimeter segments totaling 168.0 m. The plot is oriented at approximately 40 degrees counterclockwise from grid North.

### Surveyed Boundary Coordinates (DLTM EPSG:3997)

| Corner ID | Easting (m) | Northing (m) | CRS | Classification | Source & Page |
|:---|---:|---:|:---|:---|:---|
| **Corner_1_NW** | 486976.064 | 2772616.704 | `EPSG:3997` | `raw_fact` | MS-1-P393D - R5.pdf (p. [16], Drawing DEW-1-P393D Rev 07) |
| **Corner_2_NE** | 487005.204 | 2772591.303 | `EPSG:3997` | `raw_fact` | MS-1-P393D - R5.pdf (p. [16], Drawing DEW-1-P393D Rev 07) |
| **Corner_3_SE** | 486975.639 | 2772557.378 | `EPSG:3997` | `raw_fact` | MS-1-P393D - R5.pdf (p. [16], Drawing DEW-1-P393D Rev 07) |
| **Corner_4_SW** | 486950.063 | 2772579.673 | `EPSG:3997` | `raw_fact` | MS-1-P393D - R5.pdf (p. [16], Drawing DEW-1-P393D Rev 07) |

### Surveyed Boundary Segments

| Segment ID | Length (m) | Drawing Callout (mm) | Source Provenance |
|:---|---:|---:|:---|
| **Segment_1_NW_to_NE** | 38.66 m | 38660 mm | Drawing DEW-1-P393D Rev 07 (p. 16) |
| **Segment_2_NE_to_SE** | 45.00 m | 45000 mm | Drawing DEW-1-P393D Rev 07 (p. 16) |
| **Segment_3_SE_to_SW** | 33.93 m | 33930 mm | Drawing DEW-1-P393D Rev 07 (p. 16) |
| **Segment_4_SW_to_NW** | 45.27 m | 45270 mm | Drawing DEW-1-P393D Rev 07 (p. 16) |

### Regional KMZ Site Anchor
- **Placemark Name**: `E6168D - TMF Found`
- **Role**: `REGIONAL_GEOGRAPHIC_ANCHOR_ONLY`
- **Coordinates (WGS84)**: Longitude `55.20432203890749° E`, Latitude `25.05890758988347° N` (CRS: `EPSG:4326`)
- **Boundary Polygon Present in KMZ**: `False`
- **Interpretation**: The KMZ file provides a regional geographic anchor point and does NOT constitute the approved plot boundary polygon (logged and resolved under GAP-001 in PreModflowApproval.md).
- **Provenance**: `E6168D - TMF Found.kmz (SRC-001)`

### Top View / Plan View (2D Engineering Diagram)

<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 720" width="100%" height="auto" style="background-color: #ffffff; border: 1px solid #cbd5e1; border-radius: 8px; font-family: Segoe UI, Arial, sans-serif;">
<defs>
<pattern id="gridPatT" width="30" height="30" patternUnits="userSpaceOnUse">
<path d="M 30 0 L 0 0 0 30" fill="none" stroke="#f1f5f9" stroke-width="1"/>
</pattern>
<filter id="dropShadowT" x="-10%" y="-10%" width="125%" height="125%">
<feDropShadow dx="1.5" dy="1.5" stdDeviation="2" flood-opacity="0.12"/>
</filter>
</defs>
<rect width="960" height="720" fill="url(#gridPatT)"/>
<rect x="20" y="15" width="620" height="46" rx="6" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.2" filter="url(#dropShadowT)"/>
<text x="35" y="33" font-size="13.5" font-weight="bold" fill="#0f172a">PLAN VIEW: CONCEPTUAL MODEL DOMAIN &amp; WELLFIELD LAYOUT</text>
<text x="35" y="49" font-size="10" fill="#475569">CRS: DLTM EPSG:3997 &middot; Plot Area: 1633.18 m² &middot; Perimeter: 168.0 m &middot; 6 Deepwells (DW-01 to DW-06)</text>
<g transform="translate(800, 60)">
<circle cx="35" cy="35" r="30" fill="#ffffff" stroke="#cbd5e1" stroke-width="1.2" filter="url(#dropShadowT)"/>
<path d="M 35 10 L 41 35 L 35 30 Z" fill="#dc2626"/>
<path d="M 35 10 L 29 35 L 35 30 Z" fill="#991b1b"/>
<path d="M 35 60 L 41 35 L 35 40 Z" fill="#cbd5e1"/>
<path d="M 35 60 L 29 35 L 35 40 Z" fill="#94a3b8"/>
<text x="35" y="8" font-size="11" font-weight="bold" fill="#dc2626" text-anchor="middle">N</text>
<text x="35" y="77" font-size="9" font-weight="bold" fill="#0f172a" text-anchor="middle">Grid North</text>
<text x="35" y="88" font-size="8" fill="#64748b" text-anchor="middle">Rotated -40°</text>
</g>
<polygon points="330.8,128.1 517.3,290.7 328.1,507.8 164.4,365.1" fill="#fef2f2" fill-opacity="0.4"/>
<polygon points="331.1,142.1 503.5,293.1 328.6,493.8 178.0,361.7" fill="#f8fafc" stroke="#1e293b" stroke-width="3.5" stroke-linejoin="round"/>
<polygon points="330.8,128.1 517.3,290.7 328.1,507.8 164.4,365.1" fill="none" stroke="#dc2626" stroke-width="2.2" stroke-dasharray="8,4" stroke-linejoin="round"/>
<g transform="translate(394.04999999999995, 193.39999999999998)">
<rect x="0" y="0" width="94" height="20" rx="3" fill="#ffffff" stroke="#dc2626" stroke-width="1" filter="url(#dropShadowT)"/>
<text x="47" y="14" font-size="9.5" font-weight="bold" fill="#dc2626" text-anchor="middle">38.66 m (38660)</text>
</g>
<g transform="translate(430.7, 389.25)">
<rect x="0" y="0" width="94" height="20" rx="3" fill="#ffffff" stroke="#dc2626" stroke-width="1" filter="url(#dropShadowT)"/>
<text x="47" y="14" font-size="9.5" font-weight="bold" fill="#dc2626" text-anchor="middle">45.00 m (45000)</text>
</g>
<g transform="translate(199.25, 444.45000000000005)">
<rect x="0" y="0" width="94" height="20" rx="3" fill="#ffffff" stroke="#dc2626" stroke-width="1" filter="url(#dropShadowT)"/>
<text x="47" y="14" font-size="9.5" font-weight="bold" fill="#dc2626" text-anchor="middle">33.93 m (33930)</text>
</g>
<g transform="translate(147.60000000000002, 236.60000000000002)">
<rect x="0" y="0" width="94" height="20" rx="3" fill="#ffffff" stroke="#dc2626" stroke-width="1" filter="url(#dropShadowT)"/>
<text x="47" y="14" font-size="9.5" font-weight="bold" fill="#dc2626" text-anchor="middle">45.27 m (45270)</text>
</g>
<circle cx="330.8" cy="128.1" r="5.5" fill="#dc2626" stroke="#ffffff" stroke-width="1.5"/>
<g transform="translate(185.8, 92.1)">
<rect x="0" y="0" width="140" height="28" rx="4" fill="#ffffff" stroke="#dc2626" stroke-width="1" filter="url(#dropShadowT)"/>
<text x="6" y="12" font-size="9.5" font-weight="bold" fill="#0f172a">Corner_1_NW</text>
<text x="6" y="23" font-size="8" fill="#475569">486976.06E, 2772616.70N</text>
</g>
<circle cx="517.3" cy="290.7" r="5.5" fill="#dc2626" stroke="#ffffff" stroke-width="1.5"/>
<g transform="translate(529.3, 268.7)">
<rect x="0" y="0" width="140" height="28" rx="4" fill="#ffffff" stroke="#dc2626" stroke-width="1" filter="url(#dropShadowT)"/>
<text x="6" y="12" font-size="9.5" font-weight="bold" fill="#0f172a">Corner_2_NE</text>
<text x="6" y="23" font-size="8" fill="#475569">487005.20E, 2772591.30N</text>
</g>
<circle cx="328.1" cy="507.8" r="5.5" fill="#dc2626" stroke="#ffffff" stroke-width="1.5"/>
<g transform="translate(340.1, 509.8)">
<rect x="0" y="0" width="140" height="28" rx="4" fill="#ffffff" stroke="#dc2626" stroke-width="1" filter="url(#dropShadowT)"/>
<text x="6" y="12" font-size="9.5" font-weight="bold" fill="#0f172a">Corner_3_SE</text>
<text x="6" y="23" font-size="8" fill="#475569">486975.64E, 2772557.38N</text>
</g>
<circle cx="164.4" cy="365.1" r="5.5" fill="#dc2626" stroke="#ffffff" stroke-width="1.5"/>
<g transform="translate(19.400000000000006, 367.1)">
<rect x="0" y="0" width="140" height="28" rx="4" fill="#ffffff" stroke="#dc2626" stroke-width="1" filter="url(#dropShadowT)"/>
<text x="6" y="12" font-size="9.5" font-weight="bold" fill="#0f172a">Corner_4_SW</text>
<text x="6" y="23" font-size="8" fill="#475569">486950.06E, 2772579.67N</text>
</g>
<g id="DW-01">
<circle cx="333.2" cy="417.6" r="10" fill="#0284c7" fill-opacity="0.25" stroke="#0284c7" stroke-width="2"/>
<circle cx="333.2" cy="417.6" r="4" fill="#0284c7"/>
<line x1="321.2" y1="417.6" x2="345.2" y2="417.6" stroke="#0369a1" stroke-width="1.5"/>
<line x1="333.2" y1="405.6" x2="333.2" y2="429.6" stroke="#0369a1" stroke-width="1.5"/>
<rect x="349.2" y="415.6" width="140" height="24" rx="4" fill="#ffffff" stroke="#0284c7" stroke-width="1" filter="url(#dropShadowT)"/>
<text x="355.2" y="429.6" font-family="Segoe UI, Arial, sans-serif" font-size="11" font-weight="bold" fill="#0369a1">DW-01</text>
<text x="397.2" y="429.6" font-family="Segoe UI, Arial, sans-serif" font-size="8.5" fill="#475569">E:486976.44</text>
<text x="355.2" y="438.6" font-family="Segoe UI, Arial, sans-serif" font-size="8.5" fill="#475569">N:2772571.47</text>
</g>
<g id="DW-02">
<circle cx="313.4" cy="348.2" r="10" fill="#0284c7" fill-opacity="0.25" stroke="#0284c7" stroke-width="2"/>
<circle cx="313.4" cy="348.2" r="4" fill="#0284c7"/>
<line x1="301.4" y1="348.2" x2="325.4" y2="348.2" stroke="#0369a1" stroke-width="1.5"/>
<line x1="313.4" y1="336.2" x2="313.4" y2="360.2" stroke="#0369a1" stroke-width="1.5"/>
<rect x="158.39999999999998" y="344.2" width="140" height="24" rx="4" fill="#ffffff" stroke="#0284c7" stroke-width="1" filter="url(#dropShadowT)"/>
<text x="164.39999999999998" y="358.2" font-family="Segoe UI, Arial, sans-serif" font-size="11" font-weight="bold" fill="#0369a1">DW-02</text>
<text x="206.39999999999998" y="358.2" font-family="Segoe UI, Arial, sans-serif" font-size="8.5" fill="#475569">E:486973.34</text>
<text x="164.39999999999998" y="367.2" font-family="Segoe UI, Arial, sans-serif" font-size="8.5" fill="#475569">N:2772582.31</text>
</g>
<g id="DW-03">
<circle cx="238.2" cy="349.4" r="10" fill="#0284c7" fill-opacity="0.25" stroke="#0284c7" stroke-width="2"/>
<circle cx="238.2" cy="349.4" r="4" fill="#0284c7"/>
<line x1="226.2" y1="349.4" x2="250.2" y2="349.4" stroke="#0369a1" stroke-width="1.5"/>
<line x1="238.2" y1="337.4" x2="238.2" y2="361.4" stroke="#0369a1" stroke-width="1.5"/>
<rect x="83.19999999999999" y="331.4" width="140" height="24" rx="4" fill="#ffffff" stroke="#0284c7" stroke-width="1" filter="url(#dropShadowT)"/>
<text x="89.19999999999999" y="345.4" font-family="Segoe UI, Arial, sans-serif" font-size="11" font-weight="bold" fill="#0369a1">DW-03</text>
<text x="131.2" y="345.4" font-family="Segoe UI, Arial, sans-serif" font-size="8.5" fill="#475569">E:486961.60</text>
<text x="89.19999999999999" y="354.4" font-family="Segoe UI, Arial, sans-serif" font-size="8.5" fill="#475569">N:2772582.13</text>
</g>
<g id="DW-04">
<circle cx="331.4" cy="274.3" r="10" fill="#0284c7" fill-opacity="0.25" stroke="#0284c7" stroke-width="2"/>
<circle cx="331.4" cy="274.3" r="4" fill="#0284c7"/>
<line x1="319.4" y1="274.3" x2="343.4" y2="274.3" stroke="#0369a1" stroke-width="1.5"/>
<line x1="331.4" y1="262.3" x2="331.4" y2="286.3" stroke="#0369a1" stroke-width="1.5"/>
<rect x="347.4" y="258.3" width="140" height="24" rx="4" fill="#ffffff" stroke="#0284c7" stroke-width="1" filter="url(#dropShadowT)"/>
<text x="353.4" y="272.3" font-family="Segoe UI, Arial, sans-serif" font-size="11" font-weight="bold" fill="#0369a1">DW-04</text>
<text x="395.4" y="272.3" font-family="Segoe UI, Arial, sans-serif" font-size="8.5" fill="#475569">E:486976.16</text>
<text x="353.4" y="281.3" font-family="Segoe UI, Arial, sans-serif" font-size="8.5" fill="#475569">N:2772593.87</text>
</g>
<g id="DW-05">
<circle cx="334.1" cy="194.8" r="10" fill="#0284c7" fill-opacity="0.25" stroke="#0284c7" stroke-width="2"/>
<circle cx="334.1" cy="194.8" r="4" fill="#0284c7"/>
<line x1="322.1" y1="194.8" x2="346.1" y2="194.8" stroke="#0369a1" stroke-width="1.5"/>
<line x1="334.1" y1="182.8" x2="334.1" y2="206.8" stroke="#0369a1" stroke-width="1.5"/>
<rect x="350.1" y="170.8" width="140" height="24" rx="4" fill="#ffffff" stroke="#0284c7" stroke-width="1" filter="url(#dropShadowT)"/>
<text x="356.1" y="184.8" font-family="Segoe UI, Arial, sans-serif" font-size="11" font-weight="bold" fill="#0369a1">DW-05</text>
<text x="398.1" y="184.8" font-family="Segoe UI, Arial, sans-serif" font-size="8.5" fill="#475569">E:486976.57</text>
<text x="356.1" y="193.8" font-family="Segoe UI, Arial, sans-serif" font-size="8.5" fill="#475569">N:2772606.27</text>
</g>
<g id="DW-06">
<circle cx="457.2" cy="322.4" r="10" fill="#0284c7" fill-opacity="0.25" stroke="#0284c7" stroke-width="2"/>
<circle cx="457.2" cy="322.4" r="4" fill="#0284c7"/>
<line x1="445.2" y1="322.4" x2="469.2" y2="322.4" stroke="#0369a1" stroke-width="1.5"/>
<line x1="457.2" y1="310.4" x2="457.2" y2="334.4" stroke="#0369a1" stroke-width="1.5"/>
<rect x="473.2" y="312.4" width="140" height="24" rx="4" fill="#ffffff" stroke="#0284c7" stroke-width="1" filter="url(#dropShadowT)"/>
<text x="479.2" y="326.4" font-family="Segoe UI, Arial, sans-serif" font-size="11" font-weight="bold" fill="#0369a1">DW-06</text>
<text x="521.2" y="326.4" font-family="Segoe UI, Arial, sans-serif" font-size="8.5" fill="#475569">E:486995.81</text>
<text x="479.2" y="335.4" font-family="Segoe UI, Arial, sans-serif" font-size="8.5" fill="#475569">N:2772586.34</text>
</g>
<g transform="translate(660, 175)">
<rect x="0" y="0" width="280" height="350" rx="6" fill="#ffffff" stroke="#cbd5e1" stroke-width="1.2" filter="url(#dropShadowT)"/>
<rect x="0" y="0" width="280" height="30" rx="6 6 0 0" fill="#f1f5f9" stroke="#cbd5e1" stroke-width="1"/>
<text x="14" y="20" font-size="11.5" font-weight="bold" fill="#0f172a">PLAN VIEW LEGEND</text>
<line x1="14" y1="48" x2="42" y2="48" stroke="#dc2626" stroke-width="2.5" stroke-dasharray="6,3"/>
<text x="50" y="51" font-size="9.5" font-weight="bold" fill="#1e293b">Plot Boundary (1633.18 m²)</text>
<text x="50" y="62" font-size="8.5" fill="#64748b">Surveyed 4-corner boundary polygon</text>
<line x1="14" y1="82" x2="42" y2="82" stroke="#1e293b" stroke-width="4"/>
<text x="50" y="85" font-size="9.5" font-weight="bold" fill="#1e293b">Secant Pile Wall (168.0 m)</text>
<text x="50" y="96" font-size="8.5" fill="#64748b">4-sided cutoff shoring enclosure</text>
<circle cx="28" cy="120" r="8" fill="#0284c7" fill-opacity="0.3" stroke="#0284c7" stroke-width="2"/>
<circle cx="28" cy="120" r="3.5" fill="#0284c7"/>
<text x="50" y="119" font-size="9.5" font-weight="bold" fill="#0284c7">Deepwells: DW-01 to DW-06 (6 nos)</text>
<text x="50" y="130" font-size="8.5" fill="#64748b">700 mm Ø &middot; 8" slotted UPVC screen</text>
<rect x="16" y="148" width="24" height="15" fill="#f8fafc" stroke="#94a3b8" stroke-width="1"/>
<text x="50" y="155" font-size="9.5" font-weight="bold" fill="#1e293b">Excavation Footprint</text>
<text x="50" y="166" font-size="8.5" fill="#64748b">Levels 01 to 08 (down to -8.00 m DMD)</text>
<line x1="14" y1="188" x2="42" y2="188" stroke="#475569" stroke-width="2.5"/>
<text x="50" y="190" font-size="9.5" font-weight="bold" fill="#1e293b">Discharge Line (2400 m)</text>
<text x="50" y="201" font-size="8.5" fill="#64748b">Dedicated route to Nakheel line</text>
<line x1="14" y1="220" x2="42" y2="220" stroke="#059669" stroke-width="2.5" stroke-dasharray="5,2"/>
<text x="50" y="223" font-size="9.5" font-weight="bold" fill="#1e293b">French Drain Collectors</text>
<text x="50" y="234" font-size="8.5" fill="#64748b">0.50m x 0.50m aggregate channels</text>
<rect x="12" y="250" width="255" height="34" rx="4" fill="#f0fdf4" stroke="#86efac" stroke-width="1"/>
<text x="20" y="264" font-size="9.5" font-weight="bold" fill="#166534">Target Dewatering: -8.50 m DMD</text>
<text x="20" y="276" font-size="8.5" fill="#15803d">0.50 m dry clearance below -8.00m sump</text>
<rect x="12" y="292" width="255" height="44" rx="4" fill="#f0f9ff" stroke="#bae6fd" stroke-width="1"/>
<text x="20" y="306" font-size="9" font-weight="bold" fill="#0369a1">System Pumping Rates:</text>
<text x="20" y="318" font-size="8.5" fill="#0284c7">&bull; Steady Total: 46.5 m³/hr (7.75 m³/hr/well)</text>
<text x="20" y="329" font-size="8.5" fill="#0284c7">&bull; Peak Total: 93.0 m³/hr (15.5 m³/hr/well)</text>
</g>
<g transform="translate(100, 650)">
<rect x="0" y="0" width="480" height="34" rx="4" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1"/>
<line x1="20" y1="17" x2="180" y2="17" stroke="#0f172a" stroke-width="2.5"/>
<line x1="20" y1="11" x2="20" y2="23" stroke="#0f172a" stroke-width="2"/>
<line x1="100" y1="13" x2="100" y2="21" stroke="#0f172a" stroke-width="1.5"/>
<line x1="180" y1="11" x2="180" y2="23" stroke="#0f172a" stroke-width="2"/>
<text x="20" y="29" font-size="8.5" fill="#0f172a" text-anchor="middle">0m</text>
<text x="100" y="29" font-size="8.5" fill="#0f172a" text-anchor="middle">12.5m</text>
<text x="180" y="29" font-size="8.5" fill="#0f172a" text-anchor="middle">25m</text>
<text x="220" y="22" font-size="9.5" fill="#334155">Scale: 1 unit = 1 meter &middot; Grid North: 0° (Site: -40°)</text>
</g>
</svg>

> **Top View Visualization Note**: Structured engineering top/plan view capturing the spatial relationship between the surveyed plot limit, the continuous 4-sided secant pile shoring perimeter, and the 6 abstraction deepwells distributed internally.

---

## 03. Model Layers & Hydrogeology

### Stratigraphic Framework
- **Total Conceptual Layers**: 5
- **Model Ground Surface Plane (Layer 1 Top)**: **+8.25 m DMD**
- **Existing Ground Surface Decision**: **+8.45 m DMD**
- **Model Base Elevation (Layer 5 Bottom)**: **-31.75 m DMD**
- **Total Modeled Stratigraphic Column Thickness**: **40.0 m**
- **Reconciliation Notes**: Approved ground surface plane for numerical top of Layer 1 is +8.25 m DMD (REV-005 in PreModflowApproval.md, based on arithmetic mean of 5 borehole elevations: 8.15 to 8.35 m DMD). Existing ground elevation of +8.45 m DMD from calculation sheet CAL-1-P393D is retained as CONFLICT-004 decision.

### Conceptual Stratigraphic Column

| Layer ID | Geological Name | Lithology | Top (m DMD) | Bottom (m DMD) | Thickness (m) | Depth Range (m bgl) | Hydrogeological Role |
|:---:|:---|:---|---:|---:|---:|:---|:---|
| **L1 (Layer 1)** | Aeolian Dune Sand / Silt | Fine Sand with Silt | +8.25 | +6.75 | 1.5 | 0.0 - 1.5 m | **Vadose Zone / Unsaturated Cover** |
| **L2 (Layer 2)** | Upper Weathered Sandstone | Weathered Sandstone | +6.75 | -4.75 | 11.5 | 1.5 - 13.0 m | **Upper Unconfined/Semi-confined Sandstone Aquifer Unit** |
| **L3 (Layer 3)** | Moderately Weathered Sandstone | Gypsiferous Sandstone | -4.75 | -14.75 | 10.0 | 13.0 - 23.0 m | **Screened Aquifer** |
| **L4 (Layer 4)** | Conglomeratic Sandstone | Conglomeratic Sandstone | -14.75 | -19.75 | 5.0 | 23.0 - 28.0 m | **Lower Semi-pervious Transition Unit** |
| **L5 (Layer 5)** | Calcisiltite / Siltstone | Calcisiltite / Siltstone | -19.75 | -31.75 | 12.0 | 28.0 - 40.0 m | **Lower Confining Bed** |

### Layer-by-Layer Engineering & Hydrogeological Characterization

#### Layer 1 (L1) &mdash; Aeolian Dune Sand / Silt
- **Material Description**: Medium dense to very dense, light brown to brown, slightly silty, fine SAND
- **Top Elevation**: `+8.25 m DMD` &middot; **Bottom Elevation**: `+6.75 m DMD` &middot; **Thickness**: `1.5 m`
- **Depth Range Below Ground**: `0.0 to 1.5 m bgl`
- **Weathering Condition**: Unweathered modern aeolian deposit
- **Grain / Material Characteristics**: Fine grained, slightly silty, non-cohesive, medium dense to very dense
- **SPT N-Value Information**: N-values range from 18 to >50 (mean ~35)
- **UCS Rock Strength Information**: N/A (unconsolidated soil formation)
- **Hydrogeological Role**: **Vadose Zone / Unsaturated Cover**
- **Aquifer or Confining Behavior**: Unsaturated permeable soil cover (static water table is at +6.25 m DMD, below Layer 1 base)
- **Hydraulic Function**: Transmits surface infiltration where unpaved; largely desaturated under ambient conditions
- **Groundwater Table Relevance**: Located entirely above the static groundwater table (+6.25 m DMD)
- **Well Screen Interaction**: No screen interaction; deepwells are solid cased through this interval
- **Excavation Interaction**: Stage 1 bulk excavation completely removes this layer down to +6.75 m DMD in the dry
- **Shoring Interaction**: Secant pile wall penetrates completely through Layer 1
- **Hydraulic Properties Applicability**: `Final approved baseline: Kh = 2.3×10⁻⁵ m/s [1.9872 m/day], Kv = 1.0×10⁻⁵ m/s [0.864 m/day], Ss = 1.0×10⁻⁴ 1/m, Sy = 0.25 (dimensionless)`
- **Classification**: `raw_fact`
- **Source & Provenance**: `Soil report.pdf` (p. [12], Section: Table 2: Recommended Design Subsurface Profile)
- **Engineering Notes**: Top surface reconciled at +8.25 m DMD under REV-005. Fully dry prior to and during dewatering.

#### Layer 2 (L2) &mdash; Upper Weathered Sandstone
- **Material Description**: Extremely weak to very weak, light brown, fine to medium grained SANDSTONE
- **Top Elevation**: `+6.75 m DMD` &middot; **Bottom Elevation**: `-4.75 m DMD` &middot; **Thickness**: `11.5 m`
- **Depth Range Below Ground**: `1.5 to 13.0 m bgl`
- **Weathering Condition**: Highly to moderately weathered
- **Grain / Material Characteristics**: Fine to medium grained sandstone, highly fractured/fissured, weakly cemented with carbonate matrix
- **SPT N-Value Information**: N > 50 (refusal encountered throughout)
- **UCS Rock Strength Information**: 0.5 to 1.5 MPa (extremely weak to very weak rock)
- **Hydrogeological Role**: **Upper Unconfined/Semi-confined Sandstone Aquifer Unit**
- **Aquifer or Confining Behavior**: Water table aquifer hosting the static groundwater table (+6.25 m DMD)
- **Hydraulic Function**: Hosts unconfined water table; contributes to lateral seepage and storage release during dewatering
- **Groundwater Table Relevance**: Contains the static water table (+6.25 m DMD); dewatered during Phase 1 pre-drawdown
- **Well Screen Interaction**: Upper solid blank casing of deepwells passes through this layer (no screen)
- **Excavation Interaction**: Excavation step levels 01 to 04 (-3.70 to -4.60 m DMD) are founded within this layer
- **Shoring Interaction**: Secant pile wall penetrates completely through Layer 2, providing a lateral barrier across this interval
- **Hydraulic Properties Applicability**: `Final approved baseline: Kh = 5.0×10⁻⁵ m/s [4.32 m/day], Kv = 1.0×10⁻⁵ m/s [0.864 m/day], Ss = 2.5×10⁻⁵ 1/m, Sy = 0.12 (dimensionless)`
- **Classification**: `raw_fact`
- **Source & Provenance**: `Soil report.pdf` (p. [12], Section: Table 2: Recommended Design Subsurface Profile)
- **Engineering Notes**: Contains initial static water table (+6.25 m DMD). Undergoes primary water table depression during dewatering.

#### Layer 3 (L3) &mdash; Moderately Weathered Sandstone
- **Material Description**: Extremely weak to very weak, reddish brown, fine to medium grained, slightly gypsiferous SANDSTONE
- **Top Elevation**: `-4.75 m DMD` &middot; **Bottom Elevation**: `-14.75 m DMD` &middot; **Thickness**: `10.0 m`
- **Depth Range Below Ground**: `13.0 to 23.0 m bgl`
- **Weathering Condition**: Moderately weathered, containing bedding plane gypsum laminations
- **Grain / Material Characteristics**: Fine to medium grained sandstone with secondary crystalline gypsum seams and horizontal laminations
- **SPT N-Value Information**: N > 50 (refusal)
- **UCS Rock Strength Information**: 1.0 to 3.0 MPa (extremely weak to very weak rock)
- **Hydrogeological Role**: **Screened Aquifer**
- **Aquifer or Confining Behavior**: Primary productive semi-confined aquifer layer targeted for abstraction
- **Hydraulic Function**: Main water-bearing and water-yielding unit; hosts all deepwell intake screens (-7.80 to -14.50 m DMD)
- **Groundwater Table Relevance**: Direct zone of active deepwell pumping depressurization; dictates regional cone of depression
- **Well Screen Interaction**: 100% of the deepwell screen interval (-7.80 to -14.50 m DMD, 6.7 m length) for all 6 wells is located inside Layer 3
- **Excavation Interaction**: Excavation step levels 05 to 08 (-6.10 to -8.00 m DMD, including deepest elevator/sump pit at -8.00 m DMD) are excavated into this layer
- **Shoring Interaction**: Secant pile wall toes (-9.30, -10.00, -11.65 m DMD) terminate inside Layer 3. The wall is partially penetrating relative to Layer 3.
- **Hydraulic Properties Applicability**: `Final approved baseline: Kh = 5.0×10⁻⁵ m/s [4.32 m/day], Kv = 1.0×10⁻⁵ m/s [0.864 m/day], Ss = 2.5×10⁻⁵ 1/m, Sy = 0.12 (dimensionless)`
- **Classification**: `raw_fact (geology) / interpretation (Screened Aquifer role)`
- **Source & Provenance**: `Soil report.pdf / MS-1-P393D - R5.pdf` (p. [12, 19, 20], Section: Soil Report Table 2 & Method Statement CAL-1-P393D)
- **Engineering Notes**: Critical hydrogeological unit. Screened by all 6 deepwells. Secant pile toe terminates within this layer, creating a window for underflow.

#### Layer 4 (L4) &mdash; Conglomeratic Sandstone
- **Material Description**: Very weak, reddish brown, slightly gypsiferous, conglomeratic SANDSTONE
- **Top Elevation**: `-14.75 m DMD` &middot; **Bottom Elevation**: `-19.75 m DMD` &middot; **Thickness**: `5.0 m`
- **Depth Range Below Ground**: `23.0 to 28.0 m bgl`
- **Weathering Condition**: Moderately weathered conglomeratic sandstone
- **Grain / Material Characteristics**: Poorly sorted sandstone containing rounded to subangular lithic gravel clasts and gypsum seams
- **SPT N-Value Information**: N > 50 (refusal)
- **UCS Rock Strength Information**: 1.5 to 3.5 MPa (very weak rock)
- **Hydrogeological Role**: **Lower Semi-pervious Transition Unit**
- **Aquifer or Confining Behavior**: Semi-pervious transitional stratum between screened aquifer and basal confining bed
- **Hydraulic Function**: Permits vertical upward leakage into Layer 3 under pumping gradients; forms the underflow pathway beneath well toes
- **Groundwater Table Relevance**: Immediately underlies the deepwell toe (-14.50 m DMD); conduit for deep vertical underflow
- **Well Screen Interaction**: Lies below deepwell toe (-14.50 m DMD); no screen or casing penetration
- **Excavation Interaction**: Located far below excavation formation (deepest sump is at -8.00 m DMD, 6.75 m above Layer 4 top)
- **Shoring Interaction**: Secant pile wall terminates 3.10 m to 5.45 m above Layer 4 top; wall does not penetrate this unit
- **Hydraulic Properties Applicability**: `Final approved baseline: Kh = 5.8×10⁻⁶ m/s [0.50112 m/day], Kv = 5.8×10⁻⁷ m/s [0.050112 m/day], Ss = 5.0×10⁻⁶ 1/m, Sy = 0.08 (dimensionless)`
- **Classification**: `raw_fact`
- **Source & Provenance**: `Soil report.pdf` (p. [12], Section: Table 2: Recommended Design Subsurface Profile)
- **Engineering Notes**: Acts as vertical transition layer between screened aquifer Layer 3 and basal confining bed Layer 5.

#### Layer 5 (L5) &mdash; Calcisiltite / Siltstone
- **Material Description**: Very weak to weak, light brown to off-white, fine grained CALCISILTITE/ SILTSTONE
- **Top Elevation**: `-19.75 m DMD` &middot; **Bottom Elevation**: `-31.75 m DMD` &middot; **Thickness**: `12.0 m`
- **Depth Range Below Ground**: `28.0 to 40.0 m bgl`
- **Weathering Condition**: Slightly weathered to unweathered dense carbonate siltstone
- **Grain / Material Characteristics**: Very fine grained, dense, cemented calcareous siltstone / calcisiltite
- **SPT N-Value Information**: N > 50 (refusal)
- **UCS Rock Strength Information**: 2.0 to 5.0 MPa (weak rock)
- **Hydrogeological Role**: **Lower Confining Bed**
- **Aquifer or Confining Behavior**: Regional low-permeability basal aquitard / confining floor
- **Hydraulic Function**: Retards vertical groundwater flow from deeper formations; forms effective hydraulic base of active dewatering system
- **Groundwater Table Relevance**: Limits upward vertical recharge from regional deep aquifers
- **Well Screen Interaction**: Deepwells terminate 5.25 m above Layer 5 top (-14.50 m vs -19.75 m DMD); no penetration
- **Excavation Interaction**: Lies 11.75 m below deepest elevator/sump formation (-8.00 m vs -19.75 m DMD)
- **Shoring Interaction**: Secant pile wall does not reach Layer 5; wall toe is 8.10 m to 10.45 m above Layer 5 top
- **Hydraulic Properties Applicability**: `Final approved baseline: Kh = 5.0×10⁻¹⁰ m/s [4.32×10⁻⁵ m/day], Kv = 1.0×10⁻¹⁰ m/s [8.64×10⁻⁶ m/day], Ss = 1.0×10⁻⁶ 1/m, Sy = 0.03 (dimensionless)`
- **Classification**: `raw_fact (geology) / interpretation (Lower Confining Bed role)`
- **Source & Provenance**: `Soil report.pdf / MS-1-P393D - R5.pdf` (p. [12, 19, 20], Section: Soil Report Table 2 & Method Statement CAL-1-P393D)
- **Engineering Notes**: Approved as the Lower Confining Bed in PreModflowApproval.md. Defines the impervious/semi-pervious base of the conceptual model.

### Hydrogeological Interactions & Dynamics
- **Screened Aquifer vs Basal Confining Bed**: Layer 3 (-4.75 to -14.75 m DMD) acts as the primary screened aquifer, while Layer 5 (-19.75 to -31.75 m DMD) functions as the basal confining unit. Layer 4 (-14.75 to -19.75 m DMD) provides a 5.0 m transitional zone between them.
- **Deepwell Screen Placement**: All 6 deepwells (DW-01 to DW-06) have their 6.7 m screen interval placed between -7.80 and -14.50 m DMD, entirely within Layer 3. The well toe terminates at -14.50 m DMD, exactly at the base of Layer 3.
- **Excavation Penetration**: Excavation penetrates Layer 1 (0 to 1.5 m bgl), Layer 2 (1.5 to 13.0 m bgl, hosting Levels 01 to 04), and enters Layer 3 to reach deepest formation at -8.00 m DMD (Level 08 elevator/sump pit).
- **Secant Pile Shoring Interaction**: Secant pile wall penetrates through Layer 1 and Layer 2, terminating within Layer 3 at toe levels -9.30, -10.00, and -11.65 m DMD. The wall does not reach Layer 5 (-19.75 m DMD).
- **Underflow Mechanism**: Because the secant pile wall terminates at -9.30 to -11.65 m DMD while the basal confining bed begins at -19.75 m DMD, a permeable vertical gap of 8.10 m to 10.45 m exists beneath the wall toe. Groundwater underflow beneath the wall toe into the excavation drawdown cone is hydrogeologically possible and active.

### Underground Vertical View / Cross-Section (2D Engineering Diagram)

<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1120 920" width="100%" height="auto" style="background-color: #ffffff; border: 1px solid #cbd5e1; border-radius: 8px; font-family: Segoe UI, Arial, sans-serif;">
<defs>
<pattern id="soilPat1" width="16" height="16" patternUnits="userSpaceOnUse">
<circle cx="4" cy="4" r="1.2" fill="#d97706" opacity="0.35"/>
<circle cx="12" cy="12" r="1.2" fill="#d97706" opacity="0.35"/>
</pattern>
<pattern id="conglomPat" width="24" height="24" patternUnits="userSpaceOnUse">
<ellipse cx="7" cy="8" rx="4" ry="2.5" fill="#ea580c" opacity="0.45"/>
<ellipse cx="18" cy="17" rx="4.5" ry="3" fill="#ea580c" opacity="0.45"/>
</pattern>
<pattern id="secantHatchV" width="8" height="8" patternTransform="rotate(45 0 0)" patternUnits="userSpaceOnUse">
<line x1="0" y1="0" x2="0" y2="8" stroke="#334155" stroke-width="1.8"/>
</pattern>
<pattern id="screenHatchV" width="6" height="6" patternUnits="userSpaceOnUse">
<line x1="0" y1="3" x2="6" y2="3" stroke="#0284c7" stroke-width="1.8"/>
</pattern>
<filter id="shadowV" x="-5%" y="-5%" width="110%" height="110%">
<feDropShadow dx="2" dy="2" stdDeviation="2.5" flood-opacity="0.12"/>
</filter>
<marker id="seepArrow" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
<path d="M 0 0 L 10 5 L 0 10 z" fill="#0284c7"/>
</marker>
</defs>
<rect x="20" y="12" width="780" height="42" rx="6" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.2" filter="url(#shadowV)"/>
<text x="35" y="30" font-size="13.5" font-weight="bold" fill="#0f172a">VERTICAL CROSS-SECTION: HYDROSTRATIGRAPHY, EXCAVATION &amp; DEWATERING (5 STRATA)</text>
<text x="35" y="46" font-size="10" fill="#475569">Datum: Dubai Mining Datum (DMD) &middot; Baseline GWL: +6.25 m &middot; Deepest Formation: -8.00 m &middot; Target Dewatering: -8.50 m</text>
<line x1="110" y1="68.6" x2="110" y2="798.5" stroke="#475569" stroke-width="2"/>
<text x="105" y="58" font-size="10" font-weight="bold" fill="#0f172a" text-anchor="end">Elev (m DMD)</text>
<text x="45" y="58" font-size="9" fill="#64748b" text-anchor="end">Depth (bgl)</text>
<line x1="104" y1="78.5" x2="116" y2="78.5" stroke="#475569" stroke-width="1.5"/>
<text x="102" y="82.0" font-size="9" font-weight="bold" fill="#0f172a" text-anchor="end">+8.25</text>
<text x="45" y="82.0" font-size="8.5" fill="#64748b" text-anchor="end">0.00m</text>
<line x1="104" y1="105.5" x2="116" y2="105.5" stroke="#475569" stroke-width="1.5"/>
<text x="102" y="109.0" font-size="9" font-weight="bold" fill="#0f172a" text-anchor="end">+6.75</text>
<text x="45" y="109.0" font-size="8.5" fill="#64748b" text-anchor="end">1.50m</text>
<line x1="104" y1="114.5" x2="116" y2="114.5" stroke="#0284c7" stroke-width="2"/>
<text x="102" y="118.0" font-size="9" font-weight="bold" fill="#0284c7" text-anchor="end">+6.25</text>
<text x="45" y="118.0" font-size="8.5" font-weight="bold" fill="#0284c7" text-anchor="end">2.00m</text>
<line x1="104" y1="227.0" x2="116" y2="227.0" stroke="#475569" stroke-width="1"/>
<text x="102" y="230.5" font-size="8.5" fill="#334155" text-anchor="end">0.00</text>
<text x="45" y="230.5" font-size="8" fill="#64748b" text-anchor="end">8.25m</text>
<line x1="104" y1="312.5" x2="116" y2="312.5" stroke="#475569" stroke-width="1.5"/>
<text x="102" y="316.0" font-size="9" font-weight="bold" fill="#0f172a" text-anchor="end">-4.75</text>
<text x="45" y="316.0" font-size="8.5" fill="#64748b" text-anchor="end">13.00m</text>
<line x1="104" y1="371.0" x2="116" y2="371.0" stroke="#dc2626" stroke-width="2"/>
<text x="102" y="374.5" font-size="9" font-weight="bold" fill="#dc2626" text-anchor="end">-8.00</text>
<text x="45" y="374.5" font-size="8.5" font-weight="bold" fill="#dc2626" text-anchor="end">16.25m</text>
<line x1="104" y1="380.0" x2="116" y2="380.0" stroke="#059669" stroke-width="2"/>
<text x="102" y="383.5" font-size="9" font-weight="bold" fill="#059669" text-anchor="end">-8.50</text>
<text x="45" y="383.5" font-size="8.5" font-weight="bold" fill="#059669" text-anchor="end">16.75m</text>
<line x1="104" y1="407.0" x2="116" y2="407.0" stroke="#334155" stroke-width="1.5"/>
<text x="102" y="410.5" font-size="8.5" fill="#334155" text-anchor="end">-10.00</text>
<text x="45" y="410.5" font-size="8" fill="#64748b" text-anchor="end">18.25m</text>
<line x1="104" y1="492.5" x2="116" y2="492.5" stroke="#475569" stroke-width="1.5"/>
<text x="102" y="496.0" font-size="9" font-weight="bold" fill="#0f172a" text-anchor="end">-14.75</text>
<text x="45" y="496.0" font-size="8.5" fill="#64748b" text-anchor="end">23.00m</text>
<line x1="104" y1="582.5" x2="116" y2="582.5" stroke="#475569" stroke-width="1.5"/>
<text x="102" y="586.0" font-size="9" font-weight="bold" fill="#0f172a" text-anchor="end">-19.75</text>
<text x="45" y="586.0" font-size="8.5" fill="#64748b" text-anchor="end">28.00m</text>
<line x1="104" y1="798.5" x2="116" y2="798.5" stroke="#475569" stroke-width="1.5"/>
<text x="102" y="802.0" font-size="9" font-weight="bold" fill="#0f172a" text-anchor="end">-31.75</text>
<text x="45" y="802.0" font-size="8.5" fill="#64748b" text-anchor="end">40.00m</text>
<rect x="115" y="48" width="110" height="20" rx="3" fill="#f1f5f9" stroke="#cbd5e1" stroke-width="1"/>
<text x="170.0" y="62" font-size="9.5" font-weight="bold" fill="#0f172a" text-anchor="middle">STRATIGRAPHY</text>
<rect x="115" y="78.5" width="110" height="27.0" fill="#fef3c7" stroke="#d97706" stroke-width="1.2"/>
<rect x="115" y="78.5" width="110" height="27.0" fill="url(#soilPat1)"/>
<text x="170.0" y="96.0" font-size="9.5" font-weight="bold" fill="#92400e" text-anchor="middle">L1 &middot; 1.5m</text>
<rect x="115" y="105.5" width="110" height="207.0" fill="#fed7aa" fill-opacity="0.8" stroke="#ea580c" stroke-width="1.2"/>
<text x="170.0" y="135.5" font-size="10.5" font-weight="bold" fill="#9a3412" text-anchor="middle">LAYER 2</text>
<text x="170.0" y="150.5" font-size="9" font-weight="bold" fill="#9a3412" text-anchor="middle">Upper Sandstone</text>
<text x="170.0" y="165.5" font-size="8.5" fill="#c2410c" text-anchor="middle">Thk: 11.5 m</text>
<text x="170.0" y="180.5" font-size="8" fill="#7c2d12" text-anchor="middle">Upper Aquifer</text>
<text x="170.0" y="195.5" font-size="8" fill="#7c2d12" text-anchor="middle">(Water Table Host)</text>
<rect x="115" y="312.5" width="110" height="180.0" fill="#fdba74" stroke="#c2410c" stroke-width="1.5"/>
<text x="170.0" y="342.5" font-size="10.5" font-weight="bold" fill="#7c2d12" text-anchor="middle">LAYER 3</text>
<text x="170.0" y="357.5" font-size="9" font-weight="bold" fill="#7c2d12" text-anchor="middle">Screened Aquifer</text>
<text x="170.0" y="372.5" font-size="8.5" fill="#9a3412" text-anchor="middle">Thk: 10.0 m</text>
<text x="170.0" y="387.5" font-size="8" font-weight="bold" fill="#b91c1c" text-anchor="middle">PRIMARY AQUIFER</text>
<text x="170.0" y="400.5" font-size="8" fill="#7c2d12" text-anchor="middle">100% Well Screens</text>
<rect x="115" y="492.5" width="110" height="90.0" fill="#ffedd5" stroke="#ea580c" stroke-width="1.2"/>
<rect x="115" y="492.5" width="110" height="90.0" fill="url(#conglomPat)"/>
<text x="170.0" y="518.5" font-size="10" font-weight="bold" fill="#9a3412" text-anchor="middle">LAYER 4</text>
<text x="170.0" y="532.5" font-size="8.5" font-weight="bold" fill="#9a3412" text-anchor="middle">Conglomerate</text>
<text x="170.0" y="546.5" font-size="8" fill="#c2410c" text-anchor="middle">Thk: 5.0 m</text>
<text x="170.0" y="560.5" font-size="8" fill="#7c2d12" text-anchor="middle">Transition Unit</text>
<rect x="115" y="582.5" width="110" height="216.0" fill="#e2e8f0" stroke="#64748b" stroke-width="1.5"/>
<text x="170.0" y="614.5" font-size="10.5" font-weight="bold" fill="#0f172a" text-anchor="middle">LAYER 5</text>
<text x="170.0" y="630.5" font-size="9" font-weight="bold" fill="#0f172a" text-anchor="middle">Calcisiltite / Siltstone</text>
<text x="170.0" y="646.5" font-size="8.5" fill="#475569" text-anchor="middle">Thk: 12.0 m</text>
<text x="170.0" y="662.5" font-size="8" font-weight="bold" fill="#475569" text-anchor="middle">CONFINING BED</text>
<text x="170.0" y="676.5" font-size="8" fill="#64748b" text-anchor="middle">Impervious Floor</text>
<rect x="235" y="78.5" width="565" height="27.0" fill="#fef3c7" stroke="#cbd5e1" stroke-width="0.8"/>
<rect x="235" y="78.5" width="565" height="27.0" fill="url(#soilPat1)"/>
<rect x="235" y="105.5" width="565" height="207.0" fill="#fed7aa" fill-opacity="0.55" stroke="#cbd5e1" stroke-width="0.8"/>
<rect x="235" y="312.5" width="565" height="180.0" fill="#fdba74" fill-opacity="0.5" stroke="#cbd5e1" stroke-width="0.8"/>
<rect x="235" y="492.5" width="565" height="90.0" fill="#ffedd5" stroke="#cbd5e1" stroke-width="0.8"/>
<rect x="235" y="492.5" width="565" height="90.0" fill="url(#conglomPat)"/>
<rect x="235" y="582.5" width="565" height="216.0" fill="#e2e8f0" stroke="#cbd5e1" stroke-width="0.8"/>
<line x1="235" y1="78.5" x2="800" y2="78.5" stroke="#d97706" stroke-width="1.2"/>
<line x1="235" y1="105.5" x2="800" y2="105.5" stroke="#ea580c" stroke-width="1" stroke-dasharray="4,2"/>
<line x1="235" y1="312.5" x2="800" y2="312.5" stroke="#c2410c" stroke-width="1.2" stroke-dasharray="4,2"/>
<line x1="235" y1="492.5" x2="800" y2="492.5" stroke="#ea580c" stroke-width="1.2" stroke-dasharray="4,2"/>
<line x1="235" y1="582.5" x2="800" y2="582.5" stroke="#64748b" stroke-width="1.5"/>
<line x1="235" y1="114.5" x2="800" y2="114.5" stroke="#0284c7" stroke-width="2" stroke-dasharray="6,3"/>
<polygon points="245,113.5 255,113.5 250,122.5" fill="#0284c7"/>
<line x1="243" y1="111.5" x2="257" y2="111.5" stroke="#0284c7" stroke-width="1"/>
<text x="261" y="110.5" font-size="9.5" font-weight="bold" fill="#0369a1">Initial Static Groundwater Level: +6.25 m DMD (2.00 m bgl)</text>
<polygon points="314,78.5 314,293.6 348,293.6 348,306.2 390,306.2 390,336.8 440,336.8 440,367.4 490,367.4 490,371.0 550,371.0 550,367.4 605,367.4 605,336.8 652,336.8 652,78.5" fill="#ffffff" fill-opacity="0.96" stroke="#b45309" stroke-width="1.8"/>
<line x1="490" y1="371.0" x2="550" y2="371.0" stroke="#dc2626" stroke-width="3"/>
<text x="520" y="365.0" font-size="9.5" font-weight="bold" fill="#dc2626" text-anchor="middle">Deepest Formation: -8.00 m DMD (Level 08 Sump)</text>
<line x1="290" y1="380.0" x2="675" y2="380.0" stroke="#059669" stroke-width="2.2" stroke-dasharray="6,3"/>
<text x="680" y="383.5" font-size="9.5" font-weight="bold" fill="#059669">Target Dewatering: -8.50 m DMD</text>
<line x1="560" y1="371.0" x2="560" y2="380.0" stroke="#059669" stroke-width="1.5"/>
<line x1="556" y1="371.0" x2="564" y2="371.0" stroke="#059669" stroke-width="1.5"/>
<line x1="556" y1="380.0" x2="564" y2="380.0" stroke="#059669" stroke-width="1.5"/>
<text x="568" y="378.5" font-size="8.5" font-weight="bold" fill="#059669">0.50m Buffer</text>
<line x1="295" y1="114.5" x2="295" y2="380.0" stroke="#0284c7" stroke-width="1.5"/>
<polygon points="295,114.5 292,120.5 298,120.5" fill="#0284c7"/>
<polygon points="295,380.0 292,374.0 298,374.0" fill="#0284c7"/>
<text x="288" y="247.25" font-size="8.5" font-weight="bold" fill="#0369a1" text-anchor="end">Total Drawdown Δh = 14.75 m</text>
<rect x="304" y="78.5" width="14" height="328.5" fill="#334155" stroke="#0f172a" stroke-width="1.2"/>
<rect x="304" y="78.5" width="14" height="328.5" fill="url(#secantHatchV)"/>
<line x1="265" y1="407.0" x2="304" y2="407.0" stroke="#334155" stroke-width="1.2" stroke-dasharray="2,2"/>
<text x="260" y="410.5" font-size="8.5" font-weight="bold" fill="#334155" text-anchor="end">Wall Toe: -10.00 m</text>
<line x1="265" y1="436.7" x2="311" y2="436.7" stroke="#334155" stroke-width="1" stroke-dasharray="2,2"/>
<text x="260" y="440.2" font-size="8" fill="#475569" text-anchor="end">Deepest Toe: -11.65 m</text>
<rect x="652" y="78.5" width="14" height="315.9" fill="#334155" stroke="#0f172a" stroke-width="1.2"/>
<rect x="652" y="78.5" width="14" height="315.9" fill="url(#secantHatchV)"/>
<line x1="666" y1="394.4" x2="705" y2="394.4" stroke="#334155" stroke-width="1.2" stroke-dasharray="2,2"/>
<text x="710" y="397.9" font-size="8.5" font-weight="bold" fill="#334155">Wall Toe: -9.30 m</text>
<g id="deepwell_column_rep">
<rect x="368" y="78.5" width="10" height="288.9" fill="#ffffff" stroke="#0284c7" stroke-width="1.5"/>
<rect x="366" y="367.4" width="14" height="120.60000000000002" fill="#e0f2fe" stroke="#0284c7" stroke-width="2"/>
<rect x="366" y="367.4" width="14" height="120.60000000000002" fill="url(#screenHatchV)"/>
<polygon points="366,488.0 380,488.0 373,496.0" fill="#0284c7"/>
<circle cx="373" cy="395.4" r="4.5" fill="#0284c7"/>
<rect x="238" y="402.4" width="122" height="42" rx="3" fill="#ffffff" stroke="#0284c7" stroke-width="1" filter="url(#shadowV)"/>
<text x="244" y="415.4" font-size="9" font-weight="bold" fill="#0284c7">DW INTAKE SCREEN</text>
<text x="244" y="427.4" font-size="8" fill="#0369a1">-7.80 to -14.50 m DMD</text>
<text x="244" y="438.4" font-size="8" fill="#64748b">Length: 6.7 m (100% L3)</text>
</g>
<path d="M 270,409.4 Q 300,449.4 364,468.0" fill="none" stroke="#0284c7" stroke-width="2.2" stroke-dasharray="6,3" marker-end="url(#seepArrow)"/>
<path d="M 720,409.4 Q 675,454.4 382,473.0" fill="none" stroke="#0284c7" stroke-width="2.2" stroke-dasharray="6,3" marker-end="url(#seepArrow)"/>
<g transform="translate(730, 412.0)">
<line x1="0" y1="0" x2="0" y2="170.5" stroke="#9333ea" stroke-width="1.8"/>
<line x1="-5" y1="0" x2="5" y2="0" stroke="#9333ea" stroke-width="1.8"/>
<line x1="-5" y1="170.5" x2="5" y2="170.5" stroke="#9333ea" stroke-width="1.8"/>
<text x="8" y="24" font-size="9.5" font-weight="bold" fill="#9333ea">Permeable Window</text>
<text x="8" y="37" font-size="8.5" font-weight="bold" fill="#9333ea">Gap: 8.10 - 10.45 m</text>
<text x="8" y="49" font-size="7.5" fill="#6b21a8">(Toe to Layer 5 top)</text>
</g>
<g transform="translate(395, 491.0)">
<line x1="0" y1="0" x2="0" y2="91.5" stroke="#0284c7" stroke-width="1.5"/>
<line x1="-4" y1="0" x2="4" y2="0" stroke="#0284c7" stroke-width="1.5"/>
<line x1="-4" y1="91.5" x2="4" y2="91.5" stroke="#0284c7" stroke-width="1.5"/>
<text x="8" y="47.25" font-size="8.5" font-weight="bold" fill="#0284c7">5.25m Clearance to L5</text>
</g>
<rect x="420" y="510.5" width="280" height="34" rx="4" fill="#ffffff" fill-opacity="0.9" stroke="#ea580c" stroke-width="1"/>
<text x="430" y="525.5" font-size="10" font-weight="bold" fill="#9a3412">LAYER 4: Conglomeratic Sandstone (-14.75 to -19.75 m)</text>
<text x="430" y="538.5" font-size="8.5" fill="#c2410c">Thk: 5.0 m &middot; Lower Semi-Pervious Transition Unit &middot; Underflow Pathway</text>
<rect x="420" y="612.5" width="340" height="42" rx="4" fill="#ffffff" fill-opacity="0.9" stroke="#64748b" stroke-width="1.2"/>
<text x="430" y="629.5" font-size="10.5" font-weight="bold" fill="#0f172a">LAYER 5: Calcisiltite / Siltstone (-19.75 to -31.75 m)</text>
<text x="430" y="644.5" font-size="9" fill="#475569">Thk: 12.0 m &middot; Lower Confining Bed / Regional Low-Permeability Aquitard</text>
<g transform="translate(815, 12)">
<rect x="0" y="0" width="290" height="885" rx="6" fill="#ffffff" stroke="#cbd5e1" stroke-width="1.2" filter="url(#shadowV)"/>
<rect x="0" y="0" width="290" height="30" rx="6 6 0 0" fill="#f1f5f9" stroke="#cbd5e1" stroke-width="1"/>
<text x="14" y="20" font-size="11.5" font-weight="bold" fill="#0f172a">VERTICAL SECTION LEGEND</text>
<text x="14" y="46" font-size="9.5" font-weight="bold" fill="#0369a1">1. HYDROSTRATIGRAPHIC STRATA (5 LAYERS)</text>
<rect x="14" y="56" width="22" height="14" fill="#fef3c7" stroke="#d97706" stroke-width="1"/>
<text x="44" y="64" font-size="9" font-weight="bold" fill="#1e293b">Layer 1: Dune Sand / Silt (1.5 m)</text>
<text x="44" y="75" font-size="8" fill="#64748b">+8.25 to +6.75 m DMD &middot; Vadose Zone</text>
<rect x="14" y="88" width="22" height="14" fill="#fed7aa" stroke="#ea580c" stroke-width="1"/>
<text x="44" y="96" font-size="9" font-weight="bold" fill="#1e293b">Layer 2: Upper Sandstone (11.5 m)</text>
<text x="44" y="107" font-size="8" fill="#64748b">+6.75 to -4.75 m DMD &middot; Upper Aquifer / GWL</text>
<rect x="14" y="120" width="22" height="14" fill="#fdba74" stroke="#c2410c" stroke-width="1.2"/>
<text x="44" y="128" font-size="9" font-weight="bold" fill="#c2410c">Layer 3: Screened Aquifer (10.0 m)</text>
<text x="44" y="139" font-size="8" fill="#7c2d12">-4.75 to -14.75 m DMD &middot; Kh: 4.32 m/d &middot; Sy: 0.12</text>
<rect x="14" y="152" width="22" height="14" fill="#ffedd5" stroke="#ea580c" stroke-width="1"/>
<text x="44" y="160" font-size="9" font-weight="bold" fill="#1e293b">Layer 4: Conglomerate Sandstone (5.0 m)</text>
<text x="44" y="171" font-size="8" fill="#64748b">-14.75 to -19.75 m DMD &middot; Transition Unit</text>
<rect x="14" y="184" width="22" height="14" fill="#e2e8f0" stroke="#64748b" stroke-width="1.2"/>
<text x="44" y="192" font-size="9" font-weight="bold" fill="#0f172a">Layer 5: Basal Confining Bed (12.0 m)</text>
<text x="44" y="203" font-size="8" fill="#475569">-19.75 to -31.75 m DMD &middot; Regional Aquitard</text>
<line x1="14" y1="216" x2="276" y2="216" stroke="#e2e8f0" stroke-width="1"/>
<text x="14" y="232" font-size="9.5" font-weight="bold" fill="#0369a1">2. ENGINEERING &amp; DEWATERING</text>
<line x1="14" y1="248" x2="38" y2="248" stroke="#0284c7" stroke-width="2.5" stroke-dasharray="6,2"/>
<text x="44" y="251" font-size="9" font-weight="bold" fill="#0369a1">Initial Static GWL: +6.25 m DMD</text>
<text x="44" y="262" font-size="8" fill="#64748b">Depth: 2.00 m bgl (approved baseline)</text>
<line x1="14" y1="276" x2="38" y2="276" stroke="#dc2626" stroke-width="3"/>
<text x="44" y="279" font-size="9" font-weight="bold" fill="#dc2626">Deepest Excavation: -8.00 m DMD</text>
<text x="44" y="290" font-size="8" fill="#64748b">Level 08 elevator &amp; sump pits (CONFLICT-002)</text>
<line x1="14" y1="304" x2="38" y2="304" stroke="#059669" stroke-width="2.2" stroke-dasharray="6,2"/>
<text x="44" y="307" font-size="9" font-weight="bold" fill="#059669">Target Dewatering: -8.50 m DMD</text>
<text x="44" y="318" font-size="8" fill="#64748b">0.50 m dry buffer below deepest formation</text>
<rect x="14" y="330" width="18" height="16" fill="#334155"/>
<rect x="14" y="330" width="18" height="16" fill="url(#secantHatchV)"/>
<text x="44" y="339" font-size="9" font-weight="bold" fill="#1e293b">Secant Pile Cutoff Wall (168 m)</text>
<text x="44" y="350" font-size="8" fill="#64748b">Toes at -9.30, -10.00, -11.65 m DMD</text>
<rect x="16" y="362" width="14" height="16" fill="#e0f2fe" stroke="#0284c7" stroke-width="1.5"/>
<rect x="16" y="362" width="14" height="16" fill="url(#screenHatchV)"/>
<text x="44" y="371" font-size="9" font-weight="bold" fill="#0284c7">Deepwell Intake Screen (6.7 m)</text>
<text x="44" y="382" font-size="8" fill="#0369a1">-7.80 to -14.50 m DMD (wholly in Layer 3)</text>
<line x1="14" y1="396" x2="276" y2="396" stroke="#e2e8f0" stroke-width="1"/>
<text x="14" y="412" font-size="9.5" font-weight="bold" fill="#0369a1">3. HYDROGEOLOGICAL DYNAMICS</text>
<path d="M 14 428 Q 26 438 38 428" fill="none" stroke="#0284c7" stroke-width="2" stroke-dasharray="4,2" marker-end="url(#seepArrow)"/>
<text x="44" y="432" font-size="9" font-weight="bold" fill="#0284c7">Underflow Seepage Pathway</text>
<text x="44" y="443" font-size="8" fill="#64748b">Upward flow beneath partially penetrating toe</text>
<line x1="14" y1="458" x2="38" y2="458" stroke="#9333ea" stroke-width="2"/>
<text x="44" y="461" font-size="9" font-weight="bold" fill="#9333ea">Permeable Window: 8.10 - 10.45 m</text>
<text x="44" y="472" font-size="8" fill="#64748b">Vertical gap between toe and Layer 5 top</text>
<line x1="14" y1="486" x2="38" y2="486" stroke="#0284c7" stroke-width="1.5"/>
<text x="44" y="489" font-size="9" font-weight="bold" fill="#0284c7">Well Toe Clearance: 5.25 m</text>
<text x="44" y="500" font-size="8" fill="#64748b">Distance from well toe (-14.50m) to Layer 5</text>
<rect x="12" y="515" width="266" height="62" rx="4" fill="#f0f9ff" stroke="#bae6fd" stroke-width="1"/>
<text x="20" y="530" font-size="9" font-weight="bold" fill="#0369a1">SYSTEM ABSTRACTION DISCHARGE:</text>
<text x="20" y="544" font-size="8.5" fill="#0284c7">&bull; Steady Total: 46.5 m³/hr (1116 m³/day)</text>
<text x="20" y="556" font-size="8.5" fill="#0284c7">&bull; Per Well: 7.75 m³/hr (6 active deepwells)</text>
<text x="20" y="568" font-size="8.5" fill="#0284c7">&bull; Peak Total: 93.0 m³/hr (15.5 m³/hr/well)</text>
<rect x="12" y="586" width="266" height="285" rx="4" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1"/>
<text x="20" y="604" font-size="9" font-weight="bold" fill="#0f172a">KEY HYDROGEOLOGICAL FINDINGS:</text>
<text x="20" y="620" font-size="8" fill="#334155">&bull; The secant pile wall terminates inside Layer 3</text>
<text x="26" y="632" font-size="8" fill="#475569">at -9.30 to -11.65 m DMD.</text>
<text x="20" y="648" font-size="8" fill="#334155">&bull; Shoring does NOT penetrate Layer 5 basal</text>
<text x="26" y="660" font-size="8" fill="#475569">confining unit (-19.75 to -31.75 m DMD).</text>
<text x="20" y="676" font-size="8" fill="#334155">&bull; A 8.10 m to 10.45 m open permeable gap</text>
<text x="26" y="688" font-size="8" fill="#475569">exists beneath the wall toe, allowing underflow.</text>
<text x="20" y="704" font-size="8" fill="#334155">&bull; 100% of deepwell intake screens (6.7 m)</text>
<text x="26" y="716" font-size="8" fill="#475569">are positioned wholly within Layer 3.</text>
<text x="20" y="732" font-size="8" fill="#334155">&bull; Well toe terminates at -14.50 m DMD,</text>
<text x="26" y="744" font-size="8" fill="#475569">leaving 5.25 m clearance to Layer 5 top.</text>
<text x="20" y="760" font-size="8" fill="#334155">&bull; Layer 4 (conglomerate, 5.0 m) provides a</text>
<text x="26" y="772" font-size="8" fill="#475569">deep transition path beneath well toes.</text>
<text x="20" y="788" font-size="8" fill="#334155">&bull; Layer 5 acts as effective impervious base</text>
<text x="26" y="800" font-size="8" fill="#475569">for groundwater flow modeling.</text>
<text x="20" y="816" font-size="8" fill="#334155">&bull; Target dewatering achieves 0.50 m dry buffer</text>
<text x="26" y="828" font-size="8" fill="#475569">below deepest excavation sump (-8.00 m).</text>
<text x="20" y="844" font-size="8" fill="#334155">&bull; Total operational duration: 150 days</text>
<text x="26" y="856" font-size="8" fill="#475569">(7 days pre-drain + 143 days maintenance).</text>
</g>
</svg>

> **Underground Vertical View Note**: Conceptual vertical cross-section illustrating the hydrostratigraphic relationships between ground surface, static groundwater, phased excavation depths, partially penetrating secant pile wall, deepwell intake screens, and the basal confining unit.

---

## 04. Hydraulic Properties

### Governing Hydraulic Parameters

The following table is the final approved modeling baseline and is identical to the authoritative table in `PreModflowApproval.md`.

| Layer | Geological Unit | Kh Base (m/s) [m/day] | Kv Base (m/s) [m/day] | Ss Base (1/m) | Sy Base (dimensionless) |
|---|---|---|---|---|---|
| L1 | Aeolian Dune Sand / Silt | 2.3×10⁻⁵ [1.9872] | 1.0×10⁻⁵ [0.864] | 1.0×10⁻⁴ | 0.25 |
| L2 | Upper Weathered Sandstone | 5.0×10⁻⁵ [4.32] | 1.0×10⁻⁵ [0.864] | 2.5×10⁻⁵ | 0.12 |
| L3 | Moderately Weathered Sandstone | 5.0×10⁻⁵ [4.32] | 1.0×10⁻⁵ [0.864] | 2.5×10⁻⁵ | 0.12 |
| L4 | Conglomeratic Sandstone | 5.8×10⁻⁶ [0.50112] | 5.8×10⁻⁷ [0.050112] | 5.0×10⁻⁶ | 0.08 |
| L5 | Calcisiltite / Siltstone | 5.0×10⁻¹⁰ [4.32×10⁻⁵] | 1.0×10⁻¹⁰ [8.64×10⁻⁶] | 1.0×10⁻⁶ | 0.03 |

### Parameter Derivation & Basis Details

#### Horizontal and Vertical Conductivity
- **Status**: `APPROVED` &middot; **Classification**: `approved_engineering_input` &middot; **Approval Ref**: `REV-001 / REV-002 (PreModflowApproval.md)`
- **Basis**: The listed Kh and Kv values are final, layer-specific modeling inputs. Kx and Ky equal Kh, and Kz equals Kv for the respective layer.
- **Derived Kh/Kv Ratios**: L1 = 2.3, L2 = 5.0, L3 = 5.0, L4 = 10.0, and L5 = 5.0 (all dimensionless).

#### Storage Parameters
- **Status**: `APPROVED` &middot; **Classification**: `approved_engineering_input` &middot; **Approval Ref**: `REV-003 (PreModflowApproval.md)`
- **Basis**: The listed Sy and Ss values are final, layer-specific modeling inputs. Sy is dimensionless; Ss is expressed in 1/m.

### 3D Coordinate Direction Mapping

| Model Direction Variable | Directional Mapping | Value | Unit | Status |
|:---:|:---|:---|:---|:---:|
| **Kx** | `Kx = Kh` | Layer-specific Section 04 Kh baseline | `m/day` | `APPROVED` |
| **Ky** | `Ky = Kh` | Layer-specific Section 04 Kh baseline | `m/day` | `APPROVED` |
| **Kz** | `Kz = Kv` | Layer-specific Section 04 Kv baseline | `m/day` | `APPROVED` |

### Layer Applicability Policy
- **Approved Layers**: The final baseline applies to all five modeled layers, L1 through L5, exactly as tabulated above.
- **Governance Rule**: Do not substitute research ranges or former generic parameters for the final approved layer-specific baseline.

---

## 05. Initial Groundwater Conditions

### Approved Baseline Groundwater Level
- **Approved Baseline Level**: **+6.25 m_DMD** (`APPROVED`, `approved_engineering_input`, Ref: `PreModflowApproval.md (Section 06 & Section 18)`)
- **Source**: MS-1-P393D - R5.pdf (Pages 3, 20, Section 2.0 Scope Table & Appendix C Calculation Sheet)
- **Interpretation**: Approved governing pre-pumping baseline water level across the site.
- **Initial Head Field Concept**: Uniform horizontal initial hydraulic head plane set to +6.25 m DMD across all active model cells at t = 0 days.
- **Reference Datum**: `Dubai Mining Datum (DMD)`

### Geotechnical Borehole Water Observations

| Borehole ID | Ground Elev (m DMD) | Water Depth (m bgl) | Standing Water Level (m DMD) | Observation Date / Time | Classification | Provenance |
|:---|---:|---:|---:|:---|:---:|:---|
| **BH01** | +8.35 | 2.10 m | **+6.25 m DMD** | 28/02/2023 16:30 | `raw_fact` | Soil report.pdf (p. 6, 30) |
| **BH02** | +8.30 | 2.10 m | **+6.20 m DMD** | 23/02/2023 | `raw_fact` | Soil report.pdf (p. 6, 33) |
| **BH03** | +8.15 | 2.00 m | **+6.15 m DMD** | 01/03/2023 | `raw_fact` | Soil report.pdf (p. 6, 37) |
| **BH04** | +8.35 | 2.15 m | **+6.20 m DMD** | 28/02/2023 | `raw_fact` | Soil report.pdf (p. 6, 40) |
| **BH05** | +8.25 | 2.10 m | **+6.15 m DMD** | 01/03/2023 | `raw_fact` | Soil report.pdf (p. 6, 43) |

> **Borehole Observations Summary**: Range: `+6.15` to `+6.25 m DMD` &middot; Mean: `+6.21 m DMD` &middot; Max Spatial Variation: `0.10 m` (`dataset_derivation`)

### Sensitivity Reference Groundwater Level
- **Sensitivity High GWL**: `+6.75 m_DMD` (`REFERENCE_ONLY`, `raw_fact`)
- **Source**: MS-1-P393D - R5.pdf (Page 19, Appendix C CAL-1-P393D Levels)
- **Note**: Documented in Method Statement calculation sheet as high-water sensitivity reference. NOT used in active base conceptual model.

### Groundwater Monitoring Protocol
- **Water Level Monitoring**: Checked daily by day and night shift watchman using an electric contact dip meter (KLL)
- **Discharge Measurement**: Measured daily using standard V-notch tank and 6-inch electromagnetic flow meter as per Nakheel requirement
- **Provenance**: `MS-1-P393D - R5.pdf (p. 7, 14, Section 8.0 & Appendix A CHK-1-P393D)`

---

## 06. Boundary & Recharge Conditions

- **Model Domain Boundary Concept**: Conceptual boundary framework defining engineering plot limits and external aquifer continuity.
- **Hydraulic Boundary Concept**: Open regional lateral aquifer continuity. No natural impermeable lateral boundaries exist in the vicinity. The secant pile wall forms an engineered partial barrier around the excavation perimeter.

### Lateral Boundary Conditions
- **Conceptual Boundary Type**: Regional lateral hydrostatic boundary
- **Boundary Head Plane**: `+6.25 m DMD`
- **Distance Concept**: Located beyond the dewatering radius of influence (Rc = 301.5 m calculated in CAL-1-P393D).
- **Numerical Package Assignment**: `DEFERRED_TO_PHASE_2 (Specific MODFLOW packages such as CHD or GHB are NOT prematurely generated in this conceptual model).`

### Vertical Boundary Conditions
- **Top Boundary**: Atmospheric boundary / ground surface (+8.25 m DMD). Unconfined free surface condition for the upper water table.
- **Bottom Boundary**: Basal confining bed (Layer 5 Calcisiltite/Siltstone from -19.75 to -31.75 m DMD). Low permeability floor acting as effective basal confining boundary.

### Recharge Status
- **Recharge Status**: `NOT_SPECIFIED_IN_APPROVED_INPUTS`
- **Recharge Value**: `null` (`m/day`)
- **Recharge Source & Basis**: PreModflowApproval.md (Zero approved recharge in project documents. Arid urban Dubai climate; natural precipitation is low (~80 mm/yr) and episodic, with surrounding ground largely paved or developed. Recharge is explicitly not specified in approved inputs and must NOT be invented).

### Boundary Assumptions & Package Deferral
- No constant-head (CHD) packages are prematurely specified in this conceptual model.
- No general-head boundary (GHB) packages are prematurely specified in this conceptual model.
- No river (RIV), drain (DRN), or recharge (RCH) packages are prematurely created.
- The regional water table is assumed to remain stable at +6.25 m DMD at distances beyond the radius of influence (R0 = 277.9 m).

- **Boundary Data Gaps**: Exact lateral domain distance and boundary conductance coefficients will be established during Phase 2 numerical grid discretization based on CIRIA radius of influence calculations.
- **Rationale**: This section strictly defines the hydrogeological boundary concept without generating numerical MODFLOW package instructions.
- **Provenance**: Primary `PreModflowApproval.md (Section 06, 08, 11)`, Supporting `MS-1-P393D - R5.pdf (Appendix C CAL-1-P393D)`

---

## 07. Dewatering Wells & Pumping

- **Total Installed Deepwells**: **6 nos**
- **Coordinate Reference System**: `EPSG:3997 (DLTM)`
- **Coordinate Origin**: `drawing_cad_digitized_geometry`
- **Geometry Classification**: `digitized_value`

### Approved Common Wellfield Geometry
- **Total Well Depth**: `21.2 m`
- **Well Toe Elevation**: `-14.50 m DMD`
- **Screen Length**: `6.7 m`
- **Screen Interval**: `-7.80 to -14.50 m DMD`
- **Borehole Diameter**: `700.0 mm`
- **Casing Diameter & Material**: `8.0"` Slotted UPVC
- **Target Hydrogeological Stratum**: **Layer 3 (Moderately Weathered Sandstone / Screened Aquifer)**

### Deepwells Catalog (DW-01 to DW-06)

| Well ID | Easting (m) | Northing (m) | Depth (m) | Screen (m DMD) | Toe (m DMD) | Borehole Ø | Design Yield | Applicable Layer | Sector / Notes |
|:---|---:|---:|---:|:---:|---:|---:|---:|:---|:---|
| **DW-01** | 486976.438 | 2772571.467 | 21.2 m | `-7.8 to -14.5` | -14.5 | 700.0 mm | 11.1 m³/hr (266.4 m³/d) | Layer 3 (Moderately Weathered Sandstone) | Southern sector perimeter deepwell. |
| **DW-02** | 486973.338 | 2772582.310 | 21.2 m | `-7.8 to -14.5` | -14.5 | 700.0 mm | 11.1 m³/hr (266.4 m³/d) | Layer 3 (Moderately Weathered Sandstone) | Central-south internal sector deepwell. |
| **DW-03** | 486961.597 | 2772582.131 | 21.2 m | `-7.8 to -14.5` | -14.5 | 700.0 mm | 11.1 m³/hr (266.4 m³/d) | Layer 3 (Moderately Weathered Sandstone) | Western sector perimeter deepwell. |
| **DW-04** | 486976.158 | 2772593.866 | 21.2 m | `-7.8 to -14.5` | -14.5 | 700.0 mm | 11.1 m³/hr (266.4 m³/d) | Layer 3 (Moderately Weathered Sandstone) | Central-north internal sector deepwell. |
| **DW-05** | 486976.572 | 2772606.274 | 21.2 m | `-7.8 to -14.5` | -14.5 | 700.0 mm | 11.1 m³/hr (266.4 m³/d) | Layer 3 (Moderately Weathered Sandstone) | Northern sector perimeter deepwell. |
| **DW-06** | 486995.809 | 2772586.338 | 21.2 m | `-7.8 to -14.5` | -14.5 | 700.0 mm | 11.1 m³/hr (266.4 m³/d) | Layer 3 (Moderately Weathered Sandstone) | Eastern sector perimeter deepwell. |

### Approved Operational Pumping Discharge Rates

| Operational Mode | Total System Flow (m³/hr) | Total System Flow (m³/day) | Per Well Flow (m³/hr) | Per Well Flow (m³/day) | Status | Classification | Provenance Source |
|:---|---:|---:|---:|---:|:---:|:---:|:---|
| **Base Steady-State Operation** | **46.5** | **1116.0** | **7.75** | **186.0** | `APPROVED` | `source_calculation` | MS-1-P393D - R5.pdf (Section 7.0 Table & Appendix C Step 2 CIRIA calculation) |
| **Peak Transient Drawdown Operation** | **93.0** | **2232.0** | **15.5** | **372.0** | `APPROVED` | `source_calculation` | MS-1-P393D - R5.pdf (Section 7.0 Note (initial drawdown flow can be twice steady state: 46.5 x 2 = 93.0 m3/hr)) |

### Operational Hierarchy & Distinctions
- **Design Single Well Capacity**: 11.1 m³/hr (266.4 m³/day) per well based on Dupuit-Thiem single-well radial yield calculation.
- **Base Steady Operating Rate**: 7.75 m³/hr (186.0 m³/day) per well (46.5 m³/hr total system flow divided equally across 6 operating deepwells).
- **Peak Operating Rate**: 15.5 m³/hr (372.0 m³/day) per well (93.0 m³/hr total system flow during initial 7-day pre-excavation drawdown phase).

### Dewatering Operational Schedule
- **Pre-Excavation Drawdown Duration**: **7 days** (`APPROVED`, `raw_fact`)
- **Total Operational Duration**: **150 days** (approx. 5 months)
- **Provenance**: MS-1-P393D - R5.pdf (Pages 7, 19, Section 7.5 & Appendix C Duration)

### Standby Equipment & Site Infrastructure
- **Submersible Pumps**: Running pump(s) + 1 standby pump
- **Electrical Gensets**: Running genset(s) + 1 standby genset
- **French Drains**: 0.50m x 0.50m gravity drains filled with aggregate channelled to deepwells
- **Sedimentation Tank**: Baffled settlement tank with oil skimming mats and V-notch discharge monitoring
- **Provenance**: `MS-1-P393D - R5.pdf (Pages 4, 7, 9, Sections 5.1, 7.3, 10.1, 10.2)`

---

## 08. Excavation & Shoring

### 08.1 Excavation Geometry
- **Plot Surface Area**: `1633.18 m²`
- **Enclosed Shoring Perimeter**: `168.0 m`
- **Model Ground Surface Plane**: `+8.25 m DMD`
- **Existing Ground Surface Decision**: `+8.45 m DMD`
- **Spatial Relationship**: Shoring secant pile wall is offset immediately inside the 1633.18 m² surveyed plot boundary, enclosing an excavation perimeter of 168.0 m.
- **Provenance**: `PreModflowApproval.md (Section 02, 03, 13 CONFLICT-001/004)`

### 08.2 Excavation Levels (Drawing DEW-1-P393D Rev 07)

| Excavation Level ID | Formation Level (m DMD) | Depth Below +8.10m OGL (m) | Classification | Source Reference |
|:---|---:|---:|:---:|:---|
| **Level 01** | **-3.70 m DMD** | 11.80 m | `raw_fact` | Drawing DEW-1-P393D Rev 07 |
| **Level 02** | **-3.90 m DMD** | 12.00 m | `raw_fact` | Drawing DEW-1-P393D Rev 07 |
| **Level 03** | **-4.40 m DMD** | 12.50 m | `raw_fact` | Drawing DEW-1-P393D Rev 07 |
| **Level 04** | **-4.60 m DMD** | 12.70 m | `raw_fact` | Drawing DEW-1-P393D Rev 07 |
| **Level 05** | **-6.10 m DMD** | 14.20 m | `raw_fact` | Drawing DEW-1-P393D Rev 07 |
| **Level 06** | **-6.40 m DMD** | 14.50 m | `raw_fact` | Drawing DEW-1-P393D Rev 07 |
| **Level 07** | **-7.80 m DMD** | 15.90 m | `raw_fact` | Drawing DEW-1-P393D Rev 07 |
| **Level 08 Elevator Sump Pit** | **-8.00 m DMD** | 16.10 m | `raw_fact` | Drawing DEW-1-P393D Rev 07 (Revision Callouts) |

- **Deepest Excavation Formation**: **-8.00 m DMD** (`APPROVED (CONFLICT-002 in PreModflowApproval.md)`)
- **Target Dewatering Drawdown Level**: **-8.50 m DMD** (`APPROVED (REV-004 in PreModflowApproval.md)`)
- **Dewatering Buffer Beneath Deepest Sump**: **0.50 m**
- **Total Required Drawdown (Δh from +6.25m baseline)**: **14.75 m**

### 08.3 Excavation Staging Protocol
- **Stage 1 Excavation**: Bulk excavation in the dry from ground surface (+8.25 m DMD) down to approximately 50 cm above static groundwater table (+6.75 m DMD). (Operational condition: *No deepwell pumping active; dry excavation of unsaturated Layer 1 dune sand.*)
- **Stage 2 Excavation**: Deepwell pumping system operates (7-day pre-drawdown followed by continuous steady pumping) to depress groundwater level to target -8.50 m DMD, facilitating bulk and detailed excavation from +6.75 m DMD down to final formation (-8.00 m DMD) completely in the dry. (Operational condition: *Full deepwell operation with perimeter French drains channelled to deepwells.*)

### 08.4 Excavation Footprint
- **Description**: Basement excavation footprint occupies virtually the entire internal enclosed area of the 4-sided secant pile wall (~1633 m²).
- **Internal Offset**: Shoring secant pile wall is constructed immediately inside site perimeter, with internal excavation face offset immediately inward.

### 08.5 Secant Pile Wall Configuration
- **Shoring Type**: `Secant Pile Wall On 4 Sides`
- **Configuration**: Continuous interlocked secant pile perimeter enclosing all four boundaries of the plot.

### 08.6 Wall Alignment & Perimeter
- **Perimeter Length**: `168.0 m`
- **Alignment**: Offset immediately inside site boundary on all 4 sides

### 08.7 Wall Toe Geometry
- **Approved Negative Toe Levels**: **-9.30, -10.00, -11.65 m_DMD** (`APPROVED`, `approved_engineering_input`, Ref: `CONFLICT-003 (PreModflowApproval.md)`)
- **Conflict Resolution Note**: Source A narrative typo (+10.00 m DMD) was rejected; negative toe elevations (-9.30, -10.00, -11.65 m DMD) from Drawing DEW-1-P393D Notes & Legend were confirmed and approved.

### 08.8 Wall Penetration Details
- **Top of Wall Elevation**: `+8.25 m DMD`
- **Total Wall Depths**: `[17.55, 18.25, 19.9]` meters
- **Penetration Depth Below Deepest Sump (-8.00m)**: `[1.3, 2.0, 3.65]` meters
- **Penetration Depth Below Target Dewatering (-8.50m)**: `[0.8, 1.5, 3.15]` meters

### 08.9 Groundwater–Shoring Interaction
- **Cutoff Classification**: `Partially penetrating cutoff wall`
- **Basal Key Status**: **NOT KEYED into basal confining unit (Layer 5 Calcisiltite/Siltstone from -19.75 to -31.75 m DMD).**
- **Underflow Mechanism**: Because the secant pile wall toe terminates between -9.30 and -11.65 m DMD while the basal aquitard begins at -19.75 m DMD, a permeable vertical window of 8.10 m to 10.45 m thickness remains beneath the wall toe through the lower portion of Layer 3 and Layer 4. Groundwater underflow around and beneath the wall toe into the deepwell drawdown cone will occur.
- **Modeling Implication**: The conceptual model must represent this groundwater underflow consequence without prematurely overstating it as a calibrated leakage rate or numerical boundary condition.

### 08.10 Excavation–Dewatering Relationship
- **Ground Surface Plane**: `+8.25 m DMD`
- **Static Groundwater Baseline**: `+6.25 m DMD`
- **Deepest Formation**: `-8.00 m DMD`
- **Target Dewatering Level**: `-8.50 m DMD` (Buffer: `0.50 m`)
- **Well Screen Interval**: `-7.80 to -14.50 m DMD`
- **Relationship Summary**: Deepwells abstract groundwater from -7.80 to -14.50 m DMD (wholly beneath the excavation formation), drawing the regional water table down by 14.75 m to -8.50 m DMD. This provides a 0.50 m dry buffer beneath the lowest elevator/sump formation (-8.00 m DMD). The secant pile wall shields lateral inflow in the upper 17.55 to 19.90 m, forcing all residual inflow to travel vertically downward beneath the shoring toe.

### 08.11 Hydrogeological Layer Interaction Sequence

| Vertical Sequence Component | Elevation / Interval (m DMD) | Engineering Classification / Behavior |
|:---|:---:|:---|
| **Existing Ground Surface Decision** | `+8.45 m DMD` | approved_decision (CONFLICT-004) |
| **Reconciled Model Ground Surface Plane** | `+8.25 m DMD` | approved_decision (REV-005) |
| **Layer 1 (Aeolian Dune Sand / Silt)** | `+8.25 to +6.75 m DMD` | Vadose / unsaturated sand cover |
| **Static Groundwater Level Baseline** | `+6.25 m DMD` | approved_baseline |
| **Layer 2 (Upper Weathered Sandstone)** | `+6.75 to -4.75 m DMD` | Water table aquifer; hosts excavation levels 01 to 04 |
| **Excavation Levels 01 to 04** | `-3.70 to -4.60 m DMD` | Upper basement excavation steps |
| **Layer 3 (Moderately Weathered Sandstone)** | `-4.75 to -14.75 m DMD` | Screened aquifer; hosts deepwell screens and deepest excavation |
| **Excavation Levels 05 to 08** | `-6.10 to -8.00 m DMD` | Deep basement excavation steps |
| **Deepest Excavation Formation** | `-8.00 m DMD` | approved_formation (CONFLICT-002) |
| **Target Dewatering Drawdown** | `-8.50 m DMD` | approved_target (REV-004) |
| **Secant Pile Wall Toe Levels** | `-9.30, -10.00, -11.65 m DMD` | Partially penetrating toe in Layer 3 (CONFLICT-003) |
| **Deepwell Screen Interval** | `-7.80 to -14.50 m DMD` | Active abstraction screen in Layer 3 |
| **Deepwell Toe Elevation** | `-14.50 m DMD` | Well base terminates at base of Layer 3 |
| **Layer 4 (Conglomeratic Sandstone)** | `-14.75 to -19.75 m DMD` | Transitional stratum; underflow zone |
| **Layer 5 (Calcisiltite / Siltstone)** | `-19.75 to -31.75 m DMD` | Regional lower confining bed / aquitard |

### 08.12 Approved Design Values Summary

| Design Parameter | Approved Value | Unit |
|:---|---:|:---|
| **Plot Area M2** | `1633.18` | — |
| **Perimeter M** | `168.0` | — |
| **Existing Ground Surface Decision M Dmd** | `8.45` | — |
| **Reconciled Model Ground Surface Plane M Dmd** | `8.25` | — |
| **Deepest Excavation Level M Dmd** | `-8.0` | — |
| **Target Dewatering Level M Dmd** | `-8.5` | — |
| **Dewatering Buffer M** | `0.5` | — |
| **Secant Pile Toe Levels M Dmd** | `-9.3, -10.0, -11.65` | — |
| **Baseline Groundwater Level M Dmd** | `6.25` | — |
| **Deepwell Count** | `6` | — |
| **Well Depth M** | `21.2` | — |
| **Screen Interval M Dmd** | `-7.8, -14.5` | — |
| **Screen Length M** | `6.7` | — |
| **Well Toe M Dmd** | `-14.5` | — |
| **Design Yield M3 Hr Per Well** | `11.1` | — |
| **Steady Total Discharge M3 Hr** | `46.5` | — |
| **Peak Total Discharge M3 Hr** | `93.0` | — |
| **Pre Drawdown Days** | `7` | — |
| **Total Operation Days** | `150` | — |

### 08.13 Provenance
- **Primary Approval Document**: `PreModflowApproval.md (Section 03, 04, 13 CONFLICT-001/002/003/004, 15 REV-004/005, 18)`
- **Supporting Extraction Dataset**: `actual_engineering_dataset.json (section_03, section_04, section_05)`
- **Source Engineering Drawings**:
  - `MS-1-P393D - R5.pdf (Page 16, Drawing DEW-1-P393D Rev 07)`
  - `MS-1-P393D - R5.pdf (Page 17, Drawing SEC-1-P393D Rev 05)`
  - `MS-1-P393D - R5.pdf (Pages 19-20, Appendix C CAL-1-P393D)`

---

## 09. Simulation Period

- **Pre-Excavation Drawdown Duration**: **7 days**
- **Operational Dewatering Duration**: **143 days**
- **Total Modeled Simulation Period**: **150 days** (approx. 5 months)
- **Base Model Temporal Scope**: Transient 150-day dewatering simulation comprising a 7-day initial pre-excavation drawdown phase and a 143-day substructure construction maintenance phase.

### Pumping Operational Schedule Phases

#### Phase A Pre Drawdown
- **Duration**: `7 days` &middot; **Time Interval**: `Days 0 to 7`
- **Operational Mode**: Initial heavy drawdown to lower static water table (+6.25 m DMD) below excavation formation to target level (-8.50 m DMD) prior to bulk excavation.
- **Total Pumping Discharge**: `93.0 m³/hr` (`2232.0 m³/day`)
- **Per Well Pumping Discharge**: `15.5 m³/hr` (`372.0 m³/day`)
- **Status**: `APPROVED` &middot; **Provenance**: `MS-1-P393D - R5.pdf (Pages 7, 20, Section 7.0 Note)`

#### Phase B Operational Maintenance
- **Duration**: `143 days` &middot; **Time Interval**: `Days 7 to 150`
- **Operational Mode**: Continuous maintenance dewatering to maintain water level at or below target -8.50 m DMD throughout basement construction and substructure casting.
- **Total Pumping Discharge**: `46.5 m³/hr` (`1116.0 m³/day`)
- **Per Well Pumping Discharge**: `7.75 m³/hr` (`186.0 m³/day`)
- **Status**: `APPROVED` &middot; **Provenance**: `MS-1-P393D - R5.pdf (Pages 7, 20, Section 7.0 Table & Appendix C Step 2)`

### Temporal Assumptions
- Pumping operates 24 hours per day continuously throughout the 150-day simulation period as specified in Method Statement Section 7.5.
- No seasonal hydrologic variations or precipitation recharge pulses are assumed during the 150-day lifecycle in base model.
- Numerical time-stepping, stress period discretization, and solver convergence settings are strictly deferred to Phase 2 numerical model construction.

- **Provenance**: Primary `PreModflowApproval.md (Section 09 & Section 18)`, Supporting `MS-1-P393D - R5.pdf (Pages 7, 19, Section 7.5 & Appendix C Duration)`

---

## 10. Assumptions, Validation & Provenance

### A. Conceptual Assumptions

| ID | Assumption Title | Description | Status |
|:---:|:---|:---|:---:|
| **ASSUMP-001** | **Governing Source Hierarchy** | PreModflowApproval.md is the ultimate engineering source of truth, superseding raw extraction discrepancies and secondary research ranges. | `APPROVED` |
| **ASSUMP-002** | **Single Base Conceptual Model** | Only the approved base conceptual model is represented. No alternative scenarios, sensitivity cases, or speculative parameter sets are active. | `APPROVED` |
| **ASSUMP-003** | **Uniform Initial Water Table** | Initial static groundwater table is represented as a uniform horizontal surface at +6.25 m DMD across the model domain based on 5 borehole observations (+6.15 to +6.25 m DMD) exhibiting negligible regional gradient. | `APPROVED` |
| **ASSUMP-004** | **Hydrostratigraphic Uniformity Across Site** | The 5 geological strata identified in Soil Report SIR2023-0018 are assumed continuous and horizontally planar across the 1633.18 m² plot area for conceptual synthesis. | `APPROVED` |
| **ASSUMP-005** | **Secant Pile Cutoff Impermeability** | The secant pile wall is assumed to provide an effective lateral hydraulic cutoff down to its toe levels (-9.30, -10.00, -11.65 m DMD). Cutoff is partially penetrating relative to Layer 3 and Layer 5. | `APPROVED` |
| **ASSUMP-006** | **Basal Confining Floor** | Layer 5 (Calcisiltite / Siltstone from -19.75 to -31.75 m DMD) functions as the lower confining bed, providing the effective lower impermeable boundary of the active dewatering system. | `APPROVED` |
| **ASSUMP-007** | **Zero Invented Natural Recharge** | No unmeasured natural recharge rate is invented. Recharge status is explicitly marked as NOT_SPECIFIED_IN_APPROVED_INPUTS. | `APPROVED` |
| **ASSUMP-008** | **Continuous Dewatering Operation** | All 6 deepwells pump continuously 24 hr/day throughout the 150-day period (7 days pre-drawdown at peak rate + 143 days operational maintenance at steady rate). | `APPROVED` |

### B. Validation Checks

| Verification Criterion | Result | Status Meaning |
|:---|:---:|:---|
| `json_schema_valid` | **PASS ✅** | Json schema valid |
| `required_sections_present` | **PASS ✅** | Required sections present |
| `exactly_10_top_level_sections` | **PASS ✅** | Exactly 10 top level sections |
| `section_order_verified` | **PASS ✅** | Section order verified |
| `approved_values_consistent_with_PreModflowApproval` | **PASS ✅** | Approved values consistent with premodflowapproval |
| `six_wells_present` | **PASS ✅** | Six wells present |
| `well_ids_unique` | **PASS ✅** | Well ids unique |
| `screen_intervals_valid` | **PASS ✅** | Screen intervals valid |
| `excavation_levels_consistent` | **PASS ✅** | Excavation levels consistent |
| `target_dewatering_below_deepest_excavation` | **PASS ✅** | Target dewatering below deepest excavation |
| `wall_toe_levels_correctly_represented` | **PASS ✅** | Wall toe levels correctly represented |
| `layer_top_bottom_elevations_logically_ordered` | **PASS ✅** | Layer top bottom elevations logically ordered |
| `layer_thickness_consistency` | **PASS ✅** | Layer thickness consistency |
| `hydraulic_units_consistent` | **PASS ✅** | Hydraulic units consistent |
| `no_unapproved_ranges_in_active_base_parameters` | **PASS ✅** | No unapproved ranges in active base parameters |
| `no_unresolved_conflicts_used_as_active_inputs` | **PASS ✅** | No unresolved conflicts used as active inputs |
| `no_invented_recharge` | **PASS ✅** | No invented recharge |
| `no_invented_modflow_boundary_packages` | **PASS ✅** | No invented modflow boundary packages |
| `no_invented_grid_or_discretization` | **PASS ✅** | No invented grid or discretization |
| `provenance_present_for_engineering_inputs` | **PASS ✅** | Provenance present for engineering inputs |

### C. Comprehensive Provenance Hierarchy

#### Primary Source Of Truth
- **Document**: `PreModflowApproval.md`
- **Path**: `data/actual/extracted/PreModflowApproval.md`
- **Authority Role**: Ultimate downstream engineering source of truth containing all approved parameters and resolved conflicts
- **Status**: `REVIEW_COMPLETED_AND_APPROVED`

#### Supporting Raw Dataset
- **Document**: `actual_engineering_dataset.json`
- **Path**: `data/actual/extracted/actual_engineering_dataset.json`
- **Authority Role**: Raw extraction dataset providing original source references, digitized CAD coordinates, and provenance tracking
- **Status**: `FROZEN_AND_UNMODIFIED`

#### Research References
- **Document**: `HydrogeologicalParameterResearch.md`
- **Path**: `data/actual/extracted/HydrogeologicalParameterResearch.md`
- **Authority Role**: Rock mechanics derivations, parameter bounding, and authoritative literature supporting REV-001, REV-002, REV-003
- **Status**: `VERIFIED_AND_APPROVED`

#### Data Gap References
- **Document**: `HydrogeologicalDataGapResearch.md`
- **Path**: `data/actual/extracted/HydrogeologicalDataGapResearch.md`
- **Authority Role**: Systematic parameter closure for GAP-001 to GAP-005
- **Status**: `VERIFIED_AND_CLOSED`

### Model Governance & Sign-Off Status
- **Artifact File**: `actual_conceptual_model.json`
- **Workflow Stage**: `Phase 1 — Step 3: Conceptual Model Creation`
- **Ultimate Source of Truth**: `PreModflowApproval.md`
- **Supporting Extraction Source**: `actual_engineering_dataset.json`
- **Model Scope**: `BASE_CONCEPTUAL_MODEL_ONLY`
- **Current Status**: `GENERATED_PENDING_ENGINEER_APPROVAL`
- **Sign-Off Instruction**: *Requires formal manual engineer review and sign-off before creation of approved_conceptual_model.json (Phase 1 — Step 6).*
