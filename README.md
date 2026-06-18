# Maternal Health Vulnerability Index (MHVI) — Ghana

> **Where does a Ghanaian woman stand the best chance of surviving motherhood?**
>
> This project answers that question with data.

The MHVI is a machine learning-powered vulnerability index that scores and maps maternal health risk across all 16 regions of Ghana using the 2022 Demographic and Health Survey. It combines 16 indicators across 5 health domains into a single interpretable score — then uses SHAP explainability to show exactly *why* each region scores the way it does.

Built by a nursing graduate who has worked in maternal health settings in Ghana and believes data should directly improve outcomes for women.

---

## The Problem

Ghana has made measurable progress on maternal health. But national averages hide a deeper regional inequality: the difference between Upper East and Ahafo is not minor — it is structural.

Without precise measurement, policy remains generic and resources are misallocated.

---

## Live Dashboard

**👉 [View the MHVI Dashboard](https://maternal-health-risk-platform-kdrmxelbnhdsyrkzvrzqwk.streamlit.app/)**

No login required — open, select a region, and explore maternal vulnerability across Ghana.

---

## Key Findings

| Metric | Value |
|---|---|
| 🇬🇭 National Average MHVI | **0.404** |
| 🔴 Highest Vulnerability | **Upper East — 0.86** |
| 🟢 Lowest Vulnerability | **Ahafo — 0.18** |
| High-Risk Regions | **4** |
| Low-Risk Regions | **5** |

The difference between the highest and lowest regions is **0.68 index points** — reflecting a severe structural inequality gap, not a smooth distribution.

---

## Dashboard Sections

| Section | Function |
|---|---|
| KPI Cards | National overview — average MHVI, risk counts, and extremes |
| Regional Deep Dive | Region-specific indicators with contextual interpretation |
| National Comparison | Side-by-side ranking of all 16 regions |
| Choropleth Map | Geographic visualisation of vulnerability across Ghana |
| Ranking Table | Full sortable MHVI table |
| SHAP Global Importance | Key drivers of maternal vulnerability at the national level |
| SHAP Local Explanations | Why a specific region scores high or low |

SHAP transforms the model from a black box into a policy tool — explaining *why* vulnerability exists, not just where it exists.

---

## Methodology

### Data Source
Ghana Demographic and Health Survey (DHS) 2022 — StatCompiler

### Dataset
- 16 regional observations
- 16 maternal health indicators
- 5 health domains

### Indicator Domains
1. Antenatal care coverage
2. Skilled birth attendance
3. Postnatal care utilisation
4. Contraceptive prevalence
5. Child health and nutrition proxies

### Model
- **Algorithm:** Random Forest (selected for stability on small regional datasets)
- **Output:** Composite MHVI score (normalised index, 0–1)
- **Explainability:** SHAP — global feature importance and regional waterfall charts

### Tech Stack
`Python` · `Streamlit` · `Pandas` · `Scikit-learn` · `SHAP` · `Plotly` · `GeoJSON`

---

## Project Structure
maternal-health-risk-platform/

│

├── Dashboard/

│   └── app.py

│

├── Data/

│   ├── Raw/

│   ├── Processed/

│   │   ├── mhvi_processed.csv

│   │   └── final_results_mhvi.csv

│   └── geo/

│       └── ghana_regions.geojson

│

├── Maps/

├── Notebooks/

├── Policy_brief/

├── Reports/

└── README.md
---

## Getting Started

**Clone the repository:**
```bash
git clone https://github.com/emmanuella-danso/maternal-health-risk-platform.git
cd maternal-health-risk-platform
```

**Install dependencies:**
```bash
pip install -r requirements.txt
```

**Run the app:**
```bash
streamlit run Dashboard/app.py
```

---

## Policy Brief

A policy brief is included in the repository, designed for the Ghana Health Service and regional health directors. It translates MHVI scores into actionable regional recommendations.

---

## Why This Project Exists

I am a nursing graduate from the University for Development Studies, Ghana. I have worked in clinical settings and seen firsthand how resource distribution affects maternal outcomes.

Most maternal health reporting focuses on national averages, which hide regional disparities. This project shows what happens when we disaggregate that data and make inequality visible.

---

## Author

**Emmanuella Danso**  
· Health Data Scientist · Ghana

[![GitHub](https://img.shields.io/badge/GitHub-emmanuella--danso-181717?logo=github)](https://github.com/emmanuella-danso)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Emmanuella%20Danso-0A66C2?logo=linkedin)](https://www.linkedin.com/in/emmanuella-danso-699b54404/)

---

## License

MIT License — free to use with attribution.

*Built in Ghana. For Ghana.*
