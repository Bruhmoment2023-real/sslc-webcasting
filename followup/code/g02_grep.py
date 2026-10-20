import sys, pymupdf, re
f=sys.argv[1]; pat=re.compile(sys.argv[2],re.I)
d=pymupdf.open(f)
for i,p in enumerate(d):
    for ln in p.get_text().splitlines():
        if pat.search(ln): print(i+1, ln)
