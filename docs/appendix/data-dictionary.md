# Data dictionary - 04-sslc-webcasting

Generated 2026-10-17 from the files on disk by `python\depth_appendix.py`. Inventory columns are read from the files; meanings are copied from the paper's own documentation or the fixed glossary, otherwise marked 'meaning not documented'. Large raw dumps (raw API responses, cached downloads, PDFs, virtual environments) are summarised, not listed.

## Documentation that already exists in the folder (authoritative for the paper's own data)
- `data\clean\DATA_DICTIONARY.md`

## Bibliometrics layer (made by the literature-mapping pipeline)

| Path | What it is |
|---|---|
| `bibliometrics\data\clean\master.csv` | one row per corpus record after screening and hand-screening (the main table) |
| `bibliometrics\data\clean\bibliometrix_input.csv / bibliometrix_M.rds` | the same records in bibliometrix's field-tag format (AU, TI, SO, PY, TC, DE, ID, CR, C1 ...) |
| `bibliometrics\data\clean\citation_edges.csv` | direct-citation links between corpus records (citing, cited) |
| `bibliometrics\data\clean\cited_references.csv` | the references cited most often by the corpus, resolved to metadata |
| `bibliometrics\data\clean\corpus_final.jsonl.gz / corpus_stage1.jsonl.gz` | full OpenAlex JSON records after / before the last screening pass |
| `bibliometrics\data\clean\screening_log_*.csv` | every screening decision with its reason |
| `bibliometrics\data\clean\unresolved_candidates.csv` | records found by a search but not matched in OpenAlex (kept for audit) |
| `bibliometrics\data\raw\` | raw API responses per query (crossref, s2, eric, arxiv) + all_hits.csv + query_log.csv; OpenAlex records as .jsonl.gz |
| `bibliometrics\tables\` | numbers behind every figure (R_*.csv from bibliometrix, py_*.csv from Python), PRISMA counts, logs |

Access/pull date for all bibliometrics data: see `bibliometrics\data\clean\prisma_search.json` (field `date`); sources: Crossref REST API, Semantic Scholar API, ERIC API, arXiv API, OpenAlex API, OpenCitations API (all free, no key, no personal identifier sent). Known problems: OpenAlex affiliation/abstract/reference gaps for Indian journals, books and law; duplicate preprint/published versions merged by title only; keywords are machine-assigned.

## File inventory

### `bibliometrics\config.json`
- size 32 KB; modified 2026-10-13

### `bibliometrics\data\api_log.json`
- size 11 KB; modified 2026-10-17

### `bibliometrics\data\clean\bibliometrix_M.rds`
- size 1035 KB; modified 2026-10-17

### `bibliometrics\data\clean\bibliometrix_input.csv`
- size 3607 KB; modified 2026-10-17; rows 1218
- columns / contents:
  - `AU` (str; e.g. 'FRANCOIS M;DE WITTE K'): bibliometrix: authors (short form)
  - `AF` (str; e.g. 'MAXIME FRANCOIS;KRISTOF DE WITTE'): bibliometrix: authors (full names)
  - `TI` (str; e.g. 'A DECADE OF GRADE INFLATION BOOSTED BY T'): bibliometrix: title (upper case)
  - `SO` (str; e.g. 'BRITISH EDUCATIONAL RESEARCH JOURNAL'): bibliometrix: source (journal) name
  - `JI` (str; e.g. 'BRITISH EDUCATIONAL RESEARCH JOURNAL')  - *meaning not documented here (see the files above / the code that writes it)*
  - `J9` (str; e.g. 'BRITISH EDUCATIONAL RESEARCH JOURNAL'): bibliometrix: abbreviated journal
  - `DT` (str; e.g. 'ARTICLE'): bibliometrix: document type
  - `DE` (str; e.g. 'GRADE INFLATION;COVID-19 PANDEMIC;GRADIN'): bibliometrix: author/OpenAlex keywords
  - `ID` (str; e.g. 'CORONAVIRUS DISEASE 2019 (COVID-19);PAND'): bibliometrix: keywords-plus (here OpenAlex concepts/topics)
  - `AB` (str; e.g. 'ABSTRACT THE OBSERVED DECLINE IN ACADEMI'): bibliometrix: abstract
  - `C1` (str; e.g. 'KU LEUVEN, BELGIUM'): bibliometrix: author affiliations
  - `RP` (str; e.g. 'KU LEUVEN, BELGIUM'): bibliometrix: reprint (corresponding-author) address
  - `CR` (str; e.g. 'NIKOLAKAKOS E, 2012, NSUWORKS (NOVA SOUT'): bibliometrix: cited references, one label per reference, separated by ;
  - `TC` (int64; e.g. '7'): bibliometrix: total citations (OpenAlex)
  - `PY` (int64; e.g. '2025'): bibliometrix: publication year
  - `DI` (str; e.g. '10.1002/BERJ.4172'): bibliometrix: DOI
  - `LA` (str; e.g. 'ENGLISH'): bibliometrix: language
  - `UT` (str; e.g. 'W4409235431')  - *meaning not documented here (see the files above / the code that writes it)*
  - `DB` (str; e.g. 'ISI'): bibliometrix: database label
  - `SR` (str; e.g. 'FRANCOIS M, 2025, BRITISH EDUCATIONAL RE'): bibliometrix: short reference key
  - `SR_FULL` (str; e.g. 'FRANCOIS M, 2025, BRITISH EDUCATIONAL RE')  - *meaning not documented here (see the files above / the code that writes it)*
  - `AU_UN` (str; e.g. 'KU LEUVEN')  - *meaning not documented here (see the files above / the code that writes it)*
  - `AU1_UN` (str; e.g. 'KU LEUVEN')  - *meaning not documented here (see the files above / the code that writes it)*
  - `AU_CO` (str; e.g. 'BELGIUM')  - *meaning not documented here (see the files above / the code that writes it)*
  - `AU1_CO` (str; e.g. 'BELGIUM')  - *meaning not documented here (see the files above / the code that writes it)*
  - `SUBLIT` (str; e.g. 'B_grade_inflation_manipulation')  - *meaning not documented here (see the files above / the code that writes it)*
  - `LCS` (int64; e.g. '0'): bibliometrix: local citation score (citations from inside the corpus)
  - `NR` (int64; e.g. '53')  - *meaning not documented here (see the files above / the code that writes it)*
  - `id_oa` (str; e.g. 'W4409235431')  - *meaning not documented here (see the files above / the code that writes it)*

### `bibliometrics\data\clean\citation_edges.csv`
- size 66 KB; modified 2026-10-17; rows 2695
- columns / contents:
  - `citing` (str; e.g. 'W4409235431'): OpenAlex id of the citing record (inside the corpus)
  - `cited` (str; e.g. 'W35174645'): OpenAlex id of the cited record (in or outside the corpus)

### `bibliometrics\data\clean\cited_references.csv`
- size 1302 KB; modified 2026-10-17; rows 5260
- columns / contents:
  - `oa_id` (str; e.g. 'W2029355615'): OpenAlex work id (W...)
  - `local_citations` (int64; e.g. '67'): citations received from other records inside this corpus
  - `in_corpus` (int64; e.g. '1'): 1 if the cited work is itself a corpus record
  - `first_author` (str; e.g. 'Stephen P. Heyneman'): first author's name
  - `year` (str; e.g. '2004.0'): publication year
  - `title` (str; e.g. 'Education and corruption'): work title (OpenAlex)
  - `source` (str; e.g. 'International Journal of Educational Dev'): journal / repository name
  - `doi` (str; e.g. '10.1016/j.ijedudev.2004.02.005'): DOI, lower-case, no URL prefix
  - `global_citations` (int64; e.g. '237'): OpenAlex citation count
  - `cr_label` (str; e.g. 'HEYNEMAN SP, 2004, INTERNATIONAL JOURNAL'): bibliometrix-style cited-reference label

### `bibliometrics\data\clean\corpus_final.jsonl.gz`
- size 2622 KB; modified 2026-10-13

### `bibliometrics\data\clean\corpus_stage1.jsonl.gz`
- size 2295 KB; modified 2026-10-13

### `bibliometrics\data\clean\evidence_candidates.json`
- size 141 KB; modified 2026-10-17

### `bibliometrics\data\clean\evidence_notes.json`
- size 40 KB; modified 2026-10-17

### `bibliometrics\data\clean\handscreen_exclusions.json`
- size 19 KB; modified 2026-10-13

### `bibliometrics\data\clean\handscreen_titles.tsv`
- size 253 KB; modified 2026-10-13; rows 1491
- columns / contents:
  - `oa_id` (str; e.g. 'W3123468586'): OpenAlex work id (W...)
  - `year` (int64; e.g. '2003'): publication year
  - `cites` (int64; e.g. '864')  - *meaning not documented here (see the files above / the code that writes it)*
  - `origin` (str; e.g. 'seed'): search | snowball-backward | snowball-forward | seed
  - `sublit` (str; e.g. 'A_cheating_monitoring'): primary sub-literature assigned by the screening rules
  - `source` (str; e.g. 'The Quarterly Journal of Economics'): journal / repository name
  - `title` (str; e.g. 'Rotten Apples: An Investigation of the P'): work title (OpenAlex)

### `bibliometrics\data\clean\master.csv`
- size 2719 KB; modified 2026-10-17; rows 1218
- columns / contents:
  - `oa_id` (str; e.g. 'W4409235431'): OpenAlex work id (W...)
  - `doi` (str; e.g. '10.1002/berj.4172'): DOI, lower-case, no URL prefix
  - `title` (str; e.g. 'A decade of grade inflation boosted by t'): work title (OpenAlex)
  - `year` (int64; e.g. '2025'): publication year
  - `date` (str; e.g. '2025-04-07'): publication date
  - `type` (str; e.g. 'article'): OpenAlex work type (article, review, preprint, book-chapter ...)
  - `language` (str; e.g. 'en'): ISO language code
  - `source` (str; e.g. 'British Educational Research Journal'): journal / repository name
  - `source_type` (str; e.g. 'journal'): journal, repository, book series ...
  - `publisher` (str; e.g. 'Wiley')  - *meaning not documented here (see the files above / the code that writes it)*
  - `issn` (str; e.g. '0141-1926')  - *meaning not documented here (see the files above / the code that writes it)*
  - `authors` (str; e.g. 'Maxime François; Kristof De Witte'): author display names, '; '-separated
  - `n_authors` (int64; e.g. '2'): number of authors
  - `first_author` (str; e.g. 'Maxime François'): first author's name
  - `institutions` (str; e.g. 'KU LEUVEN'): author institutions, '; '-separated
  - `countries` (str; e.g. 'BE'): ISO-2 country codes of author affiliations, '; '-separated (empty when OpenAlex has no affiliation data)
  - `first_author_country` (str; e.g. 'BE')  - *meaning not documented here (see the files above / the code that writes it)*
  - `corresponding_country` (str; e.g. 'BE')  - *meaning not documented here (see the files above / the code that writes it)*
  - `international_collab` (int64; e.g. '0')  - *meaning not documented here (see the files above / the code that writes it)*
  - `cited_by_count` (int64; e.g. '7'): citations counted by OpenAlex at pull date
  - `fwci` (str; e.g. '22.8638'): field-weighted citation impact (OpenAlex; 1 = world average for field/year/type)
  - `local_citations` (int64; e.g. '0'): citations received from other records inside this corpus
  - `n_refs` (int64; e.g. '53'): number of references in OpenAlex
  - `is_oa` (bool; e.g. 'True'): open-access flag (OpenAlex)
  - `oa_status` (str; e.g. 'hybrid'): gold/green/hybrid/bronze/closed
  - `oa_url` (str; e.g. 'https://onlinelibrary.wiley.com/doi/pdfd'): best open-access landing page
  - `best_pdf_url` (str; e.g. 'https://onlinelibrary.wiley.com/doi/pdfd'): direct PDF link, if known
  - `best_oa_landing` (str; e.g. 'https://doi.org/10.1002/berj.4172')  - *meaning not documented here (see the files above / the code that writes it)*
  - `all_pdf_urls` (str; e.g. 'https://onlinelibrary.wiley.com/doi/pdfd')  - *meaning not documented here (see the files above / the code that writes it)*
  - `sublit` (str; e.g. 'B_grade_inflation_manipulation'): primary sub-literature assigned by the screening rules
  - `sublits_all` (str; e.g. 'B_grade_inflation_manipulation'): every sub-literature whose rule matched, '; '-separated
  - `origin` (str; e.g. 'search'): search | snowball-backward | snowball-forward | seed
  - `found_in` (str; e.g. 's2'): databases that returned the record (crossref, s2, eric, arxiv, seed)
  - `relevance` (float64; e.g. '5.0'): rule-based topical score (core-term hits weighted); higher = closer to the paper's topic
  - `primary_topic` (str; e.g. 'Higher Education Research Studies')  - *meaning not documented here (see the files above / the code that writes it)*
  - `subfield` (str; e.g. 'Education')  - *meaning not documented here (see the files above / the code that writes it)*
  - `field` (str; e.g. 'Social Sciences')  - *meaning not documented here (see the files above / the code that writes it)*
  - `domain` (str; e.g. 'Social Sciences')  - *meaning not documented here (see the files above / the code that writes it)*
  - `keywords` (str; e.g. 'grade inflation; COVID-19 pandemic; grad'): OpenAlex machine-assigned keywords
  - `topics` (str; e.g. 'Higher Education Research Studies; Educa'): OpenAlex topics
  - `concepts` (str; e.g. 'Coronavirus disease 2019 (COVID-19); Pan'): OpenAlex concepts
  - `abstract` (str; e.g. 'Abstract The observed decline in academi'): abstract text (rebuilt from OpenAlex inverted index or taken from S2/ERIC/Crossref)
  - `has_abstract` (int64; e.g. '1'): 1 if an abstract is present
  - `is_retracted` (bool; e.g. 'False'): OpenAlex retraction flag
  - `sr` (str; e.g. 'FRANCOIS M, 2025, BRITISH EDUCATIONAL RE'): short reference key used by bibliometrix
  - `crossref_cited_by` (str; e.g. '7.0'): Crossref is-referenced-by count
  - `crossref_n_refs` (str; e.g. '58.0')  - *meaning not documented here (see the files above / the code that writes it)*
  - `s2_citation_count` (str; e.g. '8.0'): Semantic Scholar citation count
  - `s2_pdf_url` (str; e.g. 'https://onlinelibrary.wiley.com/doi/pdfd')  - *meaning not documented here (see the files above / the code that writes it)*

### `bibliometrics\data\clean\master.rds`
- size 787 KB; modified 2026-10-17

### `bibliometrics\data\clean\prisma_search.json`
- size 1 KB; modified 2026-10-13

### `bibliometrics\data\clean\prisma_snowball.json`
- size 3 KB; modified 2026-10-13

### `bibliometrics\data\clean\refs_stats.json`
- size 0 KB; modified 2026-10-17

### `bibliometrics\data\clean\screening_log_search.csv`
- size 438 KB; modified 2026-10-13; rows 2123
- columns / contents:
  - `key` (str; e.g. 'doi:10.1001/jama.1991.03470150059031')  - *meaning not documented here (see the files above / the code that writes it)*
  - `title` (str; e.g. 'Malpractice Claims Data as a Quality Imp'): work title (OpenAlex)
  - `dbs` (str; e.g. 's2')  - *meaning not documented here (see the files above / the code that writes it)*
  - `sublits_queried` (str; e.g. 'A_cheating_monitoring')  - *meaning not documented here (see the files above / the code that writes it)*
  - `oa_id` (str; e.g. 'W2085049284'): OpenAlex work id (W...)
  - `decision` (str; e.g. 'excluded')  - *meaning not documented here (see the files above / the code that writes it)*
  - `reason` (str; e.g. 'manual_exclude: medical/legal malpractic')  - *meaning not documented here (see the files above / the code that writes it)*
  - `sublit` (str; e.g. ''): primary sub-literature assigned by the screening rules

### `bibliometrics\data\clean\screening_log_snowball.csv`
- size 285 KB; modified 2026-10-13; rows 2014
- columns / contents:
  - `key` (str; e.g. 'W32070771')  - *meaning not documented here (see the files above / the code that writes it)*
  - `kind` (str; e.g. 'back')  - *meaning not documented here (see the files above / the code that writes it)*
  - `oa_id` (str; e.g. 'W32070771'): OpenAlex work id (W...)
  - `title` (str; e.g. 'Education and social cohesion'): work title (OpenAlex)
  - `decision` (str; e.g. 'excluded')  - *meaning not documented here (see the files above / the code that writes it)*
  - `reason` (str; e.g. 'offtopic_fails_inclusion_rule')  - *meaning not documented here (see the files above / the code that writes it)*
  - `sublit` (str; e.g. ''): primary sub-literature assigned by the screening rules

### `bibliometrics\data\clean\snowball_central_papers.csv`
- size 3 KB; modified 2026-10-13; rows 25
- columns / contents:
  - `oa_id` (str; e.g. 'W2029355615'): OpenAlex work id (W...)
  - `title` (str; e.g. 'Education and corruption'): work title (OpenAlex)
  - `year` (int64; e.g. '2004'): publication year
  - `local_cites` (int64; e.g. '51')  - *meaning not documented here (see the files above / the code that writes it)*
  - `cited_by` (int64; e.g. '237')  - *meaning not documented here (see the files above / the code that writes it)*
  - `relevance` (float64; e.g. '2.0'): rule-based topical score (core-term hits weighted); higher = closer to the paper's topic

### `bibliometrics\data\clean\unresolved_candidates.csv`
- size 62 KB; modified 2026-10-13; rows 272
- columns / contents:
  - `key` (str; e.g. 'doi:10.25215/0802.161')  - *meaning not documented here (see the files above / the code that writes it)*
  - `title` (str; e.g. 'Impact of educational corruption on the '): work title (OpenAlex)
  - `first_author` (str; e.g. 'Sharma'): first author's name
  - `year` (float64; e.g. '2020.0'): publication year
  - `dbs` (str; e.g. 's2')  - *meaning not documented here (see the files above / the code that writes it)*
  - `eric` (str; e.g. '')  - *meaning not documented here (see the files above / the code that writes it)*
  - `sublits_q` (str; e.g. 'C_corruption_education')  - *meaning not documented here (see the files above / the code that writes it)*

### `bibliometrics\evidence-table.csv`
- size 51 KB; modified 2026-10-17; rows 62
- columns / contents:
  - `rank` (int64; e.g. '1')  - *meaning not documented here (see the files above / the code that writes it)*
  - `citation` (str; e.g. 'Rebecca Diamond, Petra Persson (2016). T')  - *meaning not documented here (see the files above / the code that writes it)*
  - `year` (int64; e.g. '2016'): publication year
  - `doi_or_link` (str; e.g. 'https://doi.org/10.3386/w22207')  - *meaning not documented here (see the files above / the code that writes it)*
  - `open_access_link` (str; e.g. 'https://doi.org/10.3386/w22207')  - *meaning not documented here (see the files above / the code that writes it)*
  - `oa_status` (str; e.g. 'green'): gold/green/hybrid/bronze/closed
  - `pdf_in_folder` (str; e.g. 'Diamond_2016_The-Long-term-Consequences-')  - *meaning not documented here (see the files above / the code that writes it)*
  - `sub_literature` (str; e.g. 'B_grade_inflation_manipulation')  - *meaning not documented here (see the files above / the code that writes it)*
  - `study_type` (str; e.g. 'not stated in abstract')  - *meaning not documented here (see the files above / the code that writes it)*
  - `country_or_setting` (str; e.g. 'United States')  - *meaning not documented here (see the files above / the code that writes it)*
  - `data` (str; e.g. 'not stated in abstract')  - *meaning not documented here (see the files above / the code that writes it)*
  - `method` (str; e.g. 'not stated in abstract')  - *meaning not documented here (see the files above / the code that writes it)*
  - `main_finding_from_abstract` (str; e.g. 'We examine the long-term consequences of')  - *meaning not documented here (see the files above / the code that writes it)*
  - `read_status` (str; e.g. 'abstract read')  - *meaning not documented here (see the files above / the code that writes it)*
  - `relation_to_seans_paper` (str; e.g. 'Evidence on how high-stakes results are ')  - *meaning not documented here (see the files above / the code that writes it)*
  - `local_citations` (int64; e.g. '9'): citations received from other records inside this corpus
  - `global_citations_openalex` (int64; e.g. '116')  - *meaning not documented here (see the files above / the code that writes it)*
  - `openalex_id` (str; e.g. 'W2342903512')  - *meaning not documented here (see the files above / the code that writes it)*

### `data\clean\_build_log_district_tables.txt`
- size 10 KB; modified 2026-10-13; rows 153
- columns / contents:
  - `April_2015_stats: April_2015_stats__PRO-5.txt rows=34` (str; e.g. 'SSLCAPR2017: SSLCAPR2017__PRO_5.txt rows')  - *meaning not documented here (see the files above / the code that writes it)*

### `data\clean\district_all_candidates_2014_2018.csv`
- size 17 KB; modified 2026-10-13; rows 170
- columns / contents:
  - `year` (int64; e.g. '2014'): publication year
  - `dist_code` (str; e.g. 'AN')  - *meaning not documented here (see the files above / the code that writes it)*
  - `dist_name` (str; e.g. 'BANGALORE NORTH')  - *meaning not documented here (see the files above / the code that writes it)*
  - `boys_app` (float64; e.g. '25946.0')  - *meaning not documented here (see the files above / the code that writes it)*
  - `girls_app` (float64; e.g. '23950.0')  - *meaning not documented here (see the files above / the code that writes it)*
  - `app` (float64; e.g. '49896.0')  - *meaning not documented here (see the files above / the code that writes it)*
  - `boys_pass` (float64; e.g. '19161.0')  - *meaning not documented here (see the files above / the code that writes it)*
  - `girls_pass` (float64; e.g. '19882.0')  - *meaning not documented here (see the files above / the code that writes it)*
  - `passed` (float64; e.g. '39043.0')  - *meaning not documented here (see the files above / the code that writes it)*
  - `pct` (float64; e.g. '78.24875741542408')  - *meaning not documented here (see the files above / the code that writes it)*
  - `source_file` (str; e.g. '5years.xlsx')  - *meaning not documented here (see the files above / the code that writes it)*
  - `sheet` (int64; e.g. '2014')  - *meaning not documented here (see the files above / the code that writes it)*

### `data\clean\district_malpractice_cases.csv`
- size 8 KB; modified 2026-10-13; rows 69
- columns / contents:
  - `year` (int64; e.g. '2017'): publication year
  - `exam` (str; e.g. 'April 2017 main')  - *meaning not documented here (see the files above / the code that writes it)*
  - `scope` (str; e.g. 'main_exam')  - *meaning not documented here (see the files above / the code that writes it)*
  - `dist_code` (str; e.g. 'CA')  - *meaning not documented here (see the files above / the code that writes it)*
  - `dist_name` (str; e.g. 'CHIKKABALLAPUR')  - *meaning not documented here (see the files above / the code that writes it)*
  - `govt_girl` (float64; e.g. '0.0')  - *meaning not documented here (see the files above / the code that writes it)*
  - `govt_boy` (float64; e.g. '0.0')  - *meaning not documented here (see the files above / the code that writes it)*
  - `aided_girl` (float64; e.g. '1.0')  - *meaning not documented here (see the files above / the code that writes it)*
  - `aided_boy` (float64; e.g. '0.0')  - *meaning not documented here (see the files above / the code that writes it)*
  - `unaided_girl` (float64; e.g. '0.0')  - *meaning not documented here (see the files above / the code that writes it)*
  - `unaided_boy` (float64; e.g. '0.0')  - *meaning not documented here (see the files above / the code that writes it)*
  - `total` (float64; e.g. '1.0')  - *meaning not documented here (see the files above / the code that writes it)*
  - `source_file` (str; e.g. 'SSLCAPR2017.xlsx')  - *meaning not documented here (see the files above / the code that writes it)*
  - `sheet` (str; e.g. 'PRO_10')  - *meaning not documented here (see the files above / the code that writes it)*

### `data\clean\district_other_candidate_types.csv`
- size 155 KB; modified 2026-10-13; rows 1066
- columns / contents:
  - `year` (int64; e.g. '2015'): publication year
  - `exam` (str; e.g. 'April 2015 main')  - *meaning not documented here (see the files above / the code that writes it)*
  - `scope` (str; e.g. 'main_exam')  - *meaning not documented here (see the files above / the code that writes it)*
  - `dist_code` (str; e.g. 'AN')  - *meaning not documented here (see the files above / the code that writes it)*
  - `dist_name` (str; e.g. 'BENGALURU\xa0NORTH')  - *meaning not documented here (see the files above / the code that writes it)*
  - `boys_app` (float64; e.g. '1819.0')  - *meaning not documented here (see the files above / the code that writes it)*
  - `girls_app` (float64; e.g. '856.0')  - *meaning not documented here (see the files above / the code that writes it)*
  - `app` (float64; e.g. '2675.0')  - *meaning not documented here (see the files above / the code that writes it)*
  - `boys_pass` (float64; e.g. '711.0')  - *meaning not documented here (see the files above / the code that writes it)*
  - `girls_pass` (float64; e.g. '407.0')  - *meaning not documented here (see the files above / the code that writes it)*
  - `passed` (float64; e.g. '1118.0')  - *meaning not documented here (see the files above / the code that writes it)*
  - `pct` (float64; e.g. '41.79')  - *meaning not documented here (see the files above / the code that writes it)*
  - `source_file` (str; e.g. 'April_2015_stats.xlsx')  - *meaning not documented here (see the files above / the code that writes it)*
  - `sheet` (str; e.g. 'PRO-11')  - *meaning not documented here (see the files above / the code that writes it)*
  - `cand_type` (str; e.g. 'regular_repeater')  - *meaning not documented here (see the files above / the code that writes it)*

### `data\clean\district_regular_fresh_by_gender.csv`
- size 57 KB; modified 2026-10-13; rows 378
- columns / contents:
  - `year` (int64; e.g. '2015'): publication year
  - `exam` (str; e.g. 'April 2015 main')  - *meaning not documented here (see the files above / the code that writes it)*
  - `scope` (str; e.g. 'main_exam')  - *meaning not documented here (see the files above / the code that writes it)*
  - `dist_code` (str; e.g. 'AN')  - *meaning not documented here (see the files above / the code that writes it)*
  - `dist_name` (str; e.g. 'BENGALURU\xa0NORTH')  - *meaning not documented here (see the files above / the code that writes it)*
  - `boys_app` (float64; e.g. '22638.0')  - *meaning not documented here (see the files above / the code that writes it)*
  - `boys_pass` (float64; e.g. '18743.0')  - *meaning not documented here (see the files above / the code that writes it)*
  - `boys_pct` (float64; e.g. '82.79')  - *meaning not documented here (see the files above / the code that writes it)*
  - `girls_app` (float64; e.g. '22464.0')  - *meaning not documented here (see the files above / the code that writes it)*
  - `girls_pass` (float64; e.g. '19548.0')  - *meaning not documented here (see the files above / the code that writes it)*
  - `girls_pct` (float64; e.g. '87.02')  - *meaning not documented here (see the files above / the code that writes it)*
  - `app` (float64; e.g. '45102.0')  - *meaning not documented here (see the files above / the code that writes it)*
  - `passed` (float64; e.g. '38291.0')  - *meaning not documented here (see the files above / the code that writes it)*
  - `pct` (float64; e.g. '84.9')  - *meaning not documented here (see the files above / the code that writes it)*
  - `source_file` (str; e.g. 'April_2015_stats.xlsx')  - *meaning not documented here (see the files above / the code that writes it)*
  - `sheet` (str; e.g. 'PRO-5')  - *meaning not documented here (see the files above / the code that writes it)*

### `data\clean\district_regular_fresh_by_management.csv`
- size 136 KB; modified 2026-10-13; rows 1134
- columns / contents:
  - `year` (int64; e.g. '2015'): publication year
  - `exam` (str; e.g. 'April 2015 main')  - *meaning not documented here (see the files above / the code that writes it)*
  - `scope` (str; e.g. 'main_exam')  - *meaning not documented here (see the files above / the code that writes it)*
  - `dist_code` (str; e.g. 'AN')  - *meaning not documented here (see the files above / the code that writes it)*
  - `dist_name` (str; e.g. 'BENGALURU\xa0NORTH')  - *meaning not documented here (see the files above / the code that writes it)*
  - `source_file` (str; e.g. 'April_2015_stats.xlsx')  - *meaning not documented here (see the files above / the code that writes it)*
  - `app` (float64; e.g. '5482.0')  - *meaning not documented here (see the files above / the code that writes it)*
  - `passed` (float64; e.g. '4469.0')  - *meaning not documented here (see the files above / the code that writes it)*
  - `management` (str; e.g. 'govt')  - *meaning not documented here (see the files above / the code that writes it)*
  - `pct` (float64; e.g. '81.52134257570229')  - *meaning not documented here (see the files above / the code that writes it)*

### `data\clean\district_regular_fresh_by_management_sex.csv`
- size 116 KB; modified 2026-10-13; rows 756
- columns / contents:
  - `year` (int64; e.g. '2015'): publication year
  - `exam` (str; e.g. 'April 2015 main')  - *meaning not documented here (see the files above / the code that writes it)*
  - `scope` (str; e.g. 'main_exam')  - *meaning not documented here (see the files above / the code that writes it)*
  - `dist_code` (str; e.g. 'AN')  - *meaning not documented here (see the files above / the code that writes it)*
  - `dist_name` (str; e.g. 'BENGALURU\xa0NORTH')  - *meaning not documented here (see the files above / the code that writes it)*
  - `govt_app` (float64; e.g. '2675.0')  - *meaning not documented here (see the files above / the code that writes it)*
  - `govt_pass` (float64; e.g. '2099.0')  - *meaning not documented here (see the files above / the code that writes it)*
  - `govt_pct` (float64; e.g. '78.47')  - *meaning not documented here (see the files above / the code that writes it)*
  - `aided_app` (float64; e.g. '3900.0')  - *meaning not documented here (see the files above / the code that writes it)*
  - `aided_pass` (float64; e.g. '2680.0')  - *meaning not documented here (see the files above / the code that writes it)*
  - `aided_pct` (float64; e.g. '68.72')  - *meaning not documented here (see the files above / the code that writes it)*
  - `unaided_app` (float64; e.g. '16063.0')  - *meaning not documented here (see the files above / the code that writes it)*
  - `unaided_pass` (float64; e.g. '13964.0')  - *meaning not documented here (see the files above / the code that writes it)*
  - `unaided_pct` (float64; e.g. '86.93')  - *meaning not documented here (see the files above / the code that writes it)*
  - `source_file` (str; e.g. 'April_2015_stats.xlsx')  - *meaning not documented here (see the files above / the code that writes it)*
  - `sheet` (str; e.g. 'PRO-7A')  - *meaning not documented here (see the files above / the code that writes it)*
  - `sex` (str; e.g. 'boys')  - *meaning not documented here (see the files above / the code that writes it)*

### `data\clean\district_regular_fresh_by_subject.csv`
- size 364 KB; modified 2026-10-13; rows 2200
- columns / contents:
  - `year` (int64; e.g. '2015'): publication year
  - `exam` (str; e.g. 'April 2015 main')  - *meaning not documented here (see the files above / the code that writes it)*
  - `scope` (str; e.g. 'main_exam')  - *meaning not documented here (see the files above / the code that writes it)*
  - `dist_code` (str; e.g. 'AN')  - *meaning not documented here (see the files above / the code that writes it)*
  - `dist_name` (str; e.g. 'BENGALURU\xa0NORTH')  - *meaning not documented here (see the files above / the code that writes it)*
  - `source_file` (str; e.g. 'April_2015_stats.xlsx')  - *meaning not documented here (see the files above / the code that writes it)*
  - `sheet` (str; e.g. 'PRO-2A_1_')  - *meaning not documented here (see the files above / the code that writes it)*
  - `subject` (str; e.g. 'language_1')  - *meaning not documented here (see the files above / the code that writes it)*
  - `b_app` (float64; e.g. '22590.0')  - *meaning not documented here (see the files above / the code that writes it)*
  - `b_pass` (float64; e.g. '21688.0')  - *meaning not documented here (see the files above / the code that writes it)*
  - `g_app` (float64; e.g. '22443.0')  - *meaning not documented here (see the files above / the code that writes it)*
  - `g_pass` (float64; e.g. '21860.0')  - *meaning not documented here (see the files above / the code that writes it)*
  - `app` (float64; e.g. '45033.0')  - *meaning not documented here (see the files above / the code that writes it)*
  - `passed` (float64; e.g. '43548.0')  - *meaning not documented here (see the files above / the code that writes it)*
  - `pct` (float64; e.g. '96.7024182266338')  - *meaning not documented here (see the files above / the code that writes it)*

### `data\clean\district_regular_fresh_by_urban_rural.csv`
- size 81 KB; modified 2026-10-13; rows 378
- columns / contents:
  - `year` (int64; e.g. '2015'): publication year
  - `exam` (str; e.g. 'April 2015 main')  - *meaning not documented here (see the files above / the code that writes it)*
  - `scope` (str; e.g. 'main_exam')  - *meaning not documented here (see the files above / the code that writes it)*
  - `dist_code` (str; e.g. 'AN')  - *meaning not documented here (see the files above / the code that writes it)*
  - `dist_name` (str; e.g. 'BENGALURU\xa0NORTH')  - *meaning not documented here (see the files above / the code that writes it)*
  - `b_rur_app` (float64; e.g. '1573.0')  - *meaning not documented here (see the files above / the code that writes it)*
  - `b_rur_pass` (float64; e.g. '1322.0')  - *meaning not documented here (see the files above / the code that writes it)*
  - `b_rur_pct` (float64; e.g. '84.04')  - *meaning not documented here (see the files above / the code that writes it)*
  - `b_urb_app` (float64; e.g. '21065.0')  - *meaning not documented here (see the files above / the code that writes it)*
  - `b_urb_pass` (float64; e.g. '17421.0')  - *meaning not documented here (see the files above / the code that writes it)*
  - `b_urb_pct` (float64; e.g. '82.7')  - *meaning not documented here (see the files above / the code that writes it)*
  - `g_rur_app` (float64; e.g. '1431.0')  - *meaning not documented here (see the files above / the code that writes it)*
  - `g_rur_pass` (float64; e.g. '1284.0')  - *meaning not documented here (see the files above / the code that writes it)*
  - `g_rur_pct` (float64; e.g. '89.73')  - *meaning not documented here (see the files above / the code that writes it)*
  - `g_urb_app` (float64; e.g. '21033.0')  - *meaning not documented here (see the files above / the code that writes it)*
  - `g_urb_pass` (float64; e.g. '18264.0')  - *meaning not documented here (see the files above / the code that writes it)*
  - `g_urb_pct` (float64; e.g. '86.83')  - *meaning not documented here (see the files above / the code that writes it)*
  - `rural_app` (float64; e.g. '3004.0')  - *meaning not documented here (see the files above / the code that writes it)*
  - `rural_pass` (float64; e.g. '2606.0')  - *meaning not documented here (see the files above / the code that writes it)*
  - `rural_pct` (float64; e.g. '86.75')  - *meaning not documented here (see the files above / the code that writes it)*
  - `urban_app` (float64; e.g. '42098.0')  - *meaning not documented here (see the files above / the code that writes it)*
  - `urban_pass` (float64; e.g. '35685.0')  - *meaning not documented here (see the files above / the code that writes it)*
  - `urban_pct` (float64; e.g. '84.77')  - *meaning not documented here (see the files above / the code that writes it)*
  - `source_file` (str; e.g. 'April_2015_stats.xlsx')  - *meaning not documented here (see the files above / the code that writes it)*
  - `sheet` (str; e.g. 'PRO-6A')  - *meaning not documented here (see the files above / the code that writes it)*

### `data\clean\district_regular_fresh_grade_distribution.csv`
- size 55 KB; modified 2026-10-13; rows 378
- columns / contents:
  - `year` (int64; e.g. '2015'): publication year
  - `exam` (str; e.g. 'April 2015 main')  - *meaning not documented here (see the files above / the code that writes it)*
  - `scope` (str; e.g. 'main_exam')  - *meaning not documented here (see the files above / the code that writes it)*
  - `dist_code` (str; e.g. 'AN')  - *meaning not documented here (see the files above / the code that writes it)*
  - `dist_name` (str; e.g. 'BENGALURU\xa0NORTH')  - *meaning not documented here (see the files above / the code that writes it)*
  - `app` (float64; e.g. '45102.0')  - *meaning not documented here (see the files above / the code that writes it)*
  - `passed` (float64; e.g. '38291.0')  - *meaning not documented here (see the files above / the code that writes it)*
  - `A_plus` (float64; e.g. '2890.0')  - *meaning not documented here (see the files above / the code that writes it)*
  - `A` (float64; e.g. '6176.0')  - *meaning not documented here (see the files above / the code that writes it)*
  - `B_plus` (float64; e.g. '8063.0')  - *meaning not documented here (see the files above / the code that writes it)*
  - `B` (float64; e.g. '9056.0')  - *meaning not documented here (see the files above / the code that writes it)*
  - `C_plus` (str; e.g. '8019.0')  - *meaning not documented here (see the files above / the code that writes it)*
  - `C` (str; e.g. '4087.0')  - *meaning not documented here (see the files above / the code that writes it)*
  - `source_file` (str; e.g. 'April_2015_stats.xlsx')  - *meaning not documented here (see the files above / the code that writes it)*
  - `sheet` (str; e.g. 'PRO-16')  - *meaning not documented here (see the files above / the code that writes it)*

### `data\clean\district_school_dispersion_2018_2019.csv`
- size 8 KB; modified 2026-10-13; rows 68
- columns / contents:
  - `unit` (str; e.g. 'AN')  - *meaning not documented here (see the files above / the code that writes it)*
  - `year` (int64; e.g. '2018'): publication year
  - `n_schools_10plus` (float64; e.g. '860.0')  - *meaning not documented here (see the files above / the code that writes it)*
  - `share_schools_100pct` (float64; e.g. '0.0686046511627907')  - *meaning not documented here (see the files above / the code that writes it)*
  - `share_schools_95plus` (float64; e.g. '0.1848837209302325')  - *meaning not documented here (see the files above / the code that writes it)*
  - `share_students_in_100pct_schools` (float64; e.g. '0.0713338143226196')  - *meaning not documented here (see the files above / the code that writes it)*
  - `school_pass_sd` (float64; e.g. '21.394755279085544')  - *meaning not documented here (see the files above / the code that writes it)*
  - `school_pass_p10` (float64; e.g. '43.948')  - *meaning not documented here (see the files above / the code that writes it)*
  - `school_pass_median` (float64; e.g. '79.31')  - *meaning not documented here (see the files above / the code that writes it)*
  - `school_pass_p90` (float64; e.g. '97.67')  - *meaning not documented here (see the files above / the code that writes it)*

### `data\clean\district_schools_0pct.csv`
- size 33 KB; modified 2026-10-13; rows 294
- columns / contents:
  - `year` (int64; e.g. '2017'): publication year
  - `exam` (str; e.g. 'April 2017 main')  - *meaning not documented here (see the files above / the code that writes it)*
  - `scope` (str; e.g. 'main_exam')  - *meaning not documented here (see the files above / the code that writes it)*
  - `dist_code` (str; e.g. 'AN')  - *meaning not documented here (see the files above / the code that writes it)*
  - `dist_name` (str; e.g. 'BENGALURU NORTH')  - *meaning not documented here (see the files above / the code that writes it)*
  - `govt` (float64; e.g. '0.0')  - *meaning not documented here (see the files above / the code that writes it)*
  - `aided` (float64; e.g. '1.0')  - *meaning not documented here (see the files above / the code that writes it)*
  - `unaided` (float64; e.g. '7.0')  - *meaning not documented here (see the files above / the code that writes it)*
  - `total` (float64; e.g. '8.0')  - *meaning not documented here (see the files above / the code that writes it)*
  - `source_file` (str; e.g. 'SSLCAPR2017.xlsx')  - *meaning not documented here (see the files above / the code that writes it)*
  - `sheet` (str; e.g. 'PRO_13')  - *meaning not documented here (see the files above / the code that writes it)*

### `data\clean\district_schools_100pct.csv`
- size 40 KB; modified 2026-10-13; rows 344
- columns / contents:
  - `year` (int64; e.g. '2017'): publication year
  - `exam` (str; e.g. 'April 2017 main')  - *meaning not documented here (see the files above / the code that writes it)*
  - `scope` (str; e.g. 'main_exam')  - *meaning not documented here (see the files above / the code that writes it)*
  - `dist_code` (str; e.g. 'AN')  - *meaning not documented here (see the files above / the code that writes it)*
  - `dist_name` (str; e.g. 'BENGALURU NORTH')  - *meaning not documented here (see the files above / the code that writes it)*
  - `total_schools` (float64; e.g. '882.0')  - *meaning not documented here (see the files above / the code that writes it)*
  - `govt` (float64; e.g. '1.0')  - *meaning not documented here (see the files above / the code that writes it)*
  - `aided` (float64; e.g. '1.0')  - *meaning not documented here (see the files above / the code that writes it)*
  - `unaided` (float64; e.g. '49.0')  - *meaning not documented here (see the files above / the code that writes it)*
  - `total` (float64; e.g. '51.0')  - *meaning not documented here (see the files above / the code that writes it)*
  - `source_file` (str; e.g. 'SSLCAPR2017.xlsx')  - *meaning not documented here (see the files above / the code that writes it)*
  - `sheet` (str; e.g. 'PRO_12')  - *meaning not documented here (see the files above / the code that writes it)*

### `data\clean\panel_district_year.csv`
- size 88 KB; modified 2026-10-13; rows 816
- columns / contents:
  - `unit` (str; e.g. 'AN')  - *meaning not documented here (see the files above / the code that writes it)*
  - `unit_name` (str; e.g. 'BENGALURU NORTH')  - *meaning not documented here (see the files above / the code that writes it)*
  - `division` (str; e.g. 'Bengaluru')  - *meaning not documented here (see the files above / the code that writes it)*
  - `year` (int64; e.g. '2014'): publication year
  - `series` (str; e.g. 'S1')  - *meaning not documented here (see the files above / the code that writes it)*
  - `app` (float64; e.g. '49896.0')  - *meaning not documented here (see the files above / the code that writes it)*
  - `passed` (float64; e.g. '39043.0')  - *meaning not documented here (see the files above / the code that writes it)*
  - `pass_pct` (float64; e.g. '78.24875741542408')  - *meaning not documented here (see the files above / the code that writes it)*
  - `exam` (str; e.g. 'exam')  - *meaning not documented here (see the files above / the code that writes it)*
  - `source` (str; e.g. 'KSEAB 5years.xlsx'): journal / repository name
  - `n_parts` (int64; e.g. '1')  - *meaning not documented here (see the files above / the code that writes it)*

### `data\clean\school_regular_fresh_2018_2019.csv`
- size 4067 KB; modified 2026-10-13; rows 28715
- columns / contents:
  - `year` (int64; e.g. '2018'): publication year
  - `division_file` (str; e.g. 'BANGALORE')  - *meaning not documented here (see the files above / the code that writes it)*
  - `dist_code` (str; e.g. 'AN')  - *meaning not documented here (see the files above / the code that writes it)*
  - `dist_name` (str; e.g. 'BENGALURU NORTH')  - *meaning not documented here (see the files above / the code that writes it)*
  - `taluk_code` (str; e.g. 'AN01')  - *meaning not documented here (see the files above / the code that writes it)*
  - `taluk_name` (str; e.g. 'BENGALURU NORTH-1')  - *meaning not documented here (see the files above / the code that writes it)*
  - `school_code` (str; e.g. 'AN0016')  - *meaning not documented here (see the files above / the code that writes it)*
  - `school_name` (str; e.g. 'BASAVESWARA BOYS HIGH SCHOOL')  - *meaning not documented here (see the files above / the code that writes it)*
  - `boys_app` (float64; e.g. '45.0')  - *meaning not documented here (see the files above / the code that writes it)*
  - `boys_pass` (float64; e.g. '22.0')  - *meaning not documented here (see the files above / the code that writes it)*
  - `girls_app` (float64; e.g. '0.0')  - *meaning not documented here (see the files above / the code that writes it)*
  - `girls_pass` (float64; e.g. '0.0')  - *meaning not documented here (see the files above / the code that writes it)*
  - `app` (float64; e.g. '45.0')  - *meaning not documented here (see the files above / the code that writes it)*
  - `passed` (float64; e.g. '22.0')  - *meaning not documented here (see the files above / the code that writes it)*
  - `pct` (float64; e.g. '48.89')  - *meaning not documented here (see the files above / the code that writes it)*
  - `source_file` (str; e.g. 'schoolwise_2018_BANGALORE.xlsx')  - *meaning not documented here (see the files above / the code that writes it)*

### `data\clean\taluk_regular_fresh.csv`
- size 241 KB; modified 2026-10-13; rows 2040
- columns / contents:
  - `year` (int64; e.g. '2017'): publication year
  - `scope` (str; e.g. 'main_exam')  - *meaning not documented here (see the files above / the code that writes it)*
  - `dist_code` (str; e.g. 'NA')  - *meaning not documented here (see the files above / the code that writes it)*
  - `dist_name` (str; e.g. 'CHIKODI')  - *meaning not documented here (see the files above / the code that writes it)*
  - `taluk_code` (str; e.g. 'NA07')  - *meaning not documented here (see the files above / the code that writes it)*
  - `taluk_name` (str; e.g. 'MUDALAGI')  - *meaning not documented here (see the files above / the code that writes it)*
  - `boys_app` (float64; e.g. '2889.0')  - *meaning not documented here (see the files above / the code that writes it)*
  - `boys_pass` (float64; e.g. '2671.0')  - *meaning not documented here (see the files above / the code that writes it)*
  - `girls_app` (float64; e.g. '2301.0')  - *meaning not documented here (see the files above / the code that writes it)*
  - `girls_pass` (float64; e.g. '2216.0')  - *meaning not documented here (see the files above / the code that writes it)*
  - `app` (float64; e.g. '5190.0')  - *meaning not documented here (see the files above / the code that writes it)*
  - `passed` (float64; e.g. '4887.0')  - *meaning not documented here (see the files above / the code that writes it)*
  - `pct` (float64; e.g. '94.16')  - *meaning not documented here (see the files above / the code that writes it)*
  - `source_file` (str; e.g. 'SSLCAPR2017.xlsx')  - *meaning not documented here (see the files above / the code that writes it)*

### `data\clean\transcribed\exam1_2024_district_all_candidates.csv`
- size 1 KB; modified 2026-10-13; rows 35
- columns / contents:
  - `dist_name` (str; e.g. 'UDUPI')  - *meaning not documented here (see the files above / the code that writes it)*
  - `app` (int64; e.g. '14092')  - *meaning not documented here (see the files above / the code that writes it)*
  - `passed` (int64; e.g. '13246')  - *meaning not documented here (see the files above / the code that writes it)*
  - `pct_printed` (float64; e.g. '94.0')  - *meaning not documented here (see the files above / the code that writes it)*
  - `rank_2024` (int64; e.g. '1')  - *meaning not documented here (see the files above / the code that writes it)*
  - `rank_2023` (int64; e.g. '14')  - *meaning not documented here (see the files above / the code that writes it)*

### `data\clean\transcribed\exam1_2025_district_regular_fresh.csv`
- size 1 KB; modified 2026-10-13; rows 35
- columns / contents:
  - `dist_name` (str; e.g. 'DAKSHINA KANNADA')  - *meaning not documented here (see the files above / the code that writes it)*
  - `app` (int64; e.g. '27795')  - *meaning not documented here (see the files above / the code that writes it)*
  - `passed` (int64; e.g. '25326')  - *meaning not documented here (see the files above / the code that writes it)*
  - `pct_printed` (float64; e.g. '91.12')  - *meaning not documented here (see the files above / the code that writes it)*

### `data\clean\transcribed\exam1_2026_district_regular_fresh.csv`
- size 1 KB; modified 2026-10-13; rows 35
- columns / contents:
  - `dist_name` (str; e.g. 'BAGALAKOTE')  - *meaning not documented here (see the files above / the code that writes it)*
  - `app` (int64; e.g. '30111')  - *meaning not documented here (see the files above / the code that writes it)*
  - `passed` (int64; e.g. '28731')  - *meaning not documented here (see the files above / the code that writes it)*
  - `pct_printed` (float64; e.g. '95.42')  - *meaning not documented here (see the files above / the code that writes it)*
  - `pct_2025_best_of_3_printed` (float64; e.g. '82.3')  - *meaning not documented here (see the files above / the code that writes it)*

### `data\clean\transcribed\state_first_exam_by_group.csv`
- size 4 KB; modified 2026-10-13; rows 46
- columns / contents:
  - `year` (int64; e.g. '2022'): publication year
  - `exam` (str; e.g. 'March/April 2022 main')  - *meaning not documented here (see the files above / the code that writes it)*
  - `population` (str; e.g. 'regular_fresh')  - *meaning not documented here (see the files above / the code that writes it)*
  - `dimension` (str; e.g. 'management')  - *meaning not documented here (see the files above / the code that writes it)*
  - `group` (str; e.g. 'government')  - *meaning not documented here (see the files above / the code that writes it)*
  - `appeared` (int64; e.g. '337769')  - *meaning not documented here (see the files above / the code that writes it)*
  - `passed` (int64; e.g. '297261')  - *meaning not documented here (see the files above / the code that writes it)*
  - `pct` (float64; e.g. '88.0')  - *meaning not documented here (see the files above / the code that writes it)*
  - `source` (str; e.g. 'PN_2022_Main.pdf'): journal / repository name

### `data\clean\transcribed\state_first_exam_series.csv`
- size 3 KB; modified 2026-10-13; rows 27
- columns / contents:
  - `year` (int64; e.g. '2014'): publication year
  - `exam` (str; e.g. 'April 2014 main')  - *meaning not documented here (see the files above / the code that writes it)*
  - `population` (str; e.g. 'all_candidates')  - *meaning not documented here (see the files above / the code that writes it)*
  - `appeared` (int64; e.g. '813601')  - *meaning not documented here (see the files above / the code that writes it)*
  - `passed` (int64; e.g. '661002')  - *meaning not documented here (see the files above / the code that writes it)*
  - `pct` (float64; e.g. '81.24')  - *meaning not documented here (see the files above / the code that writes it)*
  - `source` (str; e.g. '5years.xlsx sheet 5YEARS'): journal / repository name
  - `note` (str; e.g. '')  - *meaning not documented here (see the files above / the code that writes it)*

### `data\clean\transcribed\state_grade_distribution_first_exam.csv`
- size 2 KB; modified 2026-10-13; rows 24
- columns / contents:
  - `year` (int64; e.g. '2023'): publication year
  - `exam` (str; e.g. 'March/April 2023 main')  - *meaning not documented here (see the files above / the code that writes it)*
  - `population` (str; e.g. 'regular_fresh')  - *meaning not documented here (see the files above / the code that writes it)*
  - `grade` (str; e.g. 'A_plus')  - *meaning not documented here (see the files above / the code that writes it)*
  - `band` (str; e.g. '90-100')  - *meaning not documented here (see the files above / the code that writes it)*
  - `students` (int64; e.g. '61003')  - *meaning not documented here (see the files above / the code that writes it)*
  - `pct_of_passes_printed` (float64; e.g. '8.83')  - *meaning not documented here (see the files above / the code that writes it)*
  - `source` (str; e.g. 'PN_2024_Exam1.pdf table 11'): journal / repository name

### `followup\data\exam1_2024_district_all_candidates_verified.csv`
- size 1 KB; modified 2026-10-13; rows 35
- columns / contents:
  - `dist_name` (str; e.g. 'UDUPI')  - *meaning not documented here (see the files above / the code that writes it)*
  - `app` (int64; e.g. '14092')  - *meaning not documented here (see the files above / the code that writes it)*
  - `passed` (int64; e.g. '13246')  - *meaning not documented here (see the files above / the code that writes it)*
  - `pct_printed` (float64; e.g. '94.0')  - *meaning not documented here (see the files above / the code that writes it)*
  - `rank_2024` (int64; e.g. '1')  - *meaning not documented here (see the files above / the code that writes it)*
  - `rank_2023` (int64; e.g. '14')  - *meaning not documented here (see the files above / the code that writes it)*

### `followup\data\exam1_2025_district_regular_fresh_verified.csv`
- size 1 KB; modified 2026-10-13; rows 35
- columns / contents:
  - `dist_name` (str; e.g. 'DAKSHINA KANNADA')  - *meaning not documented here (see the files above / the code that writes it)*
  - `app` (int64; e.g. '27795')  - *meaning not documented here (see the files above / the code that writes it)*
  - `passed` (int64; e.g. '25326')  - *meaning not documented here (see the files above / the code that writes it)*
  - `pct_printed` (float64; e.g. '91.12')  - *meaning not documented here (see the files above / the code that writes it)*

### `followup\data\exam1_2026_district_regular_fresh_verified.csv`
- size 1 KB; modified 2026-10-13; rows 35
- columns / contents:
  - `dist_name` (str; e.g. 'BAGALAKOTE')  - *meaning not documented here (see the files above / the code that writes it)*
  - `app` (int64; e.g. '30111')  - *meaning not documented here (see the files above / the code that writes it)*
  - `passed` (int64; e.g. '28731')  - *meaning not documented here (see the files above / the code that writes it)*
  - `pct_printed` (float64; e.g. '95.42')  - *meaning not documented here (see the files above / the code that writes it)*
  - `pct_2025_best_of_3_printed` (float64; e.g. '82.3')  - *meaning not documented here (see the files above / the code that writes it)*

### `followup\data\nas2021_class10_district.csv`
- size 4 KB; modified 2026-10-13; rows 34
- columns / contents:
  - `unit_name` (str; e.g. 'BAGALAKOTE')  - *meaning not documented here (see the files above / the code that writes it)*
  - `file` (str; e.g. 'NAS21_DRC_Bagalkot.pdf')  - *meaning not documented here (see the files above / the code that writes it)*
  - `MIL` (int64; e.g. '37')  - *meaning not documented here (see the files above / the code that writes it)*
  - `MIL_se` (float64; e.g. '0.35')  - *meaning not documented here (see the files above / the code that writes it)*
  - `MIL_state` (int64; e.g. '35')  - *meaning not documented here (see the files above / the code that writes it)*
  - `MIL_natl` (int64; e.g. '41')  - *meaning not documented here (see the files above / the code that writes it)*
  - `Maths` (int64; e.g. '32')  - *meaning not documented here (see the files above / the code that writes it)*
  - `Maths_se` (float64; e.g. '0.46')  - *meaning not documented here (see the files above / the code that writes it)*
  - `Maths_state` (int64; e.g. '32')  - *meaning not documented here (see the files above / the code that writes it)*
  - `Maths_natl` (int64; e.g. '32')  - *meaning not documented here (see the files above / the code that writes it)*
  - `Science` (int64; e.g. '34')  - *meaning not documented here (see the files above / the code that writes it)*
  - `Science_se` (float64; e.g. '0.41')  - *meaning not documented here (see the files above / the code that writes it)*
  - `Science_state` (int64; e.g. '35')  - *meaning not documented here (see the files above / the code that writes it)*
  - `Science_natl` (int64; e.g. '35')  - *meaning not documented here (see the files above / the code that writes it)*
  - `SocSci` (int64; e.g. '40')  - *meaning not documented here (see the files above / the code that writes it)*
  - `SocSci_se` (float64; e.g. '0.46')  - *meaning not documented here (see the files above / the code that writes it)*
  - `SocSci_state` (int64; e.g. '39')  - *meaning not documented here (see the files above / the code that writes it)*
  - `SocSci_natl` (int64; e.g. '37')  - *meaning not documented here (see the files above / the code that writes it)*
  - `English` (int64; e.g. '44')  - *meaning not documented here (see the files above / the code that writes it)*
  - `English_se` (float64; e.g. '0.64')  - *meaning not documented here (see the files above / the code that writes it)*
  - `English_state` (int64; e.g. '46')  - *meaning not documented here (see the files above / the code that writes it)*
  - `English_natl` (int64; e.g. '43')  - *meaning not documented here (see the files above / the code that writes it)*
  - `nas_mean5` (float64; e.g. '37.4')  - *meaning not documented here (see the files above / the code that writes it)*
  - `nas_ms` (float64; e.g. '33.0')  - *meaning not documented here (see the files above / the code that writes it)*

### `followup\data\ocr_comparison_log.txt`
- size 1 KB; modified 2026-10-13
- columns / contents:
  - (could not read: ParserError)

### `followup\data\puc_district_regular_passpct.csv`
- size 21 KB; modified 2026-10-13; rows 222
- columns / contents:
  - `district` (str; e.g. 'BAGALAKOTE')  - *meaning not documented here (see the files above / the code that writes it)*
  - `year` (int64; e.g. '2016'): publication year
  - `pass_pct` (float64; e.g. '65.91')  - *meaning not documented here (see the files above / the code that writes it)*
  - `source` (str; e.g. 'DPUE press release March 2017, table 16 '): journal / repository name

### `followup\results\learning_gap_log.txt`
- size 2 KB; modified 2026-10-13
- columns / contents:
  - (could not read: ParserError)

### `followup\results\puc_analysis_log.txt`
- size 3 KB; modified 2026-10-13
- columns / contents:
  - (could not read: ParserError)

### `followup\results\tables\L_learning_gap.csv`
- size 1 KB; modified 2026-10-13; rows 11
- columns / contents:
  - `spec` (str; e.g. 'L1 d2324 ~ gap2023')  - *meaning not documented here (see the files above / the code that writes it)*
  - `n` (int64; e.g. '34')  - *meaning not documented here (see the files above / the code that writes it)*
  - `coef_gap` (str; e.g. '-3.5452915719045954')  - *meaning not documented here (see the files above / the code that writes it)*
  - `se_gap` (str; e.g. '1.0994240298768785')  - *meaning not documented here (see the files above / the code that writes it)*
  - `r2` (float64; e.g. '0.19941640525347')  - *meaning not documented here (see the files above / the code that writes it)*
  - `spearman_first` (float64; e.g. '-0.3692895339954163')  - *meaning not documented here (see the files above / the code that writes it)*
  - `coef_z_pass2023` (str; e.g. '')  - *meaning not documented here (see the files above / the code that writes it)*
  - `coef_z_NAS` (str; e.g. '')  - *meaning not documented here (see the files above / the code that writes it)*
  - `se_z_pass2023` (str; e.g. '')  - *meaning not documented here (see the files above / the code that writes it)*
  - `se_z_NAS` (str; e.g. '')  - *meaning not documented here (see the files above / the code that writes it)*
  - `coef_z_pass` (str; e.g. '')  - *meaning not documented here (see the files above / the code that writes it)*
  - `se_z_pass` (str; e.g. '')  - *meaning not documented here (see the files above / the code that writes it)*

### `followup\results\tables\U2_U3_U5_puc_pairs.csv`
- size 1 KB; modified 2026-10-13; rows 6
- columns / contents:
  - `pair` (str; e.g. '2016-2017')  - *meaning not documented here (see the files above / the code that writes it)*
  - `n` (int64; e.g. '31')  - *meaning not documented here (see the files above / the code that writes it)*
  - `spearman` (float64; e.g. '0.8814516129032259')  - *meaning not documented here (see the files above / the code that writes it)*
  - `pearson` (float64; e.g. '0.909415009376791')  - *meaning not documented here (see the files above / the code that writes it)*
  - `sd_change` (float64; e.g. '4.9644756948474615')  - *meaning not documented here (see the files above / the code that writes it)*
  - `mean_change` (float64; e.g. '-4.315483870967742')  - *meaning not documented here (see the files above / the code that writes it)*
  - `rising` (int64; e.g. '4')  - *meaning not documented here (see the files above / the code that writes it)*
  - `falling` (int64; e.g. '27')  - *meaning not documented here (see the files above / the code that writes it)*
  - `slope_level` (float64; e.g. '-0.0010258889798843')  - *meaning not documented here (see the files above / the code that writes it)*
  - `se` (float64; e.g. '0.0813540084446356')  - *meaning not documented here (see the files above / the code that writes it)*
  - `p` (float64; e.g. '0.9899387958787088')  - *meaning not documented here (see the files above / the code that writes it)*
  - `r2` (float64; e.g. '5.0426373023881865e-06')  - *meaning not documented here (see the files above / the code that writes it)*

### `followup\results\tables\U4_puc_giveback.csv`
- size 1 KB; modified 2026-10-13; rows 5
- columns / contents:
  - `spec` (str; e.g. 'change 2024->2025 on rise 2018->2024')  - *meaning not documented here (see the files above / the code that writes it)*
  - `n` (int64; e.g. '32')  - *meaning not documented here (see the files above / the code that writes it)*
  - `slope` (float64; e.g. '-0.6621782699065296')  - *meaning not documented here (see the files above / the code that writes it)*
  - `se` (float64; e.g. '0.2340494387230471')  - *meaning not documented here (see the files above / the code that writes it)*
  - `p` (float64; e.g. '0.00466610395139')  - *meaning not documented here (see the files above / the code that writes it)*
  - `r2` (float64; e.g. '0.4650678070107032')  - *meaning not documented here (see the files above / the code that writes it)*

### `followup\results\tables\U7_sslc_vs_puc_changes.csv`
- size 1 KB; modified 2026-10-13; rows 6
- columns / contents:
  - `a` (str; e.g. 'SSLC S1 change 2023->24')  - *meaning not documented here (see the files above / the code that writes it)*
  - `b` (str; e.g. 'PU change 2023->24')  - *meaning not documented here (see the files above / the code that writes it)*
  - `n` (int64; e.g. '32')  - *meaning not documented here (see the files above / the code that writes it)*
  - `spearman` (float64; e.g. '-0.1726539589442815')  - *meaning not documented here (see the files above / the code that writes it)*
  - `pearson` (float64; e.g. '-0.2111821839813197')  - *meaning not documented here (see the files above / the code that writes it)*

### `followup\results\tables\U8_same_year_sslc_vs_puc.csv`
- size 0 KB; modified 2026-10-13; rows 5
- columns / contents:
  - `year` (int64; e.g. '2018'): publication year
  - `sslc_series` (str; e.g. 'S1')  - *meaning not documented here (see the files above / the code that writes it)*
  - `n` (int64; e.g. '32')  - *meaning not documented here (see the files above / the code that writes it)*
  - `spearman` (float64; e.g. '0.0894428152492668')  - *meaning not documented here (see the files above / the code that writes it)*
  - `pearson` (float64; e.g. '0.3179339465648867')  - *meaning not documented here (see the files above / the code that writes it)*

### `results\analysis_log.txt`
- size 30 KB; modified 2026-10-13
- columns / contents:
  - (could not read: ParserError)

### `results\posthoc_log.txt`
- size 4 KB; modified 2026-10-13
- columns / contents:
  - (could not read: ParserError)

### `results\tables\P1_rank_stability.csv`
- size 1 KB; modified 2026-10-13; rows 17
- columns / contents:
  - `series` (str; e.g. 'S1 all candidates')  - *meaning not documented here (see the files above / the code that writes it)*
  - `pair` (str; e.g. '2014-2015')  - *meaning not documented here (see the files above / the code that writes it)*
  - `spearman` (float64; e.g. '0.602')  - *meaning not documented here (see the files above / the code that writes it)*
  - `pearson` (float64; e.g. '0.51')  - *meaning not documented here (see the files above / the code that writes it)*
  - `mean_abs_rank_move` (float64; e.g. '6.765')  - *meaning not documented here (see the files above / the code that writes it)*
  - `sd_change` (float64; e.g. '5.889')  - *meaning not documented here (see the files above / the code that writes it)*

### `results\tables\P2_management_first_exam_series.csv`
- size 0 KB; modified 2026-10-13; rows 10
- columns / contents:
  - `year` (int64; e.g. '2015'): publication year
  - `govt` (float64; e.g. '83.14')  - *meaning not documented here (see the files above / the code that writes it)*
  - `aided` (float64; e.g. '83.26')  - *meaning not documented here (see the files above / the code that writes it)*
  - `unaided` (float64; e.g. '88.94')  - *meaning not documented here (see the files above / the code that writes it)*
  - `unaided_minus_govt` (float64; e.g. '5.8')  - *meaning not documented here (see the files above / the code that writes it)*

### `results\tables\P2_rural_urban_first_exam_series.csv`
- size 0 KB; modified 2026-10-13; rows 9
- columns / contents:
  - `year` (int64; e.g. '2015'): publication year
  - `rural` (float64; e.g. '86.36')  - *meaning not documented here (see the files above / the code that writes it)*
  - `urban` (float64; e.g. '82.89')  - *meaning not documented here (see the files above / the code that writes it)*
  - `rural_minus_urban` (float64; e.g. '3.46')  - *meaning not documented here (see the files above / the code that writes it)*

### `results\tables\T0_S1_all_candidates_first_exam_wide.csv`
- size 2 KB; modified 2026-10-13; rows 34
- columns / contents:
  - `unit` (str; e.g. 'AN')  - *meaning not documented here (see the files above / the code that writes it)*
  - `2014` (float64; e.g. '78.25')  - *meaning not documented here (see the files above / the code that writes it)*
  - `2015` (float64; e.g. '80.8')  - *meaning not documented here (see the files above / the code that writes it)*
  - `2016` (float64; e.g. '75.4')  - *meaning not documented here (see the files above / the code that writes it)*
  - `2017` (float64; e.g. '65.87')  - *meaning not documented here (see the files above / the code that writes it)*
  - `2018` (float64; e.g. '70.66')  - *meaning not documented here (see the files above / the code that writes it)*
  - `2019` (float64; e.g. '69.99')  - *meaning not documented here (see the files above / the code that writes it)*
  - `2020` (float64; e.g. '74.71')  - *meaning not documented here (see the files above / the code that writes it)*
  - `2021` (float64; e.g. '100.0')  - *meaning not documented here (see the files above / the code that writes it)*
  - `2022` (float64; e.g. '81.33')  - *meaning not documented here (see the files above / the code that writes it)*
  - `2023` (float64; e.g. '75.45')  - *meaning not documented here (see the files above / the code that writes it)*
  - `2024` (float64; e.g. '77.09')  - *meaning not documented here (see the files above / the code that writes it)*

### `results\tables\T0_S2_regular_fresh_first_exam_wide.csv`
- size 2 KB; modified 2026-10-13; rows 34
- columns / contents:
  - `unit` (str; e.g. 'AN')  - *meaning not documented here (see the files above / the code that writes it)*
  - `2015` (float64; e.g. '84.9')  - *meaning not documented here (see the files above / the code that writes it)*
  - `2017` (float64; e.g. '71.44')  - *meaning not documented here (see the files above / the code that writes it)*
  - `2018` (float64; e.g. '77.11')  - *meaning not documented here (see the files above / the code that writes it)*
  - `2019` (float64; e.g. '75.88')  - *meaning not documented here (see the files above / the code that writes it)*
  - `2020` (float64; e.g. '79.31')  - *meaning not documented here (see the files above / the code that writes it)*
  - `2021` (float64; e.g. '100.0')  - *meaning not documented here (see the files above / the code that writes it)*
  - `2022` (float64; e.g. '85.17')  - *meaning not documented here (see the files above / the code that writes it)*
  - `2023` (float64; e.g. '80.93')  - *meaning not documented here (see the files above / the code that writes it)*
  - `2025` (float64; e.g. '72.27')  - *meaning not documented here (see the files above / the code that writes it)*
  - `2026` (float64; e.g. '95.33')  - *meaning not documented here (see the files above / the code that writes it)*

### `results\tables\T0_S3_regular_fresh_cumulative_wide.csv`
- size 1 KB; modified 2026-10-13; rows 34
- columns / contents:
  - `unit` (str; e.g. 'AN')  - *meaning not documented here (see the files above / the code that writes it)*
  - `2024` (float64; e.g. '89.33')  - *meaning not documented here (see the files above / the code that writes it)*
  - `2025` (float64; e.g. '82.71')  - *meaning not documented here (see the files above / the code that writes it)*
  - `2026` (float64; e.g. '98.9')  - *meaning not documented here (see the files above / the code that writes it)*

### `results\tables\T10_malpractice_cases.csv`
- size 0 KB; modified 2026-10-13; rows 10
- columns / contents:
  - `year` (int64; e.g. '2017'): publication year
  - `scope` (str; e.g. 'main_exam')  - *meaning not documented here (see the files above / the code that writes it)*
  - `cases` (float64; e.g. '15.0')  - *meaning not documented here (see the files above / the code that writes it)*
  - `districts_with_cases` (int64; e.g. '7')  - *meaning not documented here (see the files above / the code that writes it)*

### `results\tables\T11_gender_state_workbooks.csv`
- size 1 KB; modified 2026-10-13; rows 11
- columns / contents:
  - `year` (int64; e.g. '2015'): publication year
  - `scope` (str; e.g. 'main_exam')  - *meaning not documented here (see the files above / the code that writes it)*
  - `boys_app` (float64; e.g. '403905.0')  - *meaning not documented here (see the files above / the code that writes it)*
  - `boys_pass` (float64; e.g. '331693.0')  - *meaning not documented here (see the files above / the code that writes it)*
  - `girls_app` (float64; e.g. '384537.0')  - *meaning not documented here (see the files above / the code that writes it)*
  - `girls_pass` (float64; e.g. '337287.0')  - *meaning not documented here (see the files above / the code that writes it)*
  - `boys_pct` (float64; e.g. '82.12')  - *meaning not documented here (see the files above / the code that writes it)*
  - `girls_pct` (float64; e.g. '87.71')  - *meaning not documented here (see the files above / the code that writes it)*
  - `gap_girls_minus_boys` (float64; e.g. '5.59')  - *meaning not documented here (see the files above / the code that writes it)*

### `results\tables\T11_urban_rural_state_workbooks.csv`
- size 1 KB; modified 2026-10-13; rows 11
- columns / contents:
  - `year` (int64; e.g. '2015'): publication year
  - `scope` (str; e.g. 'main_exam')  - *meaning not documented here (see the files above / the code that writes it)*
  - `rural_app` (float64; e.g. '444771.0')  - *meaning not documented here (see the files above / the code that writes it)*
  - `rural_pass` (float64; e.g. '384096.0')  - *meaning not documented here (see the files above / the code that writes it)*
  - `urban_app` (float64; e.g. '343671.0')  - *meaning not documented here (see the files above / the code that writes it)*
  - `urban_pass` (float64; e.g. '284884.0')  - *meaning not documented here (see the files above / the code that writes it)*
  - `rural_pct` (float64; e.g. '86.36')  - *meaning not documented here (see the files above / the code that writes it)*
  - `urban_pct` (float64; e.g. '82.89')  - *meaning not documented here (see the files above / the code that writes it)*

### `results\tables\T12_exploratory_school_markers.csv`
- size 1 KB; modified 2026-10-13; rows 10
- columns / contents:
  - `spec` (str; e.g. 'change 2023-24 (S1) on share_schools_100')  - *meaning not documented here (see the files above / the code that writes it)*
  - `n` (int64; e.g. '34')  - *meaning not documented here (see the files above / the code that writes it)*
  - `slope` (float64; e.g. '4.472')  - *meaning not documented here (see the files above / the code that writes it)*
  - `se` (float64; e.g. '31.204')  - *meaning not documented here (see the files above / the code that writes it)*
  - `p` (float64; e.g. '0.886')  - *meaning not documented here (see the files above / the code that writes it)*
  - `r2` (float64; e.g. '0.001')  - *meaning not documented here (see the files above / the code that writes it)*
  - `spearman` (float64; e.g. '-0.007')  - *meaning not documented here (see the files above / the code that writes it)*

### `results\tables\T13_posthoc_division_means.csv`
- size 0 KB; modified 2026-10-13; rows 4
- columns / contents:
  - `division` (str; e.g. 'Belagavi')  - *meaning not documented here (see the files above / the code that writes it)*
  - `p2019` (float64; e.g. '75.9')  - *meaning not documented here (see the files above / the code that writes it)*
  - `p2023` (float64; e.g. '85.16')  - *meaning not documented here (see the files above / the code that writes it)*
  - `p2024` (float64; e.g. '76.33')  - *meaning not documented here (see the files above / the code that writes it)*
  - `chg` (float64; e.g. '-8.83')  - *meaning not documented here (see the files above / the code that writes it)*
  - `rf2023` (float64; e.g. '88.16')  - *meaning not documented here (see the files above / the code that writes it)*
  - `rf2025` (float64; e.g. '67.8')  - *meaning not documented here (see the files above / the code that writes it)*
  - `rf_chg` (float64; e.g. '-20.36')  - *meaning not documented here (see the files above / the code that writes it)*

### `results\tables\T2_district_change_2023_2024.csv`
- size 3 KB; modified 2026-10-13; rows 34
- columns / contents:
  - `unit` (str; e.g. 'DA')  - *meaning not documented here (see the files above / the code that writes it)*
  - `district` (str; e.g. 'MADHUGIRI')  - *meaning not documented here (see the files above / the code that writes it)*
  - `division` (str; e.g. 'Bengaluru')  - *meaning not documented here (see the files above / the code that writes it)*
  - `pass_2019` (float64; e.g. '81.62')  - *meaning not documented here (see the files above / the code that writes it)*
  - `pass_2022` (float64; e.g. '95.18')  - *meaning not documented here (see the files above / the code that writes it)*
  - `pass_2023` (float64; e.g. '91.12')  - *meaning not documented here (see the files above / the code that writes it)*
  - `pass_2024_exam1` (float64; e.g. '62.44')  - *meaning not documented here (see the files above / the code that writes it)*
  - `change_2023_24` (float64; e.g. '-28.68')  - *meaning not documented here (see the files above / the code that writes it)*
  - `rise_2019_23` (float64; e.g. '9.5')  - *meaning not documented here (see the files above / the code that writes it)*
  - `rank_2023` (float64; e.g. '7.0')  - *meaning not documented here (see the files above / the code that writes it)*
  - `rank_2024` (float64; e.g. '29.0')  - *meaning not documented here (see the files above / the code that writes it)*
  - `candidates_2024` (float64; e.g. '12715.0')  - *meaning not documented here (see the files above / the code that writes it)*

### `results\tables\T3_placebo_slopes.csv`
- size 1 KB; modified 2026-10-13; rows 9
- columns / contents:
  - `pair` (str; e.g. '2014-2015')  - *meaning not documented here (see the files above / the code that writes it)*
  - `kind` (str; e.g. 'placebo')  - *meaning not documented here (see the files above / the code that writes it)*
  - `n` (int64; e.g. '34')  - *meaning not documented here (see the files above / the code that writes it)*
  - `mean_change` (float64; e.g. '0.346')  - *meaning not documented here (see the files above / the code that writes it)*
  - `sd_change` (float64; e.g. '5.889')  - *meaning not documented here (see the files above / the code that writes it)*
  - `sd_base` (float64; e.g. '4.88')  - *meaning not documented here (see the files above / the code that writes it)*
  - `slope` (float64; e.g. '-0.308')  - *meaning not documented here (see the files above / the code that writes it)*
  - `se` (float64; e.g. '0.149')  - *meaning not documented here (see the files above / the code that writes it)*
  - `p` (float64; e.g. '0.039')  - *meaning not documented here (see the files above / the code that writes it)*
  - `r2` (float64; e.g. '0.065')  - *meaning not documented here (see the files above / the code that writes it)*
  - `spearman` (float64; e.g. '-0.412')  - *meaning not documented here (see the files above / the code that writes it)*

### `results\tables\T4_alternative_baselines.csv`
- size 1 KB; modified 2026-10-13; rows 8
- columns / contents:
  - `spec` (str; e.g. 'A4a change 2023-24 on 2018-19 average le')  - *meaning not documented here (see the files above / the code that writes it)*
  - `n` (int64; e.g. '34')  - *meaning not documented here (see the files above / the code that writes it)*
  - `slope` (float64; e.g. '0.139')  - *meaning not documented here (see the files above / the code that writes it)*
  - `se` (float64; e.g. '0.185')  - *meaning not documented here (see the files above / the code that writes it)*
  - `p` (float64; e.g. '0.452')  - *meaning not documented here (see the files above / the code that writes it)*
  - `r2` (float64; e.g. '0.015')  - *meaning not documented here (see the files above / the code that writes it)*
  - `spearman` (float64; e.g. '0.062')  - *meaning not documented here (see the files above / the code that writes it)*
  - `spearman_p` (float64; e.g. '0.727')  - *meaning not documented here (see the files above / the code that writes it)*

### `results\tables\T4_leave_one_out.csv`
- size 1 KB; modified 2026-10-13; rows 34
- columns / contents:
  - `dropped` (str; e.g. 'BENGALURU NORTH')  - *meaning not documented here (see the files above / the code that writes it)*
  - `slope_A2` (float64; e.g. '-0.311')  - *meaning not documented here (see the files above / the code that writes it)*
  - `slope_A4c` (float64; e.g. '-0.701')  - *meaning not documented here (see the files above / the code that writes it)*

### `results\tables\T5_event_study_coefficients.csv`
- size 2 KB; modified 2026-10-13; rows 50
- columns / contents:
  - `spec` (str; e.g. 'top tercile of 2023 level')  - *meaning not documented here (see the files above / the code that writes it)*
  - `year` (int64; e.g. '2014'): publication year
  - `coef` (float64; e.g. '-8.042')  - *meaning not documented here (see the files above / the code that writes it)*
  - `se` (str; e.g. '1.934')  - *meaning not documented here (see the files above / the code that writes it)*

### `results\tables\T6_district_regular_fresh.csv`
- size 2 KB; modified 2026-10-13; rows 34
- columns / contents:
  - `unit` (str; e.g. 'QQ')  - *meaning not documented here (see the files above / the code that writes it)*
  - `district` (str; e.g. 'KALABURAGI')  - *meaning not documented here (see the files above / the code that writes it)*
  - `rf_2019` (float64; e.g. '75.22')  - *meaning not documented here (see the files above / the code that writes it)*
  - `rf_2023` (float64; e.g. '84.52')  - *meaning not documented here (see the files above / the code that writes it)*
  - `rf_2025_exam1` (float64; e.g. '42.43')  - *meaning not documented here (see the files above / the code that writes it)*
  - `rf_2026_exam1` (float64; e.g. '85.06')  - *meaning not documented here (see the files above / the code that writes it)*
  - `change_2023_25` (float64; e.g. '-42.08')  - *meaning not documented here (see the files above / the code that writes it)*
  - `change_2019_25` (float64; e.g. '-32.78')  - *meaning not documented here (see the files above / the code that writes it)*

### `results\tables\T6_regular_fresh_2023_2025_2026.csv`
- size 1 KB; modified 2026-10-13; rows 12
- columns / contents:
  - `spec` (str; e.g. 'change 2023-25 on 2023 level')  - *meaning not documented here (see the files above / the code that writes it)*
  - `n` (int64; e.g. '34')  - *meaning not documented here (see the files above / the code that writes it)*
  - `mean_change` (float64; e.g. '-21.078')  - *meaning not documented here (see the files above / the code that writes it)*
  - `slope` (float64; e.g. '-0.486')  - *meaning not documented here (see the files above / the code that writes it)*
  - `se` (float64; e.g. '0.342')  - *meaning not documented here (see the files above / the code that writes it)*
  - `p` (float64; e.g. '0.155')  - *meaning not documented here (see the files above / the code that writes it)*
  - `r2` (float64; e.g. '0.054')  - *meaning not documented here (see the files above / the code that writes it)*
  - `spearman` (float64; e.g. '-0.308')  - *meaning not documented here (see the files above / the code that writes it)*

### `results\tables\T7_management_district_cumulative.csv`
- size 1 KB; modified 2026-10-13; rows 6
- columns / contents:
  - `spec` (str; e.g. 'govt: change 2023 main -> 2024 cumulativ')  - *meaning not documented here (see the files above / the code that writes it)*
  - `n` (int64; e.g. '34')  - *meaning not documented here (see the files above / the code that writes it)*
  - `mean_change` (float64; e.g. '-2.842')  - *meaning not documented here (see the files above / the code that writes it)*
  - `slope` (float64; e.g. '-0.722')  - *meaning not documented here (see the files above / the code that writes it)*
  - `se` (float64; e.g. '0.149')  - *meaning not documented here (see the files above / the code that writes it)*
  - `p` (float64; e.g. '0.0')  - *meaning not documented here (see the files above / the code that writes it)*
  - `r2` (float64; e.g. '0.385')  - *meaning not documented here (see the files above / the code that writes it)*
  - `spearman` (float64; e.g. '-0.573')  - *meaning not documented here (see the files above / the code that writes it)*

### `results\tables\T7_management_state_workbooks.csv`
- size 0 KB; modified 2026-10-13; rows 11
- columns / contents:
  - `year` (int64; e.g. '2015'): publication year
  - `scope` (str; e.g. 'main_exam')  - *meaning not documented here (see the files above / the code that writes it)*
  - `aided` (float64; e.g. '83.26')  - *meaning not documented here (see the files above / the code that writes it)*
  - `govt` (float64; e.g. '83.14')  - *meaning not documented here (see the files above / the code that writes it)*
  - `unaided` (float64; e.g. '88.94')  - *meaning not documented here (see the files above / the code that writes it)*

### `results\tables\T8_subject_state.csv`
- size 1 KB; modified 2026-10-13; rows 11
- columns / contents:
  - `year` (int64; e.g. '2015'): publication year
  - `language_1` (float64; e.g. '96.57')  - *meaning not documented here (see the files above / the code that writes it)*
  - `language_2` (float64; e.g. '87.84')  - *meaning not documented here (see the files above / the code that writes it)*
  - `language_3` (float64; e.g. '87.47')  - *meaning not documented here (see the files above / the code that writes it)*
  - `mathematics` (float64; e.g. '90.6')  - *meaning not documented here (see the files above / the code that writes it)*
  - `science` (str; e.g. '')  - *meaning not documented here (see the files above / the code that writes it)*
  - `social_science` (str; e.g. '')  - *meaning not documented here (see the files above / the code that writes it)*

### `results\tables\T9_grade_distribution_workbooks.csv`
- size 1 KB; modified 2026-10-13; rows 11
- columns / contents:
  - `year` (int64; e.g. '2015'): publication year
  - `app` (float64; e.g. '788442.0')  - *meaning not documented here (see the files above / the code that writes it)*
  - `passed` (float64; e.g. '668980.0')  - *meaning not documented here (see the files above / the code that writes it)*
  - `A_plus` (float64; e.g. '27389.0')  - *meaning not documented here (see the files above / the code that writes it)*
  - `A` (float64; e.g. '77478.0')  - *meaning not documented here (see the files above / the code that writes it)*
  - `B_plus` (float64; e.g. '123321.0')  - *meaning not documented here (see the files above / the code that writes it)*
  - `B` (float64; e.g. '164081.0')  - *meaning not documented here (see the files above / the code that writes it)*
  - `C_plus` (float64; e.g. '170371.0')  - *meaning not documented here (see the files above / the code that writes it)*
  - `C` (float64; e.g. '106341.0')  - *meaning not documented here (see the files above / the code that writes it)*
  - `C_share_of_passes` (float64; e.g. '15.9')  - *meaning not documented here (see the files above / the code that writes it)*
  - `C_share_of_appeared` (float64; e.g. '13.49')  - *meaning not documented here (see the files above / the code that writes it)*

### `data\raw\` (summarised)
- 778 files, 134 MB. Raw downloads/caches as fetched on the stated dates; not individually listed. Check the code that fills it for the source URL.
