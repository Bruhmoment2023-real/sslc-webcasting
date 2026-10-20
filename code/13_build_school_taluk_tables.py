"""Tidy the school-wise (2018, 2019) and taluk-wise (2017-2026) result tables.

Usage: python 13_build_school_taluk_tables.py DUMP_DIR CLEAN_DIR
School-wise files are the board's own bulk publication of school aggregates for regular freshers
(April 2018 and April 2019 only). They contain school names and counts, no student-level data.
"""
import sys, os, re, glob
import pandas as pd
from common import DIVISION, MERGE

dump, clean = sys.argv[1], sys.argv[2]


def num(x):
    try:
        return float((x or '').replace(',', '').strip())
    except ValueError:
        return None


# ---- schools ----
rows = []
for f in sorted(glob.glob(os.path.join(dump, 'schoolwise_201*__*.txt'))):
    stem = os.path.basename(f)
    year = int(stem[11:15])
    division_file = stem.split('_')[2]
    for line in open(f, encoding='utf-8'):
        cells = [x.strip() for x in line.rstrip('\n').split('|')]
        if len(cells) >= 17 and re.fullmatch(r'[A-Z]{2}', cells[1]) and re.fullmatch(r'[A-Z]{2}\d{4}', cells[5] or ''):
            v = [num(x) for x in cells[8:17]]
            rows.append(dict(year=year, division_file=division_file, dist_code=cells[1], dist_name=cells[2].upper(),
                             taluk_code=cells[3], taluk_name=cells[4], school_code=cells[5], school_name=cells[6],
                             boys_app=v[0], boys_pass=v[1], girls_app=v[3], girls_pass=v[4], app=v[6], passed=v[7], pct=v[8],
                             source_file=stem.split('__')[0] + '.xlsx'))
s = pd.DataFrame(rows)
s.to_csv(os.path.join(clean, 'school_regular_fresh_2018_2019.csv'), index=False)
print('schools:', s.groupby('year').agg(n=('school_code', 'nunique'), app=('app', 'sum'), passed=('passed', 'sum')).to_string())
dv = s.groupby(['division_file', 'dist_code']).size().reset_index()[['division_file', 'dist_code']].drop_duplicates()
dv['assumed'] = dv.dist_code.map(DIVISION)
print('division of each district according to the school files vs the mapping in common.py:')
print(dv.to_string(index=False))

# district-level markers from the school files
s['unit'] = s.dist_code.replace(MERGE)
big = s[s.app >= 10]
mk = big.groupby(['unit', 'year']).apply(lambda d: pd.Series({
    'n_schools_10plus': len(d),
    'share_schools_100pct': (d.passed == d.app).mean(),
    'share_schools_95plus': (d.pct >= 95).mean(),
    'share_students_in_100pct_schools': d.loc[d.passed == d.app, 'app'].sum() / d.app.sum(),
    'school_pass_sd': d.pct.std(),
    'school_pass_p10': d.pct.quantile(.1), 'school_pass_median': d.pct.median(), 'school_pass_p90': d.pct.quantile(.9),
}), include_groups=False).reset_index()
mk.to_csv(os.path.join(clean, 'district_school_dispersion_2018_2019.csv'), index=False)

# ---- taluks (PRO-8) ----
BOOKS = {'SSLCAPR2017': (2017, 'main_exam'), 'PROFORMA_APRIL_2018': (2018, 'main_exam'), 'PROFORMA_APRIL_2019': (2019, 'main_exam'),
         'PROFORMA_JUNE_JULY_2020_LATEST': (2020, 'main_exam'), 'PROFORMA_JULY_2021': (2021, 'main_exam'),
         'PROFORMA_APRIL_2022_FINAL': (2022, 'main_exam'), 'PROFORMA_APRIL_2023_FINAL': (2023, 'main_exam'),
         'SSLC_2024_best_of_3_proforma': (2024, 'best_of_3'), 'SSLC_2025_best_of_3_proforma': (2025, 'best_of_3'),
         'SSLC_2026_best_of_2_proforma': (2026, 'best_of_2'), 'April_2015_stats': (2015, 'main_exam')}
trow = []
for stem, (yr, scope) in BOOKS.items():
    fs = [p for p in glob.glob(os.path.join(dump, stem + '__*.txt')) if re.sub(r'[^A-Z0-9]', '', os.path.basename(p).split('__')[1][:-4].upper()) == 'PRO8']
    if not fs:
        print(stem, 'no PRO-8 sheet'); continue
    n = 0
    for line in open(fs[0], encoding='utf-8'):
        cells = [x.strip() for x in line.rstrip('\n').split('|')]
        for i in range(min(3, len(cells))):
            if re.fullmatch(r'[A-Z]{2}', cells[i]) and i + 3 < len(cells) and re.fullmatch(r'[A-Z]{2}\d{2}', cells[i + 2]):
                v = [num(x) for x in cells[i + 4:i + 13]]
                v += [None] * (9 - len(v))
                trow.append(dict(year=yr, scope=scope, dist_code=cells[i], dist_name=cells[i + 1].upper(), taluk_code=cells[i + 2],
                                 taluk_name=cells[i + 3].upper(), boys_app=v[0], boys_pass=v[1], girls_app=v[3], girls_pass=v[4],
                                 app=v[6], passed=v[7], pct=v[8], source_file=stem + '.xlsx'))
                n += 1
                break
    print(stem, 'taluk rows', n)
t = pd.DataFrame(trow)
t.to_csv(os.path.join(clean, 'taluk_regular_fresh.csv'), index=False)
print(t.groupby('year').agg(n=('taluk_code', 'nunique'), app=('app', 'sum'), passed=('passed', 'sum'), na=('app', lambda x: x.isna().sum())).to_string())
