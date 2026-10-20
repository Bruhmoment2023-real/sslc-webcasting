"""Query OpenAlex (free, no key) for prior work. Saves raw JSON and prints a compact listing.
Usage: python 05_openalex_search.py OUT_DIR"""
import sys, json, time, urllib.request, urllib.parse, os
sys.stdout.reconfigure(encoding='utf-8')
out = sys.argv[1]
Q = {
 'borcan': 'Fighting Corruption in Education: What Works and Who Benefits',
 'karnataka_sslc': 'Karnataka SSLC examination results',
 'sslc_webcast': 'webcasting examination Karnataka SSLC CCTV',
 'india_board_cheating': 'cheating board examination India CCTV malpractice pass rate',
 'up_board': 'Uttar Pradesh board examination cheating crackdown CCTV',
 'bihar_board': 'Bihar board examination cheating pass percentage',
 'exam_monitoring': 'monitoring examination cheating cameras high-stakes exam test scores',
 'grade_inflation_india': 'grade inflation board examination India moderation marks',
 'moderation_cbse': 'score manipulation moderation CBSE marks bunching',
 'cheating_gender': 'cheating exams monitoring gender gap test scores natural experiment',
 'teacher_cheating': 'teacher cheating external monitors test scores Italy',
 'indonesia_cbt': 'computer-based testing cheating Indonesia national exam',
 'grace_marks': 'grace marks pass threshold bunching examination India',
}
for k, q in Q.items():
    url = 'https://api.openalex.org/works?' + urllib.parse.urlencode({'search': q, 'per-page': 12,
        'select': 'id,doi,title,publication_year,cited_by_count,primary_location,authorships,type', 'mailto': 'research@example.org'})
    try:
        with urllib.request.urlopen(urllib.request.Request(url, headers={'User-Agent': 'student-research/0.1'}), timeout=40) as r:
            d = json.load(r)
    except Exception as e:
        print('##', k, 'ERROR', e); continue
    json.dump(d, open(os.path.join(out, f'openalex_{k}.json'), 'w', encoding='utf-8'), ensure_ascii=False)
    print(f"## {k} | q='{q}' | total={d['meta']['count']}")
    for w in d['results']:
        au = ', '.join(a['author']['display_name'] for a in w['authorships'][:3])
        src = ((w.get('primary_location') or {}).get('source') or {}).get('display_name')
        print(f"   {w['publication_year']} | {str(w['title'])[:105]} | {au} | {src} | c={w['cited_by_count']} | {w.get('doi')}")
    time.sleep(1.2)
