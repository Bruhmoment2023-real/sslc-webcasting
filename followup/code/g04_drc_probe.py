import sys; sys.stdout.reconfigure(encoding="utf-8")
import sys, pymupdf
d = pymupdf.open(sys.argv[1]); print(len(d), 'pages')
for i, p in enumerate(d):
    t = p.get_text()
    print('--- page', i+1, len(t), 'chars', len(p.get_images()), 'imgs'); print(t[:int(sys.argv[2]) if len(sys.argv)>2 else 400].replace('\n',' | '))
