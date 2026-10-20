import sys, pymupdf
f, pg, out = sys.argv[1], int(sys.argv[2]), sys.argv[3]
d = pymupdf.open(f); d[pg-1].get_pixmap(dpi=int(sys.argv[4]) if len(sys.argv)>4 else 110).save(out)
