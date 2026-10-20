"""POST HOC analyses, added after seeing the pre-specified results. Everything here is labelled post hoc.

Usage: python 21_posthoc.py CLEAN_DIR RESULTS_DIR
 P1 rank stability: Spearman correlation of district pass rates between adjacent first/main exams
 P2 gaps between groups (management, medium, area, gender) before and after 2024, state level
 P3 taluk-level dispersion (cumulative results after 2024, so not like-for-like)
 P4 simple permutation check for the A4c slope
"""
import sys, os
import numpy as np
import pandas as pd
from scipy import stats
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from common import read

clean, res = sys.argv[1], sys.argv[2]
BLUE, ORANGE, AQUA, INK, MUTED, SURF = '#2a78d6', '#eb6834', '#1baf7a', '#0b0b0b', '#52514e', '#fcfcfb'
plt.rcParams.update({'figure.facecolor': SURF, 'axes.facecolor': SURF, 'savefig.facecolor': SURF, 'font.size': 10,
                     'axes.edgecolor': '#c9c8c2', 'axes.labelcolor': MUTED, 'xtick.color': MUTED, 'ytick.color': MUTED,
                     'axes.spines.top': False, 'axes.spines.right': False, 'axes.grid': True, 'grid.color': '#e9e8e3',
                     'axes.titlesize': 11, 'axes.titleweight': 'bold', 'axes.titlelocation': 'left', 'legend.frameon': False})
out = []


def log(*a):
    s = ' '.join(str(x) for x in a); print(s); out.append(s)


p = read(os.path.join(clean, 'panel_district_year.csv'))
s1 = p[p.series == 'S1'].pivot(index='unit', columns='year', values='pass_pct')
s2 = p[p.series == 'S2'].pivot(index='unit', columns='year', values='pass_pct')

log('== P1 rank stability (Spearman) between adjacent first/main exams ==')
rows = []
for nm, w, prs in (('S1 all candidates', s1, [(2014, 2015), (2015, 2016), (2016, 2017), (2017, 2018), (2018, 2019), (2019, 2020), (2020, 2022), (2022, 2023), (2023, 2024)]),
                   ('S2 regular freshers', s2, [(2015, 2017), (2017, 2018), (2018, 2019), (2019, 2020), (2020, 2022), (2022, 2023), (2023, 2025), (2025, 2026)])):
    for a, b in prs:
        rho = stats.spearmanr(w[a], w[b])[0]
        rows.append(dict(series=nm, pair=f'{a}-{b}', spearman=rho, pearson=w[a].corr(w[b]),
                         mean_abs_rank_move=(w[a].rank() - w[b].rank()).abs().mean(), sd_change=(w[b] - w[a]).std()))
r = pd.DataFrame(rows)
r.round(3).to_csv(os.path.join(res, 'tables', 'P1_rank_stability.csv'), index=False)
log(r.round(3).to_string(index=False))
log('S1 2024 vs earlier years (Spearman):', {y: round(stats.spearmanr(s1[2024], s1[y])[0], 3) for y in (2014, 2015, 2016, 2017, 2018, 2019, 2020, 2022, 2023)})
log('S2 2025 vs earlier years (Spearman):', {y: round(stats.spearmanr(s2[2025], s2[y])[0], 3) for y in (2015, 2017, 2018, 2019, 2020, 2022, 2023)})
log('S1 2024 vs S2 2025 (Spearman):', round(stats.spearmanr(s1[2024], s2[2025])[0], 3))

fig, ax = plt.subplots(figsize=(7.6, 3.9))
d = r[r.series == 'S1 all candidates']
ax.bar(d.pair, d.spearman, color=[ORANGE if x == '2023-2024' else BLUE for x in d.pair], width=0.62, zorder=3)
for x, v in zip(d.pair, d.spearman):
    ax.text(x, v + 0.015, f'{v:.2f}', ha='center', fontsize=8, color=INK)
ax.set_ylim(0, 1.05); ax.set_ylabel('Rank correlation of district pass rates'); ax.tick_params(axis='x', labelsize=8)
ax.set_title('How much the district order carried over from one main exam to the next')
fig.tight_layout(); fig.savefig(os.path.join(res, 'figures', 'F6_posthoc_rank_stability.png'), dpi=170); plt.close(fig)

log('\n== P2 gaps between groups, state level ==')
mg = read(os.path.join(clean, 'district_regular_fresh_by_management.csv'))
pre = mg[mg.scope == 'main_exam'].groupby(['year', 'management'])[['app', 'passed']].sum()
pre = (100 * pre.passed / pre.app).unstack()
g = pd.read_csv(os.path.join(clean, 'transcribed', 'state_first_exam_by_group.csv'))
post = g[(g.dimension == 'management') & (g.year >= 2024)].pivot(index='year', columns='group', values='pct').rename(columns={'government': 'govt'})
m = pd.concat([pre.drop(index=2021), post])[['govt', 'aided', 'unaided']]
m['unaided_minus_govt'] = m.unaided - m.govt
m.round(2).to_csv(os.path.join(res, 'tables', 'P2_management_first_exam_series.csv'))
log('management, regular freshers, first/main exam (workbooks to 2023, press notes 2024-26):'); log(m.round(2).to_string())
ur = read(os.path.join(clean, 'district_regular_fresh_by_urban_rural.csv'))
u = ur[ur.scope == 'main_exam'].groupby('year')[['rural_app', 'rural_pass', 'urban_app', 'urban_pass']].sum()
u = pd.DataFrame({'rural': 100 * u.rural_pass / u.rural_app, 'urban': 100 * u.urban_pass / u.urban_app}).drop(index=2021)
u.loc[2025] = [65.47, 67.05]; u.loc[2026] = [94.80, 93.20]
u['rural_minus_urban'] = u.rural - u.urban
u.round(2).to_csv(os.path.join(res, 'tables', 'P2_rural_urban_first_exam_series.csv'))
log('rural/urban, regular freshers, first/main exam (2024 Exam-1 not usable: counts look swapped in the press note):'); log(u.round(2).to_string())

fig, ax = plt.subplots(figsize=(7.8, 4.2))
for c, col, mk, lab in (('govt', BLUE, 'o', 'Government'), ('aided', AQUA, 's', 'Aided'), ('unaided', ORANGE, '^', 'Unaided (private)')):
    ax.plot(m.index, m[c], color=col, lw=2, marker=mk, ms=5, label=lab)
    ax.annotate(lab, (2026, m.loc[2026, c]), xytext=(6, {'govt': -2, 'aided': -11, 'unaided': 5}[c]), textcoords='offset points', fontsize=8, color=INK)
ax.axvline(2023.5, color='#c9c8c2', lw=1, ls=(0, (3, 3)))
ax.text(2023.55, 57, 'webcasting from 2024', fontsize=8, color=MUTED)
ax.set_xlim(2014.5, 2027.6); ax.set_xticks([2015, 2017, 2018, 2019, 2020, 2022, 2023, 2024, 2025, 2026]); ax.tick_params(axis='x', labelsize=8)
ax.set_ylabel('Pass percentage, regular freshers, first/main exam')
ax.set_title('Pass rate by school management type (2021 omitted)'); ax.legend(fontsize=8, loc='lower left')
fig.tight_layout(); fig.savefig(os.path.join(res, 'figures', 'F7_posthoc_management_series.png'), dpi=170); plt.close(fig)

log('\n== P3 taluk level (regular freshers excluding residential and corporation schools; cumulative from 2024) ==')
t = pd.read_csv(os.path.join(clean, 'taluk_regular_fresh.csv'), keep_default_na=False, na_values=[''])
t['pct'] = 100 * t.passed / t.app
tw = t.pivot_table(index='taluk_code', columns='year', values='pct')
log('taluks:', len(tw), '| s.d. across taluks by year:', tw.std().round(2).to_dict())
for a, b in ((2018, 2019), (2019, 2020), (2022, 2023), (2023, 2024), (2023, 2025)):
    dd = tw[[a, b]].dropna()
    sl = stats.linregress(dd[a], dd[b] - dd[a])
    log(f'taluk change {a}->{b} on {a} level: n={len(dd)} slope={sl.slope:.3f} r2={sl.rvalue**2:.3f} spearman(levels)={stats.spearmanr(dd[a], dd[b])[0]:.3f} mean change={(dd[b]-dd[a]).mean():.2f}')

log('\n== P4 permutation check of A4c (change 2023-24 on rise 2019-23), 20000 shuffles ==')
rng = np.random.default_rng(20261013)
x = (s1[2023] - s1[2019]).values; y = (s1[2024] - s1[2023]).values
obs = stats.linregress(x, y).slope
sims = np.array([stats.linregress(rng.permutation(x), y).slope for _ in range(20000)])
log(f'observed slope {obs:.3f}; share of shuffles with slope <= observed: {(sims <= obs).mean():.4f}')

with open(os.path.join(res, 'posthoc_log.txt'), 'w', encoding='utf-8') as fh:
    fh.write('\n'.join(out))
