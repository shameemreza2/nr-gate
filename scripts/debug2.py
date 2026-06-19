import fitz, sys
sys.stdout.reconfigure(encoding="utf-8")

doc = fitz.open(r'D:\hsk3~5\新版HSK考试大纲1219.pdf')

# Dump pages 78-82 (around the 不客气 area) to see the full table structure
for pg in range(77, 83):
    page = doc[pg]
    lines = [l.strip() for l in page.get_text().splitlines() if l.strip()]
    print(f"\n====== PDF page {pg+1} ({len(lines)} tokens) ======")
    for i, l in enumerate(lines):
        print(f"  {i:3d}: {repr(l)}")
