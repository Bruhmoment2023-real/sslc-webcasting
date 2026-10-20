"""Run U1-U8 of PRESPEC_PUC_frozen_before_analysis.md exactly as written. Output: results/puc_analysis_log.txt + tables.
Usage: python -I f20_puc_analysis.py FOLLOWUP_DIR PACK_DIR"""
import sys, os, numpy as np, pandas as pd, statsmodels.api as sm
from scipy.stats import spearmanr, pearsonr
fu, pack = sys.argv[1], sys.argv[2]
puc = pd.read_csv(os.path.join(fu, 'data', 'puc_district_regular_passpct.csv'))
P = puc.pivot(index='district', columns='year', values='pass_pct')
sp = pd.read_csv(os.path.join(pack, 'data', 'clean', 'panel_district_year.csv'), keep_default_na=False, na_values=[''])
MAP = {'SIRSI': 'UTTARA KANNADA', 'MADHUGIRI': 'TUMAKURU', 'BALLARI (incl. VIJAYANAGARA)': 'BALLARI'}
sp['pu'] = sp.unit_name.replace(MAP)
g = sp.groupby(['series', 'year', 'pu'])[['app', 'passed']].sum().reset_index(); g['pct'] = 100 * g.passed / g.app
def S(series, year): return g[(g.series == series) & (g.year == year)].set_index('pu').pct
out = open(os.path.join(fu, 'results', 'puc_analysis_log.txt'), 'w', encoding='utf-8')
def log(*a):
    s = ' '.join(str(x) for x in a); print(s); out.write(s + '\n')
def ols(y, x):
    d = pd.concat([x.rename('x'), y.rename('y')], axis=1).dropna()
    m = sm.OLS(d.y, sm.add_constant(d.x)).fit(cov_type='HC3')
    return len(d), m.params['x'], m.bse['x'], m.pvalues['x'], m.rsquared
def rho(a, b):
    d = pd.concat([a, b], axis=1).dropna(); return len(d), spearmanr(d.iloc[:, 0], d.iloc[:, 1])[0], pearsonr(d.iloc[:, 0], d.iloc[:, 1])[0]
EXCL = ['BELAGAVI', 'CHIKKODI']
pairs = [(2016, 2017), (2017, 2018), (2018, 2023), (2023, 2024), (2024, 2025), (2025, 2026)]
def sub(a, b):
    x, y = P[a], P[b]
    if (a, b) == (2017, 2018): x, y = x.drop(EXCL, errors='ignore'), y.drop(EXCL, errors='ignore')
    return x, y
log('=== U2 reshuffle, U3 spread, U5 mean-reversion slope (PU regular students, pass %)')
log('pair | n | Spearman | Pearson | sd of change | mean change | n rising | n falling | slope of change on start level (se, p, R2)')
rows = []
for a, b in pairs:
    x, y = sub(a, b); d = (y - x).dropna(); n, sr, pr = rho(x, y)
    nn, sl, se, p, r2 = ols(y - x, x)
    log(f'{a}-{b} | {n} | {sr:.3f} | {pr:.3f} | {d.std():.2f} | {d.mean():.2f} | {(d>0).sum()} | {(d<0).sum()} | {sl:.2f} ({se:.2f}, p={p:.3f}, R2={r2:.2f})')
    rows.append(dict(pair=f'{a}-{b}', n=n, spearman=sr, pearson=pr, sd_change=d.std(), mean_change=d.mean(), rising=int((d > 0).sum()), falling=int((d < 0).sum()), slope_level=sl, se=se, p=p, r2=r2))
pd.DataFrame(rows).to_csv(os.path.join(fu, 'results', 'tables', 'U2_U3_U5_puc_pairs.csv'), index=False)
log('\n=== U4 give-back (OLS, HC3): change on earlier rise')
def tst(label, a0, a1, b1):
    x0, x1 = P[a0], P[a1]; y1 = P[b1]
    if 2017 in (a0, a1, b1) and 2018 in (a0, a1, b1): pass
    x = (x1 - x0)
    y = (y1 - x1)
    if label.startswith('change 2017->2018'): x = x.drop(EXCL, errors='ignore'); y = y.drop(EXCL, errors='ignore')
    n, sl, se, p, r2 = ols(y, x)
    log(f'{label}: n={n} slope={sl:.2f} (se {se:.2f}, p={p:.3f}, R2={r2:.2f})'); return dict(spec=label, n=n, slope=sl, se=se, p=p, r2=r2)
r = []
r.append(tst('change 2024->2025 on rise 2018->2024', 2018, 2024, 2025))
r.append(tst('change 2023->2024 on rise 2018->2023', 2018, 2023, 2024))
r.append(tst('change 2017->2018 on rise 2016->2017 (Belagavi, Chikkodi excluded: 2018 Belagavi no longer includes Chikkodi)', 2016, 2017, 2018))
r.append(tst('change 2024->2025 on one-year rise 2023->2024', 2023, 2024, 2025))
r.append(tst('change 2025->2026 on rise 2018->2025 (post hoc extra)', 2018, 2025, 2026))
pd.DataFrame(r).to_csv(os.path.join(fu, 'results', 'tables', 'U4_puc_giveback.csv'), index=False)
log('\n=== U4 post hoc (NOT in the frozen spec): remove the shared-2024 mechanical link')
r2_ = []
x = P[2023] - P[2018]; y = P[2025] - P[2024]; n, sl, se, p, rr = ols(y, x); log(f'change 2024->2025 on rise 2018->2023 (clean of 2024): n={n} slope={sl:.2f} (se {se:.2f}, p={p:.3f}, R2={rr:.2f})')
x = P[2023]; y = P[2025] - P[2024]; n, sl, se, p, rr = ols(y, x); log(f'change 2024->2025 on 2023 level: n={n} slope={sl:.2f} (se {se:.2f}, p={p:.3f}, R2={rr:.2f})')
x = P[2018]; y = P[2025] - P[2024]; n, sl, se, p, rr = ols(y, x); log(f'change 2024->2025 on 2018 level: n={n} slope={sl:.2f} (se {se:.2f}, p={p:.3f}, R2={rr:.2f})')
x = P[2018]; y = P[2024] - P[2023]; n, sl, se, p, rr = ols(y, x); log(f'change 2023->2024 on 2018 level (the SSLC A4a analogue timing): n={n} slope={sl:.2f} (se {se:.2f}, p={p:.3f}, R2={rr:.2f})')
log('\n=== U7 same districts: SSLC (aggregated to 32 PU districts) change vs PU change')
s2324 = S('S1', 2024) - S('S1', 2023); s2325 = S('S2', 2025) - S('S2', 2023)
pu2324 = P[2024] - P[2023]; pu2425 = P[2025] - P[2024]; pu2325 = P[2025] - P[2023]
rows = []
for nm, a in (('SSLC S1 change 2023->24', s2324), ('SSLC S2 change 2023->25', s2325)):
    for nm2, b in (('PU change 2023->24', pu2324), ('PU change 2024->25', pu2425), ('PU change 2023->25', pu2325)):
        n, sr, pr = rho(a, b); log(f'{nm} vs {nm2}: n={n} Spearman={sr:.3f} Pearson={pr:.3f}'); rows.append(dict(a=nm, b=nm2, n=n, spearman=sr, pearson=pr))
pd.DataFrame(rows).to_csv(os.path.join(fu, 'results', 'tables', 'U7_sslc_vs_puc_changes.csv'), index=False)
log('\n=== U8 same-year SSLC vs PU district pass-rate rank correlation')
rows = []
for y, ser in ((2018, 'S1'), (2023, 'S1'), (2024, 'S1'), (2025, 'S2'), (2026, 'S2')):
    n, sr, pr = rho(S(ser, y), P[y]); log(f'{y} (SSLC {ser}): n={n} Spearman={sr:.3f} Pearson={pr:.3f}'); rows.append(dict(year=y, sslc_series=ser, n=n, spearman=sr, pearson=pr))
pd.DataFrame(rows).to_csv(os.path.join(fu, 'results', 'tables', 'U8_same_year_sslc_vs_puc.csv'), index=False)
log('\n=== Context (descriptive): biggest PU changes')
for a, b in ((2023, 2024), (2024, 2025)):
    d = (P[b] - P[a]).dropna().sort_values(); log(f'{a}->{b} largest falls:', ', '.join(f'{k} {v:.1f}' for k, v in d.head(5).items()), '| largest rises:', ', '.join(f'{k} {v:+.1f}' for k, v in d.tail(4).items()))
log('\nSSLC for the same 32 units (aggregated), reshuffle check: Spearman of consecutive S1 years')
for a, b in ((2017, 2018), (2018, 2019), (2022, 2023), (2023, 2024)):
    n, sr, pr = rho(S('S1', a), S('S1', b)); log(f'SSLC S1 {a}-{b}: n={n} Spearman={sr:.3f}')
out.close()
