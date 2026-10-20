"""Cell-by-cell comparison of the OCR re-extraction with the pack's hand-typed CSVs.
Usage: python f02_compare_ocr.py OCR_DIR TRANSCRIBED_DIR OUT_DIR"""
import sys, os, re, shutil
import pandas as pd
ocr, tr, out = sys.argv[1:4]
os.makedirs(out, exist_ok=True)
SPEC = [('ocr_PN_2024_Exam1_p11_rows.txt', 'exam1_2024_district_all_candidates.csv', ['app', 'passed', 'pct_printed', 'rank_2024', 'rank_2023'], (859967, 631204, 73.40)),
        ('ocr_PN_2025_Exam1_p08_rows.txt', 'exam1_2025_district_regular_fresh.csv', ['app', 'passed', 'pct_printed'], None),
        ('ocr_PN_2026_Exam1_p07_rows.txt', 'exam1_2026_district_regular_fresh.csv', ['app', 'passed', 'pct_printed', 'pct_2025_best_of_3_printed'], None)]
norm = lambda s: re.sub(r'[^A-Z]', '', s.upper()).replace('VIUAY', 'VIJAY')
lines = []
P = lambda *a: (print(*a), lines.append(' '.join(str(x) for x in a)))
tot_cells = tot_diff = 0
for of, cf, cols, printed in SPEC:
    P('\n=====', cf, 'vs', of)
    rows, total = {}, None
    for ln in open(os.path.join(ocr, of), encoding='utf-8'):
        p = [x.strip() for x in ln.strip().split('|')]
        if re.fullmatch(r'\d{1,2}', p[0]) and len(p) == len(cols) + 2:
            rows[norm(p[1])] = [float(x) for x in p[2:]]
        elif 'TOTAL' in p[0].upper() and len(p) >= 4:
            total = [float(x) for x in p[1:]]
    d = pd.read_csv(os.path.join(tr, cf))
    P('rows in CSV', len(d), '| rows recovered by OCR', len(rows))
    nd = 0
    for r in d.itertuples():
        k = norm(r.dist_name)
        if k not in rows:
            P('  NOT FOUND IN OCR:', r.dist_name); nd += 1; continue
        for c, v in zip(cols, rows[k]):
            tot_cells += 1
            if abs(float(getattr(r, c)) - v) > 1e-9:
                P(f'  DISCREPANCY {r.dist_name} {c}: csv={getattr(r, c)} ocr={v}'); nd += 1
    extra = set(rows) - set(norm(x) for x in d.dist_name)
    if extra: P('  IN OCR BUT NOT CSV:', extra); nd += len(extra)
    tot_diff += nd
    P('cell discrepancies:', nd)
    # row check: recomputed percentage v printed
    rc = (100 * d.passed / d.app).round(2)
    bad = d[(rc - d.pct_printed).abs() > 0.011]
    P('rows whose recomputed % differs from printed by >0.01:', len(bad))
    if len(bad): P(bad.assign(recomputed=rc[bad.index]).to_string())
    P('column sums (CSV): appeared', int(d.app.sum()), 'passed', int(d.passed.sum()), 'pct', round(100 * d.passed.sum() / d.app.sum(), 2))
    if total: P('printed TOTAL row (OCR):', total, '| match:', int(total[0]) == d.app.sum() and int(total[1]) == d.passed.sum())
    if printed: P('state total printed elsewhere in the note (Table 1):', printed, '| district-table sum differs by', printed[0] - d.app.sum(), 'appeared and', printed[1] - d.passed.sum(), 'passed')
    if 'rank_2024' in d: P('rank_2024 is 1..35 in order:', list(d.rank_2024) == list(range(1, 36)), '| rank_2023 is a permutation of 1..35:', sorted(d.rank_2023) == list(range(1, 36)),
                           '| pct non-increasing:', d.pct_printed.is_monotonic_decreasing)
    shutil.copy(os.path.join(tr, cf), os.path.join(out, cf.replace('.csv', '_verified.csv')))
P('\nTOTAL cells compared:', tot_cells, '| discrepancies:', tot_diff)
open(os.path.join(out, 'ocr_comparison_log.txt'), 'w', encoding='utf-8').write('\n'.join(lines))
