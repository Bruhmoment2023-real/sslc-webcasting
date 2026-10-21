# Pass rates after exam webcasting: a descriptive district analysis of Karnataka's SSLC examination, 2014-2026

Archived on Zenodo: https://doi.org/10.5281/zenodo.23537690 (this DOI always points to the latest version).

Sean Solano Paul, Independent researcher, Bengaluru, India. Funding: none. Competing interests: none.

## Summary

In March 2024 Karnataka began live webcasting of every centre of its Class 10 board examination (SSLC) to district control rooms. The first-exam
pass rate fell from 83.89% in 2023 to 73.40% in 2024, and even that figure came after the board raised grace marks to 20% as a one-time measure;
reports put the pass rate before grace at about 54%. In 2025, with webcasting continued and the extra grace removed, the rate was 62.34%. This
repository holds a panel of the 34 educational districts from 2014 to 2026 built from the board's workbooks and press notes (every hand-typed cell
checked against the scanned pages), the code that builds and analyses it, and the results. The design is descriptive: every centre was webcast in the
same exam and several other changes arrived at once, so the data cannot separate the effect of cameras from the rest. Districts with higher pass rates
in 2023 did not fall more than ordinary mean reversion would predict (slope -0.38, against -0.66 to +0.15 in earlier years); districts whose results
had risen most between 2019 and 2023 did fall more (slope -0.75, p = 0.006); and the order of districts was reshuffled once (rank correlation between
consecutive exams 0.56-0.92 before, 0.23 for 2023-24, then 0.80-0.88).

## Repository layout

| Path | Contents |
|---|---|
| `data/clean/` | Tidy district-level tables and the 34-district panel (`panel_district_year.csv`); `DATA_DICTIONARY.md`; `transcribed/` holds hand-transcribed state and 2024-2026 tables |
| `code/` | Pipeline scripts, numbered in run order (`00`-`07` inspection, extraction and literature scripts; `10`-`13` table building; `20`-`21` analysis) and `common.py` |
| `results/` | Frozen pre-specification (`PRESPEC_frozen_before_analysis.md`), `RESULTS_SUMMARY.md`, analysis and post-hoc logs, `tables/`, `figures/` |
| `followup/` | Follow-up analyses: II PUC (Class 12) comparison, learning-gap (NAS 2021) test, OCR verification of the 2024-2026 tables (`code/`, `data/`, `results/`) |
| `docs/` | Facts timeline, prior-work notes, design, follow-up notes (`facts-update`, `puc-comparison`, `learning-gap-test`, `table-recheck`), appendix data dictionary |
| `literature/` | `citations/references.bib`, `citations/references.ris` |
| `bibliometrics/` | A literature map (OpenAlex-based): scripts, tables, figures, search protocol, cleaned corpus metadata |

## How to reproduce

Python 3.12. Install: `pip install -r requirements.txt`. Run from `code/`.

The analysis starts from `data/clean/`, which is included, so steps 2-4 run without any download. (Checked: `20_analysis.py` reproduced `results/tables/T3_placebo_slopes.csv` exactly.)

1. Optional rebuild from the Board's files (download them first, see below): `python 01_dump_sheets.py RAW_WORKBOOK_DIR DUMP_DIR`, then `python 10_build_district_tables.py DUMP_DIR ../data/clean` and `python 13_build_school_taluk_tables.py DUMP_DIR ../data/clean`.
2. `python 11_validate_tables.py ../data/clean` (checks the tables against published state totals).
3. `python 12_build_panel.py ../data/clean`
4. `python 20_analysis.py ../data/clean ../results` and `python 21_posthoc.py ../data/clean ../results` (create `../results/tables` and `../results/figures` first if absent).
5. Follow-up: scripts in `followup/code/` (`f10`/`f20` for the II PUC comparison, `f30` for the learning-gap test; `f0*` and `g*` are OCR/extraction helpers that need the original PDFs).

## Data sources and licences

| Source | Used for | Licence / terms |
|---|---|---|
| KSEAB result statistics workbooks (district-wise, 2014-2026) | District panel | Public documents of the Board; Board terms apply. Not included. Download from https://kseab.karnataka.gov.in/new-page/Result%20Statistics/en |
| KSEAB press notes (SSLC), notifications and exam guidelines | Pass rates, grace-mark rules, webcasting facts | As above. Not included. https://kseab.karnataka.gov.in/198/press-note%28sslc%29--/en and the Board's notifications and circulars pages |
| Newspaper reports (e.g. Deccan Herald) | Timeline of announcements | Publisher copyright. Not included; cited in `docs/01-facts-timeline.md` |
| II PUC (Class 12) results and NAS 2021 district tables | Follow-up comparisons | Public Government documents; not included, only the aggregated values in `followup/data/` |
| OpenAlex, Crossref metadata | Literature map | OpenAlex is CC0 |
| Derived tables, figures, results | `data/clean/`, `results/`, `followup/` | CC BY 4.0 (`LICENSE-DATA.md`) |
| Code | All scripts | MIT (`LICENSE`) |

## Not included and why

- Abstract text of third-party papers (the `abstract`/`AB` columns and abstract-derived quote columns of the bibliographic tables, and abstract fields in the OpenAlex JSON). Identifiers, titles, years, venues, keywords and citation data are kept; re-fetch abstracts with the bibliometrics pipeline if needed.
- Per-paper reading notes on the literature (they contain quotations from copyrighted papers) and the literature gap-analysis note (scoping). The scripts that built the notes are kept; run them on your own copies of the papers.
- The Board's original workbooks, PDFs, press notes and web-page captures (`data/raw/`, about 130 MB), saved news-article copies, extracted PDF text, sheet dumps and Wayback captures - third-party documents; fetch from the URLs above (the scripts take their locations as arguments).
- `followup/raw/` (about 1.1 GB: scanned pages, OCR scratch and downloaded PDFs) - third-party documents and scratch; the verified tables derived from them are in `followup/data/`.
- Full-text PDFs of papers, raw API responses and `.rds` caches in `bibliometrics/` (regenerate with `bibliometrics/python/pipeline.py`); interactive HTML figures and JavaScript libraries (PNG/SVG kept).
- Virtual environment, caches and scratch files.

Before-grace district pass rates for 2024 are not published by the Board and are not in this repository.

## Citation

Solano Paul, S. (2026). *Pass rates after exam webcasting: a descriptive district analysis of Karnataka's SSLC examination, 2014-2026* (software and data repository). See `CITATION.cff`. A Zenodo DOI will be added when the repository is made public.
