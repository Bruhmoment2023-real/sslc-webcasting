import sys, pymupdf
sys.stdout.reconfigure(encoding='utf-8')
d = pymupdf.open(sys.argv[1]); out = sys.argv[2]
t = '\n'.join(f'\n=====page {i+1}=====\n' + p.get_text() for i, p in enumerate(d))
open(out, 'w', encoding='utf-8').write(t); print(sys.argv[1], len(d), 'pages', len(t), 'chars')
