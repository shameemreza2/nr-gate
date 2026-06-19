import fitz
import sys

sys.stdout.reconfigure(encoding='utf-8')

doc = fitz.open(r'D:\hsk3~5\新版HSK考试大纲1219.pdf')
print(f'Pages: {doc.page_count}')

# Sample several pages across the doc to understand vocab list structure
sample_pages = [0, 1, 2, 3, 4, 50, 100, 150, 200]
for i in sample_pages:
    if i < doc.page_count:
        page = doc[i]
        print(f'\n=== PAGE {i+1} ===')
        print(page.get_text()[:1200])
