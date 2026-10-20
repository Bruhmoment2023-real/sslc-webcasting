# Results summary (bullets only - not manuscript text)

Run 13 October 2026. Every number below is in `results\analysis_log.txt` or
`results\posthoc_log.txt` and in the CSVs under `results\tables\`. The plan fixed beforehand is
`results\PRESPEC_frozen_before_analysis.md`. 34 districts throughout (Vijayanagara merged into
Ballari). "S1" = all candidates, first/main exam, 2014-2024. "S2" = regular freshers,
first/main exam, 2015, 2017-2023, 2025, 2026 (no 2024).

## The three stated hypotheses

- **H1 (districts with higher 2023 pass rates fell more, beyond ordinary mean reversion):
  NOT supported.**
  - Slope of the 2023-24 change on the 2023 level: -0.38 (robust s.e. 0.33, p = 0.25,
    R2 = 0.06). Weighted by candidates: -0.52 (s.e. 0.38).
  - The same regression in earlier year pairs gives slopes of -0.31, -0.30, -0.66, +0.06,
    -0.30, -0.17, -0.64 and +0.15 (table T3, figure F3). The 2023-24 slope sits in the middle
    of these. Two earlier pairs are steeper.
- **H2 (districts whose results rose most from 2019 to 2023 fell most in 2024): supported,
  with a caveat.**
  - Slope -0.75 (s.e. 0.27, p = 0.006, R2 = 0.15); Spearman -0.39. Leave-one-out range
    -0.90 to -0.63. Permutation check (post hoc): 1.1% of 20,000 shuffles are as negative.
  - Same pattern for regular freshers 2023 -> 2025: slope -1.15 (s.e. 0.46, p = 0.012).
  - Caveat: the nearest earlier analogue (change 2018-19 on the rise 2014-18) is also
    negative, -0.32 (s.e. 0.16). So part of this is ordinary give-back after a rise; the
    2024 coefficient is about twice as large, on one comparison only.
- **H3 (flat pre-trends, then a negative 2024 coefficient for high-2023 districts): NOT
  supported.**
  - With districts grouped by their 2023 level, the pre-period coefficients are far from
    zero (about -4.5 points per s.d. in 2014-2017, s.e. about 1). High-2023 districts were
    *not* on a parallel path; their 2022-23 standing was itself unusual.
  - The 2024 coefficient is -2.5 per s.d. (s.e. 2.0) with the 2023 grouping and +1.3
    (s.e. 1.6) with the 2018-19 grouping. Neither is distinguishable from zero.
  - Figure F4. A difference-in-differences on "high-baseline versus low-baseline districts"
    is not a valid design here.

## What the data do show (descriptive)

- **The fall was very uneven.** Change 2023 -> 2024 Exam-1 (after the 20% grace): mean
  -10.7 points, s.d. 10.4 - larger spread than any earlier year pair (2.7 to 8.6). 28
  districts fell, 6 rose. Largest falls: Madhugiri -28.7, Kalaburagi -25.2, Koppala -23.6,
  Chitradurga -21.8, Mandya -20.9. Rises: Shivamogga +8.5, Udupi +8.0, Dakshina Kannada +6.6,
  Bengaluru South +6.2, Bengaluru North +1.6, Sirsi +0.5. (Table T2.)
- **The district order was reshuffled once, and the new order then held (post hoc, P1).**
  - Rank correlation of district pass rates between consecutive main exams: 0.56-0.92 for
    every pair from 2014-15 to 2022-23; **0.23 for 2023-24**. For regular freshers:
    0.45-0.90 earlier; **0.15 for 2023 -> 2025**.
  - The two webcast years agree with each other: 2024 (S1) against 2025 (S2) 0.88;
    2025 -> 2026 0.80.
  - The 2024 order does not simply go back to the pre-COVID order either: 2024 against 2019
    is 0.33. (Figure F6.)
  - Taluk level, 204 taluks, cumulative results so not like-for-like: 2023 against 2024
    rank correlation 0.13; earlier pairs 0.64-0.77.
- **2023's top districts were the unusual ones.** Chitradurga (1st in 2023), Mandya,
  Chikkaballapura, Kolar, Madhugiri and Chamarajanagara all ranked in the top eight in 2023
  and fell 19-29 points; each had also risen 9.5-20 points since 2019.
- **By geography (post hoc):** mean 2023-24 change by board division: Mysuru -4.8,
  Belagavi -8.8, Bengaluru -11.7, Kalaburagi -19.8.
- **Who fell (state level, regular freshers, first exam):**
  - Government schools 86.7 (2023) -> 72.5 (2024) -> 62.7 (2025); aided 85.6 -> 72.2 -> 59.0;
    unaided 90.9 -> 86.5 -> 75.6. The unaided-minus-government gap was 4-10 points in every
    year 2015-2023 and 14.0 and 12.9 in 2024 and 2025. (Figure F7, table P2.)
  - Kannada medium 85.6 -> 69.3 -> 57.6; English medium 91.7 -> 88.3 -> 78.4.
  - Rural candidates were ahead of urban by 2-6 points in every year 2015-2023; in 2025 they
    were behind by 1.6.
  - Boys fell more than girls: all candidates, boys 80.1 -> 65.9, girls 87.9 -> 81.1 (2024).
- **Grace marks are visible in the grade table.** Passes in grade C (35-49%): 19,301 in 2023
  (2.8% of passes), 165,443 in 2024 (23.7%), 20,318 in 2025 (3.9%). (Figure F5.)
- **Same grace rule, six years apart:** regular freshers 79.4% in 2019 and 66.1% in 2025 -
  both under the 2017 statutory grace rule and a 35% pass mark; 2025 with webcasting.
- **2026 erased the differences.** Under the 33% rule regular freshers passed at 94.1%; the
  spread across districts fell to 2.8 points (11.4 in 2025). The 2025 -> 2026 change is
  almost a mirror of the 2025 level (slope -0.81, R2 0.97).
- **Booked malpractice cases** are 7-70 a year statewide in every year. They cannot measure
  copying.
- **Exploratory (A12):** share of a district's schools at 100% in 2018-19 does not predict
  the fall (R2 below 0.03). Share at 100% in 2023 does weakly (slope -20, p = 0.05).

## What cannot be said from these data

- That webcasting caused the fall. Every centre was covered in the same exam, and the
  three-exam system, 555 fewer centres, seating and phone rules, and then the 20% grace all
  arrived together. See `03-design.md`.
- Anything about district results *before grace* in 2024 - not published.
- Anything at school level after 2019 - school-wise files are published only for 2018 and 2019.
- Regular-fresher district results for Exam-1 2024 - not published.

## Checks on the numbers

- District sums reproduce the board's state totals exactly for S1 2019, 2020, 2022, 2023 and
  for S2 in every year.
- Hand-typed press-note tables: every row's percentage recomputes to the printed value.
- Standard errors with 34 clusters are rough; treat p-values as descriptive.
