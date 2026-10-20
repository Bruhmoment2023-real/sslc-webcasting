"""List every sheet of every raw workbook with its size and first rows. Read-only."""
import sys, glob, os, openpyxl
sys.stdout.reconfigure(encoding='utf-8')
raw = sys.argv[1]; nrows = int(sys.argv[2]) if len(sys.argv) > 2 else 6
pat = sys.argv[3] if len(sys.argv) > 3 else '*.xlsx'
for f in sorted(glob.glob(os.path.join(raw, pat))):
    try:
        wb = openpyxl.load_workbook(f, read_only=True, data_only=True)
    except Exception as e:
        print('##', os.path.basename(f), 'ERROR', e); continue
    print('##', os.path.basename(f))
    for ws in wb.worksheets:
        print('  --', repr(ws.title), ws.max_row, ws.max_column)
        for i, row in enumerate(ws.iter_rows(values_only=True)):
            if i >= nrows: break
            cells = [str(c)[:28] for c in row if c is not None]
            if cells: print('      ', ' | '.join(cells)[:260])
