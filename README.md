<<<<<<< HEAD
# ❤️ Exploratory Data Analysis — Heart Disease Dataset
=======
# Heart Disease -> Exploratory Data Analysis
>>>>>>> bb959ab704609d95323fb50096021ea5eda6f012

Exploratory data analysis is where every good machine learning project begins. Before writing a single line of modelling code, understanding the data — its structure, quirks, distributions, and hidden relationships — is what separates models that generalise from models that fail silently. This project applies the full EDA toolkit to a real clinical dataset, building intuition for how medical data behaves and what signals are worth pursuing.

---

## 📌 Project Snapshot

| | |
|---|---|
| **Dataset** | UCI Heart Disease Dataset |
| **Records** | 1,025 patients |
| **Features** | 13 clinical and diagnostic attributes |
| **Target** | Presence of heart disease (binary) |
| **Libraries** | `pandas` · `matplotlib` · `seaborn` |

---

## 🗂️ The Dataset

The UCI Heart Disease dataset contains records from patients who underwent cardiac evaluation. Each record captures a mix of demographic, physiological, and diagnostic measurements collected before a formal diagnosis was made. The dataset is widely used as a benchmark for medical classification and has been studied extensively in the clinical ML literature.

**Feature breakdown:**
- **Demographic:** age, sex
- **Physiological:** resting blood pressure, serum cholesterol, fasting blood sugar, maximum heart rate
- **Diagnostic:** chest pain type, resting ECG results, exercise-induced angina, ST depression, slope of ST segment, number of major vessels coloured by fluoroscopy, thalassemia type

---

## 📊 Analysis Performed

<<<<<<< HEAD
**1. Data Quality Assessment**
Checked for missing values, impossible entries, and data type issues. Verified that all 13 features are present and complete across all 1,025 records.

**2. Target Distribution**
Plotted the balance between disease and no-disease classes. A balanced dataset (~50/50) means standard accuracy is a valid starting metric — unlike many real-world medical datasets where imbalance is severe.

**3. Univariate Analysis**
Built histograms for all continuous features (age, cholesterol, blood pressure, max heart rate, ST depression) to understand their distributions — checking for skewness, outliers, and whether the data is approximately normal or requires transformation.

**4. Bivariate Analysis**
Compared feature distributions between disease and no-disease groups using side-by-side box plots. This surfaces which features discriminate most clearly between the two groups before any modelling.

**5. Correlation Heatmap**
Computed Pearson correlations between all features and visualised as a colour-coded matrix. Revealed which features move together (potential multicollinearity) and which correlate most strongly with the target outcome.

**6. Categorical Feature Analysis**
Bar charts showing disease rates broken down by chest pain type, sex, fasting blood sugar, and ECG results. Categorical features can be highly predictive in ways that continuous correlations miss entirely.

**7. Pairplot**
A grid of scatter plots for every feature combination, coloured by disease status. The most informative single visualisation — immediately shows which feature pairs produce visible class separation.
=======
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
>>>>>>> bb959ab704609d95323fb50096021ea5eda6f012

---

## 📈 Visualisations Generated

| File | Description |
|------|-------------|
| `plot1_target_distribution.png` | Class balance — disease vs no disease |
| `plot2_age_distribution.png` | Age histograms split by outcome |
| `plot3_gender_distribution.png` | Disease rates by sex |
| `plot4_cholesterol_boxplot.png` | Cholesterol spread across outcome groups |
| `plot5_heartrate_boxplot.png` | Max heart rate by disease status |
| `plot6_correlation_heatmap.png` | Full feature correlation matrix |
| `plot7_chestpain_distribution.png` | Disease rate by chest pain type |
| `plot8_pairplot.png` | Multivariate scatter grid coloured by outcome |

---

## 🔍 Key Findings

**Strongest predictors** (by correlation and visual separation):
- `ca` — number of major vessels coloured by fluoroscopy. Directly measures arterial blockage. Strongest single predictor.
- `cp` — chest pain type. Counterintuitively, asymptomatic patients (type 0) show the highest disease rates — severe disease often presents silently.
- `thalach` — maximum heart rate. Patients *with* disease have *lower* maximum heart rates. A diseased heart cannot sustain high rates under exertion.

**Weaker than expected:**
- `chol` — serum cholesterol. Surprisingly weak predictor on its own. Total cholesterol is less clinically informative than LDL/HDL ratio, which is absent from this dataset. A good reminder that feature interpretation requires domain knowledge.

**Class balance:**
- 526 disease positive (~51%), 499 disease negative (~49%). Well balanced — accuracy is a reasonable metric here.

---

## 📂 Repository Structure

```
heart-disease-eda/
├── heart.csv
├── heart_eda.py
├── plot1_target_distribution.png
├── plot2_age_distribution.png
├── plot3_gender_distribution.png
├── plot4_cholesterol_boxplot.png
├── plot5_heartrate_boxplot.png
├── plot6_correlation_heatmap.png
├── plot7_chestpain_distribution.png
├── plot8_pairplot.png
└── README.md
```

---

## ⚙️ Setup

```bash
git clone https://github.com/Shaflovescoffee19/heart-disease-eda.git
cd heart-disease-eda
pip3 install pandas matplotlib seaborn
python3 heart_eda.py
```

---

## 📚 Skills Developed

- Loading, inspecting, and profiling real-world tabular datasets with `pandas`
- Reading and interpreting statistical summaries — mean, median, std, quartiles, and what each tells you
- Building histograms, box plots, count plots, heatmaps, and pairplots with `seaborn` and `matplotlib`
- Understanding Pearson correlation — what it measures, what it misses, and why visualisation cannot be replaced by summary statistics alone
- Translating data observations into domain-grounded hypotheses about which features drive outcomes

---

## 🗺️ Learning Roadmap

**Project 1 of 10** — a structured series building from data exploration through to advanced ML techniques.

| # | Project | Focus |
|---|---------|-------|
| 1 | **Heart Disease EDA** ← | Exploratory analysis, visualisation |
| 2 | Diabetes Data Cleaning | Missing data, outliers, feature engineering |
| 3 | Cancer Risk Classification | Supervised learning, model comparison |
| 4 | Survival Analysis | Time-to-event modelling, Cox regression |
| 5 | Customer Segmentation | Clustering, unsupervised learning |
| 6 | Gene Expression Clustering | High-dimensional data, heatmaps |
| 7 | Explainable AI with SHAP | Model interpretability |
| 8 | Counterfactual Explanations | Actionable predictions |
| 9 | Multi-Modal Data Fusion | Stacking, ensemble methods |
| 10 | Transfer Learning | Neural networks, domain adaptation |
