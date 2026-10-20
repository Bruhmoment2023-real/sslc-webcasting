"""Assemble the district panel used in the analysis.

Usage: python 12_build_panel.py CLEAN_DIR
Output: CLEAN_DIR/panel_district_year.csv with one row per (unit, year, series):
  series S1 = all candidates, first/main exam
  series S2 = regular freshers, first/main exam
  series S3 = regular freshers, cumulative best of Exams 1-3 (2024, 2025) or 1-2 (2026)
Vijayanagara (TA) is merged into Ballari (TT) so the same 34 units exist every year.
"""
import sys, os
import pandas as pd
from common import read, DIST, NAME2CODE, MERGE, DIVISION

c = sys.argv[1]
rows = []


def add(df, series, exam_note, source):
    for r in df.itertuples():
        rows.append(dict(dist_code=r.dist_code, year=int(r.year), series=series, app=r.app, passed=r.passed,
                         exam=exam_note if isinstance(exam_note, str) else getattr(r, exam_note), source=source))


g = read(os.path.join(c, 'district_regular_fresh_by_gender.csv'))
o = read(os.path.join(c, 'district_other_candidate_types.csv'))
a = read(os.path.join(c, 'district_all_candidates_2014_2018.csv'))

# S2: regular freshers at the main exam (workbooks up to 2023)
add(g[g.scope == 'main_exam'], 'S2', 'exam', 'KSEAB proforma workbook, PRO-5')
# S3: cumulative best-of-N (workbooks 2024-2026)
add(g[g.scope != 'main_exam'], 'S3', 'exam', 'KSEAB proforma workbook, PRO-5 (cumulative)')

# S1 2014-2018: published directly
a['exam'] = 'April ' + a.year.astype(str) + ' main'
add(a, 'S1', 'exam', 'KSEAB 5years.xlsx')
# S1 2019-2023: regular freshers + regular repeaters (PRO-11) + private freshers (PRO-11A).
# PRO-11B (private repeaters) is already contained in PRO-11 in these years (checked against state totals).
parts = pd.concat([g[g.scope == 'main_exam'][['year', 'dist_code', 'app', 'passed']],
                   o[(o.scope == 'main_exam') & o.cand_type.isin(['regular_repeater', 'private_fresher'])][['year', 'dist_code', 'app', 'passed']]])
s1 = parts[parts.year >= 2019].groupby(['year', 'dist_code'], as_index=False)[['app', 'passed']].sum()
s1['exam'] = s1.year.astype(str) + ' main (constructed from PRO-5 + PRO-11 + PRO-11A)'
add(s1, 'S1', 'exam', 'KSEAB proforma workbook, PRO-5 + PRO-11 + PRO-11A')

# Press-note tables (hand-transcribed and checked against the printed percentages and totals)
t = os.path.join(c, 'transcribed')
for f, yr, series, note in (('exam1_2024_district_all_candidates.csv', 2024, 'S1', '2024 Exam-1 (after 20 per cent grace)'),
                            ('exam1_2025_district_regular_fresh.csv', 2025, 'S2', '2025 Exam-1'),
                            ('exam1_2026_district_regular_fresh.csv', 2026, 'S2', '2026 Exam-1 (33 per cent pass rule)')):
    d = pd.read_csv(os.path.join(t, f))
    d['dist_code'] = d.dist_name.map(NAME2CODE)
    assert d.dist_code.notna().all(), d[d.dist_code.isna()]
    d['year'] = yr
    add(d, series, note, 'KSEAB press note, district table')

p = pd.DataFrame(rows)
p['unit'] = p.dist_code.replace(MERGE)
p = p.groupby(['unit', 'year', 'series'], as_index=False).agg(app=('app', 'sum'), passed=('passed', 'sum'),
                                                              exam=('exam', 'first'), source=('source', 'first'),
                                                              n_parts=('dist_code', 'nunique'))
p['unit_name'] = p.unit.map(DIST)
p.loc[p.unit == 'TT', 'unit_name'] = 'BALLARI (incl. VIJAYANAGARA)'
p['division'] = p.unit.map(DIVISION)
p['pass_pct'] = 100 * p.passed / p.app
p = p[['unit', 'unit_name', 'division', 'year', 'series', 'app', 'passed', 'pass_pct', 'exam', 'source', 'n_parts']].sort_values(['series', 'year', 'unit'])
p.to_csv(os.path.join(c, 'panel_district_year.csv'), index=False)

chk = p.groupby(['series', 'year']).agg(units=('unit', 'nunique'), app=('app', 'sum'), passed=('passed', 'sum'))
chk['pct'] = (100 * chk.passed / chk.app).round(2)
print(chk.to_string())
