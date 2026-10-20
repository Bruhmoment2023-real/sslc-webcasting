"""Independent OCR re-extraction of the three scanned district tables (RapidOCR, free, local).
Usage: python f01_ocr_pages.py PRESSNOTE_DIR OUT_DIR
Writes OUT_DIR/ocr_<stem>_p<page>.tsv : one line per text box (y, x, text, confidence), and
OUT_DIR/ocr_<stem>_p<page>_rows.txt : boxes grouped into visual rows."""
import sys, os, numpy as np, pymupdf, cv2
from rapidocr_onnxruntime import RapidOCR
src, out = sys.argv[1], sys.argv[2]
os.makedirs(out, exist_ok=True)
eng = RapidOCR()
for stem, page in (('PN_2024_Exam1', 11), ('PN_2025_Exam1', 8), ('PN_2026_Exam1', 7)):
    doc = pymupdf.open(os.path.join(src, stem + '.pdf'))
    pix = doc[page - 1].get_pixmap(dpi=300)
    img = np.frombuffer(pix.samples, dtype=np.uint8).reshape(pix.height, pix.width, pix.n)
    img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR) if pix.n == 3 else img
    res, _ = eng(img)
    boxes = []
    for b, t, c in res or []:
        ys = [p[1] for p in b]; xs = [p[0] for p in b]
        boxes.append((sum(ys) / 4, min(xs), t, float(c), max(ys) - min(ys)))
    boxes.sort()
    with open(os.path.join(out, f'ocr_{stem}_p{page:02d}.tsv'), 'w', encoding='utf-8') as f:
        for y, x, t, c, h in boxes:
            f.write(f'{y:.0f}\t{x:.0f}\t{t}\t{c:.3f}\n')
    rows, cur, lasty = [], [], None
    med = np.median([b[4] for b in boxes]) if boxes else 20
    for b in boxes:
        if lasty is not None and b[0] - lasty > 0.6 * med:
            rows.append(cur); cur = []
        cur.append(b); lasty = b[0] if not cur[:-1] else (lasty * 0.5 + b[0] * 0.5)
    rows.append(cur)
    with open(os.path.join(out, f'ocr_{stem}_p{page:02d}_rows.txt'), 'w', encoding='utf-8') as f:
        for r in rows:
            r.sort(key=lambda b: b[1])
            f.write(' | '.join(b[2] for b in r) + '\n')
    print(stem, page, pix.width, pix.height, len(boxes), 'boxes', len(rows), 'rows')
