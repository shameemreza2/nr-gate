# Telecom Deck — private draft

Target: **700 terms** across three levels covering LTE/5G/IoT + Shenzhen internship context.
Built during Phase 2 flex hours (≈ Day 0–55), parallel to the HSK3 main track.

This branch is **private** (repo: `telecom-seed`). The public plan references the
deck count in `tracker.md` but contains none of the actual content.

---

## Files

| File | Deck name | Cards | When to start |
|---|---|---|---|
| `anki-import.txt` | Telecom Seed Deck | 200 | Phase 2 Day 0 |
| `anki-intermediate.txt` | Telecom Intermediate | 250 | Phase 2 Day 36 (after seed done) |
| `anki-advanced.txt` | Telecom Advanced | 250 | Phase 2 Day 49 (after intermediate done) |
| `deck.md` | Reference table (seed terms only) | 200 | — |
| `interview-prep.md` | Interview Q&A + self-test protocol | — | Week 2+ |

---

## Pacing plan

| Milestone | Target day | Date | Deck cum |
|---|---|---|---|
| Seed deck done | Day 35 | Mon 12 Oct | 200 |
| Intermediate done | Day 48 | Sun 25 Oct | 450 |
| Advanced done | Day 61+ | post-exam | 700 |

**Exam-week rule:** freeze new telecom cards from Day 55 (Sun 1 Nov) onward.
If advanced is not finished by Day 55, pick up after the Nov 7 exam.
The goal is to cover all three levels — advanced is only deferred, not skipped.

Daily pace during flex time: ~20 new cards/day + Anki SRS review of the existing deck.

---

## Level summary

| Level | File | Categories | Focus |
|---|---|---|---|
| Seed | `anki-import.txt` | RF, LTE, 5G, IoT, Protocol, Architecture, KPI, 业务词 | Foundation vocabulary for any telecom interview |
| Intermediate | `anki-intermediate.txt` | Advanced LTE, 5G NR advanced, Transport/sync, OSS/BSS, Security, Testing, QoS, HetNet, 中文 intermediate, Business | Depth for technical discussions and system design questions |
| Advanced | `anki-advanced.txt` | O-RAN/RIC, 5G-Advanced Rel-17/18, Network AI/ML, V2X/sidelink, Private networks, IIoT, 6G/IMT-2030, Signal processing, Advanced 中文 | Research-level topics for senior interviews and paper reading |

---

## How to commit a batch

```
git add telecom/ tracker.md
git commit -m "telecom: +N terms (level/category) | deck cum X"
git push telecom telecom-draft
```

No gate hook on this branch — it's a draft. Commit freely.
