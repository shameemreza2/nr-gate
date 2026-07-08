# scripts/tone_compare.py
"""Tone production checker — record (or load) a syllable, compare its pitch
contour against the Tone Perfect native model, and say which tone it reads as.

Handles the beginner traps that make raw Praat misleading:
  - drops unvoiced frames and trims the consonant onset / creaky tail
  - median-filters octave jumps
  - normalizes to semitones around each speaker's own median (your pitch
    range vs the native speaker's no longer matters — only the SHAPE)

Usage (from repo root):
  python scripts/tone_compare.py --record ma1              # record 1.5s, save, compare
  python scripts/tone_compare.py recordings/day00/ma1.wav  # compare an existing file
  python scripts/tone_compare.py your.wav --native ba4     # explicit native target

Output: verdict in the terminal + overlay plot saved next to your recording.
"""
import argparse
import re
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")  # Windows cp1252 console can't print ✓/✗

import numpy as np
import parselmouth

REPO = Path(__file__).resolve().parent.parent
CORPUS = REPO / "corpus" / "tone_perfect"
RECORDINGS = REPO / "recordings"

TONE_NAMES = {1: "T1 (high flat)", 2: "T2 (rising)", 3: "T3 (dip)", 4: "T4 (falling)"}
RECORD_SECONDS = 1.5
RECORD_RATE = 44100
N_POINTS = 100  # contours are resampled to this many points for comparison


def extract_contour(path):
    """Return (times01, semitones) — cleaned, normalized pitch contour."""
    snd = parselmouth.Sound(str(path))
    # Two-pass pitch: wide first, then narrowed around the speaker's median
    # to suppress octave jumps (the classic Praat artifact).
    rough = snd.to_pitch(pitch_floor=60.0, pitch_ceiling=600.0)
    f0 = rough.selected_array["frequency"]
    voiced = f0[f0 > 0]
    if len(voiced) < 10:
        return None
    med = float(np.median(voiced))
    pitch = snd.to_pitch(pitch_floor=max(60.0, med / 1.8), pitch_ceiling=min(600.0, med * 1.8))
    f0 = pitch.selected_array["frequency"]
    t = pitch.xs()

    mask = f0 > 0
    if mask.sum() < 10:
        return None
    # Keep the longest voiced run (the vowel), not stray voiced blips.
    runs, start = [], None
    for i, v in enumerate(mask):
        if v and start is None:
            start = i
        elif not v and start is not None:
            runs.append((start, i)); start = None
    if start is not None:
        runs.append((start, len(mask)))
    s, e = max(runs, key=lambda r: r[1] - r[0])
    f0, t = f0[s:e], t[s:e]

    # Trim 12% off each edge: consonant perturbation at the front,
    # breath-fade / creak at the back — both fake a fall that isn't there.
    n = len(f0)
    lo, hi = int(n * 0.12), int(n * 0.88)
    if hi - lo < 8:
        lo, hi = 0, n
    f0, t = f0[lo:hi], t[lo:hi]

    # Light median filter for residual jumps.
    if len(f0) >= 5:
        pad = np.pad(f0, 2, mode="edge")
        f0 = np.array([np.median(pad[i:i + 5]) for i in range(len(f0))])

    st = 12.0 * np.log2(f0 / np.median(f0))
    t01 = (t - t[0]) / (t[-1] - t[0])
    # Resample to fixed grid so any two contours are directly comparable.
    grid = np.linspace(0.0, 1.0, N_POINTS)
    return grid, np.interp(grid, t01, st)


def classify(st):
    """Crude but honest 4-tone read of a semitone contour."""
    start, end = float(np.mean(st[:15])), float(np.mean(st[-15:]))
    mid_min = float(np.min(st[25:75]))
    span = float(np.max(st) - np.min(st))
    rise, fall = end - start, start - end
    if span < 2.0:
        return 1, "flat (span < 2 st)"
    if mid_min < start - 1.5 and mid_min < end - 1.5:
        return 3, f"dip (falls {start - mid_min:.1f} st then rises {end - mid_min:.1f} st)"
    if rise > 2.0:
        return 2, f"rising (+{rise:.1f} st)"
    if fall > 2.0:
        return 4, f"falling (-{fall:.1f} st)"
    return 1, "flat-ish (no clear movement)"


def find_native(syllable_tone, speaker="FV1"):
    p = CORPUS / f"{syllable_tone}_{speaker}_MP3.mp3"
    if not p.exists():
        hits = sorted(CORPUS.glob(f"{syllable_tone}_*_MP3.mp3"))
        if not hits:
            sys.exit(f"No native file for '{syllable_tone}' in {CORPUS}")
        p = hits[0]
    return p


def record_to(path):
    import sounddevice as sd
    import soundfile as sf
    print(f"  Recording {RECORD_SECONDS}s — speak AFTER the prompt, hold the vowel long...")
    input("  Press Enter, then speak: ")
    audio = sd.rec(int(RECORD_SECONDS * RECORD_RATE), samplerate=RECORD_RATE, channels=1)
    sd.wait()
    path.parent.mkdir(parents=True, exist_ok=True)
    sf.write(str(path), audio, RECORD_RATE)
    print(f"  Saved: {path}")


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("wav", nargs="?", help="existing recording to check")
    ap.add_argument("--record", metavar="SYL", help="record now as e.g. ma1 (saves to recordings/dayNN/)")
    ap.add_argument("--native", metavar="SYL", help="native target e.g. ma1 (default: from filename)")
    ap.add_argument("--day", type=int, default=0, help="day number for the recordings folder (default 0)")
    ap.add_argument("--no-plot", action="store_true", help="skip the overlay plot")
    args = ap.parse_args()

    if args.record:
        target = args.record.lower()
        wav = RECORDINGS / f"day{args.day:02d}" / f"{target}.wav"
        record_to(wav)
    elif args.wav:
        wav = Path(args.wav)
        target = (args.native or re.sub(r"\.\w+$", "", wav.name)).lower()
    else:
        ap.error("give a WAV path or --record SYL")

    m = re.fullmatch(r"([a-zü]+)([1-4])", target)
    if not m:
        sys.exit(f"Target '{target}' must look like ma1 / ba4 (syllable + tone digit).")
    intended = int(m.group(2))
    native = find_native(target)

    yours = extract_contour(wav)
    model = extract_contour(native)
    if yours is None:
        sys.exit("Could not find a stable voiced stretch in your recording — "
                 "hold the vowel longer (~1s) and record closer to the mic.")
    if model is None:
        sys.exit(f"Could not extract pitch from native file {native.name} (unexpected).")

    got, why = classify(yours[1])
    corr = float(np.corrcoef(yours[1], model[1])[0, 1])

    print(f"\n  intended : {TONE_NAMES[intended]}")
    print(f"  you said : {TONE_NAMES[got]} — {why}")
    print(f"  shape match vs native ({native.stem}): r = {corr:.2f}")
    verdict = "MATCH ✓" if got == intended else "MISS ✗ — listen to the native again, exaggerate harder"
    print(f"  verdict  : {verdict}\n")

    if not args.no_plot:
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
        fig, ax = plt.subplots(figsize=(7, 4))
        ax.plot(model[0], model[1], lw=2.5, label=f"native ({native.stem})")
        ax.plot(yours[0], yours[1], lw=2.5, label="you")
        ax.axhline(0, color="0.85", lw=0.8, zorder=0)
        ax.set_xlabel("time (normalized)")
        ax.set_ylabel("pitch (semitones vs own median)")
        ax.set_title(f"{target}: intended {TONE_NAMES[intended]} → read as {TONE_NAMES[got]}")
        ax.legend(frameon=False)
        for side in ("top", "right"):
            ax.spines[side].set_visible(False)
        out = wav.with_name(wav.stem + "_compare.png")
        fig.tight_layout()
        fig.savefig(out, dpi=120)
        print(f"  plot: {out}")

    sys.exit(0 if got == intended else 1)


if __name__ == "__main__":
    main()
