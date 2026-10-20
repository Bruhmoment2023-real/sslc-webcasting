# Data dictionary - `data\clean\`

All files are aggregates published by the Karnataka School Examination and Assessment Board
(KSEAB; formerly KSEEB). No student-level records are held anywhere in this project.
Downloaded 13 October 2026 from `https://kseab.karnataka.gov.in/new-page/Result%20Statistics/en`
(workbooks) and `https://kseab.karnataka.gov.in/198/press-note%28sslc%29--/en` (press notes).

**Reading rule:** the district code for Chikkodi is `NA`. Read every CSV with
`keep_default_na=False, na_values=['']` (see `code\common.py`) or Chikkodi silently disappears.

## Terms

- **Regular fresher (CCERF):** a school student sitting the exam for the first time.
- **All candidates:** regular freshers + regular repeaters + private freshers + private repeaters.
- **Main exam / Exam-1:** the March-April examination. From 2024 it is called Exam-1 and is
  followed by Exam-2 and Exam-3 (2026: Exam-2 only).
- **scope:** `main_exam` (the workbook describes one exam) or `best_of_3` / `best_of_2`
  (2024-2026 workbooks: each student's best result across that year's exams - **not comparable
  with earlier years**).
- **Educational district:** the board's unit (34 until 2022, 35 from 2023 when Vijayanagara
  appears). The panel merges Vijayanagara (TA) into Ballari (TT) to keep 34 units.

## Files built from the workbooks (`code\10_build_district_tables.py`)

Common columns: `year`, `exam` (label), `scope`, `dist_code`, `dist_name`, `source_file`,
`sheet`. Counts are numbers of candidates; `*_pct` columns are the percentages as printed.

| File | Source sheet | Contents | Years |
|---|---|---|---|
| `district_regular_fresh_by_gender.csv` | PRO-5 | appeared / passed / % for boys, girls, total | 2015, 2017-2026 |
| `district_regular_fresh_by_management_sex.csv` | PRO-7A, PRO-7B | government / aided / unaided, by sex | 2015, 2017-2026 |
| `district_regular_fresh_by_management.csv` | derived from the above | long format, sexes summed; `pct` recomputed | same |
| `district_regular_fresh_by_urban_rural.csv` | PRO-6A | rural / urban by sex and total | 2015, 2017-2026 |
| `district_regular_fresh_by_subject.csv` | PRO-2A(1)-(3) | six subjects; `b_`/`g_` = boys/girls; `pct` recomputed | 2017-2026 (2015 partial) |
| `district_regular_fresh_grade_distribution.csv` | PRO-16 | passes by grade band A+ ... C | 2015, 2017-2026 |
| `district_other_candidate_types.csv` | PRO-11, 11A, 11B | repeaters, private freshers, private repeaters | 2015, 2017-2026 |
| `district_malpractice_cases.csv` | PRO-10 | malpractice cases booked, by management and sex (only districts with a case are listed) | 2017-2026 |
| `district_schools_100pct.csv` | PRO-12 | number of schools, and schools with a 100% result by management | 2017-2026 |
| `district_schools_0pct.csv` | PRO-13 | schools with a 0% result (only districts with such a school are listed in some years) | 2017-2026 |
| `district_all_candidates_2014_2018.csv` | `5years.xlsx` | all candidates appeared / passed by sex | 2014-2018 |
| `taluk_regular_fresh.csv` | PRO-8 | 204 taluks; regular freshers **excluding** Morarji Desai residential and corporation schools | 2017-2026 |
| `school_regular_fresh_2018_2019.csv` | four division workbooks per year | every school: code, name, taluk, appeared / passed by sex (about 14,300 schools a year) | 2018, 2019 only |
| `district_school_dispersion_2018_2019.csv` | derived | per district: share of schools (10+ candidates) at 100%, at 95%+, spread of school pass rates | 2018, 2019 |
| `_build_log_district_tables.txt` | - | which sheet was read for which year, rows found | - |

Known quirks:
- In 2015-2023 the "repeaters" sheet (PRO-11) already contains private repeaters; PRO-11B is a
  subset. All candidates = PRO-5 + PRO-11 + PRO-11A reproduces the published state totals
  exactly for 2019, 2020, 2022 and 2023. In the 2024 workbook the four types are separate.
- One blank cell in the 2024 workbook (PRO-4, Vijayapura girls appeared); PRO-5 is complete.
- 2021 is the COVID two-day exam: 99.99% passed; drop it from any trend analysis.
- The 2024 workbook is the cumulative file; a few of its sheet titles still say
  "EXAMINATION-1", but their totals match the cumulative totals.

## Hand-transcribed press-note tables (`data\clean\transcribed\`)

The 2024-2026 press notes are scanned images. These tables were typed by hand from the page
images and then checked: every row's recomputed percentage equals the printed one and the
column sums equal the printed state totals (2025, 2026 exactly; 2024 passed exactly, appeared
sums to 859,300 against a printed state total of 859,967 - the gap is in the board's table).

| File | Contents | Source |
|---|---|---|
| `exam1_2024_district_all_candidates.csv` | 35 districts, **all candidates**, 2024 Exam-1, after the 20% grace; with the board's 2024 and 2023 ranks | `PN_2024_Exam1.pdf` p. 11 |
| `exam1_2025_district_regular_fresh.csv` | 35 districts, **regular freshers**, 2025 Exam-1 | `PN_2025_Exam1.pdf` p. 8 |
| `exam1_2026_district_regular_fresh.csv` | 35 districts, **regular freshers**, 2026 Exam-1; plus printed 2025 cumulative % | `PN_2026_Exam1.pdf` p. 7 |
| `state_first_exam_series.csv` | state totals by year for all candidates, regular freshers, and cumulative | workbooks and press notes (column `source`) |
| `state_first_exam_by_group.csv` | Exam-1 by management, medium, gender, urban/rural | press notes |
| `state_grade_distribution_first_exam.csv` | regular-fresher passes by grade, 2023-2026 | press notes |

**Sean should re-check the three district tables against the PDFs himself** (it takes about
20 minutes) before any number goes into a paper.

## Analysis panel (`code\12_build_panel.py`)

`panel_district_year.csv` - one row per `unit` (34), `year`, `series`:

| Column | Meaning |
|---|---|
| `unit`, `unit_name`, `division` | district code (TA merged into TT), name, board division |
| `series` | `S1` all candidates, first/main exam (2014-2024) - `S2` regular freshers, first/main exam (2015, 2017-2023, 2025, 2026) - `S3` regular freshers cumulative (2024-2026) |
| `app`, `passed`, `pass_pct` | appeared, passed, 100 x passed / appeared |
| `exam`, `source` | exam label and where the numbers came from |
| `n_parts` | 2 where Ballari and Vijayanagara were summed |

**Gap that cannot be filled from public files:** district results for *regular freshers at
Exam-1 2024*, and for *all candidates at Exam-1 2025 and 2026*. So S1 ends in 2024 and S2
skips 2024.
