"""Dump every sheet of every raw workbook to a pipe-delimited text file (one per sheet)
so the layouts can be read and checked by eye. Usage: python 01_dump_sheets.py RAW_DIR OUT_DIR"""
import sys, glob, os, re, openpyxl
raw, out = sys.argv[1], sys.argv[2]
os.makedirs(out, exist_ok=True)
for f in sorted(glob.glob(os.path.join(raw, '*.xlsx'))):
    stem = os.path.splitext(os.path.basename(f))[0]
    try:
        wb = openpyxl.load_workbook(f, read_only=True, data_only=True)
    except Exception as e:
        print('ERROR', f, e); continue
    for ws in wb.worksheets:
        name = re.sub(r'[^A-Za-z0-9_\-]+', '_', ws.title)
        with open(os.path.join(out, f'{stem}__{name}.txt'), 'w', encoding='utf-8') as fh:
            for row in ws.iter_rows(values_only=True):
                if any(c is not None for c in row):
                    fh.write('|'.join('' if c is None else str(c).replace('\n', ' ').strip() for c in row) + '\n')
    print(stem, len(wb.worksheets))
