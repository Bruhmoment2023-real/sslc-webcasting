"""Pre-specified descriptive analysis (see results/PRESPEC_frozen_before_analysis.md).

Usage: python 20_analysis.py CLEAN_DIR RESULTS_DIR
Writes tables (CSV), figures (PNG) and a plain-text log of every number quoted in the summary.
"""
import sys, os, itertools
import numpy as np
import pandas as pd
import statsmodels.api as sm
import statsmodels.formula.api as smf
from scipy import stats
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from common import read

clean, res = sys.argv[1], sys.argv[2]
os.makedirs(os.path.join(res, 'tables'), exist_ok=True)
os.makedirs(os.path.join(res, 'figures'), exist_ok=True)
LOG = []


def log(*a):
    s = ' '.join(str(x) for x in a)
    print(s)
    LOG.append(s)


# chart style: reference palette slots 1-3, validated with the dataviz validator (light surface)
BLUE, ORANGE, AQUA, INK, MUTED, SURF = '#2a78d6', '#eb6834', '#1baf7a', '#0b0b0b', '#52514e', '#fcfcfb'
plt.rcParams.update({'figure.facecolor': SURF, 'axes.facecolor': SURF, 'savefig.facecolor': SURF, 'font.size': 10,
                     'axes.edgecolor': '#c9c8c2', 'axes.labelcolor': MUTED, 'xtick.color': MUTED, 'ytick.color': MUTED,
                     'axes.spines.top': False, 'axes.spines.right': False, 'axes.grid': True, 'grid.color': '#e9e8e3',
                     'grid.linewidth': 0.8, 'axes.titlesize': 11, 'axes.titleweight': 'bold', 'axes.titlecolor': INK,
                     'axes.titlelocation': 'left', 'legend.frameon': False})


def save(fig, name):
    fig.tight_layout()
    fig.savefig(os.path.join(res, 'figures', name), dpi=170)
    plt.close(fig)


p = read(os.path.join(clean, 'panel_district_year.csv'))
W = {s: p[p.series == s].pivot(index='unit', columns='year', values='pass_pct') for s in ('S1', 'S2', 'S3')}
N = {s: p[p.series == s].pivot(index='unit', columns='year', values='app') for s in ('S1', 'S2', 'S3')}
names = p.drop_duplicates('unit').set_index('unit').unit_name
division = p.drop_duplicates('unit').set_index('unit').division
s1, s2, s3 = W['S1'], W['S2'], W['S3']
s1.round(2).to_csv(os.path.join(res, 'tables', 'T0_S1_all_candidates_first_exam_wide.csv'))
s2.round(2).to_csv(os.path.join(res, 'tables', 'T0_S2_regular_fresh_first_exam_wide.csv'))
s3.round(2).to_csv(os.path.join(res, 'tables', 'T0_S3_regular_fresh_cumulative_wide.csv'))


def ols(y, x, w=None):
    """y on x with HC3 robust SE; returns dict."""
    d = pd.concat([y, x], axis=1).dropna()
    X = sm.add_constant(d.iloc[:, 1])
    m = (sm.WLS(d.iloc[:, 0], X, weights=w.loc[d.index]) if w is not None else sm.OLS(d.iloc[:, 0], X)).fit(cov_type='HC3')
    rho, prho = stats.spearmanr(d.iloc[:, 0], d.iloc[:, 1])
    return dict(n=len(d), slope=m.params.iloc[1], se=m.bse.iloc[1], p=m.pvalues.iloc[1], r2=m.rsquared,
                intercept=m.params.iloc[0], spearman=rho, spearman_p=prho,
                mean_change=d.iloc[:, 0].mean(), sd_change=d.iloc[:, 0].std(), sd_base=d.iloc[:, 1].std())


# ---------------- A1 state series ----------------
st = pd.read_csv(os.path.join(clean, 'transcribed', 'state_first_exam_series.csv'))
log('== A1 state series (first/main exam) ==')
log(st[st.population.isin(['all_candidates', 'regular_fresh'])].pivot(index='year', columns='population', values='pct').to_string())
fig, ax = plt.subplots(figsize=(8.2, 4.4))
for pop, col, lab in (('all_candidates', BLUE, 'All candidates'), ('regular_fresh', ORANGE, 'Regular (school) first-time candidates')):
    d = st[st.population == pop].sort_values('year')
    ax.plot(d.year, d.pct, color=col, lw=2, marker='o', ms=5, label=lab)
ax.annotate('All candidates', (2014, 81.24), xytext=(2014.0, 77.0), color=INK, fontsize=9)
ax.annotate('Regular freshers', (2015, 84.85), xytext=(2014.6, 87.5), color=INK, fontsize=9)
ax.scatter([2024], [54], s=60, facecolor=SURF, edgecolor=BLUE, lw=2, zorder=5)
ax.annotate('2024 before grace:\nabout 54 (news report)', (2024, 54), xytext=(2020.9, 50.5), fontsize=8.5, color=INK,
            arrowprops=dict(arrowstyle='-', color=MUTED, lw=0.8))
for x, t in ((2021, '2021: COVID\ntwo-day exam'), (2024, '2024: webcasting,\n3 exams, 20% grace'), (2025, '2025: extra\ngrace removed'), (2026, '2026: pass\nmark 33%')):
    ax.axvline(x, color='#c9c8c2', lw=1, ls=(0, (3, 3)), zorder=0)
ax.text(2021, 101.5, 'COVID\nexam', ha='center', fontsize=8, color=MUTED)
ax.text(2024, 101.5, 'webcasting\n+20% grace', ha='center', fontsize=8, color=MUTED)
ax.text(2025.05, 46, 'extra grace\nremoved', ha='center', fontsize=8, color=MUTED)
ax.text(2026, 101.5, 'pass mark\n33%', ha='center', fontsize=8, color=MUTED)
ax.set_ylim(44, 108); ax.set_xticks(range(2014, 2027)); ax.set_ylabel('Pass percentage, first/main exam')
ax.set_title('Karnataka SSLC pass percentage, first (main) examination, 2014-2026')
ax.legend(loc='lower left', fontsize=8.5)
save(fig, 'F1_state_series.png')

# ---------------- A2 main cross-section ----------------
log('\n== A2 change 2023->2024 (S1, all candidates) on 2023 level ==')
d2324 = s1[2024] - s1[2023]
a2 = ols(d2324.rename('chg'), s1[2023].rename('base'))
a2w = ols(d2324.rename('chg'), s1[2023].rename('base'), w=N['S1'][2023])
log('unweighted:', {k: round(v, 3) for k, v in a2.items()})
log('weighted by 2023 candidates:', {k: round(v, 3) for k, v in a2w.items()})
tab = pd.DataFrame({'district': names, 'division': division, 'pass_2019': s1[2019], 'pass_2022': s1[2022], 'pass_2023': s1[2023],
                    'pass_2024_exam1': s1[2024], 'change_2023_24': d2324, 'rise_2019_23': s1[2023] - s1[2019],
                    'rank_2023': s1[2023].rank(ascending=False), 'rank_2024': s1[2024].rank(ascending=False),
                    'candidates_2024': N['S1'][2024]}).sort_values('change_2023_24')
tab.round(2).to_csv(os.path.join(res, 'tables', 'T2_district_change_2023_2024.csv'))
log(tab.round(2).to_string())

# ---------------- A3 placebo pairs ----------------
log('\n== A3 mean-reversion placebo: change t0->t1 on level t0 (S1) ==')
pairs = [(2014, 2015), (2015, 2016), (2016, 2017), (2017, 2018), (2018, 2019), (2019, 2020), (2020, 2022), (2022, 2023), (2023, 2024)]
rows = []
for a, b in pairs:
    r = ols((s1[b] - s1[a]).rename('chg'), s1[a].rename('base'))
    r.update(pair=f'{a}-{b}', kind='webcasting year' if b == 2024 else ('placebo (2-year gap across COVID exam)' if (a, b) == (2020, 2022) else 'placebo'))
    rows.append(r)
pl = pd.DataFrame(rows)[['pair', 'kind', 'n', 'mean_change', 'sd_change', 'sd_base', 'slope', 'se', 'p', 'r2', 'spearman']]
pl.round(3).to_csv(os.path.join(res, 'tables', 'T3_placebo_slopes.csv'), index=False)
log(pl.round(3).to_string(index=False))

# ---------------- A4 different-year baselines ----------------
log('\n== A4 baselines measured in a different year (S1) ==')
pre = s1[[2018, 2019]].mean(axis=1)
specs = {
    'A4a change 2023-24 on 2018-19 average level': (d2324, pre),
    'A4b change 2023-24 on 2022 level': (d2324, s1[2022]),
    'A4c change 2023-24 on rise 2019-23': (d2324, s1[2023] - s1[2019]),
    'A4c2 change 2023-24 on rise (2018-19 avg) to (2022-23 avg)': (d2324, s1[[2022, 2023]].mean(axis=1) - pre),
    'A4d change (2018-19 avg)->2024 on 2018-19 average level': (s1[2024] - pre, pre),
    'A4e [post hoc] 2024 level on 2023 level': (s1[2024], s1[2023]),
    'A4f [post hoc] 2024 level on 2018-19 average level': (s1[2024], pre),
    'A4g [post hoc] 2023 level on 2018-19 average level': (s1[2023], pre),
}
rows = []
for k, (y, x) in specs.items():
    r = ols(y.rename('y'), x.rename('x')); r['spec'] = k; rows.append(r)
a4 = pd.DataFrame(rows)[['spec', 'n', 'slope', 'se', 'p', 'r2', 'spearman', 'spearman_p']]
a4.round(3).to_csv(os.path.join(res, 'tables', 'T4_alternative_baselines.csv'), index=False)
log(a4.round(3).to_string(index=False))
# placebo for A4c: change t->t+1 on prior 4-year rise is not available for many years; do the 2019 analogue
r = ols((s1[2019] - s1[2018]).rename('y'), (s1[2018] - s1[2014]).rename('x'))
log('placebo analogue of A4c: change 2018-19 on rise 2014-18:', {k: round(v, 3) for k, v in r.items()})
# leave-one-out for A2 and A4c
loo = []
for u in s1.index:
    k = s1.index != u
    loo.append(dict(dropped=names[u], slope_A2=ols(d2324[k].rename('y'), s1[2023][k].rename('x'))['slope'],
                    slope_A4c=ols(d2324[k].rename('y'), (s1[2023] - s1[2019])[k].rename('x'))['slope']))
loo = pd.DataFrame(loo)
loo.round(3).to_csv(os.path.join(res, 'tables', 'T4_leave_one_out.csv'), index=False)
log('leave-one-out slope range A2:', loo.slope_A2.min().round(3), loo.slope_A2.max().round(3),
    '| A4c:', loo.slope_A4c.min().round(3), loo.slope_A4c.max().round(3))

# scatter figure (A2 and A4c)
fig, axes = plt.subplots(1, 2, figsize=(10.5, 4.6), sharey=True)
for ax, x, xl, r, ttl in ((axes[0], s1[2023], 'Pass percentage in 2023', a2, 'Fall in 2024 against the 2023 level'),
                          (axes[1], s1[2023] - s1[2019], 'Rise in pass percentage, 2019 to 2023 (points)',
                           ols(d2324.rename('y'), (s1[2023] - s1[2019]).rename('x')), 'Fall in 2024 against the 2019-23 rise')):
    ax.scatter(x, d2324, s=np.sqrt(N['S1'][2024]) / 4.5, color=BLUE, edgecolor=SURF, lw=1.2, alpha=0.9, zorder=3)
    xs = np.linspace(x.min(), x.max(), 50)
    ax.plot(xs, r['intercept'] + r['slope'] * xs, color=ORANGE, lw=2, zorder=2)
    lab = list(d2324.nsmallest(4).index) + list(d2324.nlargest(4).index)
    for u in dict.fromkeys(lab):
        ax.annotate(names[u].title(), (x[u], d2324[u]), xytext=(4, 4), textcoords='offset points', fontsize=7.5, color=INK)
    ax.axhline(0, color='#c9c8c2', lw=1)
    ax.set_xlabel(xl + f"\nslope {r['slope']:.2f} (robust s.e. {r['se']:.2f}), R2 {r['r2']:.2f}, n = {r['n']}"); ax.set_title(ttl)
axes[0].set_ylabel('Change in pass percentage, 2023 to 2024 Exam-1 (points)')
save(fig, 'F2_fall_vs_baseline.png')

# placebo figure
fig, ax = plt.subplots(figsize=(7.6, 3.9))
cols = [ORANGE if k == 'webcasting year' else BLUE for k in pl.kind]
ax.bar(pl.pair, pl.slope, color=cols, width=0.62, zorder=3)
ax.errorbar(pl.pair, pl.slope, yerr=1.96 * pl.se, fmt='none', ecolor=INK, lw=1, capsize=3, zorder=4)
ax.axhline(0, color=INK, lw=0.8)
for x, v in zip(pl.pair, pl.slope):
    ax.text(x, v - 0.07 if v < 0 else v + 0.03, f'{v:.2f}', ha='center', va='top' if v < 0 else 'bottom', fontsize=8, color=INK)
ax.set_ylabel('Slope: change on previous level'); ax.tick_params(axis='x', labelsize=8)
ax.set_title('How strongly districts fall back towards the mean: 2023-24 against earlier year pairs')
save(fig, 'F3_placebo_slopes.png')

# ---------------- A5 event study ----------------
log('\n== A5 event study (S1; 2021 dropped; reference year 2023) ==')
long = s1.drop(columns=[2021]).stack().rename('y').reset_index()
long.columns = ['unit', 'year', 'y']
base23 = s1[2023]
groups = {
    'top tercile of 2023 level': (base23 >= base23.quantile(2 / 3)).astype(int),
    'standardised 2023 level': (base23 - base23.mean()) / base23.std(),
    'top tercile of 2018-19 average': (pre >= pre.quantile(2 / 3)).astype(int),
    'standardised 2018-19 average': (pre - pre.mean()) / pre.std(),
    'standardised rise 2019-23': ((s1[2023] - s1[2019]) - (s1[2023] - s1[2019]).mean()) / (s1[2023] - s1[2019]).std(),
}
years = sorted(long.year.unique())
es_rows = []
for gname, gv in groups.items():
    d = long.copy(); d['g'] = d.unit.map(gv)
    terms = []
    for y in years:
        if y != 2023:
            d[f'g_{y}'] = d.g * (d.year == y); terms.append(f'g_{y}')
    m = smf.ols('y ~ ' + ' + '.join(terms) + ' + C(unit) + C(year)', d).fit(cov_type='cluster', cov_kwds={'groups': d.unit})
    for y in years:
        es_rows.append(dict(spec=gname, year=y, coef=0.0 if y == 2023 else m.params[f'g_{y}'], se=0.0 if y == 2023 else m.bse[f'g_{y}']))
es = pd.DataFrame(es_rows)
es.round(3).to_csv(os.path.join(res, 'tables', 'T5_event_study_coefficients.csv'), index=False)
log(es.pivot(index='year', columns='spec', values='coef').round(2).to_string())
log('standard errors:'); log(es.pivot(index='year', columns='spec', values='se').round(2).to_string())

fig, axes = plt.subplots(1, 2, figsize=(10.8, 4.4))
ax = axes[0]
ter = pd.qcut(base23, 3, labels=['Lowest third in 2023', 'Middle third', 'Highest third in 2023'])
for lab, col, mk in zip(ter.cat.categories, (BLUE, AQUA, ORANGE), ('o', 's', '^')):
    u = ter[ter == lab].index
    yy = s1.loc[u].mean().drop(2021)
    ax.plot(yy.index, yy.values, color=col, lw=2, marker=mk, ms=5, label=lab)
    ax.annotate(lab.split(' in')[0], (2024, yy[2024]), xytext=(6, -3), textcoords='offset points', fontsize=8, color=INK)
ax.axvline(2023.5, color='#c9c8c2', lw=1, ls=(0, (3, 3)))
ax.set_xlim(2013.6, 2026.2); ax.set_xticks(range(2014, 2025, 2)); ax.set_ylabel('Mean district pass percentage (all candidates)')
ax.set_ylim(63, 97); ax.set_title('Districts grouped by their 2023 pass rate'); ax.legend(fontsize=8, loc='upper left', ncol=3, columnspacing=1.0, handlelength=1.5)
ax = axes[1]
for spec, col, mk, off in (('standardised 2023 level', BLUE, 'o', -0.08), ('standardised 2018-19 average', ORANGE, 's', 0.08)):
    e = es[es.spec == spec]
    ax.errorbar(e.year + off, e.coef, yerr=1.96 * e.se, color=col, marker=mk, ms=5, lw=1.5, capsize=2.5, label='Grouping variable: ' + spec.replace('standardised ', ''))
ax.axhline(0, color=INK, lw=0.8); ax.axvline(2023.5, color='#c9c8c2', lw=1, ls=(0, (3, 3)))
ax.set_xticks(range(2014, 2025, 2)); ax.set_ylabel('Points per 1 s.d. of the grouping variable, relative to 2023')
ax.set_ylim(-7.5, 10); ax.set_title('Event-study coefficients'); ax.legend(fontsize=8, loc='upper left')
save(fig, 'F4_event_study.png')

# ---------------- A6 regular freshers 2023 -> 2025 and 2026 ----------------
log('\n== A6 regular freshers (S2): change from 2023 to 2025 Exam-1 and to 2026 Exam-1 ==')
pre2 = s2[[2018, 2019]].mean(axis=1)
rows = []
for k, (y, x) in {
    'change 2023-25 on 2023 level': (s2[2025] - s2[2023], s2[2023]),
    'change 2023-25 on 2018-19 average level': (s2[2025] - s2[2023], pre2),
    'change 2023-25 on rise 2019-23': (s2[2025] - s2[2023], s2[2023] - s2[2019]),
    'change (2018-19 avg)->2025 on 2018-19 average level': (s2[2025] - pre2, pre2),
    '2025 level on 2018-19 average level': (s2[2025], pre2),
    '2025 level on 2023 level': (s2[2025], s2[2023]),
    'change 2023-26 on 2023 level': (s2[2026] - s2[2023], s2[2023]),
    'change 2025-26 on 2025 level': (s2[2026] - s2[2025], s2[2025]),
    'placebo: change 2022-23 on 2022 level': (s2[2023] - s2[2022], s2[2022]),
    'placebo: change 2018-19 on 2018 level': (s2[2019] - s2[2018], s2[2018]),
    'placebo: change 2017-18 on 2017 level': (s2[2018] - s2[2017], s2[2017]),
    'placebo: change 2019-20 on 2019 level': (s2[2020] - s2[2019], s2[2019]),
}.items():
    r = ols(y.rename('y'), x.rename('x')); r['spec'] = k; rows.append(r)
a6 = pd.DataFrame(rows)[['spec', 'n', 'mean_change', 'slope', 'se', 'p', 'r2', 'spearman']]
a6.round(3).to_csv(os.path.join(res, 'tables', 'T6_regular_fresh_2023_2025_2026.csv'), index=False)
log(a6.round(3).to_string(index=False))
t6 = pd.DataFrame({'district': names, 'rf_2019': s2[2019], 'rf_2023': s2[2023], 'rf_2025_exam1': s2[2025], 'rf_2026_exam1': s2[2026],
                   'change_2023_25': s2[2025] - s2[2023], 'change_2019_25': s2[2025] - s2[2019]}).sort_values('change_2023_25')
t6.round(2).to_csv(os.path.join(res, 'tables', 'T6_district_regular_fresh.csv'))
log(t6.round(2).to_string())
log('correlation of district falls: S1 2023-24 vs S2 2023-25:', round(d2324.corr(s2[2025] - s2[2023]), 3))
log('cross-district s.d. of pass rate by year, S1:', s1.std().round(2).to_dict())
log('cross-district s.d. of pass rate by year, S2:', s2.std().round(2).to_dict())

# ---------------- A7 management ----------------
log('\n== A7 management type ==')
grp = pd.read_csv(os.path.join(clean, 'transcribed', 'state_first_exam_by_group.csv'))
mg = read(os.path.join(clean, 'district_regular_fresh_by_management.csv'))
stm = mg.groupby(['year', 'scope', 'management'])[['app', 'passed']].sum()
stm['pct'] = 100 * stm.passed / stm.app
stm = stm.pct.unstack().round(2)
log('state totals from workbooks (main exam to 2023; cumulative from 2024):'); log(stm.to_string())
log('Exam-1 by management from press notes:')
log(grp[grp.dimension == 'management'].pivot(index='year', columns='group', values='pct').to_string())
stm.to_csv(os.path.join(res, 'tables', 'T7_management_state_workbooks.csv'))
mgw = mg.assign(unit=mg.dist_code.replace({'TA': 'TT'})).groupby(['unit', 'year', 'management'])[['app', 'passed']].sum()
mgw['pct'] = 100 * mgw.passed / mgw.app
mgp = mgw.pct.unstack(['management', 'year'])
rows = []
for m_ in ('govt', 'aided', 'unaided'):
    r = ols((mgp[(m_, 2024)] - mgp[(m_, 2023)]).rename('y'), mgp[(m_, 2023)].rename('x'))
    r['spec'] = f'{m_}: change 2023 main -> 2024 cumulative on 2023 level (S3, not like-for-like)'; rows.append(r)
    r = ols((mgp[(m_, 2025)] - mgp[(m_, 2023)]).rename('y'), mgp[(m_, 2023)].rename('x'))
    r['spec'] = f'{m_}: change 2023 main -> 2025 cumulative on 2023 level (S3, not like-for-like)'; rows.append(r)
a7 = pd.DataFrame(rows)[['spec', 'n', 'mean_change', 'slope', 'se', 'p', 'r2', 'spearman']]
a7.round(3).to_csv(os.path.join(res, 'tables', 'T7_management_district_cumulative.csv'), index=False)
log(a7.round(3).to_string(index=False))

# ---------------- A8 subjects ----------------
log('\n== A8 subject pass rates, regular freshers (main exam to 2023; cumulative from 2024) ==')
sj = read(os.path.join(clean, 'district_regular_fresh_by_subject.csv'))
sjt = sj.groupby(['year', 'subject'])[['app', 'passed']].sum(min_count=1)
sjt['pct'] = 100 * sjt.passed / sjt.app
sjt = sjt.pct.unstack().round(2)
sjt.to_csv(os.path.join(res, 'tables', 'T8_subject_state.csv'))
log(sjt.to_string())

# ---------------- A9 grades ----------------
log('\n== A9 grade distribution ==')
gd = pd.read_csv(os.path.join(clean, 'transcribed', 'state_grade_distribution_first_exam.csv'))
gp = gd.pivot(index='year', columns='grade', values='students')[['A_plus', 'A', 'B_plus', 'B', 'C_plus', 'C']]
gshare = (100 * gp.div(gp.sum(axis=1), axis=0)).round(2)
log('Exam-1 / main exam, share of passes by grade (press notes):'); log(gshare.to_string()); log(gp.to_string())
gr = read(os.path.join(clean, 'district_regular_fresh_grade_distribution.csv'))
gs = gr.groupby('year')[['app', 'passed', 'A_plus', 'A', 'B_plus', 'B', 'C_plus', 'C']].sum()
gs['C_share_of_passes'] = (100 * gs.C / gs.passed).round(2)
gs['C_share_of_appeared'] = (100 * gs.C / gs.app).round(2)
gs.to_csv(os.path.join(res, 'tables', 'T9_grade_distribution_workbooks.csv'))
log('workbooks (main exam to 2023; cumulative from 2024):'); log(gs.to_string())
fig, ax = plt.subplots(figsize=(7.6, 3.9))
order = ['A_plus', 'A', 'B_plus', 'B', 'C_plus', 'C']
labs = ['A+ (90-100)', 'A (80-89)', 'B+ (70-79)', 'B (60-69)', 'C+ (50-59)', 'C (35-49; 33-49 in 2026)']
x = np.arange(len(order)); wdt = 0.2
for i, (yr, col) in enumerate(zip((2023, 2024, 2025), (BLUE, ORANGE, AQUA))):
    ax.bar(x + (i - 1) * (wdt + 0.02), gp.loc[yr, order] / 1000, wdt, color=col, label={2023: '2023 main exam', 2024: '2024 Exam-1 (20% grace)', 2025: '2025 Exam-1'}[yr], zorder=3)
ax.set_xticks(x); ax.set_xticklabels(labs, fontsize=8); ax.set_ylabel('Regular freshers passing in grade (thousands)')
ax.set_title('Where the passes sat: grade distribution of regular freshers'); ax.legend(fontsize=8)
save(fig, 'F5_grade_distribution.png')

# ---------------- A10 malpractice ----------------
log('\n== A10 booked malpractice cases (PRO-10) ==')
mp = read(os.path.join(clean, 'district_malpractice_cases.csv'))
mpt = mp.groupby(['year', 'scope']).agg(cases=('total', 'sum'), districts_with_cases=('dist_code', 'nunique'))
mpt.to_csv(os.path.join(res, 'tables', 'T10_malpractice_cases.csv'))
log(mpt.to_string())

# ---------------- A11 gender / area ----------------
log('\n== A11 gender, medium, area (state level, press notes) ==')
for dim in ('gender', 'medium', 'area'):
    log(grp[grp.dimension == dim].pivot_table(index=['year', 'population'], columns='group', values='pct').to_string())
gg = read(os.path.join(clean, 'district_regular_fresh_by_gender.csv'))
gt = gg.groupby(['year', 'scope'])[['boys_app', 'boys_pass', 'girls_app', 'girls_pass']].sum()
gt['boys_pct'] = 100 * gt.boys_pass / gt.boys_app; gt['girls_pct'] = 100 * gt.girls_pass / gt.girls_app; gt['gap_girls_minus_boys'] = gt.girls_pct - gt.boys_pct
gt.round(2).to_csv(os.path.join(res, 'tables', 'T11_gender_state_workbooks.csv'))
log(gt[['boys_pct', 'girls_pct', 'gap_girls_minus_boys']].round(2).to_string())
ur = read(os.path.join(clean, 'district_regular_fresh_by_urban_rural.csv'))
ut = ur.groupby(['year', 'scope'])[['rural_app', 'rural_pass', 'urban_app', 'urban_pass']].sum()
ut['rural_pct'] = 100 * ut.rural_pass / ut.rural_app; ut['urban_pct'] = 100 * ut.urban_pass / ut.urban_app
ut.round(2).to_csv(os.path.join(res, 'tables', 'T11_urban_rural_state_workbooks.csv'))
log(ut[['rural_app', 'urban_app', 'rural_pct', 'urban_pct']].round(2).to_string())

# ---------------- A12 exploratory: school-level markers ----------------
log('\n== A12 (exploratory) school-level markers from 2018-19 ==')
sd = read(os.path.join(clean, 'district_school_dispersion_2018_2019.csv'))
sm_ = sd.groupby('unit')[['share_schools_100pct', 'share_schools_95plus', 'share_students_in_100pct_schools', 'school_pass_sd']].mean()
rows = []
for c_ in sm_.columns:
    r = ols(d2324.rename('y'), sm_[c_].rename('x')); r['spec'] = f'change 2023-24 (S1) on {c_} (2018-19 mean)'; rows.append(r)
    r = ols((s2[2025] - s2[2023]).rename('y'), sm_[c_].rename('x')); r['spec'] = f'change 2023-25 (S2) on {c_} (2018-19 mean)'; rows.append(r)
h = read(os.path.join(clean, 'district_schools_100pct.csv'))
h['unit'] = h.dist_code.replace({'TA': 'TT'})
hh = h.groupby(['unit', 'year'])[['total_schools', 'total']].sum()
hh['share100'] = hh.total / hh.total_schools
h23 = hh.share100.unstack()[2023]
for nm, y in (('change 2023-24 (S1)', d2324), ('change 2023-25 (S2)', s2[2025] - s2[2023])):
    r = ols(y.rename('y'), h23.rename('x')); r['spec'] = f'{nm} on share of schools with 100 per cent result in 2023'; rows.append(r)
a12 = pd.DataFrame(rows)[['spec', 'n', 'slope', 'se', 'p', 'r2', 'spearman']]
a12.round(3).to_csv(os.path.join(res, 'tables', 'T12_exploratory_school_markers.csv'), index=False)
log(a12.round(3).to_string(index=False))
log('state share of schools with 100 per cent result by year (workbooks):')
log((hh.groupby('year').sum().assign(share=lambda d: (100 * d.total / d.total_schools).round(2))).to_string())

# ---------------- post hoc: division pattern ----------------
log('\n== POST HOC: by division ==')
dv = pd.DataFrame({'division': division, 'p2019': s1[2019], 'p2023': s1[2023], 'p2024': s1[2024], 'chg': d2324,
                   'rf2023': s2[2023], 'rf2025': s2[2025], 'rf_chg': s2[2025] - s2[2023]})
log(dv.groupby('division').mean().round(2).to_string())
dv.groupby('division').mean().round(2).to_csv(os.path.join(res, 'tables', 'T13_posthoc_division_means.csv'))

with open(os.path.join(res, 'analysis_log.txt'), 'w', encoding='utf-8') as fh:
    fh.write('\n'.join(LOG))
