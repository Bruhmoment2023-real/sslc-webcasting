"""Slow, backed-off OpenAlex queries. Logs every query (time, URL, status, hit count) to raw/lit/openalex_log.jsonl and titles to raw/lit/openalex_hits_<tag>.tsv.
Usage: python -I g10_openalex.py OUT_DIR  (queries are defined below). No email or key is sent."""
import sys, os, json, time, urllib.request, urllib.parse, datetime
out = sys.argv[1]; os.makedirs(out, exist_ok=True)
SEL = 'id,doi,title,publication_year,cited_by_count,authorships,primary_location,abstract_inverted_index'
def get(url, tries=5):
    for k in range(tries):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers={'User-Agent': 'student-research-script/1.0'}), timeout=60) as r:
                return r.status, json.loads(r.read().decode('utf-8'))
        except urllib.error.HTTPError as e:
            if e.code in (429, 503): time.sleep(20 * (k + 1)); continue
            return e.code, None
        except Exception as e:
            time.sleep(10)
    return 0, None
def abstract(ii):
    if not ii: return ''
    w = {}
    for t, ps in ii.items():
        for p in ps: w[p] = t
    return ' '.join(w[i] for i in sorted(w))
def run(tag, params):
    url = 'https://api.openalex.org/works?' + urllib.parse.urlencode({**params, 'select': SEL})
    st, js = get(url); now = datetime.datetime.now().isoformat(timespec='seconds')
    n = js['meta']['count'] if js else None
    open(os.path.join(out, 'openalex_log.jsonl'), 'a', encoding='utf-8').write(json.dumps({'tag': tag, 'time': now, 'url': url, 'status': st, 'count': n}) + '\n')
    print(tag, st, n)
    if js:
        with open(os.path.join(out, f'openalex_hits_{tag}.jsonl'), 'w', encoding='utf-8') as f:
            for w in js['results']:
                f.write(json.dumps({'id': w['id'], 'doi': w.get('doi'), 'title': w['title'], 'year': w['publication_year'], 'cites': w['cited_by_count'],
                    'authors': [a['author']['display_name'] for a in w['authorships'][:6]], 'venue': ((w.get('primary_location') or {}).get('source') or {}).get('display_name'),
                    'abstract': abstract(w.get('abstract_inverted_index'))}, ensure_ascii=False) + '\n')
    time.sleep(4)
    return js
Q = [
 ('borcan', {'search': 'Fighting corruption in education: what works and who benefits Borcan Lindahl Mitrut', 'per-page': 5}),
 ('cheat_monitor', {'search': 'cheating examination monitoring cameras high-stakes exam', 'per-page': 25}),
 ('cheat_india', {'search': 'cheating board examination India copying', 'per-page': 25}),
 ('up_bihar', {'search': 'Uttar Pradesh Bihar anti-copying board exam mass cheating', 'per-page': 25}),
 ('grace_marks', {'search': 'grace marks moderation board examination India pass rate', 'per-page': 25}),
 ('karnataka_sslc', {'search': 'Karnataka SSLC examination results', 'per-page': 25}),
 ('karnataka_webcast', {'search': 'webcasting examination Karnataka SSLC malpractice', 'per-page': 25}),
 ('grade_inflation_india', {'search': 'grade inflation school board examinations India marks manipulation', 'per-page': 25}),
]
for tag, p in Q: run(tag, p)
# citing works of Borcan et al.
try:
    first = json.loads(open(os.path.join(out, 'openalex_hits_borcan.jsonl'), encoding='utf-8').readline())
    print('Borcan candidate:', first['title'], first['year'], first['id'])
    wid = first['id'].split('/')[-1]
    run('cites_borcan', {'filter': 'cites:' + wid, 'per-page': 50, 'sort': 'cited_by_count:desc'})
except Exception as e: print('no borcan', e)
