"""
Extract HSK vocabulary from 新版HSK考试大纲1219.pdf and generate:
  - hsk_anki.txt   : Anki tab-separated import (UTF-8 BOM)
  - hsk_pleco.xml  : Pleco flashcard XML, categories by HSK level

Syllabus: 中外语言交流合作中心, 2025-11, effective 2026-07
Official cumulative word counts: HSK1=300, HSK2=500, HSK3=1000, HSK4=2000, HSK5=3600
"""

import fitz
import re
import sys
from pathlib import Path
from collections import Counter, defaultdict

sys.stdout.reconfigure(encoding="utf-8")

PDF_PATH = r"D:\hsk3~5\新版HSK考试大纲1219.pdf"
OUT_DIR  = Path(r"D:\hsk3~5\decks")
OUT_DIR.mkdir(exist_ok=True)

# ── 1. Extract raw tokens from all pages ─────────────────────────────────────

doc = fitz.open(PDF_PATH)
raw_tokens = []
for page_num in range(doc.page_count):
    for line in doc[page_num].get_text().splitlines():
        t = line.strip()
        if t:
            raw_tokens.append(t)

# ── 2. Filtering ─────────────────────────────────────────────────────────────

SKIP = {
    "序号", "等级", "词语", "拼音", "词性",
    "汉考国际", "际", "汉",
    "---------------------------------------------------------------",
    "词汇大纲", "话题大纲", "任务大纲", "语法大纲",
    "认读字", "书写字",
    "HSK考试大纲", "Syllabus for the Chinese Proficiency Test",
    "中文水平考试", "中外语言交流合作中心", "发布", "实施",
    "目录", "汉考国际",
}

def is_watermark_or_header(s):
    if s in SKIP:
        return True
    # Pure ASCII decorators, page section markers
    if re.match(r"^-+$", s):
        return True
    # PDF section markers like "HSK（一级）词汇" etc. but keep actual Chinese entries
    return False

tokens = [t for t in raw_tokens if not is_watermark_or_header(t)]

# ── 3. Classification helpers ─────────────────────────────────────────────────

def is_seq_num(s):
    """Serial number: integer in range [1, 20000]"""
    return s.isdigit() and 1 <= int(s) <= 20000

def is_level(s):
    """HSK level field: '1' … '6', '7—9', '3（7-9）', etc."""
    return bool(re.match(r"^\d[\d—\-（）\(\)]*$", s)) and len(s) <= 12

def is_chinese_word(s):
    """Has at least one CJK character"""
    return bool(re.search(r"[一-鿿]", s))

def is_pinyin(s):
    """Pinyin: ASCII letters + tone marks, no CJK"""
    return (
        bool(re.search(r"[a-züāáǎàūúǔùīíǐìēéěèōóǒòǖǘǚǜ]", s, re.IGNORECASE))
        and not re.search(r"[一-鿿]", s)
    )

# POS tokens contain CJK POS abbreviation characters
_POS_CHARS = set("名动形副代介连助量数叹声缀")

def is_pos(s):
    """Part-of-speech field: contains at least one known POS character"""
    return any(c in _POS_CHARS for c in s)

def extract_base_level(level_str):
    m = re.match(r"(\d+)", level_str)
    return int(m.group(1)) if m else None

# ── 4. Parse entries ──────────────────────────────────────────────────────────
# Each entry is: seq  level  word  pinyin  [pos]
# Some entries (formulaic phrases like 你好, 不客气) have no POS field.
# Page numbers (e.g. '77', '78') appear as lone integers between entries.
# Strategy: match on (seq, level, CJK-word, pinyin); then consume POS if present.

entries = []
i = 0
n = len(tokens)

while i < n - 3:
    t0, t1, t2, t3 = tokens[i], tokens[i+1], tokens[i+2], tokens[i+3]

    if (
        is_seq_num(t0)
        and is_level(t1)
        and is_chinese_word(t2)
        and is_pinyin(t3)
    ):
        level = extract_base_level(t1)

        # Consume POS only if the next token looks like one
        if i + 4 < n and is_pos(tokens[i + 4]):
            pos     = tokens[i + 4]
            advance = 5
        else:
            pos     = ""   # formulaic phrase / missing POS
            advance = 4

        entries.append({
            "seq":       int(t0),
            "level":     level,
            "level_raw": t1,
            "word":      t2,
            "pinyin":    t3,
            "pos":       pos,
        })
        i += advance
        continue

    i += 1

print(f"Extracted {len(entries)} vocabulary entries")

by_level = Counter(e["level"] for e in entries)
cumulative = 0
for lv in sorted(k for k in by_level if k):
    cumulative += by_level[lv]
    print(f"  HSK {lv}: {by_level[lv]:4d}  (cumulative {cumulative})")

# Sample entries without POS
no_pos = [e for e in entries if not e["pos"]]
print(f"\nEntries with no POS ({len(no_pos)} total, sample):")
for e in no_pos[:10]:
    print(f"  seq={e['seq']:5d}  lv={e['level']}  {e['word']}  {e['pinyin']}")

# ── 5. POS → short English label ─────────────────────────────────────────────

POS_MAP = {
    "名": "n.",    "动": "v.",    "形": "adj.",   "副": "adv.",
    "代": "pron.", "介": "prep.", "连": "conj.",  "助": "part.",
    "量": "meas.", "数": "num.",  "叹": "interj.","拟声": "ono.",
    "前缀": "pref.", "后缀": "suf.",
}

def pos_en(pos_zh):
    if not pos_zh:
        return ""
    parts = re.split(r"[、,，/]", pos_zh)
    labels = []
    for p in parts:
        core = re.sub(r"[（）()\d]", "", p).strip()
        labels.append(POS_MAP.get(core, core))
    return "/".join(labels)

# ── 6. Write Anki import file ─────────────────────────────────────────────────
# Fields: Word | Pinyin | POS | Level | (Tags column)
# Anki import: File > Import > select this .txt, separator = Tab
# Suggested note type: "HSK" with fields: Word, Pinyin, POS, Level
# Card front: {{Word}}   back: {{Pinyin}}<br>{{POS}}<br>Level {{Level}}

anki_path = OUT_DIR / "hsk_anki.txt"
with open(anki_path, "w", encoding="utf-8-sig", newline="\n") as f:
    f.write("#separator:tab\n")
    f.write("#html:false\n")
    f.write("#tags column:5\n")
    f.write("#columns:Word\tPinyin\tPOS\tLevel\tTags\n")
    for e in entries:
        word   = e["word"]
        pinyin = e["pinyin"]
        pos    = pos_en(e["pos"])
        level  = e["level"] if e["level"] else ""
        tag    = f"HSK{level}" if level else "HSK_unknown"
        f.write(f"{word}\t{pinyin}\t{pos}\t{level}\t{tag}\n")

print(f"\nAnki  → {anki_path}  ({len(entries)} notes)")

# ── 7. Write Pleco flashcard XML ──────────────────────────────────────────────
# Import in Pleco: Flashcards > Import > select hsk_pleco.xml
# Pleco auto-looks up definitions from its built-in dictionaries (CC-CEDICT etc.)
# pron field: Pleco hypy format with tone marks (matches syllabus pinyin exactly)
# defn field: lightweight "(pos) [HSK N]" — Pleco shows its own dict def above this

PLECO_CATS = {
    1: "HSK1 (新版2026)", 2: "HSK2 (新版2026)", 3: "HSK3 (新版2026)",
    4: "HSK4 (新版2026)", 5: "HSK5 (新版2026)", 6: "HSK6 (新版2026)",
    7: "HSK7-9 (新版2026)",
}

by_level_entries = defaultdict(list)
for e in entries:
    lv = e["level"] or 0
    if lv in (8, 9):
        lv = 7
    by_level_entries[lv].append(e)

pleco_path = OUT_DIR / "hsk_pleco.xml"
with open(pleco_path, "w", encoding="utf-8") as f:
    f.write('<?xml version="1.0" encoding="UTF-8"?>\n')
    f.write('<!DOCTYPE plecoflash PUBLIC "-//Pleco//DTD Pleco 1.0//EN" '
            '"http://www.pleco.com/dtd/plecoflash.dtd">\n')
    f.write('<plecoflash version="2.0">\n<cards>\n')

    for lv in sorted(by_level_entries):
        cat = PLECO_CATS.get(lv, f"HSK{lv} (新版2026)")
        for e in by_level_entries[lv]:
            pos_label = f"({e['pos']}) " if e["pos"] else ""
            defn = f"{pos_label}[HSK {lv}]"
            f.write('  <card>\n    <entry>\n')
            f.write(f'      <headword charset="sc">{e["word"]}</headword>\n')
            f.write(f'      <pron type="hypy" tones="marks">{e["pinyin"]}</pron>\n')
            f.write(f'      <defn>{defn}</defn>\n')
            f.write('    </entry>\n')
            f.write(f'    <cat>{cat}</cat>\n')
            f.write('  </card>\n')

    f.write('</cards>\n</plecoflash>\n')

print(f"Pleco → {pleco_path}")
for lv in sorted(by_level_entries):
    print(f"  {PLECO_CATS.get(lv, lv)}: {len(by_level_entries[lv])} cards")

print("\nDone.")
