# Task 1 - Re-check of the three hand-typed district tables

Run 13 October 2026. Result: **0 discrepancies in 420 cells. No analysis changes.** Details and limits below.

## What was checked

| Table | Source page | Rows | Cells compared (app, passed, pct, plus ranks for 2024) |
|---|---|---|---|
| Exam-1 2024, all candidates, after grace, with 2024/2023 ranks | `PN_2024_Exam1.pdf` p. 11 | 35 | 35 x 5 = 175 |
| Exam-1 2025, regular freshers | `PN_2025_Exam1.pdf` p. 8 | 35 | 35 x 3 = 105 (+ total row) |
| Exam-1 2026, regular freshers (and printed 2025 cumulative %) | `PN_2026_Exam1.pdf` p. 7 | 35 | 35 x 4 = 140 (+ total row) |

Total 420 cells (the earlier agent's log counts 420).

## Method (three independent passes)

1. **Free OCR, installed inside the project folder without admin rights.** RapidOCR (ONNX runtime) in `followup\.venv-ocr`, run on 300 dpi renders of the three pages (`code\f01_ocr_pages.py`, outputs in `raw\ocr\`). The OCR reads the page images and knows nothing of the CSVs. `code\f02_compare_ocr.py` compares OCR to the pack CSVs cell by cell. Log: `data\ocr_comparison_log.txt`.
2. **Arithmetic checks.** Every row's `100 x passed / appeared` equals the printed percentage (to 0.01) in all 105 rows; column sums equal the printed TOTAL rows (2025: 790,890 / 523,075 / 66.14; 2026: 770,209 / 724,794 / 94.10). 2024 ranks are 1..35 in order and the 2023 ranks are a permutation of 1..35; 2024 percentages are non-increasing down the table.
3. **My own cell-by-cell reading of the 2024 page image** (`raw\pages\PN_2024_Exam1_p11.png`, viewed in full, all 35 rows, every number). All 35 rows match the CSV. (The 2025 and 2026 pages were checked by OCR plus the arithmetic and total-row checks only, not re-read by eye by me.)

Corrected copies are in `data\` (`exam1_2024_district_all_candidates_verified.csv`, `exam1_2025_district_regular_fresh_verified.csv`, `exam1_2026_district_regular_fresh_verified.csv`). A byte comparison (`diff`) shows they are **identical to the pack's `data\clean\transcribed\` files**, because there was nothing to correct. The pack files were not edited.

## Discrepancy list

None between the typed CSVs and the page images.

One item is in the board's printed table, not in the typing:

- **2024: the district rows sum to 859,300 appeared; the board's Table 1 (state total) prints 859,967** (difference 667). Passed sums to 631,204 exactly, matching the state total. The 2024 table appears to be missing or understating 667 appeared candidates somewhere; I cannot say which district. The district percentages use the district rows as printed. Effect on any result: none of the pack's district analyses use the 859,300 total itself; the one place it could matter is a candidate-weighted regression (weights are 2023 appeared, not 2024), so no weighted result is affected. Percentages recompute exactly from the printed counts in every row, so the gap is not a misprint in a percentage.
- The 2025 and 2026 tables print **regular fresher** totals (790,890 and 770,209), not all-candidate totals (842,173 and 856,516); this is a population difference, not an error (already documented in the pack).

## Re-run of affected analyses

Because the corrected files are byte-identical to the pack's, every number computed from them is unchanged: the pack's `20_analysis.py` / `21_posthoc.py` outputs (H1 slope -0.38 s.e. 0.33; H2 -0.75 s.e. 0.27; rank correlation 0.23 for 2023-24; 2024 vs 2025 0.88; 2025 vs 2026 0.80) stand. I did not re-execute those scripts; reproducing an identical input file cannot change them. If Sean wants a visible re-run, `code\20_analysis.py` in the pack is the one to run with the pack `.venv`.

## Limits

- OCR and my reading agree, but both read the same scan. A mistake printed in the scan itself would pass every check here. Only the total-row and percentage recomputation catch that, and they pass.
- The 2025 and 2026 pages were not re-read by eye by me; they were cleared by independent OCR (210 cells identical) plus two arithmetic checks.

Status label: tables are **confirmed from a primary source** (KSEAB press notes).
