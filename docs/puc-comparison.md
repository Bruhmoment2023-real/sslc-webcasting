# Task 2 - II PUC (Class 12) as a comparison: did the SSLC 2024 pattern repeat in PUC's first webcast year (2025)?

Run 13 October 2026. Plan frozen before any PUC statistic was computed: `results\PRESPEC_PUC_frozen_before_analysis.md` (U1-U8, R1-R5; the earlier agent wrote it). Code: `code\f10_build_puc_panel.py` (panel), `code\f20_puc_analysis.py` (all analyses). Output: `results\puc_analysis_log.txt`, `results\tables\U2_U3_U5_puc_pairs.csv`, `U4_puc_giveback.csv`, `U7_sslc_vs_puc_changes.csv`, `U8_same_year_sslc_vs_puc.csv`. Panel: `data\puc_district_regular_passpct.csv` (222 rows).

**Short answer.** Part of the SSLC pattern recurs in II PUC in 2025, in a much milder form, and not in 2024. The "give-back" signature (fall concentrated in districts whose results had risen most) appears, and the same districts that fell most in SSLC 2024 fell most in PUC 2025. The one-off district reshuffle that was so stark in SSLC (rank correlation 0.23) is weak in PUC (0.78, the lowest of its adjacent pairs but only just). A competing explanation (2024 PUC was an anomalous high year in some districts, e.g. Vijayapura) is as good as the monitoring one. Nothing here isolates webcasting.

## 1. Facts: webcasting, exams, grace in II PUC

Labels: [P] primary (board document I opened); [N] news only (outlets named); [U] unconfirmed.

| Item | Finding | Label |
|---|---|---|
| II PUC webcasting before 2025 | In 2024 "for examinations 2 and 3 of the second PUC, we identified the colleges with CCTV cameras and webstreamed the examination. The trial was successful" (a senior department official). **Exam-1 (March 2024) was not webcast**, as far as any source says. | [N] Deccan Herald 30 Oct 2024 (saved: `data\raw\news\dh_pu_livestream_3254201.html`, opened) |
| Plan for March 2025 | KSEAB "extended the webcasting" of board exams to II PUC "scheduled to be held during March-April 2025"; colleges serving as centres were asked to give CCTV camera IP numbers to district deputy directors, who with Zilla and Taluk Panchayat officials "will watch the live streaming" | [N] same article |
| Start in Exam-1 2025 | "For the first time, the Education Department introduced a webcasting surveillance system for the Class 12 examination" (Sakshi Post, 1 Mar 2025, opened). Exam-1 2025 ran 1-20 March 2025 in 1,171 centres. | [N] Sakshi Post + DH; **[P] silent**: the board's 2025 press note (English pages 9-13) does not mention webcasting or CCTV |
| Coverage "all centres" in 2025 | A Mandya district report and an Udupi report say all their centres were webcast (search-result summaries, pages not opened); I found no statewide statement that every centre was covered. Because the plan relied on cameras already installed, **statewide completeness is [U]**. | [N]/[U] |
| 2026 | Free Press Journal, 28 Feb 2026 (opened): "CCTV cameras have been installed in all exam halls" and "webcasting is being used"; newskarnataka, 18 Mar 2026 (opened): an official credits "web streaming of examination centres" and the three-examination system for clean conduct. 2026 Exam-1: 28 Feb-17 Mar, 1,217 centres. | [N] two outlets |
| Three-exam system | II PUC Exam-1, Exam-2, Exam-3 in **2024** (board press notes for each: `PRESS_STATS_EXAM1/2/3_2024.pdf` and a 2024 "consolidated" release). 2023 had one annual exam plus a supplementary (2023 SSLC pattern; PU 2023 not separately checked). 2025: Exam-1, 2, 3. 2026: Exam-1 and Exam-2 only (file titled "Exam-1 and Exam-2 consolidated"). | [P] |
| So for PUC the dates are | three-exam system **2024**; first (Exam-1) webcast **2025**. For SSLC both were 2024. | |
| Grace rules | The board's PUC press notes 2024-26 mention no grace policy. A 2018 departmental note (Kannada, my reading) restricted question-specific grace to English (3 marks on a 3-mark question) and Physics (6 marks) under the PU public examination amendment rules 2017. News/commercial sites say aggregate pass mark 33% with up to 5% grace for 2024, and a 33% rule from 2026 (Careers360, Collegedunia: conflicting). **Whether PUC had a 20% one-off grace like SSLC 2024: no evidence found.** | [U]; 2018 note [P] |
| Pass mark | SSLC and II PUC pass mark cut 35 -> 33% from 2026 (Deccan Herald 16 Oct 2025; ETV Bharat 15 Oct 2025 headline; Careers360). | [N] |
| Share of passes below 50% (PUC "pass class") | 2024 37,489 of 552,690 (6.8%); 2025 18,845 of 468,439 (4.0%); 2026 16,827 of 546,698 (3.1%). Falls, but no spike in 2024 like SSLC's grade C (2.8% -> 23.7% -> 3.9%). Suggests **no large grace in PUC 2024**, which is an inference. | [P] counts; inference mine |

## 2. State pass rates (percent; regular students = freshers unless stated)

| Year | Regular/fresher | All candidates | Source |
|---|---|---|---|
| 2016 | 65.02 | 57.20 | PU press release 2017 p.1 (Wayback) [P] |
| 2017 | 59.90 | 52.38 | same |
| 2018 | 68.29 | 59.56 | PU press release 2018 p.1 (Wayback) [P] |
| 2019, 2020, 2022 | not found in a primary source | | 2021 no exam (all passed) |
| 2023 | 78.97 | 74.67 | 2024 press note [P] |
| 2024 Exam-1 | 84.59 | 81.15 | KSEAB press note [P] |
| 2025 Exam-1 | 73.45 | 69.16 | KSEAB press note [P] |
| 2026 Exam-1 | 86.48 | 81.58 | KSEAB press note [P] |

District tables (regular students, percent only, no counts) exist in a primary source for 2016, 2017, 2018, 2023, 2024, 2025, 2026 (32 districts; 31 in 2016-17 when Chikkodi was inside Belagavi). **2019, 2020 and 2022 district tables were not found**; the Wayback copy of the 2020 results page is a single image with no usable table. Checks: the 2025 column printed in both the 2025 and 2026 notes is identical (max difference 0.00 over 32 districts); the 2016/2017 typed values were re-read by me against the page image (all 31 districts, both years match); 2018: I viewed the first page of the table image (25 rows) and the printed values agree with the OCR text, but I did not compare every row to the panel by eye; the panel rebuilds byte-for-byte from the OCR files.

## 3. Results (as pre-specified)

**U2/U3/U5 - adjacent-pair reshuffle, spread, mean reversion** (PUC, 32 districts unless stated):

| Pair | n | Spearman | s.d. of change | mean change | rising / falling | slope of change on start level (s.e.) |
|---|---|---|---|---|---|---|
| 2016-17 | 31 | 0.88 | 4.96 | -4.3 | 4 / 27 | 0.00 (0.08) |
| 2017-18 | 30 | 0.91 | 4.14 | +9.3 | 30 / 0 | -0.23 (0.05) |
| 2018-23 (five-year gap, flagged) | 32 | 0.71 | 6.27 | +11.0 | 31 / 1 | -0.40 (0.10) |
| 2023-24 | 32 | **0.96** | 2.62 | +5.3 | 32 / 0 | -0.18 (0.07) |
| **2024-25** | 32 | **0.78** | **6.77** | -11.6 | 0 / 32 | +0.16 (0.28) |
| 2025-26 | 32 | 0.81 | 6.11 | +13.5 | 32 / 0 | -0.50 (0.07) |

SSLC for comparison (same 32 units, aggregated): 2022-23 0.92; **2023-24 0.28** (pack, 34 units: 0.23).

- **R1** (2024-25 rank correlation lowest of adjacent pairs; 2023-24 unremarkable): **met on paper.** 0.78 is the lowest adjacent value, but 2025-26 is 0.81, so the margin is tiny, and the size of the reshuffle is nothing like SSLC's. 2023-24 (0.96) is the highest, not unusual in the sense required.
- **R2** (largest spread of change in 2024-25): **met** (6.77 vs 6.11 in 2025-26 and 4.96 earlier), again narrowly. The 2025-26 rebound is almost as dispersed. Note every district moved the same way in 2023-24, 2024-25 and 2025-26; in SSLC 2024 six rose and 28 fell.

**U4 - give-back** (change on earlier rise; OLS HC3):

| Specification | n | Slope (s.e.) | p | R2 |
|---|---|---|---|---|
| **Change 2024->25 on rise 2018->2024** | 32 | **-0.66 (0.23)** | 0.005 | 0.47 |
| Change 2023->24 on rise 2018->2023 | 32 | +0.03 (0.07) | 0.67 | 0.01 |
| Change 2017->18 on rise 2016->17 (Belagavi, Chikkodi excluded) | 30 | -0.42 (0.26) | 0.11 | 0.19 |
| Change 2024->25 on one-year rise 2023->24 | 32 | -1.73 (0.49) | <0.001 | 0.45 |

- **R3** (2024->25 slope negative and more negative than both comparison slopes): **met** (-0.66 against +0.03 and -0.42; the pack's SSLC analogue was -0.75).
- Caveat I should flag: the 2024 level appears on both sides of the first regression (as the end of the rise and the start of the change), which builds in a negative slope from noise alone. **Post hoc, not in the frozen plan:** with the 2024 level removed from the right-hand side (change 2024->25 on the rise 2018->2023) the slope is -0.52 (s.e. 0.24, p = 0.029, R2 0.23): weaker but still negative. The pack's H2 has the same shared-year structure.
- **Post hoc:** the 2024->25 fall is larger in historically weak districts (change on the 2018 level +0.39, s.e. 0.08, R2 0.33; on the 2023 level +0.31). The biggest falls were Vijayapura -36.1 (94.89 -> 58.81; 3rd in 2024, 29th in 2025), Yadagiri -28.8, Kalaburagi -19.8, Chikkodi -17.3, Bagalakote -14.7; the smallest were Udupi -2.9, Dakshina Kannada -3.8, Bengaluru South -4.2. That is a **different geography from SSLC**, where the 2023 high-flyers (Chitradurga, Mandya, Hassan, Kolar) fell most.

**U7 - same districts, SSLC change versus PUC change** (Spearman; Pearson in brackets):

| | PUC 2023->24 | PUC 2024->25 | PUC 2023->25 |
|---|---|---|---|
| SSLC change 2023->24 (S1, after grace) | -0.17 (-0.21) | **+0.53 (+0.42)** | +0.55 (+0.43) |
| SSLC regular-fresher change 2023->25 | -0.27 (-0.31) | **+0.65 (+0.63)** | +0.65 (+0.64) |

- **R5**: **met.** Districts whose SSLC pass rate fell most in 2024 are the ones whose PUC pass rate fell most in 2025, and there is no such link with the PUC 2023-24 change. This is the strongest single repeat. It fits "same districts, same shock a year later" and equally fits "the same weak districts are unusually exposed to any tightening".

**U8 - same-year SSLC vs PUC district rank correlation:** 2018 0.09; 2023 0.26; 2024 0.74; 2025 0.87; 2026 0.43. The district orders of the two exams were almost unrelated in 2018 and 2023 and became closely aligned in 2024-25, when both exams had tightened up. In 2026, after the pass-mark cut and the 2026 rebound in both, the link falls back to 0.43. This is a further descriptive pattern the pack did not have; **post hoc in the sense that U8 was specified but its interpretation was not**.

**U6 / R4 - groups (state level; population noted)**

| Group | 2023 | 2024 | 2025 | 2026 | Change |
|---|---|---|---|---|---|
| Govt PU colleges (regular) | - | 75.29 | 57.11 | 78.72 | 2024->25 **-18.2**; 2025->26 +21.6 |
| Aided (regular; 2026 includes bifurcated) | - | 79.82 | 62.69 (68.25 merged) | 82.90 | -17.1 |
| Unaided (regular) | - | 90.46 | 82.66 | 90.73 | **-7.8**; +8.1 |
| Unaided minus govt gap | - | 15.2 | 25.6 | 12.0 | |
| Kannada medium | - | 70.41 (all cand.) | 56.37 (regular) | 76.41 | -14.0 (populations differ); 2025->26 +20.0 |
| English medium | - | 87.40 (all cand.) | 81.75 (regular) | 90.63 | -5.7 (populations differ); +8.9 |
| Rural | 74.79 (all) | 81.31 (all) | 69.33 (regular) | 87.62 | 2023->24 +6.5; 2024->25 -12.0 (populations differ); 2025->26 +18.3 |
| Urban | 74.63 (all) | 81.10 (all) | 74.55 (regular) | 85.95 | +6.5; -6.6; +11.4 |
| Boys / girls | 69.05 / 80.25 (all) | 76.98 / 84.87 (all) | 68.20 / 77.88 (regular) | 83.65 / 88.70 | boys fell/rose more in every move |

- **R4 mostly met for government v unaided** (same population: regular students): government and aided colleges fell about 17-18 points and unaided 7.8; the unaided-government gap widened from 15.2 to 25.6 points in 2025, as the SSLC gap did in 2024 (about 4 to 13-14). Kannada-medium and rural candidates fell more than English-medium and urban ones, **but for these the 2024 table covers all candidates (incl. repeaters and private) and the 2025 table regular students, so the size of the fall is overstated** (state totals differ by 3.4 points: 81.15 vs 84.59). The 2025->26 rebound (same population) is larger for Kannada (+20.0), rural (+18.3) and government colleges (+21.6), which is consistent with those groups having fallen furthest.
- "Did not between 2023 and 2024": cannot be tested by college type or medium (no 2023 table); by urban/rural, both rose by the same amount (+6.5).

## 4. Does the SSLC pattern repeat "in its own first webcast year and not in 2024"?

| SSLC 2024 pattern | PUC 2025 (webcast Exam-1 year) | PUC 2024 (not webcast Exam-1) |
|---|---|---|
| Fall concentrated in districts that had risen most | Yes (slope -0.66; -0.52 after removing the shared year) | No (+0.03); all districts rose by 5.3 on average |
| One-off reshuffle of district ranking | Weak: 0.78, lowest of adjacent pairs but 2025-26 is 0.81 | No: 0.96 |
| Larger falls for government, Kannada-medium, rural | Yes for government v unaided; directional for medium and rural (populations differ) | not testable (no like-for-like table) |
| Same districts as SSLC | Yes (rho 0.53-0.65) | No (-0.17) |
| Spread of the change | Largest of adjacent pairs, narrowly | Smallest (2.62) |

Verdict: **the direction of every comparison favours "the pattern follows the monitoring year"**, and PUC 2024 (three exams, no Exam-1 webcasting) behaved like an ordinary rising year. But:

1. Magnitudes are small beside SSLC (reshuffle 0.78 against 0.23).
2. Only two ordinary adjacent pairs exist before 2023, so "unusual" rests on very few comparisons; no p-values are meaningful here.
3. PUC 2025 changed other things at once, none of which I could rule out: three exams for the second year, Exam-2/3 retake free for some, a harsher paper or marking (unknown), the removal of any 2024 leniency (unknown), and SSLC-style tightening in the same districts by the same officials. And Vijayapura's 2024 value (94.89) looks like a one-year anomaly that alone drives much of the 2025 reshuffle.
4. Even a full repeat would show that the pattern follows the exam where monitoring began, not that cameras were the cause.
5. In 2026 both exams rebounded to levels at or above 2024 with the pass mark cut and (per news) webcasting still on. That is hard to reconcile with a permanent "cameras lower results" effect and easy to reconcile with the pass-mark and grace rules mattering a great deal.

## 5. Files saved
`raw\puc_press\` (9 board PDFs, 2024-26), `raw\wayback\` (2014, 2017, 2018, 2020, 2021 board documents), `raw\puc_press_ocr\` (OCR rows), `raw\pages\` (page images used for visual checks).
