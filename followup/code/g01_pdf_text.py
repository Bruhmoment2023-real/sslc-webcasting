import sys, pymupdf, glob, os
for f in sorted(glob.glob(sys.argv[1]+'/*.pdf')):
    d=pymupdf.open(f); t=''.join(p.get_text() for p in d)
    print(os.path.basename(f), len(d),'pages', len(t),'chars text layer')
