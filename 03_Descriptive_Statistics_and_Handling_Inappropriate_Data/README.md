# Day 3 — Descriptive Statistics & Handling Inappropriate Data

## Topics Covered
- Dataset, Population, and Sample — and why a "sample" must represent the population's distribution
- Descriptive vs Inferential Statistics (70% / 30% split in typical workflows)
- Types of data columns: Numerical (Continuous/Discrete), Categorical, Ordinal, Pure String
- Types of variables: Qualitative vs Quantitative
- Roles in a data team: Data Analyst, Business Analyst, Data Artist, Domain Expert, Data Scientist
- Descriptive Statistics workflow (EDA phase):
  1. Check distribution of numerical columns
  2. Identify & handle inappropriate data
  3. Identify & handle outliers
  4. Identify & handle categorical data
  5. Identify & handle missing values
  6. Identify & handle ordinal data
  7. Discover associations/relationships/patterns between variables
- Internal vs External dataset procurement

## Practical Work
`1_Handling_Inappropriate_Data.ipynb` walks through a real messy hotel-feedback dataset (`sample_data/datasetExample.csv`) and applies a step-by-step guideline to:
- Remove duplicate records and duplicate columns
- Validate numerical columns against domain rules (sign, decimals, range)
- Normalize categorical data (case, spelling, formatting errors)
- Flag invalid entries as NaN instead of deleting rows outright

## Practice
`practice/` contains a self-made assignment applying all Day 3 concepts on a fresh, messier dataset (`inappropriate_data_dataset_50_records.csv` — 50 records with duplicate rows, a duplicate column, invalid ages/income/credit scores, and inconsistent categorical spellings/casing).

- `practice_questions.md` — 12 practice questions covering the full "Handling Inappropriate Data" checklist
- `inappropriate_data_practice_solution.ipynb` — worked solutions, one code cell per question, with domain-assumption comments explaining every cleaning decision (valid ranges, whether to NaN vs. drop, category unification)

