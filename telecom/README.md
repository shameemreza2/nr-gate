# Telecom Seed Deck — private draft

Target: **200 terms** covering LTE/5G/IoT + Shenzhen internship context.
Built during Phase 2 flex hours (≈ Day 0–35, parallel to 2.0 main track).

This branch is **private** (repo: `telecom-seed`). The public plan references the
deck count in `tracker.md` but contains none of the actual content.

---

## Files

| File | What it is |
|---|---|
| `deck.md` | The 200-term table — EN term, 中文, category, usage note. Fill as you go. |
| `interview-prep.md` | Interview question bank + self-test protocol for the Shenzhen internship pitch. |

---

## Deck build rules

1. **One term = one row** in `deck.md`. Fill all four columns before logging it as done.
2. **Category first** — work a full category block before jumping to the next, so SRS review clusters by topic.
3. **Chinese column is mandatory.** If you don't know the Chinese term yet, mark it `?` and flag for lookup — don't leave it blank.
4. **Usage note = one sentence showing the term in a real context** (from a datasheet, paper abstract, or spec). Not a dictionary definition.
5. Log the running count in `tracker.md` (Phase 2 `Deck cum` column) each day you add terms.

---

## Category targets (200 total)

| Category | Target | Done |
|---|---|---|
| RF / Radio fundamentals | 25 | 0 |
| LTE / 4G core | 30 | 0 |
| 5G NR / SA / NSA | 35 | 0 |
| IoT / NB-IoT / eMTC | 25 | 0 |
| Protocol stack (L1–L3) | 25 | 0 |
| Network architecture | 20 | 0 |
| Operations / KPIs | 20 | 0 |
| Chinese telecom terms (业务词) | 20 | 0 |
| **Total** | **200** | **0** |

---

## How to commit a batch

```
git add telecom/deck.md tracker.md
git commit -m "telecom: +N terms (category) | deck cum X"
git push telecom telecom-draft
```

No gate hook on this branch — it's a draft. Commit freely.
