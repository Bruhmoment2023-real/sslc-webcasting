"""Print headline, date and article body from saved news HTML (JSON-LD articleBody if present, else <p> text).
Usage: python 04_news_text.py file.html [...]"""
import sys, re, json, html
sys.stdout.reconfigure(encoding='utf-8')
for f in sys.argv[1:]:
    t = open(f, encoding='utf-8', errors='ignore').read()
    print('\n#####', f)
    done = False
    for m in re.finditer(r'<script[^>]*application/ld\+json[^>]*>(.*?)</script>', t, re.S):
        try: d = json.loads(m.group(1))
        except Exception: continue
        for o in (d if isinstance(d, list) else [d]):
            if isinstance(o, dict) and o.get('articleBody'):
                print('HEADLINE:', o.get('headline')); print('DATE:', o.get('datePublished'))
                print(html.unescape(o['articleBody'])); done = True
    if not done:
        tt = re.search(r'<title>(.*?)</title>', t, re.S); print('TITLE:', tt.group(1).strip() if tt else None)
        dm = re.search(r'"datePublished"\s*:\s*"([^"]+)"', t); print('DATE:', dm.group(1) if dm else None)
        for p in re.findall(r'<p[^>]*>(.*?)</p>', t, re.S):
            s = html.unescape(re.sub(r'<[^>]+>', '', p)).strip()
            if len(s) > 60: print(s)
