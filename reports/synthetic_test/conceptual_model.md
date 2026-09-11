# Conceptual Groundwater Model Report

## 1. Project Domain
- **Coordinate Reference System:** EPSG:32633
- **Footprint:** 1000.0 m × 1000.0 m
- **Bounding Box:** X: [500000.0, 501000.0], Y: [2700000.0, 2701000.0]
- **Terrain Elevation:** 26.0 m to 35.5 m a.s.l.

## 2. Hydrostratigraphy & Layer Discretization
| Layer | Name | Type | Horizontal K (m/d) | Vertical K (m/d) | Sy | Ss (1/m) | Bottom (m a.s.l.) |
|---|---|---|---|---|---|---|---|
| 1 | Alluvial Sand & Gravel (Upper Aquifer) | unconfined | 20.0 | 2.0 | 0.2 | 0.0001 | 10.0 |
| 2 | Silty Sand & Fractured Bedrock (Lower Aquifer) | convertible | 6.0 | 0.6000000000000001 | 0.1 | 1e-05 | -15.0 |

## 3. Hydrogeological Boundary Conditions
- **Western Inflow (CHD):** Regional hydraulic head = 32.0 m a.s.l.
- **Eastern Drainage (RIV):** River boundary stage = 24.0 m, conductance = 50.0 m²/day
- **Areal Infiltration (RCH):** 0.0005 m/day (~182.5 mm/year)
- **Extraction Well (WEL):** Well PW-01 at (500500.0, 2700500.0) pumping -500.0 m³/day

## 4. Flow Dynamics & Monitoring Targets
- Regional groundwater flows from West to East toward the river drainage network.
- 6 monitoring wells are active across the domain (4 for calibration, 2 reserved for independent validation).
