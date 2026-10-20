"""Extract NAS 2021 Class 10 district mean percent-correct (page 25 text layer) from the 34 Karnataka district report cards.
Usage: python -I g05_nas_extract.py DRC_DIR OUT_CSV"""
import sys, os, re, glob, pymupdf, csv
d, out = sys.argv[1], sys.argv[2]
rows = []
for f in sorted(glob.glob(os.path.join(d, '*.pdf'))):
    doc = pymupdf.open(f); n = len(doc)
    t = doc[24].get_text().replace('​', '')
    # triplets of "value (se)" : district, state, national for MIL, Maths, Science, SocSci, English
    m = re.findall(r'(\d+)\s*\(\s*([\d.]+)\s*\)', t)
    vals = [(int(a), float(b)) for a, b in m]
    # the text layer repeats each value twice (visible + hidden); collapse consecutive duplicates
    dd = []
    for v in vals:
        if not dd or dd[-1] != v or (len(dd) % 1 == 0 and False): dd.append(v)
    rows.append((os.path.basename(f), n, len(vals), vals[:12], len(dd), dd[:15]))
for r in rows: print(r)
