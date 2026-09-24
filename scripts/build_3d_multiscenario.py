"""
Multi-Scenario 3D Groundwater GIS Model Compiler & HTML Generator.

Compiles:
1. Unified Multi-Scenario JSON data from MODFLOW simulation outputs (Scenario 1 & 2).
2. Generates presentation-grade, cinematic 3D WebGL viewer HTML (groundwater_model_3d.html).
"""

from __future__ import annotations

import base64
import json
from pathlib import Path
import flopy
import numpy as np


WORKSPACE = Path(r"c:\Users\Shreyas-Wakhare\Desktop\TEST_001")
VIZ_DIR = WORKSPACE / r"data\actual\Visualizations\3D Model\visualization"
AERIAL_FILE = VIZ_DIR / r"assets\dubai_aerial.jpg"
GEOM_FILE = VIZ_DIR / "model_geometry_data.json"
UNIFIED_JSON = VIZ_DIR / "unified_scenario_3d_data.json"

SC1_HDS_FILE = WORKSPACE / r"data\actual\Visualizations\Scenario1(Base No pumping)\output\Stonehenge2.hds"
SC2_HDS_FILE = WORKSPACE / r"data\actual\Visualizations\Scenario2(Steady Pumping)\output\Stonehenge2.hds"
SC2_CBC_FILE = WORKSPACE / r"data\actual\Visualizations\Scenario2(Steady Pumping)\output\Stonehenge2.cbc"
MASK_FILE = WORKSPACE / r"data\actual\modflow\input\Stonehenge2_idomain_mask.dat"
DIS_FILE = WORKSPACE / r"data\actual\modflow\input\Stonehenge2.dis"

OUTPUT_HTML = VIZ_DIR / "groundwater_model_3d.html"
SC1_OUTPUT_HTML = VIZ_DIR / "Scenario1_3D_Groundwater_Model.html"
SC1_DEST_HTML = WORKSPACE / r"data\actual\Visualizations\Scenario1(Base No pumping)\3D Model\visualization\Scenario1_3D_Groundwater_Model.html"


def compile_data_and_generate_html():
    print("[1/3] Loading base geometry & masks...")
    with open(GEOM_FILE, "r", encoding="utf-8") as f:
        base_data = json.load(f)

    with open(AERIAL_FILE, "rb") as f:
        aerial_b64 = base64.b64encode(f.read()).decode("ascii")

    mask = np.loadtxt(MASK_FILE, dtype=int)
    nrow, ncol = 28, 26
    delr, delc = 2.5, 2.5
    x_orig, y_orig = 486945.0, 2772550.0

    # Ensure CAD sections have vibrant colors with Orange for Left Section
    for sec in base_data.get("cad_sections", []):
        if sec["id"] == "sec_left_blue":
            sec["cad_color"] = "#f97316"  # Vibrant Orange
            sec["hex_color"] = 16347926
            sec["name"] = "Orange Left Section"
            sec["cad_identity"] = "ORANGE LEFT SECTION (Upper Basement Excavation)"
        elif sec["id"] == "sec_main_red":
            sec["cad_color"] = "#f27172"  # Coral Red
            sec["hex_color"] = 15888754
        elif sec["id"] == "sec_inner_green":
            sec["cad_color"] = "#22c55e"  # Emerald Green
            sec["hex_color"] = 2278750
        elif sec["id"] == "sec_lower_green":
            sec["cad_color"] = "#eab308"  # Golden Yellow
            sec["hex_color"] = 15381256

    print("[2/3] Extracting Scenario 1 & 2 MODFLOW 6 Simulation Heads...")
    hds1 = flopy.utils.HeadFile(str(SC1_HDS_FILE))
    t1 = hds1.get_times()
    heads_sc1 = hds1.get_data(totim=t1[-1])
    hds1.close()

    hds2 = flopy.utils.HeadFile(str(SC2_HDS_FILE))
    t2 = hds2.get_times()
    heads_sc2 = hds2.get_data(totim=t2[-1])
    hds2.close()

    l3_sc1 = heads_sc1[2]
    l3_sc2 = heads_sc2[2]
    l2_sc1 = heads_sc1[1]
    l2_sc2 = heads_sc2[1]

    l3_sc1_clean = np.where(mask == 1, l3_sc1, 6.25)
    l3_sc2_clean = np.where(mask == 1, l3_sc2, 6.25)
    dd_l3 = np.where(mask == 1, l3_sc1 - l3_sc2, 0.0)

    # Grid cells array for 3D water mesh
    grid_cells = []
    for r in range(nrow):
        for c in range(ncol):
            is_active = bool(mask[r, c] == 1)
            cx = x_orig + (c + 0.5) * delr
            cy = y_orig + (nrow - r - 0.5) * delc
            h1 = float(l3_sc1_clean[r, c]) if is_active else 6.25
            h2 = float(l3_sc2_clean[r, c]) if is_active else 6.25
            dd = float(dd_l3[r, c]) if is_active else 0.0
            grid_cells.append({
                "row": r + 1,
                "col": c + 1,
                "x": cx,
                "y": cy,
                "active": is_active,
                "sc1_head": h1,
                "sc2_head": h2,
                "sc1_drawdown": 0.0,
                "sc2_drawdown": dd,
            })

    scenarios = {
        "base": {
            "id": "base",
            "name": "Base 3D Geotechnical Model (Static State)",
            "short_name": "Base Model View",
            "pumping_status": "OFF (0.0 m³/day)",
            "pumping_total_m3_d": 0.0,
            "pumping_total_m3_hr": 0.0,
            "head_min": 6.25,
            "head_max": 6.25,
            "head_mean": 6.25,
            "drawdown_min": 0.0,
            "drawdown_max": 0.0,
            "drawdown_mean": 0.0,
            "controlling_excavation_head": 6.25,
            "flow_status": "Hydrostatic Base Model",
            "wells": [
                {**w, "q_m3_d": 0.0, "q_m3_hr": 0.0, "head_m_dmd": 6.25, "drawdown_m": 0.0}
                for w in base_data.get("wells", [])
            ]
        },
        "sc1": {
            "id": "sc1",
            "name": "Scenario 1: Base Condition (No Pumping — Q = 0.0 m³/day)",
            "short_name": "Scenario 1 (No Pumping)",
            "pumping_status": "OFF (0.0 m³/day)",
            "pumping_total_m3_d": 0.0,
            "pumping_total_m3_hr": 0.0,
            "head_min": 6.25,
            "head_max": 6.25,
            "head_mean": 6.25,
            "drawdown_min": 0.0,
            "drawdown_max": 0.0,
            "drawdown_mean": 0.0,
            "controlling_excavation_head": 6.25,
            "flow_status": "Hydrostatic Equilibrium (Zero Gradient)",
            "wells": [
                {**w, "q_m3_d": 0.0, "q_m3_hr": 0.0, "head_m_dmd": 6.25, "drawdown_m": 0.0}
                for w in base_data.get("wells", [])
            ]
        },
        "sc2": {
            "id": "sc2",
            "name": "Scenario 2: Steady Dewatering (Pumping — Q = 265.26 m³/day)",
            "short_name": "Scenario 2 (Steady Pumping)",
            "pumping_status": "ACTIVE (265.26 m³/day / 11.05 m³/hr)",
            "pumping_total_m3_d": 265.26,
            "pumping_total_m3_hr": 11.0525,
            "head_min": float(np.min(l3_sc2_clean[mask == 1])),
            "head_max": 6.25,
            "head_mean": float(np.mean(l3_sc2_clean[mask == 1])),
            "drawdown_min": float(np.min(dd_l3[mask == 1])),
            "drawdown_max": float(np.max(dd_l3[mask == 1])),
            "drawdown_mean": float(np.mean(dd_l3[mask == 1])),
            "controlling_excavation_head": -8.50,
            "flow_status": "Active Underflow & Vertical Deepwell Extraction",
            "wells": [
                {
                    **w,
                    "q_m3_d": -44.21,
                    "q_m3_hr": -1.8421,
                    "head_m_dmd": float(l3_sc2_clean[w["row"] - 1, w["col"] - 1]),
                    "drawdown_m": float(dd_l3[w["row"] - 1, w["col"] - 1]),
                }
                for w in base_data.get("wells", [])
            ]
        }
    }

    # 3D Flow trajectory seed particles for Scenario 2
    flow_particles = []
    np.random.seed(42)
    for i in range(1200):
        angle = np.random.uniform(0, 2 * np.pi)
        radius = np.random.uniform(25, 48)
        cx = 486975.0 + radius * np.cos(angle)
        cy = 2772585.0 + radius * np.sin(angle)
        well_idx = np.random.randint(0, len(base_data["wells"]))
        target_well = base_data["wells"][well_idx]
        flow_particles.append({
            "id": i,
            "start": {"x": cx, "y": cy, "z": np.random.uniform(2.0, 6.0)},
            "underflow": {"x": 486975.0 + (radius * 0.45) * np.cos(angle), "y": 2772585.0 + (radius * 0.45) * np.sin(angle), "z": -16.5},
            "target": {"x": target_well["x"], "y": target_well["y"], "z": -11.0},
            "speed": float(np.random.uniform(0.6, 1.4)),
            "offset": float(np.random.uniform(0.0, 1.0))
        })

    unified_data = {
        **base_data,
        "grid_cells": grid_cells,
        "scenarios": scenarios,
        "flow_particles": flow_particles,
        "drawdown_colormap": {
            "min_dd": 0.0,
            "max_dd": 15.6247,
            "target_dd": 14.75,
            "target_head": -8.50,
        }
    }

    with open(UNIFIED_JSON, "w", encoding="utf-8") as f:
        json.dump(unified_data, f, indent=2)
    with open(GEOM_FILE, "w", encoding="utf-8") as f:
        json.dump(unified_data, f, indent=2)

    print("[3/3] Generating state-of-the-art Multi-Scenario 3D HTML...")
    model_data_json = json.dumps(unified_data)

    html_code = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>JVC15AMRM004 — Stonehenge 2, Dubai | Multi-Scenario 3D Groundwater GIS Model</title>
  <style>
    * {{
      box-sizing: border-box;
      margin: 0;
      padding: 0;
      user-select: none;
    }}
    body {{
      font-family: 'Segoe UI', -apple-system, BlinkMacSystemFont, Roboto, Helvetica, Arial, sans-serif;
      background: radial-gradient(circle at 50% 20%, #1e293b 0%, #0b1329 65%, #050814 100%);
      color: #e2e8f0;
      overflow: hidden;
      width: 100vw;
      height: 100vh;
      position: relative;
    }}

    #webgl-container {{
      width: 100vw;
      height: 100vh;
      position: absolute;
      top: 0;
      left: 0;
      z-index: 1;
    }}

    #axes-svg {{
      position: absolute;
      top: 0;
      left: 0;
      width: 100vw;
      height: 100vh;
      z-index: 2;
      pointer-events: none;
    }}

    .glass-panel {{
      background: rgba(11, 20, 38, 0.88);
      backdrop-filter: blur(14px);
      -webkit-backdrop-filter: blur(14px);
      border: 1px solid rgba(56, 189, 248, 0.25);
      box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.65);
      border-radius: 8px;
      z-index: 10;
      position: absolute;
    }}

    /* Top Header Bar */
    #top-header {{
      top: 14px;
      left: 16px;
      right: 16px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      padding: 10px 18px;
      height: 64px;
    }}

    .header-left {{
      display: flex;
      flex-direction: column;
      gap: 3px;
    }}

    .header-title {{
      font-size: 15px;
      font-weight: 700;
      letter-spacing: 0.5px;
      display: flex;
      align-items: center;
      gap: 8px;
      color: #f8fafc;
    }}

    .tag-live {{
      background: rgba(14, 165, 233, 0.25);
      border: 1px solid #38bdf8;
      color: #38bdf8;
      font-size: 11px;
      font-weight: 600;
      padding: 1px 8px;
      border-radius: 4px;
      text-transform: uppercase;
    }}

    .header-subtitle {{
      font-size: 11px;
      color: #94a3b8;
    }}

    /* Header Center Scenario Selector Controls */
    .scenario-selector-container {{
      display: flex;
      align-items: center;
      gap: 10px;
      background: rgba(15, 23, 42, 0.75);
      padding: 4px 12px;
      border-radius: 6px;
      border: 1px solid rgba(56, 189, 248, 0.35);
    }}

    .scenario-select-label {{
      font-size: 12px;
      font-weight: 600;
      color: #38bdf8;
      text-transform: uppercase;
      letter-spacing: 0.5px;
    }}

    .scenario-dropdown {{
      background: #0f172a;
      color: #f8fafc;
      border: 1px solid #334155;
      padding: 6px 12px;
      border-radius: 4px;
      font-size: 12px;
      font-weight: 600;
      cursor: pointer;
      outline: none;
      transition: all 0.2s ease;
    }}

    .scenario-dropdown:focus {{
      border-color: #38bdf8;
      box-shadow: 0 0 0 2px rgba(56, 189, 248, 0.25);
    }}

    .apply-btn {{
      background: linear-gradient(135deg, #0284c7 0%, #0369a1 100%);
      color: #ffffff;
      border: 1px solid #38bdf8;
      padding: 6px 14px;
      border-radius: 4px;
      font-size: 12px;
      font-weight: 700;
      cursor: pointer;
      display: flex;
      align-items: center;
      gap: 5px;
      box-shadow: 0 2px 10px rgba(2, 132, 199, 0.4);
      transition: all 0.2s ease;
    }}

    .apply-btn:hover {{
      background: linear-gradient(135deg, #0ea5e9 0%, #0284c7 100%);
      box-shadow: 0 4px 16px rgba(14, 165, 233, 0.6);
      transform: translateY(-1px);
    }}

    .apply-btn:active {{
      transform: translateY(0);
    }}

    .nav-tabs {{
      display: flex;
      gap: 6px;
    }}

    .nav-btn {{
      background: rgba(30, 41, 59, 0.7);
      border: 1px solid rgba(148, 163, 184, 0.2);
      color: #cbd5e1;
      padding: 6px 12px;
      border-radius: 4px;
      font-size: 11px;
      font-weight: 600;
      cursor: pointer;
      transition: all 0.2s ease;
    }}

    .nav-btn:hover {{
      background: rgba(56, 189, 248, 0.2);
      border-color: #38bdf8;
      color: #ffffff;
    }}

    .nav-btn.active {{
      background: #0284c7;
      border-color: #38bdf8;
      color: #ffffff;
      box-shadow: 0 0 10px rgba(56, 189, 248, 0.4);
    }}

    .nav-btn.highlight-exploded {{
      border-color: #f59e0b;
      color: #fef08a;
    }}

    .nav-btn.highlight-exploded.active {{
      background: #d97706;
      border-color: #fbbf24;
      color: #ffffff;
    }}

    /* Top Right Status Card */
    #status-card {{
      top: 88px;
      right: 16px;
      width: 250px;
      padding: 12px 16px;
      display: flex;
      flex-direction: column;
      gap: 6px;
      font-size: 11px;
    }}

    .status-row {{
      display: flex;
      justify-content: space-between;
      align-items: center;
    }}

    .status-label {{
      color: #94a3b8;
    }}

    .status-val {{
      font-weight: 600;
      color: #f1f5f9;
      font-family: monospace;
    }}

    .status-val.highlight {{
      color: #38bdf8;
    }}

    .status-val.highlight-green {{
      color: #34d399;
    }}

    .status-val.highlight-orange {{
      color: #fbbf24;
    }}

    /* Left Control Panel */
    #left-panel {{
      top: 88px;
      left: 16px;
      bottom: 24px;
      width: 260px;
      padding: 14px;
      display: flex;
      flex-direction: column;
      gap: 10px;
      overflow-y: auto;
      transition: transform 0.3s cubic-bezier(0.4, 0, 0.2, 1);
    }}

    #left-panel.collapsed {{
      transform: translateX(-290px);
    }}

    .panel-collapse-toggle {{
      position: absolute;
      top: 88px;
      left: 284px;
      width: 28px;
      height: 28px;
      border-radius: 4px;
      background: rgba(11, 20, 38, 0.9);
      border: 1px solid rgba(56, 189, 248, 0.3);
      color: #38bdf8;
      display: flex;
      align-items: center;
      justify-content: center;
      cursor: pointer;
      z-index: 11;
      font-size: 12px;
      transition: left 0.3s ease;
    }}

    .panel-collapse-toggle.collapsed {{
      left: 16px;
    }}

    .panel-title {{
      font-size: 12px;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.75px;
      color: #cbd5e1;
      border-bottom: 1px solid rgba(56, 189, 248, 0.2);
      padding-bottom: 5px;
      display: flex;
      justify-content: space-between;
      align-items: center;
    }}

    .layers-list {{
      display: flex;
      flex-direction: column;
      gap: 6px;
    }}

    .layer-row {{
      display: flex;
      align-items: center;
      gap: 8px;
      padding: 6px 8px;
      border-radius: 4px;
      background: rgba(30, 41, 59, 0.5);
      border: 1px solid transparent;
      cursor: pointer;
      transition: all 0.15s ease;
    }}

    .layer-row:hover {{
      background: rgba(56, 189, 248, 0.15);
      border-color: rgba(56, 189, 248, 0.3);
    }}

    .layer-row.active-layer {{
      border-color: #38bdf8;
      background: rgba(14, 165, 233, 0.2);
    }}

    .layer-swatch {{
      width: 14px;
      height: 14px;
      border-radius: 3px;
      flex-shrink: 0;
      border: 1px solid rgba(255, 255, 255, 0.3);
    }}

    .layer-info-text {{
      display: flex;
      flex-direction: column;
      overflow: hidden;
      flex-grow: 1;
    }}

    .layer-name-title {{
      font-size: 11px;
      font-weight: 600;
      white-space: nowrap;
      text-overflow: ellipsis;
      overflow: hidden;
    }}

    .layer-thick-badge {{
      font-size: 9px;
      color: #94a3b8;
      font-family: monospace;
    }}

    .toggles-list {{
      display: flex;
      flex-direction: column;
      gap: 5px;
    }}

    .toggle-row {{
      display: flex;
      align-items: center;
      gap: 8px;
      font-size: 11px;
      color: #e2e8f0;
      cursor: pointer;
    }}

    .toggle-row input[type="checkbox"] {{
      cursor: pointer;
      accent-color: #0284c7;
    }}

    .slider-group {{
      display: flex;
      flex-direction: column;
      gap: 4px;
    }}

    .slider-header {{
      display: flex;
      justify-content: space-between;
      font-size: 10px;
      color: #94a3b8;
    }}

    .custom-slider {{
      width: 100%;
      height: 4px;
      background: #334155;
      border-radius: 2px;
      outline: none;
      accent-color: #38bdf8;
      cursor: pointer;
    }}

    /* Bottom Left Hydraulic Legend */
    #head-legend {{
      bottom: 24px;
      left: 284px;
      padding: 10px 14px;
      display: flex;
      flex-direction: column;
      gap: 5px;
      font-size: 10px;
      transition: left 0.3s ease;
    }}

    #head-legend.collapsed {{
      left: 56px;
    }}

    .legend-title {{
      font-weight: 700;
      color: #e2e8f0;
      display: flex;
      justify-content: space-between;
      gap: 12px;
    }}

    .legend-gradient {{
      width: 200px;
      height: 10px;
      border-radius: 2px;
      border: 1px solid rgba(255, 255, 255, 0.2);
      background: linear-gradient(to right, #0284c7, #38bdf8, #7dd3fc);
      transition: background 0.4s ease;
    }}

    .legend-gradient.drawdown-rainbow {{
      background: linear-gradient(to right, #8b5cf6, #3b82f6, #06b6d4, #10b981, #eab308, #f97316, #ef4444);
    }}

    .legend-ticks {{
      display: flex;
      justify-content: space-between;
      font-size: 9px;
      font-family: monospace;
      color: #94a3b8;
    }}

    /* Right Layer Detail Panel */
    #right-panel {{
      top: 250px;
      right: 16px;
      width: 250px;
      padding: 14px;
      display: flex;
      flex-direction: column;
      gap: 8px;
      font-size: 11px;
      transition: all 0.3s ease;
    }}

    #right-panel.hidden {{
      display: none;
    }}

    .prop-row {{
      display: flex;
      justify-content: space-between;
      padding: 3px 0;
      border-bottom: 1px solid rgba(255, 255, 255, 0.05);
    }}

    .prop-label {{
      color: #94a3b8;
    }}

    .prop-val {{
      font-weight: 600;
      color: #f8fafc;
      font-family: monospace;
    }}

    /* Floating Tooltip */
    #tooltip-hud {{
      position: absolute;
      display: none;
      background: rgba(15, 23, 42, 0.95);
      border: 1px solid #38bdf8;
      border-radius: 6px;
      padding: 8px 12px;
      font-size: 11px;
      color: #f1f5f9;
      pointer-events: none;
      z-index: 100;
      box-shadow: 0 4px 20px rgba(0, 0, 0, 0.8);
      max-width: 260px;
    }}

    /* Bottom Center Scale Bar */
    #scale-bar-panel {{
      bottom: 24px;
      left: 50%;
      transform: translateX(-50%);
      padding: 6px 14px;
      display: flex;
      flex-direction: column;
      align-items: center;
      gap: 2px;
    }}

    .scale-ticks {{
      display: flex;
      justify-content: space-between;
      width: 100px;
      font-size: 9px;
      font-family: monospace;
      color: #94a3b8;
    }}

    .scale-line {{
      width: 100px;
      height: 4px;
      border: 1px solid #cbd5e1;
      border-top: none;
      background: rgba(255, 255, 255, 0.15);
    }}
  </style>
</head>
<body>

  <!-- 3D WebGL Canvas Container -->
  <div id="webgl-container"></div>
  <svg id="axes-svg"></svg>

  <!-- Top Header Bar -->
  <div id="top-header" class="glass-panel">
    <div class="header-left">
      <div class="header-title">
        <span>JVC15AMRM004 — Stonehenge 2, Dubai, UAE</span>
        <span class="tag-live" id="header-scenario-tag">Scenario 1</span>
      </div>
      <div class="header-subtitle">Multi-Scenario 3D Hydrogeological GIS Model | Cinematic Flow & Heatmap</div>
    </div>

    <!-- Scenario Selector Controls -->
    <div class="scenario-selector-container">
      <span class="scenario-select-label">Scenario:</span>
      <select id="scenario-select" class="scenario-dropdown" onchange="onScenarioDropdownChange()">
        <option value="base" selected>Base Model View (Initial Static State)</option>
        <option value="sc1">Scenario 1: Base No Pumping (Head Contour Surface)</option>
        <option value="sc2">Scenario 2: Steady Pumping (Drawdown & Cone of Depression)</option>
      </select>
      <button id="btn-apply-scenario" class="apply-btn" onclick="applySelectedScenario()">
        <span>⚡ Apply Scenario</span>
      </button>
    </div>

    <!-- View Mode Tabs -->
    <div class="nav-tabs">
      <button class="nav-btn active" id="tab-3d" onclick="setViewMode('3d')">3D View</button>
      <button class="nav-btn highlight-exploded" id="tab-exploded" onclick="setViewMode('exploded')">Exploded 3D</button>
      <button class="nav-btn" id="tab-plan" onclick="setViewMode('plan')">Plan View</button>
      <button class="nav-btn" id="tab-cross-x" onclick="setViewMode('cross-x')">Cross-Section X</button>
      <button class="nav-btn" id="tab-cross-y" onclick="setViewMode('cross-y')">Cross-Section Y</button>
      <button class="nav-btn" id="tab-flow" onclick="setViewMode('flow')">Flow Paths</button>
      <button class="nav-btn" id="tab-views" onclick="cyclePresetViews()">Views</button>
    </div>
  </div>

  <!-- Top Right Status Card -->
  <div id="status-card" class="glass-panel">
    <div class="status-row">
      <span class="status-label">Active Scenario:</span>
      <span class="status-val highlight" id="hud-scenario-name">Scenario 2</span>
    </div>
    <div class="status-row">
      <span class="status-label">Pumping Scheme:</span>
      <span class="status-val highlight-green" id="hud-pumping-rate">265.26 m³/d</span>
    </div>
    <div class="status-row">
      <span class="status-label">Controlling Head:</span>
      <span class="status-val highlight-orange" id="hud-controlling-head">-8.500 m DMD</span>
    </div>
    <div class="status-row">
      <span class="status-label">Max Drawdown:</span>
      <span class="status-val" id="hud-max-drawdown">15.62 m</span>
    </div>
    <div class="status-row">
      <span class="status-label">Model Engine:</span>
      <span class="status-val">MODFLOW 6 (v6.7.0)</span>
    </div>
    <div class="status-row">
      <span class="status-label">Mass Balance:</span>
      <span class="status-val highlight-green">0.00% Discrepancy</span>
    </div>
  </div>

  <!-- Left Control Panel -->
  <div id="left-panel" class="glass-panel">
    <div class="panel-title">
      <span>Model Layers (Top → Base)</span>
      <span style="font-size: 9px; color: #38bdf8;">Stratigraphy</span>
    </div>
    <div class="layers-list">
      <div class="layer-row" id="layer-row-1" onclick="selectLayer(1)">
        <input type="checkbox" id="lay-chk-1" checked onclick="event.stopPropagation(); toggleLayerVisibility(1)">
        <div class="layer-swatch" style="background: #eab308;"></div>
        <div class="layer-info-text">
          <span class="layer-name-title">Layer 1: Dune Sand / Silt</span>
          <span class="layer-thick-badge">+8.25 to +6.75 m (1.50 m)</span>
        </div>
      </div>
      <div class="layer-row" id="layer-row-2" onclick="selectLayer(2)">
        <input type="checkbox" id="lay-chk-2" checked onclick="event.stopPropagation(); toggleLayerVisibility(2)">
        <div class="layer-swatch" style="background: #f97316;"></div>
        <div class="layer-info-text">
          <span class="layer-name-title">Layer 2: Upper Sandstone</span>
          <span class="layer-thick-badge">+6.75 to -4.75 m (11.50 m)</span>
        </div>
      </div>
      <div class="layer-row active-layer" id="layer-row-3" onclick="selectLayer(3)">
        <input type="checkbox" id="lay-chk-3" checked onclick="event.stopPropagation(); toggleLayerVisibility(3)">
        <div class="layer-swatch" style="background: #ea580c;"></div>
        <div class="layer-info-text">
          <span class="layer-name-title">Layer 3: Screened Aquifer</span>
          <span class="layer-thick-badge">-4.75 to -14.75 m (10.00 m)</span>
        </div>
      </div>
      <div class="layer-row" id="layer-row-4" onclick="selectLayer(4)">
        <input type="checkbox" id="lay-chk-4" checked onclick="event.stopPropagation(); toggleLayerVisibility(4)">
        <div class="layer-swatch" style="background: #64748b;"></div>
        <div class="layer-info-text">
          <span class="layer-name-title">Layer 4: Conglomerate Sand</span>
          <span class="layer-thick-badge">-14.75 to -19.75 m (5.00 m)</span>
        </div>
      </div>
      <div class="layer-row" id="layer-row-5" onclick="selectLayer(5)">
        <input type="checkbox" id="lay-chk-5" checked onclick="event.stopPropagation(); toggleLayerVisibility(5)">
        <div class="layer-swatch" style="background: #334155;"></div>
        <div class="layer-info-text">
          <span class="layer-name-title">Layer 5: Basal Confining Bed</span>
          <span class="layer-thick-badge">-19.75 to -31.75 m (12.00 m)</span>
        </div>
      </div>
    </div>

    <div class="panel-title" style="margin-top: 6px;">Visual Elements</div>
    <div class="toggles-list">
      <label class="toggle-row">
        <input type="checkbox" id="chk-water-surface" checked onchange="updateVisibility('water')">
        <span>Show 3D Water Table Surface</span>
      </label>
      <label class="toggle-row">
        <input type="checkbox" id="chk-heatmap" checked onchange="updateVisibility('heatmap')">
        <span>Show Drawdown Heatmap Texture</span>
      </label>
      <label class="toggle-row">
        <input type="checkbox" id="chk-flow-particles" checked onchange="updateVisibility('flow')">
        <span>Show 3D Flow Particles</span>
      </label>
      <label class="toggle-row">
        <input type="checkbox" id="chk-layers" checked onchange="updateVisibility('layers')">
        <span>Show Layer Volumes</span>
      </label>
      <label class="toggle-row">
        <input type="checkbox" id="chk-shoring" checked onchange="updateVisibility('shoring')">
        <span>Show Secant Shoring Walls</span>
      </label>
      <label class="toggle-row">
        <input type="checkbox" id="chk-toe" checked onchange="updateVisibility('toe')">
        <span>Show Shoring Toe Line</span>
      </label>
      <label class="toggle-row">
        <input type="checkbox" id="chk-wells" checked onchange="updateVisibility('wells')">
        <span>Show 6 Deepwells (DW-01 to 06)</span>
      </label>
      <label class="toggle-row">
        <input type="checkbox" id="chk-cad-sections" checked onchange="updateVisibility('cad-sections')">
        <span>Show CAD Excavation Levels</span>
      </label>
      <label class="toggle-row">
        <input type="checkbox" id="chk-aerial" checked onchange="updateVisibility('aerial')">
        <span>Show Aerial Satellite Ground</span>
      </label>
    </div>

    <div class="slider-group" style="margin-top: 6px;">
      <div class="slider-header">
        <span>Layer Transparency</span>
        <span id="transparency-val">50%</span>
      </div>
      <input type="range" id="transparency-slider" class="custom-slider" min="0" max="90" value="50" oninput="updateTransparency(this.value)">
    </div>

    <div class="slider-group" style="margin-top: 4px;">
      <div class="slider-header">
        <span>Exploded 3D Layer Separation</span>
        <span id="exploded-val">0%</span>
      </div>
      <input type="range" id="exploded-slider" class="custom-slider" min="0" max="100" value="0" oninput="onExplodedSliderChange(this.value)">
    </div>
  </div>

  <button class="panel-collapse-toggle" id="panel-toggle-btn" onclick="toggleLeftPanel()" title="Toggle Control Panel">◀</button>

  <!-- Hydraulic Legend -->
  <div id="head-legend" class="glass-panel">
    <div class="legend-title">
      <span id="legend-title-text">Groundwater Drawdown (m)</span>
      <span style="color:#38bdf8;" id="legend-scenario-badge">Scenario 2</span>
    </div>
    <div class="legend-gradient drawdown-rainbow" id="legend-bar"></div>
    <div class="legend-ticks" id="legend-ticks-container">
      <span>0.0 m (Boundary)</span>
      <span style="color:#fbbf24;">14.75 m (Target)</span>
      <span>15.62 m (Max)</span>
    </div>
  </div>

  <!-- Right Layer Detail Panel -->
  <div id="right-panel" class="glass-panel">
    <div class="panel-title" id="detail-layer-title">Layer 3: Screened Aquifer</div>
    <div class="prop-row">
      <span class="prop-label">Lithology:</span>
      <span class="prop-val" id="det-lithology">Moderately Weathered Sandstone</span>
    </div>
    <div class="prop-row">
      <span class="prop-label">Top Elevation:</span>
      <span class="prop-val" id="det-top">-4.75 m DMD</span>
    </div>
    <div class="prop-row">
      <span class="prop-label">Bottom Elevation:</span>
      <span class="prop-val" id="det-bot">-14.75 m DMD</span>
    </div>
    <div class="prop-row">
      <span class="prop-label">Thickness:</span>
      <span class="prop-val" id="det-thick">10.00 m</span>
    </div>
    <div class="prop-row">
      <span class="prop-label">Permeability (Kh):</span>
      <span class="prop-val" id="det-kh">4.32 m/day (5.0×10⁻⁵ m/s)</span>
    </div>
    <div class="prop-row">
      <span class="prop-label">Vertical Perm (Kv):</span>
      <span class="prop-val" id="det-kv">0.864 m/day (1.0×10⁻⁵ m/s)</span>
    </div>
    <div class="prop-row">
      <span class="prop-label">Specific Yield (Sy):</span>
      <span class="prop-val" id="det-sy">0.12 (12%)</span>
    </div>
    <div class="prop-row">
      <span class="prop-label">Active Wells:</span>
      <span class="prop-val highlight" id="det-wells">6 Deepwells Screened</span>
    </div>
  </div>

  <!-- Floating Raycasting Tooltip -->
  <div id="tooltip-hud"></div>

  <!-- Scale Bar -->
  <div id="scale-bar-panel" class="glass-panel">
    <div class="scale-ticks">
      <span>0m</span>
      <span>10m</span>
      <span>20m</span>
    </div>
    <div class="scale-line"></div>
  </div>

  <!-- Core JavaScript Libraries -->
  <script src="js/three.min.js"></script>
  <script src="js/OrbitControls.js"></script>

  <script>
    // Embedded Multi-Scenario Dataset & Aerial Base64 Texture
    const MODEL_DATA = {model_data_json};
    const AERIAL_B64 = "{aerial_b64}";

    // Coordinate Conversion Constants
    const X_ORIGIN = 486977.5;
    const Y_ORIGIN = 2772585.0;
    const Z_EXAG = 1.25;
    const BASE_MODEL_VISUAL_OFFSET = 35.5; // Subtle rendering lift: Layer 5 base floats ~4.7 units above ground

    // State Variables
    let currentScenarioId = 'base';
    let scene, camera, renderer, controls;
    let waterMesh, flowParticleSystem;
    let morphStartTime = 0;
    let isMorphing = false;
    let currentWaterHeights = [];
    let targetWaterHeights = [];
    let currentWaterColors = [];
    let targetWaterColors = [];

    const groupAerial = new THREE.Group();
    const groupGroundSite = new THREE.Group();
    const groupGeologicalModel = new THREE.Group();
    const groupLayers = new THREE.Group();
    const groupMesh = new THREE.Group();
    const groupSite = new THREE.Group();
    const groupShoring = new THREE.Group();
    const groupShoringToe = new THREE.Group();
    const groupWells = new THREE.Group();
    const groupHead = new THREE.Group();
    const groupFlow = new THREE.Group();
    const groupBoundary = new THREE.Group();
    const groupCadSections = new THREE.Group();

    const layerVolumes = [];
    const interactableObjects = [];
    const raycaster = new THREE.Raycaster();
    const mouse = new THREE.Vector2();
    let clipPlane;

    function dltmToThree(easting, northing, elevationDmd) {{
      const x = easting - X_ORIGIN;
      const y = (elevationDmd + BASE_MODEL_VISUAL_OFFSET) * Z_EXAG;
      const z = -(northing - Y_ORIGIN);
      return new THREE.Vector3(x, y, z);
    }}

    function threeToDltm(x, y, z) {{
      const easting = x + X_ORIGIN;
      const northing = -z + Y_ORIGIN;
      const elevationDmd = (y / Z_EXAG) - BASE_MODEL_VISUAL_OFFSET;
      return {{ easting, northing, elevationDmd }};
    }}

    // Rainbow Colormap Function
    function getRainbowColor(val, minVal, maxVal) {{
      const t = Math.max(0, Math.min(1, (val - minVal) / (maxVal - minVal)));
      // Hue from blue (240 deg = 0.66) to red (0 deg = 0.0)
      const hue = (1.0 - t) * 0.66;
      const col = new THREE.Color();
      col.setHSL(hue, 0.95, 0.52);
      return col;
    }}

    window.onload = function() {{
      init();
    }};

    function init() {{
      const container = document.getElementById('webgl-container');

      // Scene & Camera
      scene = new THREE.Scene();
      camera = new THREE.PerspectiveCamera(42, window.innerWidth / window.innerHeight, 1, 2500);
      camera.position.set(135, 95, 155);

      // WebGL Renderer
      renderer = new THREE.WebGLRenderer({{ antialias: true, alpha: true, logarithmicDepthBuffer: true }});
      renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));
      renderer.setSize(window.innerWidth, window.innerHeight);
      renderer.shadowMap.enabled = true;
      renderer.shadowMap.type = THREE.PCFSoftShadowMap;
      renderer.localClippingEnabled = true;
      container.appendChild(renderer.domElement);

      // Orbit Controls (Targeting center of elevated geological block at Y=30)
      controls = new THREE.OrbitControls(camera, renderer.domElement);
      controls.enableDamping = true;
      controls.dampingFactor = 0.06;
      controls.target.set(0, 30, 0);
      controls.maxPolarAngle = Math.PI / 2 + 0.05;
      controls.minDistance = 20;
      controls.maxDistance = 1200;

      // Daylight Lighting
      const ambLight = new THREE.AmbientLight(0xffffff, 0.92);
      scene.add(ambLight);

      const sunLight = new THREE.DirectionalLight(0xfff7ed, 1.05);
      sunLight.position.set(110, 180, 90);
      sunLight.castShadow = true;
      scene.add(sunLight);

      const skyFill = new THREE.DirectionalLight(0x38bdf8, 0.45);
      skyFill.position.set(-90, 70, -80);
      scene.add(skyFill);

      // Clipping plane
      clipPlane = new THREE.Plane(new THREE.Vector3(0, -1, 0), (8.25 + BASE_MODEL_VISUAL_OFFSET) * Z_EXAG);

      // Model Hierarchy
      groupGeologicalModel.add(groupLayers);
      groupGeologicalModel.add(groupMesh);
      groupGeologicalModel.add(groupSite);
      groupGeologicalModel.add(groupShoring);
      groupGeologicalModel.add(groupShoringToe);
      groupGeologicalModel.add(groupWells);
      groupGeologicalModel.add(groupHead);
      groupGeologicalModel.add(groupFlow);
      groupGeologicalModel.add(groupBoundary);
      groupGeologicalModel.add(groupCadSections);

      scene.add(groupAerial);
      scene.add(groupGroundSite);
      scene.add(groupGeologicalModel);

      // Build Components
      buildDubaiSurroundingTerrain();
      buildGroundSiteAndGuideLines();
      build3dElevationDatumAxis();
      buildTrueStratigraphicVolumes();
      buildCadSections();
      buildSitePolygon();
      buildShoringWall();
      buildShoringToe();
      buildDeepwells();
      buildDynamicWaterTableMesh();
      buildAnimatedFlowParticles();
      buildBoundaryConditions();

      // Event Listeners
      window.addEventListener('resize', onWindowResize);
      window.addEventListener('mousemove', onMouseMove);
      window.addEventListener('click', onMouseClick);

      // Initialize default Base View
      applySelectedScenario();
      selectLayer(3);
      animate();
    }}

    // Aerial Ground Texture (Positioned at Base Level Y = 0)
    function buildDubaiSurroundingTerrain() {{
      const texLoader = new THREE.TextureLoader();
      const terrainTex = texLoader.load('data:image/jpeg;base64,' + AERIAL_B64);
      terrainTex.wrapS = THREE.ClampToEdgeWrapping;
      terrainTex.wrapT = THREE.ClampToEdgeWrapping;

      const terrainSize = 420.0;
      const terrainGeom = new THREE.PlaneGeometry(terrainSize, terrainSize);
      terrainGeom.rotateX(-Math.PI / 2);

      const terrainMat = new THREE.MeshStandardMaterial({{
        map: terrainTex,
        roughness: 0.88,
        metalness: 0.05,
        side: THREE.DoubleSide
      }});

      const terrainMesh = new THREE.Mesh(terrainGeom, terrainMat);
      terrainMesh.position.set(0, 0, 0); // Ground plane anchored at Y = 0
      terrainMesh.receiveShadow = true;
      terrainMesh.userData = {{
        type: 'aerial_ground',
        title: 'Dubai Aerial Ground Surface (+8.25 m DMD)',
        description: 'Georeferenced Dubai satellite photo anchored at base terrain level. The entire 3D geological cutaway model floats above this ground.'
      }};
      groupAerial.add(terrainMesh);
      interactableObjects.push(terrainMesh);
    }}

    function buildGroundSiteAndGuideLines() {{
      const poly = MODEL_DATA.site_polygon;
      const groundPts = poly.map(p => new THREE.Vector3(p.x - X_ORIGIN, 0.15, -(p.y - Y_ORIGIN)));
      groundPts.push(groundPts[0].clone());

      const groundLineGeom = new THREE.BufferGeometry().setFromPoints(groundPts);
      const groundLineMat = new THREE.LineBasicMaterial({{ color: 0x38bdf8, linewidth: 2 }});
      groupGroundSite.add(new THREE.Line(groundLineGeom, groundLineMat));

      // Guide pillars connecting ground footprint to elevated model base (Layer 5 Bottom at -31.75 m DMD)
      poly.forEach(p => {{
        const ptBottom = new THREE.Vector3(p.x - X_ORIGIN, 0.15, -(p.y - Y_ORIGIN));
        const ptElevated = dltmToThree(p.x, p.y, -31.75);
        const pillarGeom = new THREE.BufferGeometry().setFromPoints([ptBottom, ptElevated]);
        const pillarMat = new THREE.LineDashedMaterial({{
          color: 0x38bdf8,
          dashSize: 1.5,
          gapSize: 1.0,
          transparent: true,
          opacity: 0.85
        }});
        const pillar = new THREE.Line(pillarGeom, pillarMat);
        pillar.computeLineDistances();
        groupGroundSite.add(pillar);

        // Ground anchor marker dot
        const dotGeo = new THREE.CircleGeometry(0.8, 16);
        dotGeo.rotateX(-Math.PI / 2);
        const dotMat = new THREE.MeshBasicMaterial({{ color: 0x0284c7, side: THREE.DoubleSide }});
        const dot = new THREE.Mesh(dotGeo, dotMat);
        dot.position.copy(ptBottom);
        groupGroundSite.add(dot);
      }});
    }}

    // 3D Elevation Datum Axis & Vertical Engineering Ruler
    function build3dElevationDatumAxis() {{
      const axisX = -32.0;
      const axisZ = 34.0;
      const ptGround = new THREE.Vector3(axisX, 0, axisZ);
      const ptTop = new THREE.Vector3(axisX, (8.25 + BASE_MODEL_VISUAL_OFFSET) * Z_EXAG + 2.0, axisZ);

      // Main vertical spine
      const axisGeo = new THREE.BufferGeometry().setFromPoints([ptGround, ptTop]);
      const axisMat = new THREE.LineBasicMaterial({{ color: 0x94a3b8, linewidth: 2 }});
      groupGroundSite.add(new THREE.Line(axisGeo, axisMat));

      // Elevation tick marks
      const ticks = [
        {{ label: '+8.25 m (L1 Top / Ground)', elev: 8.25, color: 0xeab308 }},
        {{ label: '+6.75 m (L2 Top)', elev: 6.75, color: 0xf97316 }},
        {{ label: '+6.25 m (Static GWL)', elev: 6.25, color: 0x38bdf8 }},
        {{ label: '-4.75 m (L3 Aquifer)', elev: -4.75, color: 0xea580c }},
        {{ label: '-8.00 m (Sump Pit)', elev: -8.00, color: 0x22c55e }},
        {{ label: '-8.50 m (Target Head)', elev: -8.50, color: 0x10b981 }},
        {{ label: '-14.75 m (Shoring Toe)', elev: -14.75, color: 0xef4444 }},
        {{ label: '-19.75 m (L5 Top)', elev: -19.75, color: 0x64748b }},
        {{ label: '-31.75 m (Model Base)', elev: -31.75, color: 0x334155 }},
        {{ label: 'Dubai Aerial Ground (0.0)', elev: -BASE_MODEL_VISUAL_OFFSET, color: 0x38bdf8 }}
      ];

      ticks.forEach(t => {{
        const yPos = (t.elev + BASE_MODEL_VISUAL_OFFSET) * Z_EXAG;
        const tickGeo = new THREE.BufferGeometry().setFromPoints([
          new THREE.Vector3(axisX - 1.5, yPos, axisZ),
          new THREE.Vector3(axisX + 1.5, yPos, axisZ)
        ]);
        const tickMat = new THREE.LineBasicMaterial({{ color: t.color, linewidth: 2 }});
        groupGroundSite.add(new THREE.Line(tickGeo, tickMat));
      }});
    }}

    // Helper: 2D Point-in-polygon test
    function isPointInPolygon2D(x, y, poly) {{
      if (!poly || poly.length < 3) return false;
      let inside = false;
      for (let i = 0, j = poly.length - 1; i < poly.length; j = i++) {{
        const xi = poly[i].x, yi = poly[i].y;
        const xj = poly[j].x, yj = poly[j].y;
        const intersect = ((yi > y) !== (yj > y)) && (x < (xj - xi) * (y - yi) / (yj - yi) + xi);
        if (intersect) inside = !inside;
      }}
      return inside;
    }}

    function isInsideShoring(x, y) {{
      const poly = MODEL_DATA.shoring_polygon || [];
      return isPointInPolygon2D(x, y, poly);
    }}

    // Get stepped excavation level (m DMD) at specific coordinate
    function getExcavationLevel(x, y) {{
      const sections = MODEL_DATA.cad_sections || [];
      // 1. Check Green Inner Sump Pit (-8.00 m DMD)
      const secGreen = sections.find(s => s.id === 'sec_inner_green');
      if (secGreen && isPointInPolygon2D(x, y, secGreen.coordinates)) return -8.00;

      // 2. Check Orange Left Section (-4.60 m DMD)
      const secOrange = sections.find(s => s.id === 'sec_left_blue');
      if (secOrange && isPointInPolygon2D(x, y, secOrange.coordinates)) return -4.60;

      // 3. Check Yellow Lower Section (-6.40 m DMD)
      const secYellow = sections.find(s => s.id === 'sec_lower_green');
      if (secYellow && isPointInPolygon2D(x, y, secYellow.coordinates)) return -6.40;

      // 4. Check Red Main Section (-6.10 m DMD)
      const secRed = sections.find(s => s.id === 'sec_main_red');
      if (secRed && isPointInPolygon2D(x, y, secRed.coordinates)) return -6.10;

      return -6.10; // Default general excavation floor
    }}

    // Stratigraphic Geological Layers (Prism Extrusions with Stepped Excavation Cutout)
    function buildTrueStratigraphicVolumes() {{
      const activeCells = MODEL_DATA.active_cells;
      const cellSize = MODEL_DATA.grid.delr; // 2.5 m
      const boxW = cellSize * 0.985;
      const boxD = cellSize * 0.985;

      MODEL_DATA.layers.forEach(layer => {{
        const groupLayer = new THREE.Group();
        groupLayer.name = 'LayerGroup_' + layer.layer;

        const baseColor = new THREE.Color(layer.color);
        const mat = new THREE.MeshStandardMaterial({{
          color: baseColor,
          roughness: 0.55,
          metalness: 0.15,
          transparent: true,
          opacity: 0.70,
          clippingPlanes: [clipPlane]
        }});

        activeCells.forEach(cell => {{
          const inPit = isInsideShoring(cell.x, cell.y);
          let cellTop = layer.z_top;
          let cellBot = layer.z_bot;

          if (inPit) {{
            const excavFloor = getExcavationLevel(cell.x, cell.y);
            // If layer is entirely above excavation floor, it is completely excavated:
            if (cellBot >= excavFloor) return;
            // If excavation floor cuts through layer, trim top down to floor:
            if (cellTop > excavFloor) {{
              cellTop = excavFloor;
            }}
          }}

          const cellThick = cellTop - cellBot;
          if (cellThick <= 0.05) return;

          const zMid = (cellTop + cellBot) / 2;
          const boxH = cellThick * Z_EXAG;

          const geom = new THREE.BoxGeometry(boxW, boxH, boxD);
          const mesh = new THREE.Mesh(geom, mat);
          mesh.position.copy(dltmToThree(cell.x, cell.y, zMid));
          mesh.castShadow = true;
          mesh.receiveShadow = true;
          mesh.userData = {{
            type: 'geological_cell',
            layerInfo: layer,
            cell: cell,
            thickness: cellThick,
            z_top: cellTop,
            z_bot: cellBot
          }};
          groupLayer.add(mesh);
          interactableObjects.push(mesh);
        }});

        groupLayers.add(groupLayer);
        layerVolumes.push({{ layerNumber: layer.layer, group: groupLayer, defaultY: groupLayer.position.y }});
      }});
    }}

    // CAD Sections (Red Main, Green Sump, Yellow Bench, Orange Left Sections)
    function buildCadSections() {{
      if (!MODEL_DATA.cad_sections) return;
      MODEL_DATA.cad_sections.forEach(sec => {{
        if (!sec.coordinates || sec.coordinates.length < 3) return;
        const shape = new THREE.Shape();
        sec.coordinates.forEach((p, idx) => {{
          const px = p.x - X_ORIGIN;
          const pz = -(p.y - Y_ORIGIN);
          if (idx === 0) shape.moveTo(px, -pz);
          else shape.lineTo(px, -pz);
        }});
        shape.closePath();

        // Cutout nested inner sump pit if hole coordinates exist
        if (sec.hole_coordinates && sec.hole_coordinates.length >= 3) {{
          const hole = new THREE.Path();
          sec.hole_coordinates.forEach((p, idx) => {{
            const px = p.x - X_ORIGIN;
            const pz = -(p.y - Y_ORIGIN);
            if (idx === 0) hole.moveTo(px, -pz);
            else hole.lineTo(px, -pz);
          }});
          hole.closePath();
          shape.holes.push(hole);
        }}

        const geom = new THREE.ShapeGeometry(shape);
        geom.rotateX(-Math.PI / 2);

        // Position at stepped excavation design level + visual lift offset
        const yElev = (sec.design_level_m_dmd + BASE_MODEL_VISUAL_OFFSET) * Z_EXAG + 0.12;

        const mat = new THREE.MeshStandardMaterial({{
          color: new THREE.Color(sec.cad_color),
          roughness: 0.25,
          metalness: 0.10,
          transparent: false,
          opacity: 1.0,
          side: THREE.DoubleSide
        }});
        const mesh = new THREE.Mesh(geom, mat);
        mesh.position.y = yElev;
        mesh.userData = {{ type: 'cad_section', ...sec }};
        groupCadSections.add(mesh);
        interactableObjects.push(mesh);

        // Crisp white border outline for stepped floor boundaries
        const borderPts = sec.coordinates.map(p => new THREE.Vector3(p.x - X_ORIGIN, yElev + 0.08, -(p.y - Y_ORIGIN)));
        borderPts.push(borderPts[0].clone());
        const borderGeo = new THREE.BufferGeometry().setFromPoints(borderPts);
        const borderMat = new THREE.LineBasicMaterial({{ color: 0xffffff, linewidth: 2 }});
        groupCadSections.add(new THREE.Line(borderGeo, borderMat));
      }});
    }}

    // Site Polygon
    function buildSitePolygon() {{
      const poly = MODEL_DATA.site_polygon;
      const pts = poly.map(p => dltmToThree(p.x, p.y, 8.35));
      pts.push(pts[0].clone());
      const lineGeom = new THREE.BufferGeometry().setFromPoints(pts);
      const lineMat = new THREE.LineBasicMaterial({{ color: 0xef4444, linewidth: 3 }});
      groupSite.add(new THREE.Line(lineGeom, lineMat));
    }}

    // Secant Shoring Wall
    function buildShoringWall() {{
      const segments = MODEL_DATA.shoring_wall_segments || [];
      const pileRadius = 0.38;
      const wallTop = 8.25;
      const pileGeom = new THREE.CylinderGeometry(pileRadius, pileRadius, 1, 12);
      const pileMat = new THREE.MeshStandardMaterial({{
        color: 0x475569,
        metalness: 0.5,
        roughness: 0.35,
        clippingPlanes: [clipPlane]
      }});

      segments.forEach(seg => {{
        const p1 = seg.start;
        const p2 = seg.end;
        const dist = Math.hypot(p2.x - p1.x, p2.y - p1.y);
        const steps = Math.max(1, Math.round(dist / 0.70));
        const toe = seg.elevation_dmd;
        const pileH = (wallTop - toe) * Z_EXAG;

        for (let s = 0; s < steps; s++) {{
          const t = (s + 0.5) / steps;
          const px = p1.x + (p2.x - p1.x) * t;
          const py = p1.y + (p2.y - p1.y) * t;
          const pMesh = new THREE.Mesh(pileGeom, pileMat);
          pMesh.scale.set(1, pileH, 1);
          pMesh.position.copy(dltmToThree(px, py, (wallTop + toe) / 2));
          pMesh.castShadow = true;
          pMesh.userData = {{ type: 'shoring_wall', segment: seg, toe: toe }};
          groupShoring.add(pMesh);
          interactableObjects.push(pMesh);
        }}
      }});
    }}

    // Shoring Toe
    function buildShoringToe() {{
      const segments = MODEL_DATA.shoring_wall_segments || [];
      const toePts = [];
      segments.forEach((seg, i) => {{
        if (toePts.length === 0) toePts.push(dltmToThree(seg.start.x, seg.start.y, seg.elevation_dmd));
        toePts.push(dltmToThree(seg.end.x, seg.end.y, seg.elevation_dmd));
        const nextSeg = segments[(i + 1) % segments.length];
        if (Math.abs(nextSeg.elevation_dmd - seg.elevation_dmd) > 0.01) {{
          toePts.push(dltmToThree(seg.end.x, seg.end.y, nextSeg.elevation_dmd));
        }}
      }});
      if (toePts.length > 0) toePts.push(toePts[0].clone());

      const toeGeom = new THREE.BufferGeometry().setFromPoints(toePts);
      const toeMat = new THREE.LineDashedMaterial({{
        color: 0xf59e0b,
        dashSize: 1.5,
        gapSize: 0.8,
        linewidth: 3,
        clippingPlanes: [clipPlane]
      }});
      const toeLine = new THREE.Line(toeGeom, toeMat);
      toeLine.computeLineDistances();
      toeLine.userData = {{ type: 'shoring_toe', desc: 'Structural Stepped Toe (-9.30 to -11.65 m DMD)' }};
      groupShoringToe.add(toeLine);
      interactableObjects.push(toeLine);
    }}

    // Deepwells (DW-01 to DW-06)
    function buildDeepwells() {{
      const casingMat = new THREE.MeshStandardMaterial({{ color: 0x0284c7, metalness: 0.7, roughness: 0.2, clippingPlanes: [clipPlane] }});
      const screenMat = new THREE.MeshStandardMaterial({{ color: 0x38bdf8, emissive: 0x0284c7, emissiveIntensity: 0.9, wireframe: true, clippingPlanes: [clipPlane] }});
      const headMat = new THREE.MeshStandardMaterial({{ color: 0x38bdf8, emissive: 0x0284c7, emissiveIntensity: 0.8 }});

      MODEL_DATA.wells.forEach(well => {{
        const groupW = new THREE.Group();
        groupW.name = 'Well_' + well.id;
        groupW.userData = {{ type: 'well', wellId: well.id, info: well }};

        // Solid Casing (+8.25 to -7.80)
        const casingH = (well.z_top - well.scr_top) * Z_EXAG;
        const casingGeom = new THREE.CylinderGeometry(0.38, 0.38, casingH, 16);
        const casingMesh = new THREE.Mesh(casingGeom, casingMat);
        casingMesh.position.copy(dltmToThree(well.x, well.y, (well.z_top + well.scr_top) / 2));
        groupW.add(casingMesh);

        // Slotted Screen (-7.80 to -14.50)
        const screenH = (well.scr_top - well.scr_bot) * Z_EXAG;
        const screenGeom = new THREE.CylinderGeometry(0.42, 0.42, screenH, 16);
        const screenMesh = new THREE.Mesh(screenGeom, screenMat);
        screenMesh.position.copy(dltmToThree(well.x, well.y, (well.scr_top + well.scr_bot) / 2));
        groupW.add(screenMesh);

        // Collar at Surface
        const headGeom = new THREE.CylinderGeometry(0.75, 0.75, 0.65, 16);
        const headMesh = new THREE.Mesh(headGeom, headMat);
        headMesh.position.copy(dltmToThree(well.x, well.y, well.z_top + 0.35));
        groupW.add(headMesh);

        groupW.traverse(c => {{
          if (c.isMesh) {{
            c.userData = {{ type: 'well', wellId: well.id, info: well }};
            interactableObjects.push(c);
          }}
        }});
        groupWells.add(groupW);
      }});
    }}

    // -------------------------------------------------------------------------
    // DYNAMIC 3D PHREATIC WATER TABLE & HEATMAP MESH
    // -------------------------------------------------------------------------
    function buildDynamicWaterTableMesh() {{
      const cells = MODEL_DATA.grid_cells;
      const nrow = MODEL_DATA.grid.nrow; // 28
      const ncol = MODEL_DATA.grid.ncol; // 26

      const geom = new THREE.PlaneGeometry(ncol * 2.5, nrow * 2.5, ncol - 1, nrow - 1);
      geom.rotateX(-Math.PI / 2);

      const posAttr = geom.attributes.position;
      const vertexCount = posAttr.count;

      const colors = new Float32Array(vertexCount * 3);
      currentWaterHeights = new Float32Array(vertexCount);
      targetWaterHeights = new Float32Array(vertexCount);
      currentWaterColors = new Float32Array(vertexCount * 3);
      targetWaterColors = new Float32Array(vertexCount * 3);

      // Initialize coordinates and vertex colors for Scenario 2
      for (let i = 0; i < vertexCount; i++) {{
        const r = Math.floor(i / ncol);
        const c = i % ncol;
        const idx = Math.min(r * ncol + c, cells.length - 1);
        const cell = cells[idx];

        const x = (cell.x - X_ORIGIN);
        const z = -(cell.y - Y_ORIGIN);
        posAttr.setX(i, x);
        posAttr.setZ(i, z);

        const sc1_h = cell.sc1_head;
        const sc2_h = cell.sc2_head;
        const sc1_y = (sc1_h + BASE_MODEL_VISUAL_OFFSET) * Z_EXAG;
        const sc2_y = (sc2_h + BASE_MODEL_VISUAL_OFFSET) * Z_EXAG;

        currentWaterHeights[i] = sc2_y;
        targetWaterHeights[i] = sc2_y;
        posAttr.setY(i, sc2_y);

        // Rainbow color based on drawdown
        const dd = cell.sc2_drawdown;
        const cRainbow = getRainbowColor(dd, 0.0, 15.6247);
        const cCyan = new THREE.Color(0x0ea5e9);

        // Set colors
        colors[i * 3] = cRainbow.r;
        colors[i * 3 + 1] = cRainbow.g;
        colors[i * 3 + 2] = cRainbow.b;

        currentWaterColors[i * 3] = cRainbow.r;
        currentWaterColors[i * 3 + 1] = cRainbow.g;
        currentWaterColors[i * 3 + 2] = cRainbow.b;
      }}

      geom.setAttribute('color', new THREE.BufferAttribute(colors, 3));
      geom.computeVertexNormals();

      const mat = new THREE.MeshStandardMaterial({{
        vertexColors: true,
        roughness: 0.20,
        metalness: 0.15,
        transparent: true,
        opacity: 0.40,
        side: THREE.DoubleSide,
        depthWrite: false,
        clippingPlanes: [clipPlane]
      }});

      waterMesh = new THREE.Mesh(geom, mat);
      waterMesh.userData = {{
        type: 'water_table_surface',
        title: '3D Groundwater Surface (Phreatic Horizon)',
        desc: 'Dynamically deformed surface displaying simulated heads and drawdown.'
      }};
      groupHead.add(waterMesh);
      interactableObjects.push(waterMesh);
    }}

    // -------------------------------------------------------------------------
    // ANIMATED 3D GROUNDWATER FLOW PARTICLES
    // -------------------------------------------------------------------------
    function buildAnimatedFlowParticles() {{
      const particles = MODEL_DATA.flow_particles || [];
      const pCount = particles.length;

      const geom = new THREE.BufferGeometry();
      const positions = new Float32Array(pCount * 3);
      const colors = new Float32Array(pCount * 3);

      particles.forEach((p, i) => {{
        const pt = dltmToThree(p.start.x, p.start.y, p.start.z);
        positions[i * 3] = pt.x;
        positions[i * 3 + 1] = pt.y;
        positions[i * 3 + 2] = pt.z;

        colors[i * 3] = 0.22;
        colors[i * 3 + 1] = 0.74;
        colors[i * 3 + 2] = 0.97;
      }});

      geom.setAttribute('position', new THREE.BufferAttribute(positions, 3));
      geom.setAttribute('color', new THREE.BufferAttribute(colors, 3));

      const mat = new THREE.PointsMaterial({{
        size: 3.5,
        vertexColors: true,
        transparent: true,
        opacity: 0.88,
        blending: THREE.AdditiveBlending,
        clippingPlanes: [clipPlane]
      }});

      flowParticleSystem = new THREE.Points(geom, mat);
      flowParticleSystem.userData = {{
        type: 'flow_streamlines',
        title: '3D Groundwater Flow Particle Streamlines',
        desc: 'Particles entering via Layer 4 underflow and rising into deepwells.'
      }};
      groupFlow.add(flowParticleSystem);
    }}

    // Update particle streamlines in animation loop
    function updateFlowParticles(timeSeconds) {{
      if (!flowParticleSystem || currentScenarioId !== 'sc2') {{
        if (flowParticleSystem) flowParticleSystem.visible = false;
        return;
      }}
      const flowChk = document.getElementById('chk-flow-particles');
      flowParticleSystem.visible = flowChk ? flowChk.checked : true;

      const particles = MODEL_DATA.flow_particles || [];
      const posAttr = flowParticleSystem.geometry.attributes.position;

      for (let i = 0; i < particles.length; i++) {{
        const p = particles[i];
        const t = (timeSeconds * 0.25 * p.speed + p.offset) % 1.0;

        // Quadratic Bezier Curve from Start -> Underflow (Layer 4) -> Target Well
        const p0 = dltmToThree(p.start.x, p.start.y, p.start.z);
        const p1 = dltmToThree(p.underflow.x, p.underflow.y, p.underflow.z);
        const p2 = dltmToThree(p.target.x, p.target.y, p.target.z);

        const omt = 1 - t;
        const x = omt * omt * p0.x + 2 * omt * t * p1.x + t * t * p2.x;
        const y = omt * omt * p0.y + 2 * omt * t * p1.y + t * t * p2.y;
        const z = omt * omt * p0.z + 2 * omt * t * p1.z + t * t * p2.z;

        posAttr.setXYZ(i, x, y, z);
      }}
      posAttr.needsUpdate = true;
    }}

    // -------------------------------------------------------------------------
    // SCENARIO SWITCHING LOGIC (DYNAMIC 3D MORPHING)
    // -------------------------------------------------------------------------
    function onScenarioDropdownChange() {{
      const select = document.getElementById('scenario-select');
      const targetId = select.value;
      triggerScenarioTransition(targetId);
    }}

    function applySelectedScenario() {{
      const select = document.getElementById('scenario-select');
      const targetId = select.value;
      triggerScenarioTransition(targetId);
    }}

    function triggerScenarioTransition(scenarioId) {{
      currentScenarioId = scenarioId;
      const sc = MODEL_DATA.scenarios[scenarioId];
      if (!sc) return;

      // Update Header & HUD
      document.getElementById('header-scenario-tag').innerText = sc.short_name;
      document.getElementById('hud-scenario-name').innerText = sc.short_name;
      document.getElementById('hud-pumping-rate').innerText = sc.pumping_status;
      document.getElementById('hud-controlling-head').innerText = (sc.controlling_excavation_head > 0 ? '+' : '') + sc.controlling_excavation_head.toFixed(3) + ' m DMD';
      document.getElementById('hud-max-drawdown').innerText = sc.drawdown_max.toFixed(2) + ' m';

      // Update Legend
      const legendTitle = document.getElementById('legend-title-text');
      const legendBadge = document.getElementById('legend-scenario-badge');
      const legendBar = document.getElementById('legend-bar');
      const legendTicks = document.getElementById('legend-ticks-container');

      if (scenarioId === 'base') {{
        legendTitle.innerText = 'Groundwater Surface (+6.25 m DMD)';
        legendBadge.innerText = 'Base View';
        legendBar.className = 'legend-gradient';
        legendTicks.innerHTML = '<span>Min: +6.250 m DMD</span><span>Static Water Table</span><span>Max: +6.250 m DMD</span>';
        if (flowParticleSystem) flowParticleSystem.visible = false;
      }} else if (scenarioId === 'sc1') {{
        legendTitle.innerText = 'Hydraulic Head Elevation (m DMD)';
        legendBadge.innerText = 'Scenario 1';
        legendBar.className = 'legend-gradient';
        legendTicks.innerHTML = '<span>Min: +6.250 m DMD</span><span>Baseline Equilibrium</span><span>Max: +6.250 m DMD</span>';
        if (flowParticleSystem) flowParticleSystem.visible = false;
      }} else {{
        legendTitle.innerText = 'Groundwater Drawdown (m)';
        legendBadge.innerText = 'Scenario 2';
        legendBar.className = 'legend-gradient drawdown-rainbow';
        legendTicks.innerHTML = '<span>0.0 m (Boundary)</span><span style="color:#fbbf24;">14.75 m (Target)</span><span>15.62 m (Max)</span>';
        const flowChk = document.getElementById('chk-flow-particles');
        if (flowParticleSystem) flowParticleSystem.visible = flowChk ? flowChk.checked : true;
      }}

      // Prepare target heights & colors for water mesh
      const cells = MODEL_DATA.grid_cells;
      const ncol = MODEL_DATA.grid.ncol;
      const vertexCount = waterMesh.geometry.attributes.position.count;

      for (let i = 0; i < vertexCount; i++) {{
        const r = Math.floor(i / ncol);
        const c = i % ncol;
        const idx = Math.min(r * ncol + c, cells.length - 1);
        const cell = cells[idx];

        let targetHead = 6.25;
        if (scenarioId === 'sc2') {{
          targetHead = cell.sc2_head;
        }} else if (scenarioId === 'sc1') {{
          targetHead = cell.sc1_head;
        }}
        targetWaterHeights[i] = (targetHead + BASE_MODEL_VISUAL_OFFSET) * Z_EXAG;

        let col;
        if (scenarioId === 'sc2') {{
          col = getRainbowColor(cell.sc2_drawdown, 0.0, 15.6247);
        }} else if (scenarioId === 'sc1') {{
          col = new THREE.Color(0x0ea5e9);
        }} else {{
          col = new THREE.Color(0x0284c7);
        }}
        targetWaterColors[i * 3] = col.r;
        targetWaterColors[i * 3 + 1] = col.g;
        targetWaterColors[i * 3 + 2] = col.b;
      }}

      isMorphing = true;
      morphStartTime = performance.now();
    }}

    function animateWaterMorph(currentTime) {{
      if (!isMorphing || !waterMesh) return;
      const elapsed = (currentTime - morphStartTime) / 1000;
      const duration = 1.2; // 1.2s smooth quadratic transition
      const progress = Math.min(1.0, elapsed / duration);
      const ease = progress < 0.5 ? 2 * progress * progress : -1 + (4 - 2 * progress) * progress;

      const posAttr = waterMesh.geometry.attributes.position;
      const colAttr = waterMesh.geometry.attributes.color;
      const vertexCount = posAttr.count;

      for (let i = 0; i < vertexCount; i++) {{
        const startY = currentWaterHeights[i];
        const endY = targetWaterHeights[i];
        const newY = startY + (endY - startY) * ease;
        posAttr.setY(i, newY);

        const r = currentWaterColors[i * 3] + (targetWaterColors[i * 3] - currentWaterColors[i * 3]) * ease;
        const g = currentWaterColors[i * 3 + 1] + (targetWaterColors[i * 3 + 1] - currentWaterColors[i * 3 + 1]) * ease;
        const b = currentWaterColors[i * 3 + 2] + (targetWaterColors[i * 3 + 2] - currentWaterColors[i * 3 + 2]) * ease;

        colAttr.setXYZ(i, r, g, b);
      }}
      posAttr.needsUpdate = true;
      colAttr.needsUpdate = true;
      waterMesh.geometry.computeVertexNormals();

      if (progress >= 1.0) {{
        isMorphing = false;
        for (let i = 0; i < vertexCount; i++) {{
          currentWaterHeights[i] = targetWaterHeights[i];
          currentWaterColors[i * 3] = targetWaterColors[i * 3];
          currentWaterColors[i * 3 + 1] = targetWaterColors[i * 3 + 1];
          currentWaterColors[i * 3 + 2] = targetWaterColors[i * 3 + 2];
        }}
      }}
    }}

    // Boundary Conditions
    function buildBoundaryConditions() {{
      const chdMat = new THREE.MeshStandardMaterial({{
        color: 0x10b981,
        emissive: 0x059669,
        emissiveIntensity: 0.65,
        clippingPlanes: [clipPlane]
      }});

      MODEL_DATA.active_cells.forEach(cell => {{
        if (cell.row === 2 || cell.row === 25 || cell.col === 4 || cell.col === 23) {{
          const box = new THREE.BoxGeometry(2.4, 2.5 * Z_EXAG, 2.4);
          const mesh = new THREE.Mesh(box, chdMat);
          mesh.position.copy(dltmToThree(cell.x, cell.y, 6.25));
          mesh.userData = {{ type: 'chd_boundary', head: '+6.250 m DMD', desc: 'Constant Head Perimeter' }};
          groupBoundary.add(mesh);
        }}
      }});
    }}

    // -------------------------------------------------------------------------
    // UI CONTROLS & EVENT HANDLERS
    // -------------------------------------------------------------------------
    function updateVisibility(type) {{
      if (type === 'water') groupHead.visible = document.getElementById('chk-water-surface').checked;
      if (type === 'heatmap') {{
        const showHeatmap = document.getElementById('chk-heatmap').checked;
        if (waterMesh) {{
          waterMesh.material.vertexColors = showHeatmap;
          waterMesh.material.needsUpdate = true;
        }}
      }}
      if (type === 'flow') groupFlow.visible = document.getElementById('chk-flow-particles').checked;
      if (type === 'layers') groupLayers.visible = document.getElementById('chk-layers').checked;
      if (type === 'shoring') groupShoring.visible = document.getElementById('chk-shoring').checked;
      if (type === 'toe') groupShoringToe.visible = document.getElementById('chk-toe').checked;
      if (type === 'wells') groupWells.visible = document.getElementById('chk-wells').checked;
      if (type === 'cad-sections') groupCadSections.visible = document.getElementById('chk-cad-sections').checked;
      if (type === 'aerial') groupAerial.visible = document.getElementById('chk-aerial').checked;
    }}

    function updateTransparency(val) {{
      const opacity = (100 - val) / 100;
      document.getElementById('transparency-val').innerText = val + '%';
      groupLayers.traverse(child => {{
        if (child.isMesh && child.material) {{
          child.material.opacity = opacity * 0.75;
          child.material.transparent = true;
        }}
      }});
    }}

    function onExplodedSliderChange(val) {{
      document.getElementById('exploded-val').innerText = val + '%';
      const factor = val / 100 * 22.0;
      layerVolumes.forEach(lv => {{
        const offset = (3 - lv.layerNumber) * factor;
        lv.group.position.y = offset;
      }});
    }}

    function selectLayer(layerNum) {{
      for (let i = 1; i <= 5; i++) {{
        const row = document.getElementById('layer-row-' + i);
        if (row) row.classList.remove('active-layer');
      }}
      const selRow = document.getElementById('layer-row-' + layerNum);
      if (selRow) selRow.classList.add('active-layer');

      const layer = MODEL_DATA.layers.find(l => l.layer === layerNum);
      if (layer) {{
        document.getElementById('detail-layer-title').innerText = layer.name;
        document.getElementById('det-lithology').innerText = layer.geology;
        document.getElementById('det-top').innerText = (layer.z_top > 0 ? '+' : '') + layer.z_top.toFixed(2) + ' m DMD';
        document.getElementById('det-bot').innerText = layer.z_bot.toFixed(2) + ' m DMD';
        document.getElementById('det-thick').innerText = layer.thickness.toFixed(2) + ' m';
        document.getElementById('det-kh').innerText = layer.kh + ' m/day';
        document.getElementById('det-kv').innerText = layer.kv + ' m/day';
        document.getElementById('det-sy').innerText = (layer.sy * 100).toFixed(0) + '%';
      }}
    }}

    function toggleLayerVisibility(layerNum) {{
      const chk = document.getElementById('lay-chk-' + layerNum);
      const lv = layerVolumes.find(l => l.layerNumber === layerNum);
      if (lv) lv.group.visible = chk.checked;
    }}

    function toggleLeftPanel() {{
      const panel = document.getElementById('left-panel');
      const btn = document.getElementById('panel-toggle-btn');
      const legend = document.getElementById('head-legend');
      panel.classList.toggle('collapsed');
      btn.classList.toggle('collapsed');
      legend.classList.toggle('collapsed');
      btn.innerText = panel.classList.contains('collapsed') ? '▶' : '◀';
    }}

    function setViewMode(mode) {{
      document.querySelectorAll('.nav-btn').forEach(b => b.classList.remove('active'));
      const activeBtn = document.getElementById('tab-' + mode);
      if (activeBtn) activeBtn.classList.add('active');

      if (mode === '3d') {{
        controls.target.set(0, 30, 0);
        camera.position.set(135, 95, 155);
      }} else if (mode === 'exploded') {{
        document.getElementById('exploded-slider').value = 75;
        onExplodedSliderChange(75);
        controls.target.set(0, 30, 0);
        camera.position.set(140, 95, 150);
      }} else if (mode === 'plan') {{
        controls.target.set(0, 30, 0);
        camera.position.set(0, 240, 0);
      }} else if (mode === 'cross-x') {{
        controls.target.set(0, 30, 0);
        camera.position.set(0, 30, 190);
      }} else if (mode === 'cross-y') {{
        controls.target.set(0, 30, 0);
        camera.position.set(190, 30, 0);
      }} else if (mode === 'flow') {{
        controls.target.set(0, 30, 0);
        camera.position.set(85, 60, 105);
      }}
    }}

    function cyclePresetViews() {{
      const presets = [
        {{ pos: [135, 95, 155], target: [0, 30, 0] }},
        {{ pos: [-130, 85, 140], target: [0, 30, 0] }},
        {{ pos: [0, 230, 0], target: [0, 30, 0] }},
        {{ pos: [0, 30, 180], target: [0, 30, 0] }}
      ];
      const p = presets[Math.floor(Math.random() * presets.length)];
      camera.position.set(...p.pos);
      controls.target.set(...p.target);
    }}

    function onMouseMove(event) {{
      mouse.x = (event.clientX / window.innerWidth) * 2 - 1;
      mouse.y = -(event.clientY / window.innerHeight) * 2 + 1;

      raycaster.setFromCamera(mouse, camera);
      const intersects = raycaster.intersectObjects(interactableObjects, true);
      const hud = document.getElementById('tooltip-hud');

      if (intersects.length > 0) {{
        const obj = intersects[0].object;
        const data = obj.userData;
        if (data && data.type) {{
          hud.style.display = 'block';
          hud.style.left = (event.clientX + 14) + 'px';
          hud.style.top = (event.clientY + 14) + 'px';

          if (data.type === 'well') {{
            const w = data.info;
            const sc = MODEL_DATA.scenarios[currentScenarioId];
            const wSc = sc.wells.find(x => x.id === w.id) || w;
            hud.innerHTML = `<strong>Deepwell ${{w.id}}</strong><br>Pumping Rate: ${{wSc.q_m3_d}} m³/d (${{wSc.q_m3_hr}} m³/hr)<br>Screen: ${{w.scr_top}} to ${{w.scr_bot}} m DMD<br>Simulated Head: ${{wSc.head_m_dmd ? wSc.head_m_dmd.toFixed(2) : '-8.50'}} m DMD<br>Drawdown: ${{wSc.drawdown_m ? wSc.drawdown_m.toFixed(2) : '15.32'}} m`;
          }} else if (data.type === 'geological_cell') {{
            hud.innerHTML = `<strong>${{data.layerInfo.name}}</strong><br>Elev: ${{data.z_top}} to ${{data.z_bot}} m DMD<br>Permeability (Kh): ${{data.layerInfo.kh}} m/d<br>Role: ${{data.layerInfo.role}}`;
          }} else if (data.type === 'water_table_surface') {{
            hud.innerHTML = `<strong>3D Water Table Surface</strong><br>Scenario: ${{MODEL_DATA.scenarios[currentScenarioId].short_name}}<br>Current Pumping: ${{MODEL_DATA.scenarios[currentScenarioId].pumping_status}}<br>Excavation Head: ${{MODEL_DATA.scenarios[currentScenarioId].controlling_excavation_head}} m DMD`;
          }} else if (data.type === 'cad_section') {{
            hud.innerHTML = `<strong>${{data.name}}</strong><br>Level: ${{data.level_code}} (${{data.design_level_m_dmd}} m DMD)<br>Area: ${{data.net_area_m2}} m² (${{data.area_percentage}}%)<br>${{data.description}}`;
          }} else {{
            hud.innerHTML = `<strong>${{data.title || data.type}}</strong><br>${{data.desc || ''}}`;
          }}
          return;
        }}
      }}
      hud.style.display = 'none';
    }}

    function onMouseClick(event) {{
      // Select layer on click
      raycaster.setFromCamera(mouse, camera);
      const intersects = raycaster.intersectObjects(interactableObjects, true);
      if (intersects.length > 0) {{
        const data = intersects[0].object.userData;
        if (data && data.layerInfo) {{
          selectLayer(data.layerInfo.layer);
        }}
      }}
    }}

    function onWindowResize() {{
      camera.aspect = window.innerWidth / window.innerHeight;
      camera.updateProjectionMatrix();
      renderer.setSize(window.innerWidth, window.innerHeight);
    }}

    // Main Render Loop
    function animate(time) {{
      requestAnimationFrame(animate);
      const tSec = (time || 0) / 1000;

      animateWaterMorph(time || performance.now());
      updateFlowParticles(tSec);

      controls.update();
      renderer.render(scene, camera);
    }}
  </script>
</body>
</html>
"""

    OUTPUT_HTML.parent.mkdir(parents=True, exist_ok=True)
    with open(OUTPUT_HTML, "w", encoding="utf-8") as f:
        f.write(html_code)

    print(f"Successfully generated 3D Model: {OUTPUT_HTML}")


if __name__ == "__main__":
    compile_data_and_generate_html()
