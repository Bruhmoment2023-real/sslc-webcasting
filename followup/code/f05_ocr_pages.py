"""OCR chosen pages of a PDF (RapidOCR). Usage: python f05_ocr_pages.py PDF OUT_DIR DPI p1 p2 ...
Refuses to write pages that list individual students."""
import sys, os, numpy as np, pymupdf, cv2
from rapidocr_onnxruntime import RapidOCR
pdf, out, dpi = sys.argv[1], sys.argv[2], int(sys.argv[3])
os.makedirs(out, exist_ok=True)
eng = RapidOCR(); doc = pymupdf.open(pdf); stem = os.path.splitext(os.path.basename(pdf))[0]
for pg in map(int, sys.argv[4:]):
    pix = doc[pg - 1].get_pixmap(dpi=dpi)
    img = np.frombuffer(pix.samples, dtype=np.uint8).reshape(pix.height, pix.width, pix.n)
    img = cv2.cvtColor(img, cv2.COLOR_RGBA2BGR if pix.n == 4 else cv2.COLOR_RGB2BGR) if pix.n >= 3 else img
    res, _ = eng(img)
    boxes = sorted((sum(p[1] for p in b) / 4, min(p[0] for p in b), t, max(p[1] for p in b) - min(p[1] for p in b)) for b, t, c in (res or []))
    txt = ' '.join(b[2] for b in boxes).upper()
    o = os.path.join(out, f'{stem}_p{pg:02d}.txt')
    if 'TOPPER' in txt or 'CONTACT NO' in txt or 'FATHER' in txt:
        open(o, 'w').write('[skipped: individual students]\n'); print(stem, pg, 'SKIPPED'); continue
    med = np.median([b[3] for b in boxes]) if boxes else 20
    rows, cur, lasty = [], [], None
    for b in boxes:
        if lasty is not None and b[0] - lasty > 0.6 * med: rows.append(cur); cur = []
        cur.append(b); lasty = b[0]
    rows.append(cur)
    with open(o, 'w', encoding='utf-8') as f:
        for r in rows: f.write(' | '.join(b[2] for b in sorted(r, key=lambda b: b[1])) + '\n')
    print(stem, pg, len(boxes), 'boxes', flush=True)
