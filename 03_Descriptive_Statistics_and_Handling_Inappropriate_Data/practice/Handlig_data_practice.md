# Day 3 Practice — Handling Inappropriate Data

**Dataset:** `inappropriate_data_dataset_50_records.csv`
**Goal:** Apply the 8-step "Handling Inappropriate Data" guideline end-to-end on a real, messy dataset.



---

## Q1. Column Type Identification
List every column in the dataset and classify it as **Numerical (Continuous / Discrete)**, **Categorical**, or **Ordinal**.
- Is `Age` continuous or discrete? Justify using the domain-expert rule from class.
- Is `Credit_Score` continuous or discrete?

## Q2. Duplicate Records
Check for and remove fully duplicate rows (`.duplicated()` / `.drop_duplicates()`). Report how many existed before and after.

## Q3. Duplicate Columns
`City` and `City_dup` appear identical. Prove this with a boolean comparison (don't just eyeball `.head()`) — check for whitespace/case mismatches too — then drop the redundant column.

## Q4. Numerical Column — `Age`
- Are decimal values valid for `Age`? (e.g. `29.5`, `45.2`)
- Are negative values valid? (e.g. `-5`)
- What's a realistic upper domain limit? (e.g. `102`, `150`)
- Apply the guideline: convert invalid entries to `NaN`, don't just delete the whole row yet.

## Q5. Numerical Column — `Monthly_Income`
- Should negative income exist in this domain? Handle any found.
- Should zero income (`0.0`) be treated as valid or inappropriate? Justify your decision.
- Should this column allow decimals? (Yes/No — justify)

## Q6. Numerical Column — `Credit_Score`
- Real-world credit scores typically range **300–900**. Flag/handle any value outside this range.
- Should this column allow decimals? (e.g. `720.5`) — decide and apply consistently.

## Q7. Categorical Column — `Gender`
- Get unique values using `.unique()`.
- Normalize spelling errors (`Femlae`), inconsistent casing (`FEMALE`, `femAle`, `M`, `F`), and stray whitespace (`" MALE "`) into a single standard set, e.g. `Male` / `Female`.
- Decide: is `"Unknown"` a valid category, or should those rows be dropped? Justify.

## Q8. Categorical Column — `Education_Level`
- Unify `Gradute` (typo), `Under Graduate`, `Undergraduate`, `UG` into **one** consistent label.
- Unify `Post Graduate`, `post graduate`, `PG` into one consistent label.

## Q9. Categorical Column — `City`
- Fix case inconsistency (`PUNE` vs `Pune`) and stray leading/trailing whitespace (`" Delhi "`).
- Decide: should `Bangalore` and `Bengaluru` be unified as the same city? Apply your decision.

## Q10. Categorical Column — `Loan_Status`
- Unify `Rejectd` (typo), `rejected`, `Rejected`, `REJECTED` into one label.
- Unify `approved`, `Approved`, `APPROVED` into one label.
- Unify `Pending` variants if any casing issues exist.

## Q11. Post-Cleaning Verification
- Run `.info()` and `.describe()` again after all cleaning steps.
- Compare row count and column count before vs. after cleaning.
- Summarize in 3–4 bullet points what changed and why.

## Q12. Reflection (Stretch)
Which column(s) are now fully ready for analysis, and which still need a domain expert's sign-off before you'd trust the valid ranges (e.g. is age 102 actually impossible, or just rare)? Write 2–3 sentences.

---
