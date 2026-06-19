# Graph Report - D:/hsk3~5  (2026-06-19)

## Corpus Check
- 0 files · ~99,999 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 421 nodes · 521 edges · 24 communities (23 shown, 1 thin omitted)
- Extraction: 87% EXTRACTED · 13% INFERRED · 0% AMBIGUOUS · INFERRED: 68 edges (avg confidence: 0.83)
- Token cost: 0 input · 0 output

## Community Hubs (Navigation)
- [[_COMMUNITY_Phase 1 Tracker — Daily Gate Log|Phase 1 Tracker — Daily Gate Log]]
- [[_COMMUNITY_2026-06-19-hvpt-mandarin-design.|2026-06-19-hvpt-mandarin-design.]]
- [[_COMMUNITY_test_hvpt_engine.py|test_hvpt_engine.py]]
- [[_COMMUNITY_Day 3 — Retroflex zh ch sh r + D|Day 3 — Retroflex zh ch sh r + D]]
- [[_COMMUNITY_hvpt_engine.py|hvpt_engine.py]]
- [[_COMMUNITY_Day 22 — Stage B Sprint Start|Day 22 — Stage B Sprint Start]]
- [[_COMMUNITY_Phase 2 Engine — HSK3 2.0 + HSKK|Phase 2 Engine — HSK3 2.0 + HSKK]]
- [[_COMMUNITY_Day 26 — 了 Aspect Particle + Rat|Day 26 — 了 Aspect Particle + Rat]]
- [[_COMMUNITY_Day 13 — Week-2 Gate Lock Tone|Day 13 — Week-2 Gate: Lock Tone ]]
- [[_COMMUNITY_weights|weights]]
- [[_COMMUNITY_Day 14 — Climb Toward 95 (Week 3|Day 14 — Climb Toward 95 (Week 3]]
- [[_COMMUNITY_hvpt.py|hvpt.py]]
- [[_COMMUNITY_Day 4 — Deload Consolidate Week|Day 4 — Deload: Consolidate Week]]
- [[_COMMUNITY_build_decks.py|build_decks.py]]
- [[_COMMUNITY_hvpt_config.json|hvpt_config.json]]
- [[_COMMUNITY_Day 28 — Time and Dates|Day 28 — Time and Dates]]
- [[_COMMUNITY_Day 37 — 60-Second Mandarin Self|Day 37 — 60-Second Mandarin Self]]
- [[_COMMUNITY_Day 7 — Tone Pairs Begin (Week 2|Day 7 — Tone Pairs Begin (Week 2]]
- [[_COMMUNITY_Day 19 — Pre-Unlock Push|Day 19 — Pre-Unlock Push]]
- [[_COMMUNITY_Vocab 300 Floor (Day 21)|Vocab 300 Floor (Day 21)]]

## God Nodes (most connected - your core abstractions)
1. `Phase 1 Tracker — Daily Gate Log` - 20 edges
2. `2026-06-19-hvpt-mandarin-design.md — HVPT Design Spec` - 16 edges
3. `hvpt_engine.py — HVPT Pure Logic Engine` - 15 edges
4. `phase1/README.md — Phase 1 Sprint Parameters` - 13 edges
5. `Phase 2 Engine — HSK3 2.0 + HSKK Sprint` - 13 edges
6. `Build Output v3 — Clean UTF-8 (10994 vocab entries)` - 12 edges
7. `main()` - 8 edges
8. `hvpt.py — HVPT Tone Trainer Runner` - 8 edges
9. `Day 22 — Stage B Sprint Start` - 8 edges
10. `Day 4 — Deload: Consolidate Week-1 Initials` - 7 edges

## Surprising Connections (you probably didn't know these)
- `make_alt_corpus.py — Edge-TTS Alt Corpus Generator` --semantically_similar_to--> `Tone Perfect Corpus (MSU)`  [INFERRED] [semantically similar]
  scripts/make_alt_corpus.py → docs/specs/2026-06-19-hvpt-mandarin-design.md
- `build_decks.py — HSK PDF Extractor` --shares_data_with--> `hsk_anki.txt — Anki Import File`  [EXTRACTED]
  scripts/build_decks.py → decks/hsk_anki.txt
- `build_decks.py — HSK PDF Extractor` --shares_data_with--> `hsk_pleco.xml — Pleco Flashcard XML`  [EXTRACTED]
  scripts/build_decks.py → decks/hsk_pleco.xml
- `新版HSK考试大纲1219.pdf — HSK Syllabus PDF` --references--> `debug_parse.py — Token Context Debugger`  [EXTRACTED]
  新版HSK考试大纲1219.pdf → scripts/debug_parse.py
- `新版HSK考试大纲1219.pdf — HSK Syllabus PDF` --references--> `peek_pdf.py — PDF Structure Inspector`  [EXTRACTED]
  新版HSK考试大纲1219.pdf → scripts/peek_pdf.py

## Import Cycles
- None detected.

## Hyperedges (group relationships)
- **HVPT Core System — Runner, Engine, Config** — hvpt_runner, hvpt_engine, hvpt_config [EXTRACTED 1.00]
- **Corpus Swap Workflow — Alt, Test, Official** — make_alt_corpus, make_test_corpus, corpus_tone_perfect_dir [EXTRACTED 0.95]
- **PDF Debugging Cluster — peek, debug2, debug_parse** — peek_pdf_script, debug2_script, debug_parse_script [INFERRED 0.80]
- **Week 1 Stage A: Initials and Pinyin Foundation (Days 2-6)** — day02_card, day03_card, day04_card, day05_card, day06_card [EXTRACTED 0.95]
- **Week 2 Stage A: Tone-Pair Identification Progression (Days 7-13)** — day07_card, day08_card, day09_card, day10_card, day11_card, day12_card, day13_card [EXTRACTED 0.95]
- **Week 3 Stage A: Climb to 92% and Vocab Unlock (Days 14-20)** — day14_card, day15_card, day16_card, day17_card, day18_card, day19_card, day20_card [EXTRACTED 0.95]
- **Stage B Grammar Ramp: Aspect Particles and Verb Patterns (Days 26–34)** — day26_le_aspect, day33_guo_aspect, day34_resultative_verbs, day35_ba_construction, day27_modals, day30_progressive [INFERRED 0.82]
- **Weekly Deload Cycle: No-New-Words Tone Audit Days (Days 25, 32)** — day25_deload_week4, day32_deload_week5, deload_pattern [EXTRACTED 1.00]
- **Tone Gate Escalation Stages: 95% → 96% → 97% Terminal (Days 21–33)** — day21_tone_pair_gate, day22_tone_gate_95, day27_tone_gate_96, day33_tone_gate_97_terminal, day36_gate_sentence_level_tones [INFERRED 0.88]
- **HSK Level Vocabulary Boundaries (1–4)** — tracker_level_hsk1_300, tracker_level_hsk2_500, tracker_level_hsk3_1000, tracker_level_hsk4_2000 [EXTRACTED 1.00]
- **Phase 1 Vocab Completion Milestones** — tracker_day20_hsk1_done, tracker_day29_hsk2_done, tracker_day44_hsk3_vocab_done, tracker_day47_fly_ready [EXTRACTED 1.00]
- **Build Script Output Files (v1, v2, v3)** — build_out_build_out, build_out2_build_out2, build_out3_build_out3 [INFERRED 0.85]

## Communities (24 total, 1 thin omitted)

### Community 0 - "Phase 1 Tracker — Daily Gate Log"
Cohesion: 0.05
Nodes (48): Build Output v2 (10994 vocab entries extracted), Entries with No POS Tag (495 total in v2 build), Build Output v3 — Clean UTF-8 (10994 vocab entries), HSK 1 Boundary — 300 words (v3 build), HSK 2 Boundary — 500 words cumulative (v3 build), HSK 3 Boundary — 1000 words cumulative (v3 build), HSK 4 Boundary — 1999 words cumulative (v3 build), HSK 5 Boundary — 3596 words cumulative (v3 build) (+40 more)

### Community 1 - "2026-06-19-hvpt-mandarin-design."
Cohesion: 0.09
Nodes (41): hsk_anki.txt — Anki Import File, 新版HSK考试大纲1219.pdf — HSK Syllabus PDF, hsk_pleco.xml — Pleco Flashcard XML, build_decks.py — HSK PDF Extractor, Alt Corpus — Edge-TTS zh-CN TTS, Bangla-L1 T2↔T3 Hardest Pair, Day-0 Baseline Anchor Row, 4×4 Tone Confusion Matrix (+33 more)

### Community 2 - "test_hvpt_engine.py"
Cohesion: 0.07
Nodes (16): _make_corpus(), Helper: build fake corpus list without real files., _sample_gates(), _sample_scores(), test_baseline_exists_ignores_day0_non_baseline(), test_baseline_exists_no_baseline_row(), test_baseline_exists_true(), test_build_trial_set_count() (+8 more)

### Community 3 - "Day 3 — Retroflex zh ch sh r + D"
Cohesion: 0.07
Nodes (33): Concept: Bangla-L1 Learner Error Profile, Concept: Multi-Speaker Generalisation, Concept: Retroflex vs Dental Minimal-Pair Drill, Concept: T2↔T3 Dedicated Subtest, Concept: Tone-3 Sandhi (T3+T3 → T2+T3), Day 3 — Retroflex zh ch sh r + Dentals z c s, Day 3 Hard Gate: Single-tone ID ≥78% and Retroflex/Dental ≥70%, Day 3 Rationale: Retroflex is documented #1 initials error for Bangla-L1 (+25 more)

### Community 4 - "hvpt_engine.py"
Cohesion: 0.09
Nodes (25): Path, baseline_exists(), build_trial_set(), check_gates(), format_csv_row(), format_tracker_line(), load_corpus(), parse_filename() (+17 more)

### Community 5 - "Day 22 — Stage B Sprint Start"
Cohesion: 0.08
Nodes (26): Rationale: 95% Gate Protects Every Word Added Next, Stage-B Scaling Deck Build (Day 21), T2↔T3 ≥92% Gate (Day 21), Tone-Pair ID ≥95% Hard Gate (Day 21), Day 21 — Unlock Day, Grammar: 是/有/在 Basic Sentences, 30 New Words ≥85% Retention Gate (Day 22), Day 22 — Stage B Sprint Start (+18 more)

### Community 6 - "Phase 2 Engine — HSK3 2.0 + HSKK"
Cohesion: 0.10
Nodes (26): 4-slot skim 目的/方法/结果/结论 + frame phrases, Verified: 2026 exam = HSK 2.0 not 3.0, Gate-driven: slip Dec13 / pull-forward Oct17, 150 书写字 over-prep (3.0 hedge), HSKK 初级: 27 items / 100 / pass 60, SRS floor: 1000 vocab + tones >=97% held, Day 41: 150 first-pass done, Day 61: EXAM (Nov 7) (+18 more)

### Community 7 - "Day 26 — 了 Aspect Particle + Rat"
Cohesion: 0.10
Nodes (22): Grammar: 了 Completed Action / Change of State, Day 26 — 了 Aspect Particle + Rate Increase to 35/day, Rate Step-Up: 35 New Words/Day (Day 26), Vocab Target 425 (Day 26), Grammar: 想/要/会/能 + Verb, Day 27 — Modal Verbs 想/要/会/能, Tone Gate ≥96% (Day 27 — Terminal Target Nudge), Vocab Target 460 (Day 27) (+14 more)

### Community 8 - "Day 13 — Week-2 Gate: Lock Tone "
Cohesion: 0.13
Nodes (21): Concept: Single-Tone Identification (HVPT), Concept: Vocab Unlock (after tone gate cleared), Concept: Week Gate (blocks start of next week), Day 2 — Initials g k h + j q x (Palatals), Day 2 Hard Gate: Single-tone ID ≥75%, Day 2 Study Blocks (~5.5h), Day 2 Vocab Target: 25 words, Day 6 — Compound Finals + Week-1 Gate (+13 more)

### Community 9 - "weights"
Cohesion: 0.10
Nodes (21): T1, T2, T3, T4, T1, T2, T3, T4 (+13 more)

### Community 10 - "Day 14 — Climb Toward 95 (Week 3"
Cohesion: 0.12
Nodes (19): Day 14 — Climb Toward 95 (Week 3), Day 14 Hard Gate: Pair ID ≥86% and T2↔T3 ≥80% (new speakers), Day 14 Rationale: Literature says ~90% reachable around this point; pushing past it, Day 14 Study Blocks (~5.5h), Day 14 Vocab Target: 215 words, Day 15 — Disyllabic-Word Tones, Day 15 Hard Gate: Pair ID ≥88% and T2↔T3 ≥82%, Day 15 Study Blocks (~5.5h) (+11 more)

### Community 11 - "hvpt.py"
Cohesion: 0.19
Nodes (15): append_csv(), append_tracker(), flag_retake_in_csv(), get_keypress(), load_config(), main(), play_audio(), print_end_report() (+7 more)

### Community 12 - "Day 4 — Deload: Consolidate Week"
Cohesion: 0.19
Nodes (15): Concept: Deload Day (no new material, ~3h), SRS Floor 20 min/day Non-Negotiable Rule, Day 4 — Deload: Consolidate Week-1 Initials, Day 4 Hard Gate: Pinyin Dictation ≥80%, Day 4 Rationale: Spacing beats bingeing — deload on purpose, Day 4 Study Blocks (~3h, deload), Day 4 Vocab Target: 40 words (no new), Day 11 — Deload: Consolidate Tone Pairs (+7 more)

### Community 13 - "build_decks.py"
Cohesion: 0.13
Nodes (11): is_chinese_word(), is_level(), is_pinyin(), is_pos(), is_seq_num(), Extract HSK vocabulary from 新版HSK考试大纲1219.pdf and generate:   - hsk_anki.txt   :, Serial number: integer in range [1, 20000], HSK level field: '1' … '6', '7—9', '3（7-9）', etc. (+3 more)

### Community 14 - "hvpt_config.json"
Cohesion: 0.13
Nodes (14): corpus_path, feedback_pause_ms, gate, flyday_overall, flyday_t2t3, unlock_overall, unlock_t2t3, log_path (+6 more)

### Community 15 - "Day 28 — Time and Dates"
Cohesion: 0.18
Nodes (12): Grammar: Time Words + Word Order (Time Before Verb), Day 28 — Time and Dates, Vocab Target 495 (Day 28), Grammar: 在 + Place; Direction/Position Words 上/下/里/外/前/后, Day 29 — Locations and Directions, Vocab Target 530 (Day 29), Grammar: 正在/在…呢 Ongoing Action, Day 30 — Progressive 在…呢 (+4 more)

### Community 16 - "Day 37 — 60-Second Mandarin Self"
Cohesion: 0.29
Nodes (7): Gate: Written 60-Second Self-Intro with Tones Marked (Day 37), Self-Intro as Phase-2 Seed / Supervisor-Meeting Pitch, Day 37 — 60-Second Mandarin Self-Introduction Draft, Vocab Target 790 (Day 37), Gate: ≥70% Comprehension on Fresh HSK-3 Listening Passage (Day 38), Day 38 — Listening at HSK-3 Speed, Vocab Target 830 (Day 38)

### Community 17 - "Day 7 — Tone Pairs Begin (Week 2"
Cohesion: 0.40
Nodes (6): Concept: Tone-Pair Identification, Day 7 — Tone Pairs Begin (Week 2), Day 7 Hard Gate: Tone-pair ID ≥70%, Day 7 Rationale: Difficulty lives in two-syllable combinations, not single tones, Day 7 Study Blocks (~5.5h), Day 7 Vocab Target: 95 words

### Community 18 - "Day 19 — Pre-Unlock Push"
Cohesion: 0.50
Nodes (4): Day 19 — Pre-Unlock Push, Day 19 Hard Gate: Pair ID ≥91% and T2↔T3 ≥87%, Day 19 Study Blocks (~5.5h), Day 19 Vocab Target: 290 words

## Knowledge Gaps
- **133 isolated node(s):** `corpus_path`, `log_path`, `tracker_path`, `feedback_pause_ms`, `T1` (+128 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **1 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `hvpt_engine.py — HVPT Pure Logic Engine` connect `2026-06-19-hvpt-mandarin-design.` to `test_hvpt_engine.py`, `hvpt.py`?**
  _High betweenness centrality (0.095) - this node is a cross-community bridge._
- **Why does `phase1/README.md — Phase 1 Sprint Parameters` connect `2026-06-19-hvpt-mandarin-design.` to `Day 4 — Deload: Consolidate Week`, `Phase 2 Engine — HSK3 2.0 + HSKK`?**
  _High betweenness centrality (0.078) - this node is a cross-community bridge._
- **Are the 3 inferred relationships involving `Phase 1 Tracker — Daily Gate Log` (e.g. with `Vocab Cumulative Target 870 (Day 40)` and `Vocab Cumulative Target 910 (Day 41)`) actually correct?**
  _`Phase 1 Tracker — Daily Gate Log` has 3 INFERRED edges - model-reasoned connections that need verification._
- **Are the 2 inferred relationships involving `phase1/README.md — Phase 1 Sprint Parameters` (e.g. with `hsk_anki.txt — Anki Import File` and `SRS floor: 1000 vocab + tones >=97% held`) actually correct?**
  _`phase1/README.md — Phase 1 Sprint Parameters` has 2 INFERRED edges - model-reasoned connections that need verification._
- **What connects `Extract HSK vocabulary from 新版HSK考试大纲1219.pdf and generate:   - hsk_anki.txt   :`, `Serial number: integer in range [1, 20000]`, `HSK level field: '1' … '6', '7—9', '3（7-9）', etc.` to the rest of the system?**
  _153 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `Phase 1 Tracker — Daily Gate Log` be split into smaller, more focused modules?**
  _Cohesion score 0.0549645390070922 - nodes in this community are weakly interconnected._
- **Should `2026-06-19-hvpt-mandarin-design.` be split into smaller, more focused modules?**
  _Cohesion score 0.08780487804878048 - nodes in this community are weakly interconnected._