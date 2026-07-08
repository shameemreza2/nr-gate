# CLAUDE.md — hsk3-5

## Daily learning flow (PERSISTENT RULE — applies every session, every device)

Phase 1 = 48-day tone-first sprint (calendar dates live in local memory and
`study-progress.md`, not here). Target ~1075 words (full HSK3 vocab).
Learning happens **game-shaped**, not list-shaped:

1. **Session opener (zero decisions).** At the start of every session in this
   repo, state: "Day N, unit = X" — the next unfinished sprint unit. Track
   progress in `study-progress.md` (create on first use, one line per
   completed unit with date). Do not ask the user what they want to do.

2. **Drill rounds are the primary path.** Vocab lists and phase files are
   reference material. Default unit = one drill round: Claude quizzes tones /
   words / sentences as a game round (score kept in-session), user answers,
   Claude corrects with why. Active recall, never passive re-reading.

3. **10-minute minimum, binary done.** A unit counts as done after one drill
   round — even a 10-minute one. Bad day = 10 minutes still counts. Never
   raise the bar.

4. **Plan-freeze.** No new plans, no re-planning the sprint, no side-quests
   until today's unit is done. If the user drifts, redirect once: "Unit
   first, then that." After the unit is done, anything goes.

## Repo facts

- 2026 exams still HSK 2.0 (not 3.0); speaking = HSKK 初级; HSK3 written
  pass = 180/300 (verified from official syllabus PDF).
- Knowledge graph output lives in `graphify-out\` inside this repo; run
  `/graphify <repo path> --update` after adding new phase files.

## Commit style

Never add Co-Authored-By or other trailers to commits.
