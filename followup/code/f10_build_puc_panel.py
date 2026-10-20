"""Build the II PUC district panel (regular students, annual exam / Exam-1, pass % as printed).
Usage: python f10_build_puc_panel.py OCR_DIR OUT_CSV
2023-2026 and 2018 are parsed from the OCR row files; 2016-2017 are typed from the page image
(the scan is skewed and OCR scrambles the row order) and were checked against the OCR number list."""
import sys, os, re
import pandas as pd
ocr, out = sys.argv[1], sys.argv[2]
CANON = {'DAKSHINAKANNADA': 'DAKSHINA KANNADA', 'DAKSBINAKANNADA': 'DAKSHINA KANNADA', 'UDUPI': 'UDUPI', 'VIJAYAPURA': 'VIJAYAPURA', 'UTTARAKANNADA': 'UTTARA KANNADA',
         'UTHARAKANNADA': 'UTTARA KANNADA', 'KODAGU': 'KODAGU', 'BENGALURUSOUTH': 'BENGALURU SOUTH', 'BENGALURUNORTH': 'BENGALURU NORTH',
         'SHIVAMOGGA': 'SHIVAMOGGA', 'SHIVAMOGA': 'SHIVAMOGGA', 'CHIKKAMAGALURU': 'CHIKKAMAGALURU', 'CHIKKAMANGALURU': 'CHIKKAMAGALURU',
         'BENGALURURURAL': 'BENGALURU RURAL', 'BENGALURURURAI': 'BENGALURU RURAL', 'BAGALKOTE': 'BAGALAKOTE', 'BAGALKOT': 'BAGALAKOTE', 'BAGAIKOT': 'BAGALAKOTE',
         'KOLAR': 'KOLAR', 'HASSAN': 'HASSAN', 'CHAMARAJANAGARA': 'CHAMARAJANAGARA', 'CHAMRAJNAGAR': 'CHAMARAJANAGARA', 'CHIKKODI': 'CHIKKODI',
         'RAMANAGARA': 'RAMANAGARA', 'RAMANAGAR': 'RAMANAGARA', 'MYSURU': 'MYSURU', 'MYSORE': 'MYSURU', 'CHIKKABALLAPURA': 'CHIKKABALLAPURA',
         'CHIKKABALAPURA': 'CHIKKABALLAPURA', 'BIDAR': 'BIDAR', 'TUMAKURU': 'TUMAKURU', 'DAVANAGERE': 'DAVANAGERE', 'DAVANGERE': 'DAVANAGERE',
         'KOPPAL': 'KOPPALA', 'DHARWAD': 'DHARWAD', 'MANDYA': 'MANDYA', 'HAVERI': 'HAVERI', 'YADGIRI': 'YADAGIRI', 'YADGIR': 'YADAGIRI',
         'BELAGAVI': 'BELAGAVI', 'KALABURAGI': 'KALABURAGI', 'KALABURGI': 'KALABURAGI', 'BALLARI': 'BALLARI', 'RAICHUR': 'RAICHURU',
         'CHITRADURGA': 'CHITRADURGA', 'GADAG': 'GADAG'}
rows = []
def parse(fn, years, src):
    n = 0
    for ln in open(os.path.join(ocr, fn), encoding='utf-8'):
        if 'Malpractice' in ln: break   # the next table on the page lists the same district names
        p = [x.strip() for x in ln.strip().split('|')]
        if len(p) < 3: continue
        k = re.sub(r'[^A-Z]', '', p[1].upper())
        if k not in CANON: continue
        vals = [float(re.sub(r'[^0-9.]', '', x.replace(',', '.')).rstrip('.')) for x in p[2:2 + len(years)]]
        for y, v in zip(years, vals): rows.append((CANON[k], y, v, src))
        n += 1
    print(fn, n, 'districts')
parse('PRESS_STATS_EXAM1_2024_p14.txt', [2024, 2023], 'KSEAB II PUC Exam-1 2024 press note, table 16 (regular students)')
parse('PRESS_STAT_2025_II_PUC_EXAM_1_p12.txt', [2025], 'KSEAB II PUC Exam-1 2025 press note, table 17')
parse('Press_stat_2026_Exam_1_p15.txt', [2026, 20250], 'KSEAB II PUC Exam-1 2026 press note, table 17 (freshers)')
parse('PUC_Press_Release_2018_p13.txt', [2018], 'DPUE press release March 2018, table 15 (regular students); Wayback copy')
parse('PUC_Press_Release_2018_p14.txt', [2018], 'DPUE press release March 2018, table 15 (regular students); Wayback copy')
rows.append(('BIDAR', 2018, 52.63, 'DPUE press release March 2018, table 15; district name read from the page image (OCR dropped it)'))
T = """UDUPI 90.01 90.35|DAKSHINA KANNADA 89.92 90.48|UTTARA KANNADA 71.99 76.44|KODAGU 70.83 79.35|CHIKKAMAGALURU 68.03 67.34|SHIVAMOGGA 68.00 69.28|BENGALURU NORTH 67.17 70.83|BENGALURU SOUTH 66.63 70.88|CHAMARAJANAGARA 65.34 64.86|BAGALAKOTE 63.11 65.91|HASSAN 59.88 65.47|BENGALURU RURAL 59.64 66.38|CHIKKABALLAPURA 59.63 63.74|MYSURU 59.03 65.53|KOLAR 57.87 61.76|KOPPALA 56.84 54.32|MANDYA 56.43 56.52|DHARWAD 55.73 62.86|DAVANAGERE 55.17 58.01|BALLARI 55.13 59.09|HAVERI 54.95 60.54|TUMAKURU 54.72 56.63|GADAG 53.11 49.28|RAMANAGARA 51.55 56.36|CHITRADURGA 47.31 47.55|RAICHURU 46.98 49.61|KALABURAGI 44.94 57.05|BELAGAVI 44.25 62.05|VIJAYAPURA 43.00 60.39|YADAGIRI 42.07 44.16|BIDAR 42.05 52.07"""
for it in T.split('|'):
    *nm, a, b = it.split(); nm = ' '.join(nm)
    rows.append((nm, 2017, float(a), 'DPUE press release March 2017, table 16 (regular students); Wayback copy; typed from page image'))
    rows.append((nm, 2016, float(b), 'DPUE press release March 2017, table 16 (regular students); Wayback copy; typed from page image'))
d = pd.DataFrame(rows, columns=['district', 'year', 'pass_pct', 'source'])
# cross-check: the 2025 column is printed in both the 2025 and the 2026 note
a = d[d.year == 2025].set_index('district').pass_pct; b = d[d.year == 20250].set_index('district').pass_pct
print('2025 column printed twice: max abs difference', (a - b).abs().max(), '| districts', len(a), len(b))
d = d[d.year != 20250]
print(d.groupby('year').agg(n=('district', 'nunique'), mean=('pass_pct', 'mean'), mn=('pass_pct', 'min'), mx=('pass_pct', 'max')).round(2))
assert not d.duplicated(['district', 'year']).any()
d.sort_values(['year', 'district']).to_csv(out, index=False)
