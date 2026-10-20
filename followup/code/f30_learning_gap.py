"""Run L0-L6 of PRESPEC_LEARNING_GAP_frozen_before_analysis.md. Usage: python -I f30_learning_gap.py FOLLOWUP_DIR PACK_DIR"""
import sys, os, numpy as np, pandas as pd, statsmodels.api as sm
from scipy.stats import spearmanr, pearsonr
fu, pack = sys.argv[1], sys.argv[2]
nas = pd.read_csv(os.path.join(fu, 'data', 'nas2021_class10_district.csv')).set_index('unit_name')
sp = pd.read_csv(os.path.join(pack, 'data', 'clean', 'panel_district_year.csv'), keep_default_na=False, na_values=[''])
def S(series, y): return sp[(sp.series == series) & (sp.year == y)].set_index('unit_name').pass_pct
z = lambda s: (s - s.mean()) / s.std()
out = open(os.path.join(fu, 'results', 'learning_gap_log.txt'), 'w', encoding='utf-8')
def log(*a):
    s = ' '.join(str(x) for x in a); print(s); out.write(s + '\n')
def ols(y, X):
    d = pd.concat([y.rename('y')] + [x.rename(f'x{i}') for i, x in enumerate(X)], axis=1).dropna()
    m = sm.OLS(d.y, sm.add_constant(d.drop(columns='y'))).fit(cov_type='HC3'); return m, len(d)
def rep(label, y, X, names):
    m, n = ols(y, X); parts = [f'{nm}={m.params[f"x{i}"]:.2f} (se {m.bse[f"x{i}"]:.2f}, p={m.pvalues[f"x{i}"]:.3f})' for i, nm in enumerate(names)]
    sr = spearmanr(pd.concat([y, X[0]], axis=1).dropna().iloc[:, 0], pd.concat([y, X[0]], axis=1).dropna().iloc[:, 1])[0]
    log(f'{label}: n={n} ' + '; '.join(parts) + f'; R2={m.rsquared:.2f}; Spearman(y, first x)={sr:.2f}')
    return dict(spec=label, n=n, **{f'coef_{nm}': m.params[f'x{i}'] for i, nm in enumerate(names)}, **{f'se_{nm}': m.bse[f'x{i}'] for i, nm in enumerate(names)}, r2=m.rsquared, spearman_first=sr)
log('NAS 2021 Class 10 district means (34 districts): mean5 mean=%.2f sd=%.2f min=%.1f max=%.1f' % (nas.nas_mean5.mean(), nas.nas_mean5.std(), nas.nas_mean5.min(), nas.nas_mean5.max()))
log('typical NAS se per subject (median) = %.2f' % nas[[c for c in nas.columns if c.endswith('_se')]].stack().median())
N = nas.nas_mean5; zN = z(N); zM = z(nas.nas_ms)
log('\n=== L0 correlation of NAS (mean5) with pass rate')
for lab, s in (('S1 2019', S('S1', 2019)), ('S1 2022', S('S1', 2022)), ('S1 2023', S('S1', 2023)), ('S1 2024', S('S1', 2024)), ('S2 2025', S('S2', 2025)), ('S2 2023', S('S2', 2023))):
    d = pd.concat([N, s], axis=1).dropna(); log(f'{lab}: n={len(d)} Spearman={spearmanr(d.iloc[:,0], d.iloc[:,1])[0]:.3f} Pearson={pearsonr(d.iloc[:,0], d.iloc[:,1])[0]:.3f}')
p19, p22, p23, p24 = S('S1', 2019), S('S1', 2022), S('S1', 2023), S('S1', 2024)
p2223 = (p22 + p23) / 2
d2324 = p24 - p23; d2223 = p23 - p22; d1819 = S('S1', 2019) - S('S1', 2018)
res = []
log('\n=== L1 primary: change 2023->24 (S1) on Gap_2023 = z(pass 2023) - z(NAS)')
res.append(rep('L1 d2324 ~ gap2023', d2324, [z(p23) - zN], ['gap']))
log('\n=== L2 other baselines')
res.append(rep('L2a d2324 ~ gap2022', d2324, [z(p22) - zN], ['gap']))
res.append(rep('L2b d2324 ~ gap(mean 2022-23)', d2324, [z(p2223) - zN], ['gap']))
res.append(rep('L2c d2324 ~ gap2023 using Maths+Science NAS', d2324, [z(p23) - zM], ['gap']))
log('\n=== L3 pre-COVID baseline')
res.append(rep('L3 d2324 ~ gap2019', d2324, [z(p19) - zN], ['gap']))
log('\n=== L4 two-variable')
res.append(rep('L4 d2324 ~ z(pass2023) + z(NAS)', d2324, [z(p23), zN], ['z_pass2023', 'z_NAS']))
log('\n=== L5 regular freshers 2023->2025')
d2325 = S('S2', 2025) - S('S2', 2023)
res.append(rep('L5 S2 d2325 ~ gap2023(S2)', d2325, [z(S('S2', 2023)) - zN], ['gap']))
res.append(rep('L5b S2 d2325 ~ z(pass S2 2023) + z(NAS)', d2325, [z(S('S2', 2023)), zN], ['z_pass', 'z_NAS']))
log('\n=== L6 placebos')
res.append(rep('L6a d2223 ~ gap2022', d2223, [z(p22) - zN], ['gap']))
res.append(rep('L6b d1819 ~ gap2019', d1819, [z(p19) - zN], ['gap']))
res.append(rep('L6c d2324 ~ NAS only', d2324, [zN], ['z_NAS']))
pd.DataFrame(res).to_csv(os.path.join(fu, 'results', 'tables', 'L_learning_gap.csv'), index=False)
out.close()
