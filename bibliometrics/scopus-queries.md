# Scopus and Web of Science queries - paper 04 (SSLC webcasting)

Status: **not run.** There is no Scopus or Web of Science login on this machine. `scopus-drop\` was empty on 2026-10-13.
These strings mirror the four sub-literatures in `search-protocol.md`. Paste each into the *Advanced search* box.

How to use
- Scopus: Advanced document search -> paste -> Search -> Export -> **CSV**, tick *Citation information, Bibliographical information, Abstract & keywords, Include references* (max 20,000 records per export; with references the cap is 2,000 per file, so export in year slices if needed). BibTeX with the same fields also works.
- Web of Science: Advanced Search (Core Collection) -> paste -> Export -> **BibTeX** or *Plain text file*, Record Content = **Full Record and Cited References** (500 records per file).
- Save every export into `bibliometrics\scopus-drop\` (any file names; `.csv`, `.bib` or `.txt`). Then ask for the pipeline to be re-run: the drop folder is checked at the start of each run and the files are merged with `bibliometrix::convert2df()` + `mergeDbSources()`.
- Record the date, the database, and the number of results for each string (add a line under each query below).

## A. Exam cheating, malpractice and monitoring

Scopus
```
TITLE-ABS-KEY ( ( exam* OR "high-stakes" OR "standardi?ed test*" OR "test score*" OR baccalaureate OR matriculation OR "national assessment*" )
  AND ( cheat* OR malpractice* OR "academic dishonesty" OR invigilat* OR proctor* OR cctv OR "surveillance camera*" OR "video surveillance" OR "external examiner*" OR "external monitor*" OR "paper leak*" OR impersonat* ) )
AND NOT TITLE ( plagiaris* OR "contract cheating" OR "deep learning" OR "neural network*" OR "machine learning" OR "face recognition" OR chatgpt OR "generative AI" OR medical OR nursing OR dental )
AND PUBYEAR > 1989 AND ( LIMIT-TO ( LANGUAGE , "English" ) )
AND ( LIMIT-TO ( SUBJAREA , "SOCI" ) OR LIMIT-TO ( SUBJAREA , "ECON" ) OR LIMIT-TO ( SUBJAREA , "PSYC" ) OR LIMIT-TO ( SUBJAREA , "ARTS" ) OR LIMIT-TO ( SUBJAREA , "BUSI" ) )
```
Web of Science
```
TS=((exam* OR "high-stakes" OR "standardi$ed test*" OR "test score*" OR baccalaureate OR matriculation OR "national assessment*")
  AND (cheat* OR malpractice* OR "academic dishonesty" OR invigilat* OR proctor* OR CCTV OR "surveillance camera*" OR "video surveillance" OR "external examiner*" OR "external monitor*" OR "paper leak*" OR impersonat*))
NOT TI=(plagiaris* OR "contract cheating" OR "deep learning" OR "neural network*" OR "machine learning" OR "face recognition" OR chatgpt OR "generative AI" OR medical OR nursing OR dental)
AND PY=(1990-2026) AND LA=(English)
```
Refine by Web of Science Categories: Education & Educational Research; Economics; Psychology Educational; Social Sciences Interdisciplinary.

## B. Grade inflation and manipulation of high-stakes results

Scopus
```
TITLE-ABS-KEY ( ( "grade inflation" OR "grading standard*" OR "grading leniency" OR "lenient grading" OR "score manipulation" OR "test score manipulation" OR "manipulation of test scores" OR "score inflation"
   OR "teacher cheating" OR "teacher discretion" OR "discretion in grading" OR "gaming the system" OR "grace marks" OR "moderation of marks" OR ( bunching W/5 ( score* OR mark* OR grade* OR threshold* ) )
   OR ( inflat* W/3 ( "pass rate*" OR mark* OR score* OR result* ) ) )
  AND ( exam* OR "test score*" OR school* OR student* OR teacher* OR "high-stakes" ) )
AND PUBYEAR > 1989 AND ( LIMIT-TO ( LANGUAGE , "English" ) )
```
Web of Science
```
TS=(("grade inflation" OR "grading standard*" OR "grading leniency" OR "lenient grading" OR "score manipulation" OR "test score manipulation" OR "manipulation of test scores" OR "score inflation"
   OR "teacher cheating" OR "teacher discretion" OR "discretion in grading" OR "gaming the system" OR "grace marks" OR "moderation of marks" OR (bunching NEAR/5 (score* OR mark* OR grade* OR threshold*))
   OR (inflat* NEAR/3 ("pass rate*" OR mark* OR score* OR result*)))
  AND (exam* OR "test score*" OR school* OR student* OR teacher* OR "high-stakes"))
AND PY=(1990-2026) AND LA=(English)
```

## C. Corruption in education

Scopus
```
TITLE-ABS-KEY ( ( corrupt* OR brib* OR malfeasance OR "informal payment*" OR "ghost teacher*" ) W/8 ( education* OR school* OR universit* OR academ* OR exam* OR admission* OR teacher* OR student* ) )
AND NOT TITLE ( plagiaris* OR "research misconduct" OR "predatory journal*" OR medical OR nursing )
AND PUBYEAR > 1989 AND ( LIMIT-TO ( LANGUAGE , "English" ) )
```
Web of Science
```
TS=((corrupt* OR brib* OR malfeasance OR "informal payment*" OR "ghost teacher*") NEAR/8 (education* OR school* OR universit* OR academ* OR exam* OR admission* OR teacher* OR student*))
NOT TI=(plagiaris* OR "research misconduct" OR "predatory journal*" OR medical OR nursing)
AND PY=(1990-2026) AND LA=(English)
```

## D. Indian board examinations and learning outcomes

Scopus
```
TITLE-ABS-KEY ( ( india OR indian OR karnataka OR "tamil nadu" OR kerala OR maharashtra OR bihar OR "uttar pradesh" OR "andhra pradesh" OR telangana OR gujarat OR rajasthan OR "madhya pradesh" OR "west bengal" OR odisha OR punjab OR haryana OR delhi )
  AND ( "board exam*" OR sslc OR "class 10" OR "class X" OR "class 12" OR "class XII" OR "secondary school leaving certificate" OR "secondary school certificate" OR cbse OR icse OR matriculation OR "public examination*"
        OR "learning outcome*" OR "learning level*" OR aser OR "test score*" OR "student achievement" OR "learning crisis" OR "pass rate*" OR "pass percentage*" OR "national achievement survey" OR "examination reform*" OR "high-stakes" )
  AND ( school* OR schooling OR primary OR secondary OR elementary OR children OR pupils ) )
AND NOT TITLE ( medical OR dental OR nursing OR pharmac* OR clinical OR engineering )
AND PUBYEAR > 1989 AND ( LIMIT-TO ( LANGUAGE , "English" ) )
AND ( LIMIT-TO ( SUBJAREA , "SOCI" ) OR LIMIT-TO ( SUBJAREA , "ECON" ) OR LIMIT-TO ( SUBJAREA , "PSYC" ) OR LIMIT-TO ( SUBJAREA , "ARTS" ) )
```
Web of Science
```
TS=((India OR Indian OR Karnataka OR "Tamil Nadu" OR Kerala OR Maharashtra OR Bihar OR "Uttar Pradesh" OR "Andhra Pradesh" OR Telangana OR Gujarat OR Rajasthan OR "Madhya Pradesh" OR "West Bengal" OR Odisha OR Punjab OR Haryana OR Delhi)
  AND ("board exam*" OR SSLC OR "class 10" OR "class X" OR "class 12" OR "class XII" OR "secondary school leaving certificate" OR "secondary school certificate" OR CBSE OR ICSE OR matriculation OR "public examination*"
       OR "learning outcome*" OR "learning level*" OR ASER OR "test score*" OR "student achievement" OR "learning crisis" OR "pass rate*" OR "pass percentage*" OR "National Achievement Survey" OR "examination reform*" OR "high-stakes")
  AND (school* OR schooling OR primary OR secondary OR elementary OR children OR pupils))
NOT TI=(medical OR dental OR nursing OR pharmac* OR clinical OR engineering)
AND PY=(1990-2026) AND LA=(English)
```

## Narrow "direct analogue" query (run this first; it should return tens, not thousands)

Scopus
```
TITLE-ABS-KEY ( ( cctv OR camera* OR webcast* OR "video surveillance" OR "video monitoring" OR "external monitor*" OR "external examiner*" OR invigilat* OR "anti-cheating" OR "anti-fraud" OR "fraud prevention" )
  AND ( exam* OR "high-stakes" OR baccalaureate OR "national assessment*" )
  AND ( cheat* OR fraud* OR corrupt* OR manipulat* OR malpractice* )
  AND ( "pass rate*" OR "test score*" OR "exam score*" OR "exam result*" OR achievement OR grades ) )
AND PUBYEAR > 1989
```
Web of Science
```
TS=((CCTV OR camera* OR webcast* OR "video surveillance" OR "video monitoring" OR "external monitor*" OR "external examiner*" OR invigilat* OR "anti-cheating" OR "anti-fraud" OR "fraud prevention")
  AND (exam* OR "high-stakes" OR baccalaureate OR "national assessment*")
  AND (cheat* OR fraud* OR corrupt* OR manipulat* OR malpractice*)
  AND ("pass rate*" OR "test score*" OR "exam score*" OR "exam result*" OR achievement OR grades))
AND PY=(1990-2026)
```

Notes
- `W/n` (Scopus) and `NEAR/n` (WoS) are proximity operators; `?` (Scopus) and `$` (WoS) match zero or one character.
- Scopus indexes very few Indian state-level education journals; expect sub-literature D to stay thin there too. EconLit (if a mentor has it) is the better third database for A-C.
