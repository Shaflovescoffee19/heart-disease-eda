# ❤️ Heart Disease — Exploratory Data Analysis (EDA)

A beginner Machine Learning project performing full Exploratory Data Analysis on the UCI Heart Disease dataset. This is **Project 1 of 10** in my ML learning roadmap toward computational biology research.

---

## 📌 Project Overview

| Feature | Details |
|---|---|
| Dataset | UCI Heart Disease Dataset |
| Patients | 1,025 records |
| Features | 13 medical attributes |
| Target | Heart Disease (0 = No, 1 = Yes) |
| Techniques | EDA, Statistical Analysis, Data Visualization |
| Libraries | `pandas`, `matplotlib`, `seaborn` |

---

## 🧠 What Is EDA and Why Does It Matter?

Before building any Machine Learning model, you must first **understand your data**. EDA is the process of:
- Checking the structure and quality of the data
- Finding and handling missing values
- Understanding distributions of each feature
- Discovering which features are related to the target outcome

In my research roadmap, this skill directly maps to **Aim 1 of a computational biology research proposal** on colorectal cancer risk prediction — where genomic and clinical data must be explored and cleaned before any ML model can be built.

---

## 📊 Visualizations Generated

| Plot | What It Shows |
|---|---|
| Target Distribution | Balance of disease vs no-disease patients |
| Age Distribution | Age spread by disease status |
| Gender Distribution | Heart disease rates by sex |
| Cholesterol Box Plot | Cholesterol spread across disease groups |
| Max Heart Rate Box Plot | Heart rate differences between groups |
| Correlation Heatmap | Which features relate most to heart disease |
| Chest Pain Distribution | Disease rates by chest pain type |
| Pairplot | All key features plotted against each other |

---

## 🔍 Key Findings

- The dataset is well balanced (~50% disease, ~50% no disease)
- **cp** (chest pain type), **thalach** (max heart rate), and **ca** (vessel count) are the strongest predictors
- Patients **with** heart disease tend to have **lower** max heart rates — counterintuitive but medically meaningful
- Males show higher rates of heart disease in this dataset
- Cholesterol alone is a weaker predictor than expected

---

## 📂 Project Structure

```
heart-disease-eda/
├── heart.csv                        # Dataset
├── heart_eda.py                     # Main EDA script
├── plot1_target_distribution.png    # Disease balance chart
├── plot2_age_distribution.png       # Age histogram
├── plot3_gender_distribution.png    # Gender bar chart
├── plot4_cholesterol_boxplot.png    # Cholesterol box plot
├── plot5_heartrate_boxplot.png      # Heart rate box plot
├── plot6_correlation_heatmap.png    # Correlation heatmap
├── plot7_chestpain_distribution.png # Chest pain chart
├── plot8_pairplot.png               # Full pairplot
└── README.md                        # This file
```

---

## ⚙️ Setup Instructions

**1. Clone the repository**
```bash
git clone https://github.com/Shaflovescoffee19/heart-disease-eda.git
cd heart-disease-eda
```

**2. Install dependencies**
```bash
pip3 install pandas matplotlib seaborn
```

**3. Run the analysis**
```bash
python3 heart_eda.py
```

---

## 📚 What I Learned

- How to load and inspect a real medical dataset using **pandas**
- How to detect and handle missing values
- How to read and interpret statistical summaries (mean, std, quartiles)
- How to build histograms, box plots, bar charts, and heatmaps using **seaborn**
- What **correlation** means and how to use a heatmap to spot important features
- How to identify which features are most predictive of a medical outcome

---

## 🗺️ Part of My ML Learning Roadmap

This is **Project 1 of 10** in a structured roadmap building toward computational biology and precision oncology research.

| # | Project | Status |
|---|---|---|
| 1 | Heart Disease EDA | ✅ Complete |
| 2 | Diabetes Data Cleaning | 🔜 Next |
| 3 | Cancer Risk Classification | ⏳ Upcoming |
| 4 | Survival Analysis | ⏳ Upcoming |
| 5 | Customer Segmentation | ⏳ Upcoming |
| 6 | Gene Expression Clustering | ⏳ Upcoming |
| 7 | Explainable AI with SHAP | ⏳ Upcoming |
| 8 | Counterfactual Explanations | ⏳ Upcoming |
| 9 | Multi-Modal Data Fusion | ⏳ Upcoming |
| 10 | Transfer Learning | ⏳ Upcoming |

---

## 🙋 Author

**Shaflovescoffee19** — building ML skills from scratch toward computational biology research.
