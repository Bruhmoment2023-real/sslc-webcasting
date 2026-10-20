"""OCR every page of the scanned PDFs in a folder (RapidOCR, local, free).
Usage: python f03_ocr_pdf.py PDF_DIR OUT_DIR [dpi]
One text file per page with boxes grouped into visual rows, cells separated by ' | '.
Pages that are lists of individual students (toppers: names, phone numbers) are NOT written out."""
import sys, os, glob, numpy as np, pymupdf, cv2, time
from rapidocr_onnxruntime import RapidOCR
src, out = sys.argv[1], sys.argv[2]
dpi = int(sys.argv[3]) if len(sys.argv) > 3 else 200
os.makedirs(out, exist_ok=True)
eng = RapidOCR()
for pdf in sorted(glob.glob(os.path.join(src, '*.pdf'))):
    stem = os.path.splitext(os.path.basename(pdf))[0]
    doc = pymupdf.open(pdf)
    for i, page in enumerate(doc):
        o = os.path.join(out, f'{stem}_p{i+1:02d}.txt')
        if os.path.exists(o): continue
        t0 = time.time()
        pix = page.get_pixmap(dpi=dpi)
        img = np.frombuffer(pix.samples, dtype=np.uint8).reshape(pix.height, pix.width, pix.n)
        if pix.n == 4: img = cv2.cvtColor(img, cv2.COLOR_RGBA2BGR)
        elif pix.n == 3: img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
        res, _ = eng(img)
        boxes = sorted((sum(p[1] for p in b) / 4, min(p[0] for p in b), t, max(p[1] for p in b) - min(p[1] for p in b)) for b, t, c in (res or []))
        txt = ' '.join(b[2] for b in boxes).upper()
        if 'TOPPER' in txt or 'CONTACT NO' in txt or "FATHER" in txt:
            open(o, 'w', encoding='utf-8').write('[page skipped: list of individual students - not extracted]\n')
            print(stem, i + 1, 'SKIPPED (individual students)', flush=True); continue
        med = np.median([b[3] for b in boxes]) if boxes else 20
        rows, cur, lasty = [], [], None
        for b in boxes:
            if lasty is not None and b[0] - lasty > 0.6 * med:
                rows.append(cur); cur = []
            cur.append(b); lasty = b[0]
        rows.append(cur)
        with open(o, 'w', encoding='utf-8') as f:
            for r in rows:
                f.write(' | '.join(b[2] for b in sorted(r, key=lambda b: b[1])) + '\n')
        print(stem, i + 1, len(boxes), 'boxes', round(time.time() - t0, 1), 's', flush=True)
