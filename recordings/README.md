# recordings/

Personal voice recordings (baseline artifacts, tone-gate self-tests, self-intro takes).
One subfolder per day: `recordings/dayNN/`. Audio files (`*.wav`/`*.mp3`/`*.m4a`) are
git-ignored — this is personal voice data in a public repo, never commit the audio itself.
This README (and any future notes) is the only thing tracked.

## Day 0 baseline (10 pinyin syllables)

Reuses the 10-syllable set already vetted in the (now-removed) alt-corpus generator —
clean initials/finals, unambiguous across all 4 tones:

`ba · ma · fan · da · guo · yi · wang · ni · jia · tu`

Read each once, natural/neutral delivery (this is an accent baseline, not the tone-pair
gate). Save as `recordings/day00/baseline.wav`.

## Tone-gate recordings (block 2 onward)

The gate wants 4 tones on 5 syllables (`mā má mǎ mà ma` pattern). Record each take,
compare pitch contour in Praat against the matching native file in `corpus/tone_perfect/`
(e.g. `ba1_FV1_MP3.mp3` for bā). Save as `recordings/dayNN/<syllable><tone>.wav`.
