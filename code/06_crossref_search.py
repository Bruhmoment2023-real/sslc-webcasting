"""Query Crossref (free, no key) for prior work; fall back when OpenAlex is rate-limited.
Usage: python 06_crossref_search.py OUT_DIR"""
import sys, json, time, urllib.request, urllib.parse, os
sys.stdout.reconfigure(encoding='utf-8')
out = sys.argv[1]
Q = {
 'borcan': 'Fighting Corruption in Education: What Works and Who Benefits',
 'karnataka_sslc': 'Karnataka SSLC examination results analysis',
 'sslc_webcast': 'webcasting examination centres Karnataka SSLC CCTV pass percentage',
 'india_board_cheating': 'cheating board examinations India CCTV malpractice pass rate',
 'up_board': 'Uttar Pradesh board examination cheating crackdown CCTV dropouts',
 'bihar_board': 'Bihar board examination cheating pass percentage',
 'exam_monitoring': 'monitoring cheating cameras high-stakes exam test scores',
 'grade_inflation_india': 'grade inflation board examination India moderation of marks',
 'manipulation_bunching': 'manipulation exam scores bunching pass threshold grading leniency',
 'external_monitors': 'external monitors classroom cheating test scores natural experiment',
 'indonesia_cbt': 'computer-based testing cheating Indonesia national examination integrity',
 'cheating_cost': 'costs of corruption cheating exams learning long-run outcomes anti-cheating campaign',
}
for k, q in Q.items():
    url = 'https://api.crossref.org/works?' + urllib.parse.urlencode({'query.bibliographic': q, 'rows': 10,
        'select': 'DOI,title,author,issued,container-title,type,is-referenced-by-count', 'mailto': 'research@example.org'})
    try:
        with urllib.request.urlopen(urllib.request.Request(url, headers={'User-Agent': 'student-research/0.1 (mailto:research@example.org)'}), timeout=60) as r:
            d = json.load(r)
    except Exception as e:
        print('##', k, 'ERROR', e); time.sleep(3); continue
    json.dump(d, open(os.path.join(out, f'crossref_{k}.json'), 'w', encoding='utf-8'), ensure_ascii=False)
    print(f"## {k} | q='{q}'")
    for w in d['message']['items']:
        au = ', '.join((a.get('family') or a.get('name') or '?') for a in w.get('author', [])[:3])
        yr = (w.get('issued', {}).get('date-parts') or [[None]])[0][0]
        print(f"   {yr} | {(w.get('title') or ['?'])[0][:110]} | {au} | {(w.get('container-title') or [''])[0][:40]} | c={w.get('is-referenced-by-count')} | {w.get('DOI')}")
    time.sleep(2)
