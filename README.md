\# Maternal Health Vulnerability Index (MHVI) — Ghana

\### \*Where does a Ghanaian woman stand the best chance of surviving motherhood?\*



This project answers that question with data.



The MHVI is a machine learning-powered vulnerability index that scores and maps maternal health risk across all 16 regions of Ghana using the 2022 Demographic and Health Survey. It combines 16 indicators across 5 health domains into a single interpretable score — then uses SHAP explainability to show exactly \*why\* each region scores the way it does.



Built by a nursing graduate who has sat beside women in labour in Ghana's health facilities and decided that data should do more for them than it currently does.



\---



\## 🔴 The Problem



Ghana has made measurable progress on maternal health. But national averages hide a brutal geographic truth: the gap between a woman's chances in Upper East and her chances in Ahafo is not a small statistical variation. It is a structural emergency.



Without a tool that names that gap precisely, policy stays generic. Resources get distributed by assumption. Women pay the cost.



\---



\## 🟢 Live Dashboard



\*\*\[→ View the MHVI Dashboard](http://localhost:8501/)\*\*



No login. No setup. Open it, select a region, see the risk profile.



\---



\## Key Findings



| | |

|---|---|

| 🇬🇭 National Average MHVI | \*\*0.404\*\* |

| 🔴 Highest Vulnerability | \*\*Upper East — 0.86\*\* |

| 🟢 Lowest Vulnerability | \*\*Ahafo — 0.18\*\* |

| High-Risk Regions | \*\*4\*\* |

| Low-Risk Regions | \*\*5\*\* |



The difference between the highest and lowest scoring region is \*\*0.68 index points\*\* — nearly the entire range of the scale. This is not a gradient. This is a divide.



\---



\## What the Dashboard Does



| Section | What It Shows |

|---|---|

| \*\*KPI Cards\*\* | National snapshot — average MHVI, high-risk count, regional range |

| \*\*Regional Deep Dive\*\* | Every indicator for any selected region, scored and contextualised |

| \*\*National Comparison\*\* | All 16 regions ranked side by side |

| \*\*Choropleth Map\*\* | Geographic heatmap — vulnerability made visible on Ghana's map |

| \*\*Ranking Table\*\* | Sortable full-region vulnerability table |

| \*\*SHAP Feature Importance\*\* | Which indicators drive national vulnerability most |

| \*\*SHAP Waterfall Chart\*\* | Region-level explanation — exactly what pushed that score up or down |



The SHAP section is what separates this from a static report. It does not just say Upper East is high risk. It shows \*which indicators are responsible\* and \*by how much\* — giving health planners an actionable entry point, not just a red colour on a map.



\---



\## Methodology



\### Data

\*\*Ghana Demographic and Health Survey (DHS) 2022\*\* via DHS StatCompiler

\- 16 regional observations

\- 16 indicators selected across 5 maternal health domains



\### Indicator Domains

1\. Antenatal care coverage

2\. Skilled birth attendance

3\. Postnatal care utilisation

4\. Contraceptive prevalence

5\. Child nutrition and mortality proxies



\### Model

\- \*\*Algorithm:\*\* Random Forest — chosen for robustness on small regional datasets and compatibility with SHAP explainability

\- \*\*Index Construction:\*\* Composite weighted scoring normalised across all 16 regions

\- \*\*Explainability:\*\* SHAP (SHapley Additive exPlanations) — both global feature importance and per-region waterfall decomposition



\### Technical Stack

`Python` · `Streamlit` · `Scikit-learn` · `SHAP` · `Plotly` · `Pandas` · `GeoJSON` · `Random Forest`



\---



\## Project Structure

maternal-health-risk-platform/



│



├── dashboard/



│   └── app.py                   # Full Streamlit application



│



├── data/



│   ├── raw/                     # Original DHS StatCompiler exports



│   ├── processed/               # mhvi\_processed.csv — clean, analysis-ready



│   └── geo/                     # Ghana regional GeoJSON (16 regions)



│



├── maps/                        # SHAP visualisation exports (.png)



├── notebooks/                   # Full analysis pipeline (Jupyter)



├── policy\_brief/                # Policy brief · 



└── README.md



├── report/



\---



\## Run It Locally



```bash

git clone https://github.com/emmanuella-danso/maternal-health-vulnerability-index.git

cd maternal-health-vulnerability-index

pip install -r requirements.txt

streamlit run dashboard/app.py

```



\---



\## Policy Brief



A plain-language policy brief is included in `/docs/` — written for Ghana Health Service and regional health directorates, not data scientists. It translates index scores into specific, actionable resource allocation recommendations by region.



\---



\## Why This Project Exists



I am a nursing graduate from the University for Development Studies, Ghana. I have worked in health facilities in this country. I know what it looks like when a system is under-resourced in the wrong places.



Health data science in Ghana is not yet doing the work it could do. Most maternal health reporting stops at national averages. Interventions get designed at the aggregate level, for an average Ghanaian woman who does not exist, while the women in Upper East, Northern, and Savannah regions carry a disproportionate burden that the average actively conceals.



This project is my argument that data, when built with clinical context and deployed with clarity, can change that.



\---



\## Author



\*\*Emmanuella Danso\*\*

Nursing Graduate · Health Data Scientist

&#x20;Ghana



\[GitHub](https://github.com/emmanuella-danso) · 



\[LinkedIn](https://www.linkedin.com/in/emmanuella-danso-699b54404/)



\---



\## License



MIT — free to use, adapt, and build on with attribution.



\---



\*Built in Ghana. For Ghana.\*

