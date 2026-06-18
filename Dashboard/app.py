import streamlit as st
import pandas as pd
import os
import json
import plotly.express as px
from pathlib import Path

# -----------------------------
# PAGE CONFIG
# -----------------------------
st.set_page_config(
    page_title="MHVI Ghana Dashboard",
    layout="wide"
)

# -----------------------------
# BASE DIRECTORY
# -----------------------------
BASE_DIR = Path(__file__).resolve().parent.parent

# -----------------------------
# LOAD DATA
# -----------------------------
@st.cache_data
def load_data():
    file_path = BASE_DIR / "Data" / "Processed" / "final_results_mhvi.csv"
    return pd.read_csv(file_path)

df = load_data()

# -----------------------------
# REGION NAME MAPPING
# -----------------------------
region_name_map = {
    "oti": "Oti Region",
    "volta": "Volta Region",
    "greater accra": "Greater Accra Region",
    "ahafo": "Ahafo Region",
    "bono east": "Bono East Region",
    "savannah": "Savannah Region",
    "northern": "Northern Region",
    "western north": "Western North Region",
    "eastern": "Eastern Region",
    "central": "Central Region",
    "western": "Western Region",
    "ashanti": "Ashanti Region",
    "upper west": "Upper West Region",
    "upper east": "Upper East Region",
    "bono": "Bono Region",
    "north east": "North East Region"
}

df["Region_GEO"] = df["Region"].map(region_name_map)

# -----------------------------
# LOAD GEOJSON
# -----------------------------
@st.cache_data
def load_geo():
    geo_path = BASE_DIR / "Data" / "geo" / "ghana_regions.geojson"
    with open(geo_path, "r") as f:
        return json.load(f)

ghana_geojson = load_geo()

# -----------------------------
# KPI CALCULATIONS
# -----------------------------
national_avg = df["MHVI_Correct"].mean()
highest_region = df.loc[df["MHVI_Correct"].idxmax(), "Region"]
lowest_region = df.loc[df["MHVI_Correct"].idxmin(), "Region"]
high_risk_count = len(df[df["Vulnerability_Category"].str.contains("High", case=False, na=False)])
low_risk_count = len(df[df["Vulnerability_Category"].str.contains("Low", case=False, na=False)])

# -----------------------------
# TITLE + KPI CARDS
# -----------------------------
st.title("🇬🇭 Maternal Health Vulnerability Index (MHVI) — Ghana")
st.markdown("### National Overview")

col1, col2, col3, col4 = st.columns(4)
col1.metric("National Avg MHVI", f"{national_avg:.3f}")
col2.metric("Highest Risk Region", highest_region.title())
col3.metric("High Risk Regions", high_risk_count)
col4.metric("Low Risk Regions", low_risk_count)

st.markdown("---")

# -----------------------------
# REGION SELECTOR
# -----------------------------
st.subheader("🔍 Regional Deep Dive")

selected_region = st.selectbox("Select a Region", sorted(df["Region"].tolist()))
region_data = df[df["Region"] == selected_region].iloc[0]

# -----------------------------
# TWO-COLUMN INSIGHT LAYOUT
# -----------------------------
col1, col2 = st.columns([1, 1])

with col1:
    st.markdown("### 📍 Region Profile")
    st.metric("MHVI Score", f"{region_data['MHVI_Correct']:.3f}")
    st.metric("Risk Category", region_data["Vulnerability_Category"])
    st.markdown("#### 🧠 Key Drivers")
    st.write(region_data["Top_Drivers_Improved"])

with col2:
    st.markdown("### 🌍 National Comparison")
    diff = region_data["MHVI_Correct"] - national_avg
    if diff > 0:
        st.error(f"⬆ Above national average by {diff:.3f}")
    else:
        st.success(f"⬇ Below national average by {abs(diff):.3f}")
    st.markdown("#### Interpretation")
    if diff > 0:
        st.write("This region shows **higher-than-average maternal vulnerability**, indicating urgent policy attention.")
    else:
        st.write("This region performs **better than the national average**, but still requires sustained investment.")

st.markdown("---")

# -----------------------------
# NATIONAL RANKING TABLE
# -----------------------------
st.subheader("📊 National Ranking (MHVI)")

ranked_df = df[["Region", "MHVI_Correct", "Vulnerability_Category", "Top_Drivers_Improved"]].sort_values(
    "MHVI_Correct", ascending=False
).reset_index(drop=True)

def highlight_selected(row):
    return [
        "background-color: #ffe066" if row["Region"] == selected_region else ""
        for _ in row
    ]

st.dataframe(
    ranked_df.style.apply(highlight_selected, axis=1),
    use_container_width=True
)

st.markdown("---")

# -----------------------------
# BAR CHART
# -----------------------------
st.subheader("📈 MHVI Comparison Across Regions")

bar_df = df[["Region", "MHVI_Correct"]].sort_values("MHVI_Correct", ascending=True)

fig_bar = px.bar(
    bar_df,
    x="Region",
    y="MHVI_Correct",
    color="MHVI_Correct",
    color_continuous_scale="Reds",
    labels={"MHVI_Correct": "MHVI Score", "Region": "Region"},
    title="MHVI Score by Region (Low to High)"
)

fig_bar.update_layout(
    xaxis_tickangle=-45,
    margin={"r": 0, "t": 40, "l": 0, "b": 80}
)

st.plotly_chart(fig_bar, use_container_width=True)

st.markdown("---")

# -----------------------------
# CHOROPLETH MAP (MAPBOX)
# -----------------------------
st.subheader("🗺️ Ghana Vulnerability Map")

fig_map = px.choropleth_mapbox(
    df,
    geojson=ghana_geojson,
    locations="Region_GEO",
    featureidkey="properties.shapeName",
    color="MHVI_Correct",
    color_continuous_scale="Reds",
    mapbox_style="white-bg",
    zoom=5.2,
    center={"lat": 7.9, "lon": -1.0},
    opacity=0.85,
    hover_name="Region_GEO",
    hover_data={
        "MHVI_Correct": ":.3f",
        "Vulnerability_Category": True,
        "Region_GEO": False
    },
    title="Ghana Maternal Health Vulnerability Index (MHVI)"
)

fig_map.update_layout(
    margin={"r": 0, "t": 40, "l": 0, "b": 0},
    height=600
)

st.plotly_chart(fig_map, use_container_width=True)

st.markdown("### 🧭 Interpretation Guide")
st.markdown("""
- 🔴 **High MHVI** → Urgent maternal health intervention required  
- 🟠 **Medium MHVI** → Strengthen healthcare access and staffing  
- 🟢 **Low MHVI** → Maintain current health system performance  
""")

st.markdown("---")

# -----------------------------
# SHAP EXPLAINABILITY
# -----------------------------
st.subheader("🧠 Explainability — What Is Driving Vulnerability?")

st.markdown("""
These charts show which indicators have the most influence on MHVI scores 
across Ghana's regions, using SHAP (SHapley Additive exPlanations) values 
from a Random Forest model trained on the regional data.
""")

col1, col2 = st.columns([1, 1])

with col1:
    st.markdown("#### National Feature Importance")
    st.markdown("Which indicators drive MHVI scores across all 16 regions.")
    shap_summary_path = BASE_DIR / "Maps" / "shap_summary.png"
    if shap_summary_path.exists():
        st.image(str(shap_summary_path), use_container_width=True)
    else:
        st.warning(f"SHAP summary plot not found at: {shap_summary_path}")

with col2:
    st.markdown("#### Upper East Region — Highest Risk")
    st.markdown("What specifically is driving Upper East's vulnerability score.")
    shap_ue_path = BASE_DIR / "Maps" / "shap_upper_east.png"
    if shap_ue_path.exists():
        st.image(str(shap_ue_path), use_container_width=True)
    else:
        st.warning(f"SHAP Upper East plot not found at: {shap_ue_path}")

st.markdown("---")
st.caption("MHVI Dashboard — Decision Support Tool for Maternal Health Planning in Ghana")