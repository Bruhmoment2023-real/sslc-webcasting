"""Render pages of scanned PDFs to PNG so they can be read by eye.
Usage: python 03_render_pdf_pages.py PDF OUT_DIR [first] [last] [dpi]"""
import sys, os, fitz
pdf, out = sys.argv[1], sys.argv[2]
first = int(sys.argv[3]) if len(sys.argv) > 3 else 1
last = int(sys.argv[4]) if len(sys.argv) > 4 else 999
dpi = int(sys.argv[5]) if len(sys.argv) > 5 else 110
os.makedirs(out, exist_ok=True)
doc = fitz.open(pdf)
stem = os.path.splitext(os.path.basename(pdf))[0]
for i in range(first - 1, min(last, len(doc))):
    pix = doc[i].get_pixmap(dpi=dpi)
    pix.save(os.path.join(out, f'{stem}_p{i+1:02d}.png'))
print(stem, len(doc), 'pages')
