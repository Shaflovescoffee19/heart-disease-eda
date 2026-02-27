# Heart Disease -> Exploratory Data Analysis

Before building any model, you need to actually understand what you're working with. This project is about that step. EDA gets skipped or rushed in most tutorials and it shows up later as models that fail in confusing ways. I wanted to do it properly on a real clinical dataset and build the habit of knowing my data before touching a model.

---

## Project Snapshot

| | |
|---|---|
| **Dataset** | UCI Heart Disease Dataset |
| **Records** | 1,025 patients |
| **Features** | 13 clinical and diagnostic attributes |
| **Target** | Presence of heart disease (binary) |
| **Libraries** | `pandas`, `matplotlib`, `seaborn` |

---

## The Dataset

The UCI Heart Disease dataset contains records from patients who went through cardiac evaluation. Each record has a mix of demographic, physiological, and diagnostic measurements taken before a formal diagnosis. Features include age, sex, resting blood pressure, serum cholesterol, fasting blood sugar, maximum heart rate, chest pain type, ECG results, exercise-induced angina, ST depression, number of major vessels coloured by fluoroscopy, and thalassemia type.

---

## What I Did

## **Data quality check**
### Checked for missing values, impossible entries, and data type issues. All 13 features are present and complete across all 1,025 records, which is unusual for a medical dataset.

## **Target distribution**
### Plotted the class balance. About 50/50 between disease and no disease, which means accuracy is actually a valid metric here unlike most real-world medical datasets.

## **Univariate analysis**
### Histograms for all continuous features to understand distributions. Checking for skew, outliers, whether anything looks unusual before comparing across groups.

## **Bivariate analysis**
### Side-by-side box plots comparing feature distributions between disease and no-disease groups. This is where you start to see which features actually separate the two groups.

## **Correlation heatmap**
### Pearson correlations between all features visualised as a colour matrix. Useful for spotting which features move together and which correlate most with the outcome.

## **Categorical features**
### Bar charts showing disease rates by chest pain type, sex, fasting blood sugar, and ECG results. Categorical features can be highly predictive in ways that continuous correlations miss completely.

## **Pairplot**
### Scatter plots for every feature combination coloured by disease status. The most informative single visualisation in the whole project.

---

## Visualisations

| File | What it shows |
|------|---------------|
| `plot1_target_distribution.png` | Class balance |
| `plot2_age_distribution.png` | Age split by outcome |
| `plot3_gender_distribution.png` | Disease rates by sex |
| `plot4_cholesterol_boxplot.png` | Cholesterol across outcome groups |
| `plot5_heartrate_boxplot.png` | Max heart rate by disease status |
| `plot6_correlation_heatmap.png` | Full feature correlation matrix |
| `plot7_chestpain_distribution.png` | Disease rate by chest pain type |
| `plot8_pairplot.png` | Multivariate scatter grid |

---

## Key Findings

`ca` (number of major vessels) turned out to be the strongest predictor. It directly measures arterial blockage so that makes sense clinically.

`thalach` (maximum heart rate) was interesting. Patients with disease actually have lower maximum heart rates. A diseased heart cannot sustain high rates under exertion, so the direction of the relationship is counterintuitive until you think about the biology.

`cp` (chest pain type) was surprising. Asymptomatic patients showed the highest disease rates. Severe disease often presents silently, which is a well-known clinical problem.

`chol` (cholesterol) was weaker than I expected. Total cholesterol is less clinically informative than LDL/HDL ratio, which is not in this dataset. A good reminder that you need domain knowledge to interpret feature importance correctly.

---

## Setup

```bash
git clone https://github.com/Shaflovescoffee19/heart-disease-eda.git
cd heart-disease-eda
pip3 install pandas matplotlib seaborn
python3 heart_eda.py
```

---

## What I Learned

- How to properly profile a dataset before modelling
- Reading statistical summaries and knowing what each one tells you and what it misses
- Building histograms, box plots, heatmaps, and pairplots and actually interpreting them
- Why visualisation cannot be replaced by summary statistics alone
- How domain knowledge changes the way you read feature importance

---

## Part of a 10-Project Series

| # | Project | Focus |
|---|---------|-------|
| 1 | **Heart Disease EDA** | Exploratory analysis, visualisation |
| 2 | Diabetes Data Cleaning | Missing data, outliers, feature engineering |
| 3 | Cancer Risk Classification | Supervised learning, model comparison |
| 4 | Survival Analysis | Time-to-event modelling, Cox regression |
| 5 | Customer Segmentation | Clustering, unsupervised learning |
| 6 | Gene Expression Clustering | High-dimensional data, heatmaps |
| 7 | Explainable AI with SHAP | Model interpretability |
| 8 | Counterfactual Explanations | Actionable predictions |
| 9 | Multi-Modal Data Fusion | Stacking, ensemble methods |
| 10 | Transfer Learning | Neural networks, domain adaptation |
