# AAL Apparel Sales Analysis — Q4 2020 🇦🇺

Exploratory data analysis on a quarter of retail transactions for an Australian apparel brand (AAL), built to answer a real business question: **which states, demographics, and time slots drive revenue — and where should the company focus next?**

![Python](https://img.shields.io/badge/Python-3.11-blue)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Wrangling-150458)
![Seaborn](https://img.shields.io/badge/Seaborn-Visualization-4c72b0)
![Status](https://img.shields.io/badge/Status-Complete-brightgreen)

## Problem Statement

AAL has stores across multiple Australian states. The Head of Sales & Marketing needs a data-driven breakdown of Q4 2020 (Oct–Dec) sales to:
1. Identify the highest- and lowest-revenue states
2. Understand demand by demographic group (Kids / Men / Women / Seniors) and time of day
3. Recommend where to focus FY2021 sales & marketing effort

## Dataset

- **Source:** `AusApparalSales4thQrt2020.csv`
- **Size:** 7,560 transactions
- **Columns:** `Date`, `Time` (Morning/Afternoon/Evening), `State`, `Group`, `Unit`, `Sales`
- **Period:** 1 Oct 2020 – 30 Dec 2020

## Approach

| Stage | What was done |
|---|---|
| **Data Wrangling** | Checked for nulls, duplicates, and dtype issues; caught a silent whitespace bug in `State`/`Group`/`Time` (e.g. `' WA'` vs `'WA'`) that `isna()` doesn't catch but breaks `groupby()`; parsed `Date` to datetime; **min-max normalized** `Sales` and `Unit` |
| **Data Analysis** | Mean/median/mode/std-dev, skewness check, highest/lowest revenue segments, weekly/monthly/quarterly resampling |
| **Data Visualization** | Bar charts, heatmap, boxplots, and trend lines using Seaborn |
| **Insights** | Translated the numbers into concrete FY2021 recommendations |

## Key Findings

**Revenue is concentrated by state, not by demographic or time slot:**

| State | Total Sales (AUD) |
|---|---|
| 🥇 VIC | $105,565,000 |
| 🥈 NSW | $74,970,000 |
| 🥉 SA | $58,857,500 |
| QLD | $33,417,500 |
| TAS | $22,760,000 |
| NT | $22,580,000 |
| WA | $22,152,500 |

- VIC alone earns **~41% more than the #2 state (NSW)**, and nearly **5x** the bottom three states combined.
- Demographic groups are nearly balanced nationally — Men, Women, Kids and Seniors are all within **2%** of each other.
- Time of day (Morning/Afternoon/Evening) is also nearly flat, within **2%** — no dramatic peak-hour effect in this quarter.
- **Recommendation:** the revenue gap is a *state footprint/reach* problem, not a product-assortment problem — since underperformance in WA/NT/TAS is consistent across every demographic group.

### Visuals

<p align="center">
  <img src="images/02_state_group_heatmap.png" width="480"/>
  <img src="images/03_group_wise_sales_across_states.png" width="480"/>
</p>
<p align="center">
  <img src="images/04_time_of_day_peak_offpeak.png" width="480"/>
  <img src="images/06_sales_unit_distribution.png" width="480"/>
</p>

## Tech Stack

`Python` · `Pandas` · `NumPy` · `SciPy` · `Matplotlib` · `Seaborn` · `Jupyter Notebook`

## Project Structure

```
AAL-Apparel-Sales-Analysis/
├── README.md
├── requirements.txt
├── data/
│   └── AusApparalSales4thQrt2020.csv
├── notebook/
│   └── AAL_Sales_Analysis.ipynb
└── images/
    └── (exported charts)
```

## Run It Yourself

```bash
git clone https://github.com/shridharnaikodi/Data-Science-Journey.git
cd Data-Science-Journey/Projects/AAL-Apparel-Sales-Analysis
pip install -r requirements.txt
jupyter notebook notebook/AAL_Sales_Analysis.ipynb
```

---
*Part of my [Data Science Journey](https://github.com/shridharnaikodi/Data-Science-Journey) — a running log of data science and ML projects.*
