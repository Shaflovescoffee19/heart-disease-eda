# ============================================================
# PROJECT 1: Heart Disease - Exploratory Data Analysis (EDA)
# ============================================================
# WHAT THIS SCRIPT DOES (step by step):
#   1. Loads the dataset
#   2. Explores its basic structure
#   3. Cleans missing/bad values
#   4. Visualizes distributions and patterns
#   5. Builds a correlation heatmap
#   6. Saves all charts as image files
# ============================================================

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ── Visual style ──────────────────────────────────────────
sns.set_theme(style="whitegrid")
plt.rcParams["figure.dpi"] = 150

# ===========================================================
# STEP 1: LOAD THE DATA
# ===========================================================
# pd.read_csv() reads a CSV file and turns it into a
# DataFrame — think of it as a Python Excel table.

df = pd.read_csv("heart.csv")

print("=" * 55)
print("STEP 1: LOADING THE DATA")
print("=" * 55)
print(f"Rows    : {df.shape[0]}")   # number of patients
print(f"Columns : {df.shape[1]}")   # number of features
print()

# ===========================================================
# STEP 2: UNDERSTAND THE COLUMNS
# ===========================================================
# Each column represents one piece of patient information.
# Here is what every column means:
#
#   age      - Patient age in years
#   sex      - 1 = Male, 0 = Female
#   cp       - Chest pain type (0-3, higher = more severe)
#   trestbps - Resting blood pressure (mm Hg)
#   chol     - Serum cholesterol (mg/dl)
#   fbs      - Fasting blood sugar > 120 mg/dl (1 = True)
#   restecg  - Resting ECG results (0, 1, 2)
#   thalach  - Maximum heart rate achieved
#   exang    - Exercise induced angina (1 = Yes)
#   oldpeak  - ST depression induced by exercise
#   slope    - Slope of peak exercise ST segment (0-2)
#   ca       - Number of major vessels colored by fluoroscopy
#   thal     - Thalassemia type (0-3)
#   target   - 0 = No Heart Disease, 1 = Heart Disease ← THIS IS WHAT WE PREDICT

print("=" * 55)
print("STEP 2: COLUMN NAMES AND DATA TYPES")
print("=" * 55)
print(df.dtypes)
print()

# ===========================================================
# STEP 3: EXPLORE THE DATA
# ===========================================================
# .describe() gives you count, mean, min, max for every column.
# This is the first thing any data scientist does with a
# new dataset — get a feel for the numbers.

print("=" * 55)
print("STEP 3: STATISTICAL SUMMARY")
print("=" * 55)
print(df.describe().round(2))
print()

# ===========================================================
# STEP 4: CHECK FOR MISSING VALUES
# ===========================================================
# Missing values break ML models. We check every column
# for nulls (empty cells). If count is 0 — we're clean.

print("=" * 55)
print("STEP 4: MISSING VALUES PER COLUMN")
print("=" * 55)
missing = df.isnull().sum()
print(missing)
print()
if missing.sum() == 0:
    print("  No missing values found! Dataset is clean.")
else:
    print("  Missing values detected — filling with column median.")
    df.fillna(df.median(), inplace=True)
print()

# ===========================================================
# STEP 5: TARGET DISTRIBUTION
# ===========================================================
# How many patients have heart disease vs don't?
# A heavily imbalanced dataset (e.g. 95% No, 5% Yes) would
# make modeling tricky. Let's check.

print("=" * 55)
print("STEP 5: TARGET DISTRIBUTION")
print("=" * 55)
counts = df["target"].value_counts()
print(f"  No Heart Disease (0) : {counts[0]} patients")
print(f"  Heart Disease    (1) : {counts[1]} patients")
print()

fig, ax = plt.subplots(figsize=(6, 4))
sns.countplot(x="target", data=df, palette=["#4C72B0", "#DD8452"], ax=ax)
ax.set_title("Heart Disease Distribution", fontsize=14, fontweight="bold")
ax.set_xlabel("Target (0 = No Disease, 1 = Disease)")
ax.set_ylabel("Number of Patients")
ax.set_xticks([0, 1])
ax.set_xticklabels(["No Disease", "Heart Disease"])
for p in ax.patches:
    ax.annotate(f'{int(p.get_height())}',
                (p.get_x() + p.get_width() / 2., p.get_height()),
                ha='center', va='bottom', fontsize=12)
plt.tight_layout()
plt.savefig("plot1_target_distribution.png")
plt.close()
print("  Saved: plot1_target_distribution.png")

# ===========================================================
# STEP 6: AGE DISTRIBUTION
# ===========================================================
# A histogram shows how age is spread across all patients.
# We split by disease status to see if older patients are
# more at risk — which is what we'd medically expect.

fig, ax = plt.subplots(figsize=(8, 5))
sns.histplot(data=df, x="age", hue="target", bins=20,
             palette=["#4C72B0", "#DD8452"], kde=True, ax=ax)
ax.set_title("Age Distribution by Heart Disease Status", fontsize=14, fontweight="bold")
ax.set_xlabel("Age (years)")
ax.set_ylabel("Number of Patients")
ax.legend(title="Target", labels=["No Disease", "Heart Disease"])
plt.tight_layout()
plt.savefig("plot2_age_distribution.png")
plt.close()
print("  Saved: plot2_age_distribution.png")

# ===========================================================
# STEP 7: GENDER vs HEART DISEASE
# ===========================================================
# Bar chart showing how many males vs females have
# heart disease. Sex is encoded as 1 = Male, 0 = Female.

fig, ax = plt.subplots(figsize=(6, 4))
sns.countplot(x="sex", hue="target", data=df,
              palette=["#4C72B0", "#DD8452"], ax=ax)
ax.set_title("Heart Disease by Gender", fontsize=14, fontweight="bold")
ax.set_xlabel("Sex (0 = Female, 1 = Male)")
ax.set_ylabel("Number of Patients")
ax.legend(title="Target", labels=["No Disease", "Heart Disease"])
plt.tight_layout()
plt.savefig("plot3_gender_distribution.png")
plt.close()
print("  Saved: plot3_gender_distribution.png")

# ===========================================================
# STEP 8: CHOLESTEROL vs HEART DISEASE
# ===========================================================
# Box plot: shows the median, spread, and outliers of
# cholesterol for disease vs no-disease patients.
# If the boxes are at very different heights, cholesterol
# is a useful predictor.

fig, ax = plt.subplots(figsize=(6, 5))
sns.boxplot(x="target", y="chol", data=df,
            palette=["#4C72B0", "#DD8452"], ax=ax)
ax.set_title("Cholesterol Levels by Heart Disease Status", fontsize=14, fontweight="bold")
ax.set_xlabel("Target (0 = No Disease, 1 = Disease)")
ax.set_ylabel("Cholesterol (mg/dl)")
ax.set_xticks([0, 1])
ax.set_xticklabels(["No Disease", "Heart Disease"])
plt.tight_layout()
plt.savefig("plot4_cholesterol_boxplot.png")
plt.close()
print("  Saved: plot4_cholesterol_boxplot.png")

# ===========================================================
# STEP 9: MAX HEART RATE vs HEART DISEASE
# ===========================================================
# thalach = maximum heart rate achieved during stress test.
# Counterintuitively, LOWER max heart rate often indicates
# heart disease — the heart can't work as hard.

fig, ax = plt.subplots(figsize=(6, 5))
sns.boxplot(x="target", y="thalach", data=df,
            palette=["#4C72B0", "#DD8452"], ax=ax)
ax.set_title("Max Heart Rate by Heart Disease Status", fontsize=14, fontweight="bold")
ax.set_xlabel("Target (0 = No Disease, 1 = Disease)")
ax.set_ylabel("Max Heart Rate (bpm)")
ax.set_xticks([0, 1])
ax.set_xticklabels(["No Disease", "Heart Disease"])
plt.tight_layout()
plt.savefig("plot5_heartrate_boxplot.png")
plt.close()
print("  Saved: plot5_heartrate_boxplot.png")

# ===========================================================
# STEP 10: CORRELATION HEATMAP
# ===========================================================
# Correlation tells us how much two features move together.
# Values close to +1 or -1 mean strong relationship.
# Values close to 0 mean no relationship.
#
# The heatmap color-codes every pair of columns so you can
# instantly spot which features are related to the target.
# This is critical in your research proposal — it tells
# you which variants/features are worth including in models.

print()
print("=" * 55)
print("STEP 10: CORRELATION WITH TARGET (Heart Disease)")
print("=" * 55)
correlations = df.corr()["target"].sort_values(ascending=False)
print(correlations.round(3))
print()
print("  Interpretation:")
print("  Positive value = feature increases with heart disease risk")
print("  Negative value = feature decreases with heart disease risk")
print("  Closer to 1 or -1 = stronger relationship")

fig, ax = plt.subplots(figsize=(12, 9))
sns.heatmap(df.corr().round(2), annot=True, fmt=".2f",
            cmap="coolwarm", center=0,
            linewidths=0.5, ax=ax)
ax.set_title("Correlation Heatmap — All Features", fontsize=15, fontweight="bold")
plt.tight_layout()
plt.savefig("plot6_correlation_heatmap.png")
plt.close()
print("  Saved: plot6_correlation_heatmap.png")

# ===========================================================
# STEP 11: CHEST PAIN TYPE vs HEART DISEASE
# ===========================================================
# cp = chest pain type (0-3). Type 0 is asymptomatic
# (no pain), which is actually most associated with disease.
# This is a great example of a counterintuitive finding
# that only EDA reveals.

fig, ax = plt.subplots(figsize=(7, 5))
sns.countplot(x="cp", hue="target", data=df,
              palette=["#4C72B0", "#DD8452"], ax=ax)
ax.set_title("Chest Pain Type vs Heart Disease", fontsize=14, fontweight="bold")
ax.set_xlabel("Chest Pain Type (0=Asymptomatic, 1=Atypical, 2=Non-anginal, 3=Typical)")
ax.set_ylabel("Number of Patients")
ax.legend(title="Target", labels=["No Disease", "Heart Disease"])
plt.tight_layout()
plt.savefig("plot7_chestpain_distribution.png")
plt.close()
print("  Saved: plot7_chestpain_distribution.png")

# ===========================================================
# STEP 12: PAIRPLOT — THE BIG PICTURE
# ===========================================================
# A pairplot shows scatter plots for every pair of key
# features, colored by disease status. It's the single
# most informative visualization in EDA — you can spot
# clusters, separations, and patterns all at once.

print()
print("  Building pairplot (this takes ~10 seconds)...")
key_features = ["age", "chol", "thalach", "oldpeak", "target"]
pair = sns.pairplot(df[key_features], hue="target",
                    palette=["#4C72B0", "#DD8452"],
                    plot_kws={"alpha": 0.5})
pair.fig.suptitle("Pairplot of Key Features", y=1.02,
                  fontsize=14, fontweight="bold")
pair.fig.savefig("plot8_pairplot.png", bbox_inches="tight")
plt.close()
print("  Saved: plot8_pairplot.png")

# ===========================================================
# FINAL SUMMARY
# ===========================================================
print()
print("=" * 55)
print("EDA COMPLETE — KEY FINDINGS SUMMARY")
print("=" * 55)
print(f"  Total patients analysed : {len(df)}")
print(f"  Heart disease cases     : {df['target'].sum()} ({df['target'].mean()*100:.1f}%)")
print(f"  Average patient age     : {df['age'].mean():.1f} years")
print(f"  Average cholesterol     : {df['chol'].mean():.1f} mg/dl")
print(f"  Average max heart rate  : {df['thalach'].mean():.1f} bpm")
print()
print("  Top 3 features correlated with heart disease:")
top3 = df.corr()["target"].drop("target").abs().sort_values(ascending=False).head(3)
for i, (feat, val) in enumerate(top3.items(), 1):
    print(f"    {i}. {feat} (correlation: {val:.3f})")
print()
print("  8 plots saved in your project folder.")
print("  Push everything to GitHub when ready!")
print("=" * 55)
