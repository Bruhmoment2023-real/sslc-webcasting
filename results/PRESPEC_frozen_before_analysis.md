# Pre-specified analysis plan (frozen before any district regression was run)

Written 13 October 2026, after the raw data were downloaded and tidied but before any
district-level correlation, regression or event-study figure was computed.

## What had already been seen when this was written (disclosed)

- The state-level totals in the board's press notes and workbooks (pass percentage by year).
- The 2024 Exam-1 press note's district table, including its "rank in 2023" column. From that
  table it was already visible, by eye, that several districts ranked at the top in 2023
  (Chitradurga 1st, Mandya 2nd, Hassan 3rd) ranked much lower in 2024. So the *sign* of the
  main relationship was suspected before the plan was written. No slope, correlation,
  placebo or figure had been computed.
- The validation output of `code/11_validate_tables.py` (state sums only).

Because the sign was suspected in advance, the placebo comparison (A3) and the
"different-year baseline" checks (A4) carry the weight, not the sign of the main slope.

## Units

- Educational districts of Karnataka as used by the board: 34 units in every year after
  merging Vijayanagara (code TA, created by splitting Ballari) back into Ballari (code TT), so
  the same 34 units exist from 2014 to 2026.

## Outcome series (kept separate; never spliced silently)

- **S1, all candidates, first/main exam.** Passed / appeared.
  - 2014-2018: board workbook `5years.xlsx` (published directly).
  - 2019, 2020, 2022, 2023: regular freshers (PRO-5) + regular repeaters (PRO-11) + private
    freshers (PRO-11A). This combination reproduces the published state totals; private
    repeaters (PRO-11B) are already inside PRO-11 in those years.
  - 2024: Exam-1 district table in the board's press note of 9 May 2024 (after the one-time
    20 per cent grace).
  - 2021 is dropped from every regression (the COVID two-day exam passed 99.99 per cent).
- **S2, regular freshers, first/main exam.** 2015, 2017-2020, 2022, 2023 from PRO-5;
  2025 Exam-1 and 2026 Exam-1 from the press notes. There is **no 2024 point** because the
  board did not publish Exam-1 regular-fresher results by district.
- **S3, regular freshers, cumulative best of Exams 1-3 (2024, 2025) or 1-2 (2026).**
  Described in tables only. Not comparable with S1/S2, because before 2024 supplementary
  passes were never added to the annual figure.

## Analyses

- **A1. State series.** Table and figure of the pass percentage 2014-2026 with every rule
  change marked.
- **A2. Main cross-section.** For the 34 districts, change in S1 pass percentage from 2023 to
  2024 regressed on the 2023 level. OLS, heteroskedasticity-robust (HC3) standard errors.
  Primary: unweighted. Secondary: weighted by candidates appeared in 2023. Also report the
  Spearman rank correlation.
- **A3. Mean-reversion placebo.** The identical regression for every adjacent pair of
  "ordinary" years in S1: 2014-15, 2015-16, 2016-17, 2017-18, 2018-19, 2019-20, 2022-23
  (and the two-year gap 2020-22, reported but flagged). The 2023-24 slope is compared with
  the placebo slopes. With 34 districts this is a ranking, not a formal test.
- **A4. Baselines measured in a different year** (to break the mechanical link between a
  noisy baseline and the change from it):
  - (a) change 2023-24 on the 2018-19 average level;
  - (b) change 2023-24 on the 2022 level;
  - (c) change 2023-24 on the rise from 2019 to 2023 (the "COVID-era rise", a pre-trend
    measure): did districts whose results rose most between 2019 and 2023 fall most?
  - (d) change from the 2018-19 average to 2024 on the 2018-19 average (does 2024 simply
    return districts to their pre-COVID level?).
- **A5. Event study.** S1, years 2014-2020, 2022-2024, district and year fixed effects,
  2023 as the reference year, standard errors clustered by district:
  - (a) high-baseline indicator (top tercile of the 2023 S1 pass rate) x year dummies;
  - (b) continuous standardised 2023 baseline x year dummies;
  - (c) the same two with groups defined by the 2018-19 average instead of 2023.
  Plot coefficients with 95 per cent intervals. Also plot raw group means by year.
- **A6. Regular freshers after the extra grace was removed.** A2-A4 repeated on S2 for
  2023 to 2025 (Exam-1, grace back to the statutory rule) and, separately, 2023 to 2026
  (new 33 per cent pass rule; expected to compress all districts towards 100).
- **A7. Management type.** State-level Exam-1 pass rates for government, aided and unaided
  schools by year from the press notes. District x management only on S3 (cumulative),
  reported as descriptive.
- **A8. Subjects.** Subject-wise pass rates by year. Exam-1 subject figures for 2024-25 are
  not published; S3 figures are shown and flagged.
- **A9. Grade distribution.** Share of regular-fresher passes in grade C (35-49 per cent) by
  year, state level; by district on S3.
- **A10. Booked malpractice cases** per year from PRO-10, as a descriptive table.
- **A11. Gender and urban/rural gaps** at state level by year.
- **A12 (exploratory, labelled as such).** From the 2018 and 2019 school-wise workbooks: the
  share of each district's schools with a 100 per cent result, and the share of its schools
  above 95 per cent, as alternative "suspiciously high" markers; correlate with the
  2023-24 change.

## Stated expectations

- H1: the A2 slope is negative and more negative than every placebo slope in A3.
- H2: in A4(c), districts with the larger 2019-23 rise have the larger 2023-24 fall.
- H3: in A5, the high-baseline group shows no differential pre-trend before 2020 and a
  negative coefficient in 2024.
- Whatever the results, none of A2-A12 can by itself separate webcasting from the other
  changes that took effect in the same exam (grace-mark rule, three-exam system, fewer
  centres, seating changes, question-paper difficulty, cohort). That question is handled in
  the identification section of `03-design.md`, not by these regressions.

## Rules for reporting

- Every pre-specified analysis is reported whether or not it supports the hypotheses.
- Anything added after seeing results is labelled "post hoc".
- No district is dropped as an outlier in a primary specification; leave-one-out results are
  shown as a robustness check.
