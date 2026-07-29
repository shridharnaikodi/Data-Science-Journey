# Day 4 — Data Distribution, Outlier Detection & Preprocessing

## Topics Covered
- **Descriptive Statistics recap:** the 7-step EDA checklist (distribution → inappropriate data → outliers → categorical → missing values → ordinal → associations)
- **Measures of Central Tendency**
  - Mean — sum of all values ÷ count, applicable only to numerical columns
  - Median — middle value after sorting; odd-count vs even-count position formulas
  - Mode — most frequent value; applicable to numerical, categorical, and ordinal data; tie-breaking rule (sort tied values ascending, take the first)
- **Data Distribution**
  - Normal/Gaussian Distribution (bell curve) — mean ≈ median ≈ mode, indicates a well-generalized column that represents the population
  - Skewed Distribution — right-skew vs left-skew, tails indicate outliers/extreme values
- **Quartiles (Q1–Q4)** — dividing a dataset into 4 equal parts (25/50/75/100%), with step-by-step manual calculation for both odd- and even-length datasets
- **Outlier Detection — Tukey's Method (1.5 × IQR Rule)**
  - IQR = Q3 − Q1
  - Lower Range = Q1 − (1.5 × IQR), Upper Range = Q3 + (1.5 × IQR)
  - Any value outside this range is flagged as an outlier
- **Missing Value Handling (Data Preprocessing)**
  - Statistical approach: mode for categorical columns, median/mean for numerical columns depending on skew
  - Practical use of `.isna().sum()`, `.value_counts()`, and `.fillna()`

## Practical Work
- `1_Data_Distribution_and_Outlier_Detection.ipynb` — builds a salary dataset with a planted extreme outlier, visualizes distribution with `sns.displot(kind='kde')`, computes quartiles via NumPy/Pandas, applies Tukey's 1.5×IQR rule to detect and remove the outlier, then compares the mean/distribution before vs after cleaning
- `2_Data_Preprocessing_Techniques.ipynb` — works on `sample_data/preprocessExample.csv` to detect missing values (`Country`, `Age`, `Salary` columns), checks distribution shape to decide mean vs median, and fills missing values using the statistically appropriate method

## Key Takeaway
> A dataset column that forms a near-perfect bell curve is likely a **generalized column** — high probability it faithfully represents the population. Outliers distort this shape and must be detected (Tukey's Method) before trusting mean-based statistics.