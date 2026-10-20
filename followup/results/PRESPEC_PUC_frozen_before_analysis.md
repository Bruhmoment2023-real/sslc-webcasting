# II PUC comparison - specification written before any PUC statistic was computed

Written 13 October 2026, after the II PUC press notes were downloaded and the district tables
OCR-read, before any correlation, slope or spread was computed on them.

## Already seen when this was written (disclosed)

- The state totals in the board's II PUC press notes (regular students: 78.97 in 2023, 84.59
  in 2024, 73.45 in 2025, 86.48 in 2026), and the college-type, medium and urban/rural
  tables for 2024 and 2025.
- The district tables themselves, read line by line while checking the OCR. One thing was
  noticed by eye: Vijayapura is 3rd in 2024 (94.89) and 29th in 2025 (58.81). No rank
  correlation, slope or standard deviation had been computed.
- All SSLC results in the original pack.

## Data

- Unit: the board's PU district. 32 in 2018 and 2023-2026; 31 in 2016-2017 (Chikkodi not yet
  separate from Belagavi).
- Outcome: pass percentage of regular (fresher) students at the March annual exam / Exam-1,
  as printed. Percentages only: the district tables print no counts, so nothing is weighted
  and districts cannot be merged.
- Years with a primary-source district table: 2016, 2017 (PUE press release 2017, Wayback
  copy), 2018 (PUE press release 2018, Wayback copy), 2023, 2024 (KSEAB press note 2024
  Exam-1), 2025 (KSEAB press note 2025 Exam-1), 2026 (KSEAB press note 2026 Exam-1).
  2019, 2020, 2022 district tables were not found in a primary source; they are not used.
  2021 had no exam.
- Treatment timing (to be confirmed in the facts file): SSLC Exam-1 webcast from 2024;
  II PUC Exam-1 webcast statewide from 2025. Both moved to three exams in 2024.

## Analyses

- U1. State series for II PUC with every known rule change, beside the SSLC series.
- U2. Reshuffle. Spearman and Pearson correlation of district pass percentages between
  consecutive available years: 2016-17, 2017-18, 2018-23 (five-year gap; flagged, not a
  like-for-like placebo), 2023-24, 2024-25, 2025-26. 2016-17 on 31 districts; 2017-18 on the
  30 districts that exclude Belagavi and Chikkodi; later pairs on 32.
- U3. Spread of the change: standard deviation across districts of the year-to-year change
  for the same pairs; number rising and falling.
- U4. Give-back. Change 2024 -> 2025 regressed on the rise 2018 -> 2024 (OLS, HC3).
  Comparison regressions: change 2023 -> 2024 on the rise 2018 -> 2023; change 2017 -> 2018
  on the rise 2016 -> 2017. Also change 2024 -> 2025 on the one-year rise 2023 -> 2024.
- U5. Level. Change on the starting level for each adjacent pair (the mean-reversion slope).
- U6. Groups (state level): government / aided / unaided colleges, Kannada / English medium,
  urban / rural, boys / girls, 2023 or 2024 against 2025, with the population of each table
  stated (some 2024 tables cover all candidates, the 2025 ones regular students).
- U7. Same districts? SSLC units are aggregated to PU districts where they differ
  (Tumakuru + Madhugiri, Uttara Kannada + Sirsi, Ballari + Vijayanagara), giving 32 common
  units. Correlate the SSLC change 2023 -> 2024 (S1, all candidates, after grace) with
  (a) the PUC change 2024 -> 2025 and (b) the PUC change 2023 -> 2024. Also the SSLC
  regular-fresher change 2023 -> 2025 with both.
- U8. Cross-exam ranks. Rank correlation between SSLC and PUC district pass rates in the
  same year, 2018, 2023, 2024 (SSLC S1), 2025, 2026 (SSLC S2).

## What would count as "the SSLC pattern repeated in II PUC a year later"

- R1: the rank correlation for 2024-25 is the lowest of all adjacent PUC pairs, and the
  2023-24 one is not unusual (within or above the range of the other adjacent pairs).
- R2: the spread of the 2024-25 change is the largest of the adjacent pairs.
- R3: the U4 slope for 2024 -> 2025 is negative and more negative than both comparison slopes.
- R4: government, Kannada-medium and rural candidates fall more than unaided,
  English-medium and urban ones between 2024 and 2025, and did not between 2023 and 2024.
- R5 (U7): the SSLC 2023-24 district change correlates positively with the PUC 2024-25
  change and more strongly than with the PUC 2023-24 change.

## Limits fixed in advance

- Only two ordinary adjacent pairs exist before 2023 (2016-17, 2017-18), so "unusual" rests
  on very few comparisons. This is a description, not a test with a p-value.
- Even a full repeat would not isolate webcasting: any other change that reached II PUC in
  2025 and SSLC in 2024 (seating, phone rules, centre changes, grace policy) moves with it.
  A repeat would show that the pattern follows the monitoring year rather than the calendar
  year or the three-exam reform; a non-repeat would count against the monitoring reading.
- Every result is reported whichever way it comes out.
