"""Check the tidy district tables against published state totals. Usage: python 11_validate_tables.py CLEAN_DIR"""
import sys, os
import pandas as pd
from common import read
c = sys.argv[1]
pd.set_option('display.width', 200)
g = read(os.path.join(c, 'district_regular_fresh_by_gender.csv'))
print('Regular freshers, sum over districts (PRO-5):')
t = g.groupby('year').agg(n_dist=('dist_code', 'nunique'), app=('app', 'sum'), passed=('passed', 'sum'), na=('app', lambda s: s.isna().sum()))
t['pct'] = (100 * t.passed / t.app).round(2); print(t)
o = read(os.path.join(c, 'district_other_candidate_types.csv'))
ot = o.groupby(['year', 'cand_type'])[['app', 'passed']].sum().unstack()
print('\nOther candidate types (sum over districts):'); print(ot)
allc = (g.groupby('year')[['app', 'passed']].sum() + o.groupby('year')[['app', 'passed']].sum())
allc['pct'] = (100 * allc.passed / allc.app).round(2)
print('\nConstructed all-candidates = PRO-5 + PRO-11 + 11A + 11B:'); print(allc)
a = read(os.path.join(c, 'district_all_candidates_2014_2018.csv'))
at = a.groupby('year')[['app', 'passed']].sum(); at['pct'] = (100 * at.passed / at.app).round(2)
print('\n5-years workbook, all candidates:'); print(at)
# district-level comparison constructed vs published for 2017, 2018
cons = pd.concat([g[['year', 'dist_code', 'app', 'passed']], o[['year', 'dist_code', 'app', 'passed']]]).groupby(['year', 'dist_code'], as_index=False).sum()
mrg = cons.merge(a[['year', 'dist_code', 'app', 'passed']], on=['year', 'dist_code'], suffixes=('_cons', '_pub'))
mrg['d_app'] = mrg.app_cons - mrg.app_pub; mrg['d_pass'] = mrg.passed_cons - mrg.passed_pub
print('\nConstructed minus published by district (2015, 2017, 2018):'); print(mrg.groupby('year')[['d_app', 'd_pass']].agg(['min', 'max', 'sum']))
for f in ['district_regular_fresh_by_management.csv', 'district_regular_fresh_by_subject.csv']:
    d = read(os.path.join(c, f)); k = [x for x in ('management', 'subject') if x in d.columns][0]
    s = d.groupby(['year', k])[['app', 'passed']].sum(); s['pct'] = (100 * s.passed / s.app).round(2)
    print('\n', f); print(s['pct'].unstack().round(2)); print(s['app'].unstack())
gr = read(os.path.join(c, 'district_regular_fresh_grade_distribution.csv'))
print('\nGrade distribution, state sums:'); print(gr.groupby('year')[['app', 'passed', 'A_plus', 'A', 'B_plus', 'B', 'C_plus', 'C']].sum())
