"""Contact sheets of scanned PDFs so the table pages can be located by eye.
Usage: python f04_contact_sheet.py PDF OUT_PNG [cols] [thumb_width]"""
import sys, pymupdf
from PIL import Image, ImageDraw
pdf, out = sys.argv[1], sys.argv[2]
cols = int(sys.argv[3]) if len(sys.argv) > 3 else 5
tw = int(sys.argv[4]) if len(sys.argv) > 4 else 380
doc = pymupdf.open(pdf)
th = []
for i, p in enumerate(doc):
    z = tw / max(p.rect.width, 1)
    pix = p.get_pixmap(matrix=pymupdf.Matrix(z, z))
    im = Image.frombytes('RGB', (pix.width, pix.height), pix.samples)
    ImageDraw.Draw(im).rectangle([0, 0, 46, 22], fill='yellow'); ImageDraw.Draw(im).text((4, 4), f'p{i+1}', fill='black')
    th.append(im)
h = max(t.height for t in th); rows = (len(th) + cols - 1) // cols
sheet = Image.new('RGB', (cols * tw, rows * h), 'white')
for i, t in enumerate(th): sheet.paste(t, ((i % cols) * tw, (i // cols) * h))
sheet.save(out); print(out, len(th), 'pages', sheet.size)
