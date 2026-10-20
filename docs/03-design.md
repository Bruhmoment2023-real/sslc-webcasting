# 03 - Design: question, pre-specified analysis, identification, threats

## 1. Research question

- **As posed:** did live webcasting of Karnataka SSLC exam centres from 2024 cut pass rates
  most where earlier results were most inflated?
- **What the public data can answer:** how did the fall in the first-exam pass rate from
  2023 to 2024-25 vary across districts, school types, media and candidate groups, and is
  that pattern what earlier year-to-year movements would predict?
- **What they cannot answer:** how much of the fall webcasting itself caused.

## 2. Analysis plan

The plan was written before any district regression was run and is frozen in
`results\PRESPEC_frozen_before_analysis.md` (units, three outcome series, analyses A1-A12,
hypotheses H1-H3, reporting rules). That file also discloses what had already been seen: the
state totals and the 2024 press-note district table with its rank column, so the sign of the
main relationship was suspected in advance.

Deviations and additions after seeing results (all labelled post hoc in code and tables):

- A4e-A4g: level-on-level regressions.
- P1: rank correlations between consecutive exams.
- P2: management and rural/urban gap series.
- P3: taluk-level rank correlations (cumulative results after 2024).
- P4: permutation check of A4c.
- Division means.
- No pre-specified analysis was dropped. A8 (subjects) and the district x management part of
  A7 could only be run on cumulative results, as the plan anticipated.

Code: `code\10_...` to `code\13_...` build the data; `code\20_analysis.py` runs A1-A12;
`code\21_posthoc.py` runs P1-P4. Results: `results\RESULTS_SUMMARY.md`.

## 3. Can webcasting be separated from the other changes? No, not with public aggregates.

Reasons, in order of importance:

1. **Everyone was treated at once.** Webcasting covered all 2,750 centres in Exam-1 2024
   (board press note). No district, centre, subject or paper was left out, and there was no
   pilot year for SSLC. A difference-in-differences needs an untreated group; inside the
   SSLC there is none.
2. **A bundle arrived in the same exam:** webcasting; a phone ban and changed seating
   (news); 555 fewer centres than 2023; the switch from main-plus-supplementary to three
   exams; a new cohort. These cannot be told apart by any comparison across districts.
3. **Grace was set after the results were seen.** The board raised grace to 20% because the
   pass rate had "declined by 30%". The published 2024 figures are therefore outcomes that
   were adjusted in response to the very fall being studied. Where the fall was largest, more
   candidates sat in the 25-35% band that grace rescued, so the after-grace district figures
   understate the true differences between districts by an unknown amount.
4. **The baseline is itself distorted.** 2022 and 2023 had the COVID 10%-in-three-subjects
   grace and (2022) easier papers by the board's own statement. So "the fall from 2023" mixes
   the end of COVID leniency with everything in point 2.
5. **"More inflated" is not observed.** The hypothesis needs a measure of prior inflation.
   The 2023 pass rate is not one: the event study shows high-2023 districts were on a
   different path for a decade (H3 fails), and a high pass rate can be real learning.
6. **Small numbers.** 34 districts; one treated year per series.

What the district regressions can and cannot carry:

- They can show the fall was unusually uneven and that the district order changed more than
  in any earlier year. That is a fact about the results.
- They cannot show the reshuffle was caused by cameras rather than by fewer centres, travel
  to unfamiliar centres, the three-exam system, or the end of COVID-era grace.

## 4. Comparisons that would be more convincing, and whether the data exist

| Comparison | Why it helps | Data status (checked 13 Oct 2026) |
|---|---|---|
| **II PUC (Class 12), same board, same districts** | II PUC also moved to three exams in 2024 but was webcast statewide only from March 2025 (news); so SSLC-versus-PUC in 2024 holds the three-exam reform fixed while webcasting differs, and PUC's own 2024 -> 2025 change is a second event. Closest thing to a staggered rollout. | **Not obtained.** The board's PUC statistics page (`dpue-exam.karnataka.gov.in/kseabdpuepresstats01/`) is a dynamic form; the "II PUC Result Statistics" menu on kseab was not explored. District-wise PUC results are routinely published. **First thing to try next.** Caveats: different students, PUC grace rules unknown, PUC Exams 2-3 of 2024 were trial-webcast in some colleges. That II PUC had three exams in 2024 is from memory **[unconfirmed]**. |
| **Before-grace district pass rates, 2024** | Removes point 3 above | **Not published.** Would need an RTI request or a written request to KSEAB by an adult. Students were given their "actual marks" individually in 2024, so the board holds the data. |
| **Regular-fresher Exam-1 results by district, 2024** | Makes 2024 comparable with the 2025 and 2026 district tables | **Not published.** Same route. |
| **School-level results 2022-2025** | 15,000+ units instead of 34; allows school fixed effects, management x baseline, and the Indonesian-style "drop versus prior implausibility" test | **Published in bulk only for 2018 and 2019** (four division workbooks each). Later years exist only behind school logins and per-student look-ups. Do **not** scrape the roll-number look-up: personal data of minors. Request the school-wise proforma from KSEAB. |
| **CBSE Class 10 in Karnataka** | Same state, same cohorts, no webcasting change | CBSE's statistics page is reachable (`cbse.gov.in/cbsenew/statistics.html`). CBSE publishes pass % by region in its annual result press release; whether a Karnataka-only (not Bengaluru-region) series exists for 2019-2025 **was not checked**. Gives one control series, not a panel. CBSE students differ sharply from state-board students. |
| **Neighbouring state boards** (Maharashtra, Tamil Nadu, Andhra Pradesh, Telangana, Kerala) | A state-year panel for a synthetic-control style comparison of Karnataka's 2024 fall | State totals are easy to collect from each board's result press release. **Not collected.** Weak: each state has its own grace and moderation practice, COVID exam formats differed, and one treated unit gives little inference. |
| **An outside, low-stakes yardstick: NAS 2021 Class 10 district scores** | If the post-webcasting district order agrees with an independent survey better than the 2023 order does, that is direct evidence that 2023 results were distorted - the most persuasive single test available without new board data | `nas.gov.in` did not respond in this session; district report cards for NAS 2021 are public documents. **Not obtained.** NAS uses revenue districts (about 31), so the board's 34 educational districts must be mapped. |
| **Supplementary / Exam-2, Exam-3** | Were later exams less monitored? | Whether Exam-2 and Exam-3 of 2024 were webcast is unconfirmed; candidates are a selected group (those who failed). Not useful. |
| **Subjects or papers not covered** | Within-exam control | None: all papers and centres were covered. |
| **UDISE+ school and district characteristics** | Covariates (management mix, rural share, teacher vacancies) | `udiseplus.gov.in` reachable; data.gov.in search page reachable. **Nothing downloaded or merged.** UDISE+ bulk downloads have at times needed registration - check; do not create an account under this project's rules. The board's own workbooks already give management, rural/urban and medium by district. |

## 5. Threats to validity (for whatever version is written)

- **Regression to the mean.** Handled by the placebo year pairs (A3) and baselines from other
  years (A4); the result is that the level-on-change slope is ordinary.
- **Changing populations.** S1 is all candidates and S2 regular freshers; they must not be
  spliced. Repeater numbers swing a lot (e.g. regular repeaters 4,618 registered in 2022).
- **District boundary change.** Vijayanagara split from Ballari; merged back here.
- **After-grace outcomes.** 2024 is not a clean measure of performance (section 3, point 3).
- **Cumulative versus single-exam figures.** The 2024-2026 workbooks are best-of-N. Any
  management, subject, grade or taluk number for those years from the workbooks is
  cumulative and is not comparable with 2023.
- **Board data quirks.** Urban/rural counts in the 2024 press note look swapped; small
  disagreements between press notes and workbooks; 667 candidates missing from the 2024
  district table.
- **Hand transcription** of three district tables from scanned pages (checked by recomputing
  percentages and totals, but Sean should re-check).
- **Inference.** 34 clusters, one event. P-values are descriptive. No multiple-testing
  correction was applied across A1-A12.
- **Garden of forking paths.** The rank-reshuffle result was found after the pre-specified
  slope failed. It is robust in the sense that it holds in both series, at taluk level and
  against every earlier year, but it is post hoc and must be labelled so.
- **Interpretation.** A reshuffle is what one would expect if earlier differences between
  districts partly reflected differences in malpractice. It is also what one would expect if
  centre consolidation or the loss of COVID grace hit some districts harder. The data here do
  not choose between these.

## 6. Ethics and data rules followed

- Aggregate public data only; no student-level records; no scraping of result look-ups.
- The 2024 press note's toppers page contains children's names and phone numbers. It was not
  extracted and must not be reproduced. The school-wise 2018-19 files contain school names
  and counts only.
- No accounts, logins or payments. Government servers were fetched one file at a time with
  pauses.
