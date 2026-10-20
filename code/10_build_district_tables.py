"""Build tidy CSVs from the KSEAB result-statistics workbooks (via the sheet dumps made by 01_dump_sheets.py).

Usage: python 10_build_district_tables.py DUMP_DIR CLEAN_DIR
Every output row carries `source_file` and `sheet` so each number can be traced to the raw workbook.
No student-level data is read; all tables are aggregates published by the board.
"""
import sys, os, re, glob
import pandas as pd

dump, clean = sys.argv[1], sys.argv[2]
os.makedirs(clean, exist_ok=True)

# workbook stem -> (exam year, exam label, scope)
BOOKS = {
    'April_2015_stats': (2015, 'April 2015 main', 'main_exam'),
    'SSLCAPR2017': (2017, 'April 2017 main', 'main_exam'),
    'PROFORMA_APRIL_2018': (2018, 'April 2018 main', 'main_exam'),
    'PROFORMA_APRIL_2019': (2019, 'April 2019 main', 'main_exam'),
    'PROFORMA_JUNE_JULY_2020_LATEST': (2020, 'June/July 2020 main (COVID-delayed)', 'main_exam'),
    'PROFORMA_JULY_2021': (2021, 'July 2021 (COVID two-day MCQ exam, all passed)', 'main_exam'),
    'PROFORMA_APRIL_2022_FINAL': (2022, 'March/April 2022 main', 'main_exam'),
    'PROFORMA_APRIL_2023_FINAL': (2023, 'March/April 2023 main', 'main_exam'),
    'SSLC_2024_best_of_3_proforma': (2024, '2024 best of Exams 1-3 (cumulative)', 'best_of_3'),
    'SSLC_2025_best_of_3_proforma': (2025, '2025 best of Exams 1-3 (cumulative)', 'best_of_3'),
    'SSLC_2026_best_of_2_proforma': (2026, '2026 best of Exams 1-2 (cumulative)', 'best_of_2'),
}
CODE = re.compile(r'^[A-Z]{2}$')


def num(x):
    x = (x or '').strip().replace(',', '')
    try:
        return float(x)
    except ValueError:
        return None


def read_rows(path):
    """Yield (code, name, [values after name]) for each district row in a dumped sheet."""
    with open(path, encoding='utf-8') as fh:
        for line in fh:
            cells = [c.strip() for c in line.rstrip('\n').split('|')]
            for i, c in enumerate(cells[:4]):
                if CODE.match(c) and i + 1 < len(cells) and re.search('[A-Za-z]{3}', cells[i + 1]):
                    yield c, cells[i + 1].upper(), [num(v) for v in cells[i + 2:]]
                    break


def title(path):
    with open(path, encoding='utf-8') as fh:
        return ' / '.join(l.strip('|\n ').replace('|', ' ') for l in list(fh)[:5])[:400]


def norm(name):
    """PRO-2A(1), PRO_2A_1 and PRO-2A_1_ all become PRO2A1 (sheet names differ between years)."""
    return re.sub(r'[^A-Z0-9]', '', name.upper())


def sheet_path(stem, *names):
    have = {norm(os.path.basename(p).split('__', 1)[1][:-4]): p for p in glob.glob(os.path.join(dump, stem + '__*.txt'))}
    for n in names:
        if norm(n) in have:
            return have[norm(n)]
    return None


log = []


def collect(sheet_names, cols, must_contain):
    """sheet_names: candidate sheet names; cols: names for the numeric values after the district name."""
    out = []
    for stem, (yr, label, scope) in BOOKS.items():
        p = sheet_path(stem, *sheet_names)
        if not p:
            log.append(f'{stem}: sheet {sheet_names} MISSING')
            continue
        t = re.sub(r'\s+', ' ', title(p).upper())  # collapses double and non-breaking spaces
        if not all(k in t for k in must_contain):
            log.append(f'{stem}: {os.path.basename(p)} TITLE MISMATCH -> {t[:160]}')
            continue
        n = 0
        for code, name, vals in read_rows(p):
            vals = (vals + [None] * len(cols))[:len(cols)]
            out.append(dict(year=yr, exam=label, scope=scope, dist_code=code, dist_name=name,
                            **dict(zip(cols, vals)), source_file=stem + '.xlsx',
                            sheet=os.path.basename(p).split('__')[1][:-4]))
            n += 1
        log.append(f'{stem}: {os.path.basename(p)} rows={n}')
    return pd.DataFrame(out)


KEYS = ['year', 'exam', 'scope', 'dist_code', 'dist_name', 'source_file']

# 1. District x gender, regular freshers (PRO-5)
g = collect(['PRO-5'], ['boys_app', 'boys_pass', 'boys_pct', 'girls_app', 'girls_pass', 'girls_pct', 'app', 'passed', 'pct'],
            ['GENDER', 'DISTRICT'])
g.to_csv(os.path.join(clean, 'district_regular_fresh_by_gender.csv'), index=False)

# 2. District x management type (PRO-7A boys + PRO-7B girls), regular freshers
parts = []
for nm, sex in ((['PRO-7A'], 'boys'), (['PRO-7B'], 'girls')):
    d = collect(nm, ['govt_app', 'govt_pass', 'govt_pct', 'aided_app', 'aided_pass', 'aided_pct',
                     'unaided_app', 'unaided_pass', 'unaided_pct'], ['SCHOOL TYPE'])
    d['sex'] = sex
    parts.append(d)
m = pd.concat(parts)
m.to_csv(os.path.join(clean, 'district_regular_fresh_by_management_sex.csv'), index=False)
long = []
for mg in ('govt', 'aided', 'unaided'):
    s = m.groupby(KEYS, as_index=False)[[f'{mg}_app', f'{mg}_pass']].sum(min_count=1)
    s = s.rename(columns={f'{mg}_app': 'app', f'{mg}_pass': 'passed'})
    s['management'] = mg
    long.append(s)
ml = pd.concat(long)
ml['pct'] = 100 * ml.passed / ml.app
ml.to_csv(os.path.join(clean, 'district_regular_fresh_by_management.csv'), index=False)

# 3. District x urban/rural (PRO-6A)
u = collect(['PRO-6A'], ['b_rur_app', 'b_rur_pass', 'b_rur_pct', 'b_urb_app', 'b_urb_pass', 'b_urb_pct',
                         'g_rur_app', 'g_rur_pass', 'g_rur_pct', 'g_urb_app', 'g_urb_pass', 'g_urb_pct',
                         'rural_app', 'rural_pass', 'rural_pct', 'urban_app', 'urban_pass', 'urban_pct'], ['URBAN'])
u.to_csv(os.path.join(clean, 'district_regular_fresh_by_urban_rural.csv'), index=False)

# 4. District x subject (PRO-2A(1): lang1, lang2; (2): lang3, maths; (3): science, social science)
subj = []
for nm, pair in ((['PRO-2A_1_'], ('language_1', 'language_2')),
                 (['PRO-2A_2_'], ('language_3', 'mathematics')),
                 (['PRO-2A_3_'], ('science', 'social_science'))):
    cols = [f'{s}_{x}' for s in ('s1', 's2') for x in ('b_app', 'b_pass', 'b_pct', 'g_app', 'g_pass', 'g_pct')]
    d = collect(nm, cols, ['SUBJECT'])
    for k, sname in zip(('s1', 's2'), pair):
        e = d[KEYS + ['sheet']].copy()
        e['subject'] = sname
        for c in ('b_app', 'b_pass', 'g_app', 'g_pass'):
            e[c] = d[f'{k}_{c}']
        e['app'] = e.b_app + e.g_app
        e['passed'] = e.b_pass + e.g_pass
        subj.append(e)
sj = pd.concat(subj)
sj['pct'] = 100 * sj.passed / sj.app
sj.to_csv(os.path.join(clean, 'district_regular_fresh_by_subject.csv'), index=False)

# 5. District grade distribution (PRO-16)
gr = collect(['PRO-16'], ['app', 'passed', 'A_plus', 'A', 'B_plus', 'B', 'C_plus', 'C'], ['GRADE'])
gr.to_csv(os.path.join(clean, 'district_regular_fresh_grade_distribution.csv'), index=False)

# 6. Other candidate types by district (PRO-11 repeaters, 11A private freshers, 11B private repeaters)
oc = []
for nm, typ in ((['PRO-11'], 'regular_repeater'), (['PRO-11A'], 'private_fresher'), (['PRO-11B'], 'private_repeater')):
    d = collect(nm, ['boys_app', 'girls_app', 'app', 'boys_pass', 'girls_pass', 'passed', 'pct'], ['DIST'])
    d['cand_type'] = typ
    oc.append(d)
pd.concat(oc).to_csv(os.path.join(clean, 'district_other_candidate_types.csv'), index=False)

# 7. Malpractice cases booked (PRO-10)
mp = collect(['PRO-10'], ['govt_girl', 'govt_boy', 'aided_girl', 'aided_boy', 'unaided_girl', 'unaided_boy', 'total'],
             ['MALPRACTICE'])
mp.to_csv(os.path.join(clean, 'district_malpractice_cases.csv'), index=False)

# 8. Schools with 100% and 0% results (PRO-12, PRO-13)
h = collect(['PRO-12'], ['total_schools', 'govt', 'aided', 'unaided', 'total'], ['100'])
h.to_csv(os.path.join(clean, 'district_schools_100pct.csv'), index=False)
z = collect(['PRO-13'], ['govt', 'aided', 'unaided', 'total'], ['0%'])
z.to_csv(os.path.join(clean, 'district_schools_0pct.csv'), index=False)

# 9. All candidates by district 2014-2018 (the "5 years" workbook)
ac = []
for y in range(2014, 2019):
    p = os.path.join(dump, f'5years__{y}.txt')
    for code, name, v in read_rows(p):
        v = (v + [None] * 9)[:9]
        ac.append(dict(year=y, dist_code=code, dist_name=name, boys_app=v[0], girls_app=v[1], app=v[2],
                       boys_pass=v[3], girls_pass=v[4], passed=v[5], pct=v[8], source_file='5years.xlsx', sheet=str(y)))
pd.DataFrame(ac).to_csv(os.path.join(clean, 'district_all_candidates_2014_2018.csv'), index=False)

with open(os.path.join(clean, '_build_log_district_tables.txt'), 'w', encoding='utf-8') as fh:
    fh.write('\n'.join(log))
print('\n'.join(log))
for f in sorted(glob.glob(os.path.join(clean, 'district_*.csv'))):
    d = pd.read_csv(f)
    print(os.path.basename(f), d.shape, sorted(d.year.unique()))
