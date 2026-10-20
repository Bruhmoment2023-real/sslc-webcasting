"""Verify candidate references against Crossref by title (top 3 hits printed for each). Saves JSON.
Usage: python 07_verify_refs.py OUT_JSON"""
import sys, json, time, urllib.request, urllib.parse
sys.stdout.reconfigure(encoding='utf-8')
T = [
 "When the cat is near, the mice won't play: The effect of external examiners in Italian schools",
 "Cheating and social interactions. Evidence from a randomized experiment in a national evaluation program",
 "In a Small Moment: Class Size and Moral Hazard in the Italian Mezzogiorno",
 "Rotten Apples: An Investigation of the Prevalence and Predictors of Teacher Cheating",
 "The Causes and Consequences of Test Score Manipulation: Evidence from the New York Regents Examinations",
 "The Long-term Consequences of Teacher Discretion in Grading of High-stakes Tests",
 "Cheating and Incentives: Learning from a Policy Experiment",
 "Counting rotten apples: Student achievement and score manipulation in Italian elementary Schools",
 "The impact of an unexpected wage cut on corruption: Evidence from a Xeroxed exam",
 "Using technology to prevent fraud in high stakes national school examinations: Evidence from Indonesia",
 "The School Governance Environment in Uttar Pradesh, India: Implications for Teacher Accountability and Effort",
 "Myths of Official Measurement: Auditing and Improving Administrative Data in Developing Countries",
 "Does cheating pay? The role of externalities in examination malpractice India",
 "Curbing cheating in board examinations Uttar Pradesh anti-copying",
 "Exam cheating secondary school India evidence",
 "Do Classroom Cameras Deter Cheating? evidence exam surveillance",
 "The effect of monitoring on cheating in exams: evidence from China gaokao surveillance",
 "Teacher cheating and student outcomes Chile SIMCE or Mexico ENLACE manipulation",
 "Manipulation of school leaving exam scores India grade inflation bunching CBSE",
 "Learning loss COVID-19 India school closures test scores Karnataka",
 "Private school effects board examination results Karnataka SSLC determinants district",
]
out = {}
for t in T:
    url = 'https://api.crossref.org/works?' + urllib.parse.urlencode({'query.bibliographic': t, 'rows': 4,
        'select': 'DOI,title,author,issued,container-title,type,volume,page', 'mailto': 'research@example.org'})
    try:
        with urllib.request.urlopen(urllib.request.Request(url, headers={'User-Agent': 'student-research/0.1 (mailto:research@example.org)'}), timeout=60) as r:
            d = json.load(r)
    except Exception as e:
        print('ERR', t, e); time.sleep(3); continue
    out[t] = d['message']['items']
    print('##', t[:90])
    for w in d['message']['items']:
        au = ', '.join((a.get('family') or '?') for a in w.get('author', [])[:5])
        yr = (w.get('issued', {}).get('date-parts') or [[None]])[0][0]
        print(f"   {yr} | {(w.get('title') or ['?'])[0][:105]} | {au} | {(w.get('container-title') or [''])[0][:45]} {w.get('volume','')}:{w.get('page','')} | {w.get('DOI')}")
    time.sleep(1.5)
json.dump(out, open(sys.argv[1], 'w', encoding='utf-8'), ensure_ascii=False)
