import fitz, re, sys
sys.stdout.reconfigure(encoding="utf-8")

doc = fitz.open(r'D:\hsk3~5\新版HSK考试大纲1219.pdf')

# Find "不客气" in the raw text and show surrounding context
target = "不客气"
for page_num in range(doc.page_count):
    text = doc[page_num].get_text()
    if target in text:
        lines = text.splitlines()
        for j, line in enumerate(lines):
            if target in line:
                start = max(0, j-5)
                end = min(len(lines), j+10)
                print(f"Page {page_num+1}, line {j}:")
                for k in range(start, end):
                    print(f"  [{k}] {repr(lines[k])}")
                print()
        break

# Also dump a page that straddles a boundary (e.g., around entry 300)
# Find where HSK1 ends roughly
print("\n--- Page 57 raw (likely near HSK1/HSK2 boundary) ---")
for i in [56, 57, 58]:
    page = doc[i]
    lines = [l.strip() for l in page.get_text().splitlines() if l.strip()]
    print(f"\nPage {i+1} ({len(lines)} lines):")
    for line in lines[:60]:
        print(f"  {repr(line)}")
