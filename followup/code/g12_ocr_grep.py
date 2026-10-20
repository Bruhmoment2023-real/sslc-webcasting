import sys, numpy as np, pymupdf, cv2, re
sys.stdout.reconfigure(encoding='utf-8')
from rapidocr_onnxruntime import RapidOCR
eng = RapidOCR(); pdf = sys.argv[1]; pages = [int(x) for x in sys.argv[2].split(',')]; out = sys.argv[3]
doc = pymupdf.open(pdf); txt = []
for p in pages:
    pix = doc[p-1].get_pixmap(dpi=150); img = np.frombuffer(pix.samples, dtype=np.uint8).reshape(pix.height, pix.width, pix.n)
    img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR) if pix.n == 3 else img
    res, _ = eng(img); t = ' | '.join(r[1] for r in (res or [])); txt.append(f'=== page {p}\n{t}')
open(out, 'w', encoding='utf-8').write('\n'.join(txt))
for m in re.finditer(r'(?i)(web ?cast|web ?stream|cctv|grace|live|camera|surveillance|moderat)', '\n'.join(txt)): print(pdf.split('/')[-1], m.group(0))
print('done', pdf, len(txt))
