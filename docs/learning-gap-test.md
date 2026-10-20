# Task 3 - Learning-gap test (NAS 2021) and other external series

Run 13 October 2026. Specification frozen before matching: `results\PRESPEC_LEARNING_GAP_frozen_before_analysis.md`. Code: `code\g05_nas_extract.py`, `g06_nas_table.py`, `f30_learning_gap.py`. Log: `results\learning_gap_log.txt`. Table: `results\tables\L_learning_gap.csv`. Data: `data\nas2021_class10_district.csv`.

## 1. Availability check

| Source | Free district-level data? | What I found (13 Oct 2026) |
|---|---|---|
| **NAS 2021, Class 10, Karnataka** | **Yes, no login.** | NCERT page `https://ncert.nic.in/DRC_2021.php?ln=en` lists "Karnataka" with a Download link to `https://ncert.nic.in/pdf/NAS/drc_2021/Karnataka.rar` (522 MB; fetched once, politely). It holds **34 district report cards** (Chikkodi, Madhugiri and Sirsi have their own cards; Ballari's card presumably includes Vijayanagara, unverified). Each card is 32 pages; page 25 is Class 10: participation (e.g. Gadag: 81 schools, 369 teachers, 2,338 students) and district / state / national mean percent correct (with standard error) for five subjects, plus performance-level shares. The page 25 numbers are in the PDF text layer. Opened in full for Gadag (viewed) and parsed for all 34. Status: **primary source, opened in full.** |
| **PARAKH Rashtriya Sarvekshan 2024, district scores** | **No (not for Class 10, and the district list is gated).** | PRS 2024 tested Classes 3, 6 and 9, **not Class 10** (page `https://parakh.ncert.gov.in/prs-reports-2024`, opened). The district-list page `.../prs-reports-2024-districtlist` returns "Access denied: you are not authorized to access this page" (saved page by the earlier agent; my own request got HTTP 403). I did not try to get round it. Status: **not obtainable without login**; Class 9 would in any case be a different cohort (the 2024 SSLC takers were Class 9 in 2022-23). |
| **CBSE Class 10, Karnataka** | **No (region level only).** | CBSE publishes region-wise pass rates, not state or district. News reports (Careers360, Amar Ujala summaries; CBSE release not opened) give Bengaluru region 99.26% in 2024 (one outlet 99.22%) and 98.90% in 2025 (an Odisha outlet). At about 99% the series has no room to move, so it cannot work as a control. Status: **confirmed from news only; unusable as a control.** |
| **Neighbouring state boards, by year** | State level yes; district level partly. | Tamil Nadu SSLC 2025: 93.80% overall, district ranking published (news: Dinamalar, StudyCafe, search summaries only). Kerala SSLC 2025: 99.5% (2024: 99.69%), district figures in news (Careers360 summary). Andhra Pradesh and Telangana: no source found. Maharashtra, Goa: not searched. I did not collect a multi-year series: with pass rates in Kerala and Tamil Nadu at 94-99.7% they would show nothing, and each state has its own grace rules. Status: **not collected; listed as "ready to collect"** (official sites: tnresults.nic.in, results.kite.kerala.gov.in). |
| **UDISE+ district characteristics** | Probably yes, not downloaded. | UDISE+ 2023-24 national report PDF is on `dsel.education.gov.in` (not opened). A community catalogue lists a Bengaluru Urban 2023-24 UDISE+ dataset. A third-party analysis notes UDISE+ moved from school-level to student-level collection from 2022-23, so 2021-22 and 2023-24 are not like-for-like. I found no data.gov.in listing of Karnataka district tables in a quick search. Status: **unconfirmed; not downloaded**. |

## 2. NAS data in brief (all numbers from the cards)

- State Class 10 averages (percent correct): MIL 35, Mathematics 32, Science 35, Social Science 39, English 46. National: 41, 32, 35, 37, 43.
- Mean of the five subjects ("NAS") across the 34 districts: mean 37.1, s.d. 2.84, range 32.4 to 41.8. Median standard error per subject mean about 0.43, so measurement noise is small against the between-district spread.
- The test was on 12 November 2021, so the cohort tested sat SSLC in March-April 2022.

## 3. Results (as run; pre-specified L0-L6; HC3 standard errors; n = 34 unless noted)

L0 - Rank/linear correlation of NAS with pass rates:

| Pass rate | Spearman | Pearson |
|---|---|---|
| S1 2019 | 0.14 | 0.24 |
| S1 2022 | -0.06 | 0.02 |
| S1 2023 | 0.10 | 0.14 |
| **S1 2024** | **0.40** | **0.42** |
| **S2 2025 (regular freshers)** | **0.44** | **0.47** |

The 2022 and 2023 district orders (COVID-era grace) have essentially no relation to measured learning in 2021. The 2024 and 2025 orders do (moderately).

Regressions of the change in the S1 pass rate on the gap (gap = z(pass) - z(NAS); positive gap = pass rate high for measured learning):

| Spec | Coefficient per s.d. of gap (s.e.) | p | R2 |
|---|---|---|---|
| **L1 (primary): change 2023->24 on Gap_2023** | **-3.55 (1.10)** | 0.001 | 0.20 |
| L2a: Gap_2022 | -3.49 (1.16) | 0.003 | 0.22 |
| L2b: Gap using 2022-23 mean | -3.56 (1.12) | 0.002 | 0.21 |
| L2c: Gap_2023 using Maths + Science only | -1.46 (1.44) | 0.31 | 0.03 |
| L3: Gap_2019 (pre-COVID pass rate) | -1.97 (1.55) | 0.20 | 0.06 |
| L4: z(pass 2023) and z(NAS) together | pass -3.03 (1.54), p = 0.049; **NAS +4.06 (1.91), p = 0.034** | | 0.21 |
| L5: regular freshers, change 2023->25 on gap | -4.24 (1.08) | <0.001 | 0.23 |
| L5b: both variables, S2 | pass -3.47 (1.21); NAS +5.01 (1.99), p = 0.012 | | 0.24 |
| L6a placebo: change 2022->23 on Gap_2022 | -0.02 (0.38) | 0.96 | 0.00 |
| L6b placebo: change 2018->19 on Gap_2019 | +1.18 (0.70) | 0.09 | 0.06 |
| L6c: change 2023->24 on NAS alone | +3.63 (1.87) | 0.052 | 0.12 |

Reading, in plain terms:

- **Yes: the pre-2024 gap between pass rate and NAS predicts the 2024 fall** (primary spec, p = 0.001, R2 0.20, Spearman -0.37), and also the 2025 change for regular freshers. Both placebos are flat or go the other way, so ordinary year-to-year churn does not produce a slope like this.
- **Part of it is the 2023 pass rate again.** In the two-variable model the pass-rate coefficient is the same one the pack's H1 found (not distinguishable from ordinary mean reversion on its own); what is new is that **NAS carries its own coefficient**: for a given 2023 pass rate, districts with higher measured learning fell less (+4.06 points per s.d. of NAS).
- **Not robust to the measure of learning.** With Maths + Science only (L2c), the slope shrinks to -1.46 and is not significant. The result weakens when English and the Modern Indian Language scores are left out; I have not tested why (one possibility, untested, is that those subjects track medium of instruction). Five-subject mean was the pre-specified primary, but the dependence on subject choice must be reported.
- **Not robust to the baseline year.** With the pre-COVID 2019 pass rate the slope is -1.97 (p = 0.20).
- Many specifications were run (12). The pre-specification fixes which was primary, and all are shown.

## 4. What this does and does not mean

- Consistent with the idea that the 2024 fall was larger where pass rates had run ahead of learning. It is equally consistent with the **fall being larger where the district had more weak-medium, government-school candidates** (those fell most, per the pack), and NAS could be higher where there are more English-medium or urban students (a hypothesis I have not tested). NAS cannot separate "inflated results" from "composition" without school-management shares per district, which I did not merge (the pack's management tables could do this next).
- It cannot separate webcasting from the grace-mark rule, the three-exam system, fewer centres or paper difficulty (same limitation as the pack's design).
- NAS is a 2021 sample survey of about 2,300 students per district with a different test; 34 observations; p-values are descriptive.

## 5. Ready to run next (not done)

- Add district government/aided/unaided and Kannada/English shares (from `data\clean\district_regular_fresh_by_management.csv`) to L4 to see whether NAS keeps its coefficient.
- NAS Class 8 cards (same files, pages 19 and 20) as a second learning proxy for the cohort who sat SSLC in 2025.
- Check the Ballari/Vijayanagara card assumption by opening that PDF's first pages.
