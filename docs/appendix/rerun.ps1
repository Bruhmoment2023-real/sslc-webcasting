# rerun.ps1 - rebuild 04-sslc-webcasting from raw data, in order.   Usage:  powershell -File rerun.ps1            (dry run: checks inputs and syntax only)
#                                                          powershell -File rerun.ps1 -Run       (runs everything; slow, uses the network)
# Run one job at a time on this laptop. Nothing is installed or set machine-wide.
param([switch]$Run, [switch]$SkipPack, [switch]$SkipBiblio)
if (-not (Test-Path 'D:\')) { throw 'D: is missing - stop.' }
$Paper   = 'D:\Research-Publishing\04-sslc-webcasting'
$Biblio  = Join-Path $Paper 'bibliometrics'
$Kit     = 'D:\Research-Publishing\_tools\biblio-kit'
$KitPy   = 'D:\Research-Publishing\_tools\biblio-venv\Scripts\python.exe'
$PackPy  = 'D:\Research-Publishing\04-sslc-webcasting\.venv\Scripts\python.exe'
$Rscript = 'C:\Program Files\R\R-4.5.3\bin\Rscript.exe'
$env:PYTHONIOENCODING = 'utf-8'
$env:R_LIBS_USER = 'D:\Research-Publishing\_tools\R-lib;C:\Users\seans\AppData\Local\R\win-library\4.5'   # this process only
function Do-Step($Name, [scriptblock]$Cmd, $Check) {
    if ($Run) { Write-Host "== $Name"; & $Cmd; if ($LASTEXITCODE -ne 0) { throw "$Name failed ($LASTEXITCODE)" } }
    else { $ok = if ($Check) { Test-Path $Check } else { $true }; Write-Host ("[dry run] {0,-60} input/script present: {1}" -f $Name, $ok) }
}
# 1. the paper's own pipeline (numbered scripts in code\; see data\...\DATA_DICTIONARY or code\README.md for what each does and which need the network)
if (-not $SkipPack) {
  $steps = @(
    @{ Name = '00_inspect_workbooks.py'; Cmd = { & $PackPy 'D:\Research-Publishing\04-sslc-webcasting\code\00_inspect_workbooks.py' } }
    @{ Name = '01_dump_sheets.py'; Cmd = { & $PackPy 'D:\Research-Publishing\04-sslc-webcasting\code\01_dump_sheets.py' } }
    @{ Name = '02_pdf_text.py'; Cmd = { & $PackPy 'D:\Research-Publishing\04-sslc-webcasting\code\02_pdf_text.py' } }
    @{ Name = '03_render_pdf_pages.py'; Cmd = { & $PackPy 'D:\Research-Publishing\04-sslc-webcasting\code\03_render_pdf_pages.py' } }
    @{ Name = '04_news_text.py'; Cmd = { & $PackPy 'D:\Research-Publishing\04-sslc-webcasting\code\04_news_text.py' } }
    @{ Name = '05_openalex_search.py'; Cmd = { & $PackPy 'D:\Research-Publishing\04-sslc-webcasting\code\05_openalex_search.py' } }
    @{ Name = '06_crossref_search.py'; Cmd = { & $PackPy 'D:\Research-Publishing\04-sslc-webcasting\code\06_crossref_search.py' } }
    @{ Name = '07_verify_refs.py'; Cmd = { & $PackPy 'D:\Research-Publishing\04-sslc-webcasting\code\07_verify_refs.py' } }
    @{ Name = '10_build_district_tables.py'; Cmd = { & $PackPy 'D:\Research-Publishing\04-sslc-webcasting\code\10_build_district_tables.py' } }
    @{ Name = '11_validate_tables.py'; Cmd = { & $PackPy 'D:\Research-Publishing\04-sslc-webcasting\code\11_validate_tables.py' } }
    @{ Name = '12_build_panel.py'; Cmd = { & $PackPy 'D:\Research-Publishing\04-sslc-webcasting\code\12_build_panel.py' } }
    @{ Name = '13_build_school_taluk_tables.py'; Cmd = { & $PackPy 'D:\Research-Publishing\04-sslc-webcasting\code\13_build_school_taluk_tables.py' } }
    @{ Name = '20_analysis.py'; Cmd = { & $PackPy 'D:\Research-Publishing\04-sslc-webcasting\code\20_analysis.py' } }
    @{ Name = '21_posthoc.py'; Cmd = { & $PackPy 'D:\Research-Publishing\04-sslc-webcasting\code\21_posthoc.py' } }
  )
  foreach ($s in $steps) {
    if ($Run) { Write-Host "== $($s.Name)"; & $s.Cmd }
    else { & $PackPy -I -m py_compile (Join-Path 'D:\Research-Publishing\04-sslc-webcasting\code' $s.Name); Write-Host ("[dry run] {0,-40} compiles: {1}" -f $s.Name, ($LASTEXITCODE -eq 0)) }
  }
}
# 2. the literature map (cached responses are reused; delete D:\Research-Publishing\_tools\biblio-cache to force a fresh pull)
if (-not $SkipBiblio) {
  Do-Step 'bibliometrics pipeline' { & $KitPy "$Kit\pipeline.py" $Biblio search enrich snowball refs master } "$Biblio\config.json"
  Do-Step 'bibliometrix (R)'       { & $Rscript "$Kit\R\bibliometrix_analysis.R" $Biblio } "$Kit\R\bibliometrix_analysis.R"
  Do-Step 'python figures'         { & $KitPy "$Kit\figures.py" $Biblio } "$Kit\figures.py"
  Do-Step 'burst detection'        { & $KitPy "$Kit\depth_networks.py" $Biblio } "$Kit\depth_networks.py"
  Do-Step 'evidence + PDFs'        { & $KitPy "$Kit\evidence_auto.py" $Biblio 48; & $KitPy "$Kit\pdfs.py" $Biblio download; & $KitPy "$Kit\pdfs.py" $Biblio evidence } "$Kit\pdfs.py"
  Do-Step 'reading notes'          { & $KitPy "$Kit\depth_notes.py" $Paper } "$Kit\depth_notes.py"
  Do-Step 'citation library'       { & $KitPy "$Kit\depth_citations.py" $Paper } "$Kit\depth_citations.py"
  Do-Step 'docs'                   { & $KitPy "$Kit\docs.py" $Biblio } "$Kit\docs.py"
}
Write-Host ($(if ($Run) { 'done' } else { 'dry run finished - re-run with -Run to execute' }))
