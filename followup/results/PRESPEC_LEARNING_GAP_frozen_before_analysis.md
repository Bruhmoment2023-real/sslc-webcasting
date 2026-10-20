# Learning-gap test: specification written before any NAS number was matched to a pass rate

Written 13 October 2026, after the 34 NAS 2021 district report cards were downloaded and the Class 10 page of
each was read (extraction check only: 15 numbers per file), and before any correlation or regression between
NAS and SSLC pass rates was computed.

## Already seen (disclosed)
- The state-level NAS Class 10 figures printed on every card (state average percent correct: MIL 35, Maths 32,
  Science 35, Social Science 39, English 46; national 41, 32, 35, 37, 43).
- A visual scan of a few cards: district averages sit within about 26 to 40 points on every subject.
- The pack's SSLC results (H1-H3, post hoc tables) and the II PUC results in this folder.

## Measures
- NAS = unweighted mean of the five Class 10 subject scores (percent correct) of the district report card
  (Modern Indian Language, Mathematics, Science, Social Science, English). Also reported: Maths+Science only.
- The NAS Class 10 test was held on 12 November 2021, so the tested cohort sat SSLC in March-April 2022.
- Units: the 34 educational districts of the SSLC panel. NAS cards exist for exactly these units (Chikkodi,
  Madhugiri and Sirsi have their own cards; Ballari's card is taken to include Vijayanagara - unverified).
- Pass rate: S1 (all candidates, first/main exam) from `data\clean\panel_district_year.csv`; S2 (regular freshers)
  for 2025.
- z-scores are computed across the 34 districts within each measure.
- Gap_t = z(pass rate in year t) minus z(NAS). A positive gap means the district's pass rate looks high for its
  measured learning.

## Analyses (OLS, HC3 standard errors; Spearman reported beside every slope)
- L0. Spearman and Pearson correlation of NAS with S1 pass rate in 2019, 2022, 2023, 2024, and S2 in 2025.
- L1 (primary). Change in S1 pass rate 2023 -> 2024 on Gap_2023.
- L2. Same on Gap_2022 (the NAS cohort's own SSLC year) and on Gap using the 2022-23 mean pass rate.
- L3. Same on Gap_2019 (pre-COVID pass rate against 2021 NAS).
- L4. Two-variable model: change 2023 -> 2024 on z(pass 2023) and z(NAS) together, so the gap's coefficient
  is not just the pass-rate coefficient already seen in H1.
- L5. Change in S2 pass rate 2023 -> 2025 on Gap_2023 (regular freshers; grace back to the statutory rule).
- L6. Placebo: the same regression for the 2022 -> 2023 change on Gap_2022, and 2018 -> 2019 on Gap_2019.

## Expectation stated in advance
If the 2024 fall was concentrated where results had run ahead of learning, the L1 slope is negative and larger
than the L6 placebo slopes. If NAS is only a weak proxy for learning (small, sampled, a different age and
exam, 2021 conditions), the slope will be near zero and this proves nothing either way.

## Limits fixed in advance
- NAS is a sample survey (about 2,300 students in a district such as Gadag), a different test and different
  content from the SSLC, taken in November 2021 after school closures.
- 34 observations; p-values are descriptive.
- Whatever the result, it does not separate webcasting from the other changes of 2024.
- Every result is reported.
