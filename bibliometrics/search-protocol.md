# Search protocol - 04-sslc-webcasting

- Paper question: Did exam-hall webcasting/CCTV cut Karnataka Class 10 (SSLC) pass rates most where results were most inflated?
- Date of search and data pull: **2026-10-13**
- Years covered: 1990-2026; language: English (OpenAlex language field `en` or missing)
- Built by an AI agent (Claude) with the scripts in `python\` and `R\`; all numbers below are read from the run logs.

## 1. Databases

| Role | Database | Access | Note |
|---|---|---|---|
| Discovery | Crossref REST API | free, no key, `mailto` polite pool | relevance-ranked keyword search; top N per query |
| Discovery | Semantic Scholar Graph API (bulk search) | free, no key | boolean search on title/abstract; top N by citations per query |
| Discovery | ERIC API | free, no key | education topics only |
| Discovery | arXiv API | free, no key | preprints |
| Enrichment (authors, institutions, countries, topics, keywords, abstracts, references, citation counts, OA links) | **OpenAlex** single-record lookups (`/works/doi:...`, `/works/mag:...`, `/works/W...`) | free, no key | see limit 1 below |
| Forward citations for snowballing | OpenCitations Index API v2 | free, no key | DOI-to-DOI citations only |
| Cross-check | Crossref (per-DOI), Semantic Scholar (batch) | free, no key | citation counts and reference-list coverage compared in `tables\coverage_crosscheck.csv` |
| Not used | Scopus, Web of Science, Lens, Dimensions | need accounts | equivalent strings are in `scopus-queries.md` |
| Not usable | RePEc/IDEAS | its API needs a registered access code; the public search page returned no parseable result list to a script | economics working papers still enter via Crossref, Semantic Scholar and snowballing |

**Why OpenAlex was not the search engine.** Since 2026 OpenAlex charges keyless list/search calls against a small daily budget shared by everyone on the same IP address ($0.10/day). On the day of the pull that budget was already exhausted by other work on this network, and an API key needs an account (ruled out). Single-record lookups remain free and unlimited, so records were *discovered* in Crossref / Semantic Scholar / ERIC / arXiv and then *enriched* one by one from OpenAlex. Consequence: a work that is in OpenAlex but not found by any of the four discovery databases is missed, except where snowballing caught it.

## 2. Exact search strings

### A_cheating_monitoring: Exam cheating, malpractice and monitoring

| database | query | hits in database | records retrieved | status |
|---|---|---|---|---|
| crossref | exam cheating monitoring invigilation effect on test scores | 3941689.0 | 250 | ok |
| crossref | examination malpractice secondary school | 1320254.0 | 250 | ok |
| crossref | CCTV cameras examination halls cheating | 210075.0 | 250 | ok |
| crossref | cheating high-stakes exams monitoring natural experiment | 4458394.0 | 250 | ok |
| crossref | proctored versus unproctored exam scores cheating | 615410.0 | 250 | ok |
| crossref | external monitors examiners test scores cheating schools | 974759.0 | 250 | ok |
| s2 | (exam \| exams \| examination \| examinations \| test) + (cheating \| malpractice) + (monitoring \| invigilation \| cameras \| CCTV \| surveillance \| proctoring) | 1580.0 | 800 | ok |
| s2 | "examination malpractice" \| "exam malpractice" \| "examination malpractices" | 781.0 | 781 | ok |
| s2 | cheating + ("high-stakes" \| "national exam" \| "national exams" \| baccalaureate \| "standardized test" \| "standardized tests") + (students \| schools) | 214.0 | 214 | ok |
| s2 | (proctored \| proctoring) + (unproctored \| cheating) + (exam \| exams \| test) | 479.0 | 479 | ok |
| eric | cheating AND (examination OR exams OR tests) AND (monitoring OR invigilation OR proctoring OR surveillance) | 91.0 | 88 | ok |
| eric | "examination malpractice" | 25.0 | 25 | ok |

### B_grade_inflation_manipulation: Grade inflation and manipulation of high-stakes results

| database | query | hits in database | records retrieved | status |
|---|---|---|---|---|
| crossref | test score manipulation high-stakes exams | 3450156.0 | 250 | ok |
| crossref | grade inflation secondary school grading standards | 1510800.0 | 250 | ok |
| crossref | teacher cheating standardized tests manipulation | 568367.0 | 250 | ok |
| crossref | bunching test scores pass threshold manipulation teacher discretion | 1056115.0 | 250 | ok |
| crossref | inflated pass rates examination results manipulation | 1190846.0 | 250 | ok |
| s2 | "score manipulation" \| "test score manipulation" \| "teacher cheating" \| "manipulation of test scores" \| "score inflation" | 266.0 | 266 | ok |
| s2 | "grade inflation" + (school \| schools \| secondary \| exam \| examination \| examinations) | 449.0 | 449 | ok |
| s2 | (bunching \| discretion \| leniency) + ("test scores" \| "exam scores" \| grading) + (threshold \| cutoff \| pass) | 211.0 | 211 | ok |
| s2 | accountability + (gaming \| cheating \| manipulation) + ("test scores" \| testing) | 559.0 | 559 | ok |
| eric | "grade inflation" AND (secondary OR "high school" OR examination) | 187.0 | 141 | ok |
| eric | "score manipulation" OR "teacher cheating" OR "test score inflation" | 19.0 | 18 | ok |
| arxiv | all:"grade inflation" | 11.0 | 11 | ok |
| arxiv | all:"test score manipulation" OR all:"score manipulation" AND all:exam | 0.0 | 0 | ok |

### C_corruption_education: Corruption in education

| database | query | hits in database | records retrieved | status |
|---|---|---|---|---|
| crossref | corruption in education | 2985191.0 | 250 | ok |
| crossref | corruption education sector bribery schools universities | 3464608.0 | 250 | ok |
| crossref | academic corruption admissions exams bribery | 538643.0 | 250 | ok |
| crossref | fighting corruption in education evidence | 3976405.0 | 250 | ok |
| s2 | "corruption in education" \| "educational corruption" \| "corruption in higher education" \| "academic corruption" \| "education corruption" | 935.0 | 800 | ok |
| s2 | (corruption \| bribery) + education + (schools \| teachers \| universities \| examinations) | 3908.0 | 800 | ok |
| eric | corruption AND (education OR schools) AND (bribery OR fraud OR examination) | 71.0 | 68 | ok |

### D_india_boards_learning: Indian board examinations and learning outcomes

| database | query | hits in database | records retrieved | status |
|---|---|---|---|---|
| crossref | board examinations India secondary school results | 3103379.0 | 250 | ok |
| crossref | SSLC Karnataka examination results | 875215.0 | 250 | ok |
| crossref | learning outcomes India schools test scores | 4726017.0 | 250 | ok |
| crossref | India high-stakes examinations class 10 class 12 | 13162351.0 | 250 | ok |
| crossref | examination reform India secondary education | 4237497.0 | 250 | ok |
| crossref | ASER learning levels India primary schools | 4497527.0 | 250 | ok |
| s2 | (India \| Indian) + ("board examination" \| "board examinations" \| "board exams" \| SSLC \| CBSE \| "class 10" \| "class X" \| matriculation \| "secondary school certificate") | 749.0 | 749 | ok |
| s2 | (India \| Indian) + ("learning outcomes" \| "learning levels" \| "test scores" \| "student achievement") + (schools \| schooling \| children) | 1385.0 | 800 | ok |
| s2 | Karnataka + (schools \| education \| students) + (examination \| learning \| achievement) | 935.0 | 800 | ok |
| eric | India AND ("board examination" OR "public examination" OR SSLC OR CBSE OR "class X") | 14.0 | 14 | ok |
| eric | India AND "learning outcomes" AND (primary OR secondary) AND schools | 20.0 | 20 | ok |

Per-query retrieval caps: crossref = 250, s2 = 800, eric = 300, arxiv = 100. Crossref totals are large because its search is an OR-type relevance ranking; only the top-ranked records were taken. Raw responses for every query are in `data\raw\<database>\`.

### Seed papers (known key works, each verified to exist by a Crossref title match; they bypass the keyword rules)

| seed title | result |
|---|---|
| Fighting Corruption in Education: What Works and Who Benefits? | matched 10.1257/pol.20150074 |
| The Causes and Consequences of Test Score Manipulation: Evidence from the New York Regents Examinations | matched 10.1257/app.20170520 |
| Rotten Apples: An Investigation of the Prevalence and Predictors of Teacher Cheating | matched 10.1162/00335530360698441 |
| Long-Term Consequences of Teacher Discretion in Grading of High-Stakes Tests | matched 10.3386/w22207 |
| Cheating and Incentives: Learning from a Policy Experiment | matched 10.2139/ssrn.2606487 |
| Counting Rotten Apples: Student Achievement and Score Manipulation in Italian Elementary Schools | matched 10.1016/j.jeconom.2017.06.015 |
| When the cat is near, the mice won't play: The effect of external examiners in Italian schools | matched 10.2139/ssrn.2085216 |
| In a Small Moment: Class Size and Moral Hazard in the Italian Mezzogiorno | matched 10.1257/app.20160267 |
| Cheating and social interactions. Evidence from a randomized experiment in a national evaluation program | matched 10.1016/j.jebo.2014.12.006 |
| From Cheating to Learning: An Evaluation of Fraud Prevention on National Exams in Indonesia | matched 10.35489/bsg-rise-wp_2020/046 |
| Catching Cheating Teachers: The Results of an Unusual Experiment in Implementing Theory | matched 10.1353/urb.2003.0010 |
| The impact of an unexpected wage cut on corruption: Evidence from a "Xeroxed" exam | matched 10.2139/ssrn.2195506 |
| Corrupting learning: Evidence from missing federal education funds in Brazil | matched 10.3386/w18150 |
| Do the Cheated Ever Prosper? The Long-Run Effects of Test-Score Manipulation by Teachers on Student Outcomes | NOT MATCHED in Crossref |
| Myths of Official Measurement: Auditing and Improving Administrative Data in Developing Countries | matched 10.35489/bsg-rise-wp_2020/042 |
| Limitations in the Use of Achievement Tests as Measures of Educators' Productivity | matched 10.2307/3069616 |

## 3. Inclusion and exclusion rules (applied identically to search hits and snowballed records)

A record is **included** if all of the following hold:
1. It resolves to an OpenAlex work record (by DOI, MAG id, or a Crossref title match of at least 93% similarity).
2. OpenAlex type is article, review, preprint, book chapter, book, dissertation, report or other (editorials, errata, paratext, datasets, peer reviews are dropped).
3. Publication year 1990-2026; language English or unrecorded.
4. It satisfies at least one sub-literature rule below: every `include` pattern must match in title + abstract, and every `title_must` pattern must match in the title.
5. Its title does not match the exclusion pattern.

Book-series and proceedings trap: a record whose abstract is a series/proceedings blurb (detected by wording such as 'this volume constitutes the refereed proceedings', or the same abstract shared by 3+ records) is screened on its title alone; whole-volume records (titles starting 'Proceedings of', 'Front matter', etc.) are dropped.

The patterns are case-insensitive regular expressions (`\b` = word boundary, `\w*` = any word ending, `.{0,80}` = within 80 characters).

**A_cheating_monitoring - Exam cheating, malpractice and monitoring**

- include (title+abstract): `\b(exams?|examinations?|test[- ]takers?|high[- ]stakes|standardi[sz]ed tests?|test scores?|testing|national assessments?|baccalaureate|matriculation)\b`
- include (title+abstract): `\b(cheat\w*|malpractices?|academic dishonesty|invigilat\w*|proctor\w*|cctv|surveillance cameras?|video surveillance|camera monitoring|external (examiners?|monitors?|monitoring)|paper leak\w*|impersonat\w*)`
- title_must (title): `(cheat\w*|malpractices?|invigilat\w*|proctor\w*|cctv|dishonest\w*|external (examiners?|monitor\w*)|fraud\w*|leak\w*|anti-cheating|monitor\w*|surveillance|integrity)`

**B_grade_inflation_manipulation - Grade inflation and manipulation of high-stakes results**

- include (title+abstract): `(grade inflation|grading (standards?|leniency)|lenient grading|score manipulation|manipulat\w+ (of )?(the )?(test|exam|grades?|scores?|results)|(test|exam|grade|score)s? manipulation|inflat\w+ (of )?(grades?|scores?|marks|results|pass rates?)|(grades?|scores?|marks|pass rates?) inflation|teacher discretion|discretion in grading|bunching (of|in|at) |teacher cheating|rotten apples|score inflation|gaming the (system|test)|grace marks|moderation of marks)`
- include (title+abstract): `\b(exams?|examinations?|test scores?|tests?|grades|grading|schools?|students?|teachers?)\b`
- title_must (title): `(grade inflation|grading|inflat\w+|manipulat\w+|teacher cheating|rotten apples|bunching|discretion|gaming|lenien\w+|standards|cheat\w*)`

**C_corruption_education - Corruption in education**

- include (title+abstract): `((corrupt\w*|brib\w*|malfeasance|informal payments?|ghost teachers?).{0,70}\b(education\w*|school\w*|universit\w+|academ\w+|exam\w*|admissions?|teachers?|students?)|\b(education\w*|school\w*|universit\w+|academ\w+|exam\w*|admissions?|teachers?|students?)\b.{0,70}(corrupt\w*|brib\w*|malfeasance|informal payments?))`
- title_must (title): `(corrupt\w*|brib\w*|malfeasance|informal payments?|ghost teachers?|fraud\w*|leakage|missing|embezzl\w*)`
- title_must (title): `(education\w*|school\w*|universit\w+|academ\w+|exam\w*|admissions?|teachers?|students?|learning|college)`

**D_india_boards_learning - Indian board examinations and learning outcomes**

- include (title+abstract): `\b(india|indian|karnataka|tamil nadu|kerala|maharashtra|bihar|uttar pradesh|andhra pradesh|telangana|gujarat|rajasthan|madhya pradesh|west bengal|odisha|punjab|haryana|delhi)\b`
- include (title+abstract): `\b(board exam\w*|sslc|class (10|x|12|xii)\b|secondary school (leaving )?(certificate|examinations?)|cbse|icse|matriculation|public examinations?|learning outcomes?|learning levels?|aser\b|test scores?|student achievement|learning crisis|pass (rates?|percentages?)|national achievement survey|examination reforms?|high[- ]stakes)`
- include (title+abstract): `\b(schools?|schooling|primary|secondary|elementary|children|pupils|class (10|x|12|xii))\b`
- title_must (title): `\b(india|indian|karnataka|tamil nadu|kerala|maharashtra|bihar|uttar pradesh|andhra pradesh|telangana|gujarat|rajasthan|madhya pradesh|west bengal|odisha|punjab|haryana|delhi)\b`
- title_must (title): `(exam\w*|board|sslc|cbse|icse|matriculation|learning (outcomes?|levels?|crisis|achievement|gaps?|loss)|test scores?|achievement|pass (rate|percentage)|aser\b|assessment|high[- ]stakes|private school|school quality|learning)`

**Exclusion pattern (title):** `(plagiaris|contract cheating|essay mill|deep learning|neural network|machine learning|\byolo|computer vision|face recognition|\biot\b|raspberry|blockchain|eye[- ]?track|\bgaze\b|head pose|keystroke|\bmedical|\bdental|\bnursing|pharmac|clinical|surg|anatomy|veterinar|\bsports?\b|doping|\btax|financial statement|accounting fraud|insurance|election|chatgpt|generative ai|large language model|artificial intelligence|\bmooc|e-commerce|video ?gam|marital|infidelity|spous|romantic|at work|workplace|organi[sz]ational|employee|\bhealth|hypertens|diabet|\boral\b|anxiety|nutrition|stunting|cardio|osce\b|clerkship|script concordance|engineering|laborator|flipped|e-?learning|metacogni|yoga|intelligence|personality|stress)`

A record matching several rules is assigned to the first one in the order listed (its other matches are kept in `sublits_all`).

## 4. Snowballing (one round)

- Central papers: the 25 corpus records ranked highest on local citations + topical relevance + log(global citations) - listed in `data\clean\snowball_central_papers.csv`.
- Backward: every OpenAlex `referenced_works` entry of those papers not already in the corpus (709 candidates).
- Forward: citing DOIs from OpenCitations, up to 150 per central paper (1305 candidates). OpenCitations only knows DOI-to-DOI links, so citing preprints and books without DOIs are missed.
- All candidates were looked up in OpenAlex and screened with the rules in section 3: 29 backward and 113 forward records were added.

## 5. PRISMA-style counts

| stage | n |
|---|---|
| Records identified through database searching (all query hits) | 13380 |
|    of which from arxiv | 11 |
|    of which from crossref | 5250 |
|    of which from eric | 374 |
|    of which from s2 | 7708 |
|    of which from seed | 37 |
| Duplicates removed (same DOI / id / title across queries and databases) | 2799 |
| Unique records screened on title (+ abstract where the database supplied one) | 10581 |
| Removed at title pre-screen (off-topic) | 8458 |
| Records looked up in OpenAlex | 2123 |
| Duplicates removed after OpenAlex matching (same work / same title) | 29 |
| Excluded at full screen: offtopic_fails_inclusion_rule | 298 |
| Excluded at full screen: no_openalex_record (no DOI / not indexed) | 272 |
| Excluded at full screen: manual_exclude | 266 |
| Excluded at full screen: type_excluded | 156 |
| Excluded at full screen: language_not_english | 24 |
| Excluded at full screen: paratext_or_container_record | 2 |
| Included after search screening | 1076 |
| Snowball: central papers used | 25 |
| Snowball: backward-reference candidates | 709 |
| Snowball: forward-citation candidates (OpenCitations) | 1305 |
| Snowball: duplicates of corpus records | 23 |
| Snowball excluded: offtopic_fails_inclusion_rule | 1117 |
| Snowball excluded: offtopic_exclusion_term_in_title | 230 |
| Snowball excluded: type_excluded | 224 |
| Snowball excluded: no_openalex_record | 118 |
| Snowball excluded: year_out_of_range | 77 |
| Snowball excluded: language_not_english | 41 |
| Snowball excluded: manual_exclude | 31 |
| Snowball excluded: paratext_or_container_record | 11 |
| Snowball: included (backward) | 29 |
| Snowball: included (forward) | 113 |
| Corpus before hand-screening | 1218 |
| Removed at hand-screening (see tables/hand_screen_removed.csv) | 0 |
| FINAL CORPUS | 1218 |
|    with abstract | 1025 |
|    with DOI | 951 |
|    with a reference list in OpenAlex | 790 |
| Distinct cited references / resolved to metadata | 15057 / 4762 |

Figure: `figures\py_01_prisma_flow.png`.

## 6. Hand-screening

After rule screening and snowballing, the agent read the titles (with source and year) of the whole corpus and removed 0 records as off-topic or mis-matched; every removal and its reason is in `tables\hand_screen_removed.csv`. This is a single-screener pass by an AI agent on titles, not a two-person human screen; borderline records were kept.

## 7. Coverage and cross-checks

| item | value |
|---|---|
| corpus records | 1218.0 |
| records with DOI | 951.0 |
| found in Crossref (DOI lookup) | 908.0 |
| found in Semantic Scholar (batch DOI lookup) | 892.0 |
| Spearman corr. OpenAlex vs Crossref cited-by | 0.932 |
| Spearman corr. OpenAlex vs Semantic Scholar cited-by | 0.915 |
| median cited-by: OpenAlex | 3.0 |
| median cited-by: Crossref | 2.0 |
| median cited-by: Semantic Scholar | 4.0 |
| records with no reference list in OpenAlex | 428.0 |
|   of which Crossref holds a reference list | 8.0 |
| records with no institution/country data | 423.0 |
| records without abstract | 193.0 |
| open-access records (OpenAlex) | 695.0 |
| origin: search | 1056.0 |
| origin: snowball_forward | 113.0 |
| origin: snowball_backward | 29.0 |
| origin: seed | 20.0 |
| retrieved by: s2 | 1050.0 |
| retrieved by: openalex_snowball | 142.0 |
| retrieved by: eric | 80.0 |
| retrieved by: seed | 20.0 |
| retrieved by: arxiv | 3.0 |


- 272 title-screened candidates could not be matched to any OpenAlex record (no DOI or MAG id, or not indexed) and are **not** in the corpus. They are listed in `data\clean\unresolved_candidates.csv` (s2: 204, eric: 68). ERIC reports and theses and Indian or legal journal articles without DOIs dominate this list.

- Cited references: 15057 distinct works are cited by the corpus (23310 links); 4762 of the 5000 outside the corpus were resolved to metadata for the co-citation and RPYS analyses.


### Named prior work (seed list / the substance agent's saved papers) - is it in the corpus?

| id | kind | in_corpus |
|---|---|---|
| 10.1016/j.econlet.2021.109742 | doi | 1 |
| 10.1016/j.jdeveco.2024.103307 | doi | 1 |
| 10.1016/j.jebo.2014.12.006 | doi | 1 |
| 10.1016/j.jeconom.2017.06.015 | doi | 1 |
| 10.1016/j.jpubeco.2013.04.010 | doi | 1 |
| 10.1016/j.jpubeco.2014.08.003 | doi | 1 |
| 10.1080/00220388.2012.700397 | doi | 1 |
| 10.1162/00335530360698441 | doi | 1 |
| 10.1257/app.20160267 | doi | 1 |
| 10.1257/app.20170520 | doi | 1 |
| 10.1257/pol.20150066 | doi | 1 |
| 10.1257/pol.20150074 | doi | 1 |
| 10.2139/ssrn.2708374 | doi | 0 |
| 10.21648/arthavij/2000/v42/i1/115907 | doi | 1 |
| 10.3368/jhr.0620-10947r1 | doi | 1 |
| 10.3386/w22207 | doi | 1 |
| 10.35489/bsg-rise-wp_2020/042 | doi | 1 |
| 10.35489/bsg-rise-wp_2020/046 | doi | 1 |

## 8. API failures during the run

- api.openalex.org: failed after retries: {"error":"Rate limit exceeded","message":"Rate l (x27)


## 9. Scopus / Web of Science exports
- `scopus-drop\`: EMPTY - no Scopus/WoS export to merge; corpus is OpenAlex-only.
- Ready-to-paste strings: `scopus-queries.md`.
