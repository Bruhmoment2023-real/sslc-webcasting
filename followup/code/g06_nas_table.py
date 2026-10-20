"""Build data/nas2021_class10_district.csv from the 34 report cards (page 25 text layer). Usage: python -I g06_nas_table.py DRC_DIR OUT_CSV"""
import sys, os, re, glob, pymupdf, csv
d, out = sys.argv[1], sys.argv[2]
MAP = {'Bagalkot': 'BAGALAKOTE', 'Ballari': 'BALLARI (incl. VIJAYANAGARA)', 'Belagavi Chikkodi': 'CHIKKODI', 'Belagavi': 'BELAGAVI',
       'Bengaluru Rural': 'BENGALURU RURAL', 'Bengaluru U North': 'BENGALURU NORTH', 'Bengaluru U South': 'BENGALURU SOUTH', 'Bidar': 'BIDAR',
       'Chamarajanagara': 'CHAMARAJANAGARA', 'Chikkaballapura': 'CHIKKABALLAPURA', 'Chikkamangaluru': 'CHIKKAMAGALURU', 'Chitradurga': 'CHITRADURGA',
       'Dakshina Kannada': 'DAKSHINA KANNADA', 'Davanagere': 'DAVANAGERE', 'Dharwad': 'DHARWAD', 'Gadag': 'GADAG', 'Hassan': 'HASSAN', 'Haveri': 'HAVERI',
       'Kalburgi': 'KALABURAGI', 'Kodagu': 'KODAGU', 'Kolar': 'KOLAR', 'Koppal': 'KOPPALA', 'Mandya': 'MANDYA', 'Mysuru': 'MYSURU', 'Raichur': 'RAICHURU',
       'Ramanagara': 'RAMANAGARA', 'Shivamogga': 'SHIVAMOGGA', 'Tumakuru Madhugiri': 'MADHUGIRI', 'Tumakuru': 'TUMAKURU', 'Udupi': 'UDUPI',
       'Uttara Kannada Sirsi': 'SIRSI', 'Uttara Kannada': 'UTTARA KANNADA', 'Vijayapura': 'VIJAYAPURA', 'Yadagiri': 'YADAGIRI'}
SUBJ = ['MIL', 'Maths', 'Science', 'SocSci', 'English']
rows = []
for f in sorted(glob.glob(os.path.join(d, '*.pdf'))):
    key = os.path.basename(f)[len('NAS21_DRC_'):-4]
    t = pymupdf.open(f)[24].get_text().replace('​', '')
    v = [(int(a), float(b)) for a, b in re.findall(r'(\d+)\s*\(\s*([\d.]+)\s*\)', t)]
    dd = [x for i, x in enumerate(v) if i % 2 == 0]           # every value appears twice in the text layer
    assert len(dd) == 15 and all(v[2*i] == v[2*i+1] for i in range(15)), key
    r = {'unit_name': MAP[key], 'file': os.path.basename(f)}
    for i, s in enumerate(SUBJ):
        r[s] = dd[3*i][0]; r[s + '_se'] = dd[3*i][1]; r[s + '_state'] = dd[3*i+1][0]; r[s + '_natl'] = dd[3*i+2][0]
    r['nas_mean5'] = sum(r[s] for s in SUBJ) / 5; r['nas_ms'] = (r['Maths'] + r['Science']) / 2
    rows.append(r)
assert len({r['unit_name'] for r in rows}) == 34
with open(out, 'w', newline='', encoding='utf-8') as fh:
    w = csv.DictWriter(fh, fieldnames=list(rows[0])); w.writeheader(); w.writerows(rows)
print(len(rows), 'rows written')
