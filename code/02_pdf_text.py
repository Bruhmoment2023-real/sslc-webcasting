"""Extract the text layer (if any) of each PDF in a folder to OUT_DIR/<name>.txt and report pages/characters.
Usage: python 02_pdf_text.py PDF_DIR OUT_DIR"""
import sys, glob, os, pdfplumber
src, out = sys.argv[1], sys.argv[2]
os.makedirs(out, exist_ok=True)
for f in sorted(glob.glob(os.path.join(src, '*.pdf'))):
    try:
        with pdfplumber.open(f) as pdf:
            n = len(pdf.pages); chars = 0
            with open(os.path.join(out, os.path.basename(f)[:-4] + '.txt'), 'w', encoding='utf-8') as fh:
                for i, p in enumerate(pdf.pages[:60]):
                    t = p.extract_text() or ''
                    chars += len(t); fh.write(f'\n===== page {i+1} =====\n{t}\n')
        print(f'{os.path.basename(f):45s} pages={n:3d} text_chars={chars}')
    except Exception as e:
        print(os.path.basename(f), 'ERROR', e)
