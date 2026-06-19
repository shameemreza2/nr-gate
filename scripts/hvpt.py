# scripts/hvpt.py
"""HVPT Mandarin tone trainer — runner. See docs/specs/2026-06-19-hvpt-mandarin-design.md"""
import argparse
import csv
import json
import sys
import time
from datetime import date
from pathlib import Path

import msvcrt  # Windows-only; intentional — spec is Windows-exclusive (§12)
import pygame

import hvpt_engine as engine

SCRIPT_DIR = Path(__file__).parent
MODES = ["default", "baseline", "focus-T2T3", "diagnostic"]


def load_config():
    with open(SCRIPT_DIR / "hvpt_config.json", encoding="utf-8") as f:
        return json.load(f)


def resolve(cfg, key):
    """Resolve a config path relative to the script's own directory."""
    return (SCRIPT_DIR / cfg[key]).resolve()


def get_keypress():
    """Block until user presses 1/2/3/4. Re-prompt on any other key."""
    while True:
        ch = msvcrt.getwch()
        if ch in ("1", "2", "3", "4"):
            return int(ch)
        print("\r  → Press 1 / 2 / 3 / 4 : ", end="", flush=True)


def play_audio(path):
    """Play a single audio file, blocking until playback finishes."""
    try:
        pygame.mixer.music.load(str(path))
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            time.sleep(0.05)
    except Exception as e:
        print(f"\n  [warn] could not play {path.name}: {e} — skipping")


def run_trials(trials, mode, day_number, feedback_pause_ms, scored=True):
    """Run a block of trials. Returns list of (correct_tone, given) pairs (empty if unscored)."""
    responses = []
    n = len(trials)
    correct_so_far = 0
    total_so_far = 0

    for i, trial in enumerate(trials, 1):
        running = f"{100*correct_so_far/total_so_far:.1f}%" if total_so_far else "–"
        print(f"\n{'─'*45}")
        if scored:
            print(f"HVPT  Day {day_number:02d}  [{mode}]")
            print(f"Trial {i} / {n}  |  Running: {running}")
        else:
            print(f"Warm-up {i} / {n}  (unscored — calibrate your ear)")
        print("─" * 45)
        print("  [playing...]", flush=True)
        play_audio(trial["path"])
        while True:
            print("\r  r=replay  |  1/2/3/4 : ", end="", flush=True)
            ch = msvcrt.getwch()
            if ch == "r":
                print("\r  [replaying...]                    ")
                play_audio(trial["path"])
            elif ch in ("1", "2", "3", "4"):
                given = int(ch)
                break
        correct = trial["tone"]
        if given == correct:
            print(f"\r  ✓ Correct — Tone {correct}                    ")
            if scored:
                correct_so_far += 1
        else:
            print(f"\r  ✗ You said {given}  |  Correct: {correct}          ")
        if scored:
            total_so_far += 1
            responses.append((correct, given))
        time.sleep(feedback_pause_ms / 1000)

    return responses


def print_end_report(scores, gates, n_trials, mode, day_number, gate_cfg):
    print(f"\n{'─'*45}")
    print(f"SESSION COMPLETE — {n_trials} trials — Day {day_number:02d}")
    print("─" * 45)
    print(f"Overall accuracy:    {scores['accuracy_pct']}%")
    print("\nPer-tone:")
    print(f"  T1 (─ high-level):  {scores['t1_pct']}%")
    print(f"  T2 (╱ rising):      {scores['t2_pct']}%")
    print(f"  T3 (∨ dipping):     {scores['t3_pct']}%")
    print(f"  T4 (╲ falling):     {scores['t4_pct']}%")
    print("\nConfusion matrix (heard → said):")
    print("           Said →   T1    T2    T3    T4")
    for heard in range(1, 5):
        cells = "  ".join(f"{scores[f'cm_t{heard}t{said}']:4d}" for said in range(1, 5))
        print(f"  Heard T{heard}          {cells}")
    u_sym = "✓" if gates["unlock_gate"] else "✗"
    f_sym = "✓" if gates["flyday_gate"] else "✗"
    u_oa = gate_cfg["unlock_overall"] * 100
    u_t  = gate_cfg["unlock_t2t3"]   * 100
    f_oa = gate_cfg["flyday_overall"] * 100
    f_t  = gate_cfg["flyday_t2t3"]   * 100
    print("\nGate checks:")
    print(f"  Unlock  (≥{u_oa:.0f}% + T2↔T3 ≥{u_t:.0f}%):  {u_sym}  "
          f"[{scores['accuracy_pct']}% / {scores['t2t3_pct']}%]")
    print(f"  Fly-day (≥{f_oa:.0f}% + T2↔T3 ≥{f_t:.0f}%):  {f_sym}  "
          f"[{scores['accuracy_pct']}% / {scores['t2t3_pct']}%]")
    print("─" * 45)


def append_csv(log_path, row):
    log_path.parent.mkdir(parents=True, exist_ok=True)
    fieldnames = list(row.keys())
    # Single-process assumption: check then open has a TOCTOU window but is safe in practice
    write_header = not log_path.exists()
    with open(log_path, "a", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        if write_header:
            writer.writeheader()
        writer.writerow(row)


def append_tracker(tracker_path, line):
    if not tracker_path.exists():
        print(f"  [warn] tracker.md not found at {tracker_path} — skipping")
        return
    with open(tracker_path, "a", encoding="utf-8") as f:
        f.write("\n" + line)


def main():
    parser = argparse.ArgumentParser(description="HVPT Mandarin tone trainer")
    parser.add_argument("--mode", default="default", choices=MODES)
    parser.add_argument("--day", type=int, required=True,
                        help="Sprint day number (0–47)")
    args = parser.parse_args()

    cfg = load_config()
    mode = args.mode
    day_number = args.day

    corpus_path  = resolve(cfg, "corpus_path")
    log_path     = resolve(cfg, "log_path")
    tracker_path = resolve(cfg, "tracker_path")

    # Corpus check — hard stop before any trial
    corpus = engine.load_corpus(corpus_path)
    if not corpus:
        print(f"ERROR: No audio files found in {corpus_path}")
        print("  Place Tone Perfect MP3/WAV files there (e.g. fan3_FV1_MP3.mp3).")
        print("  Or run: python scripts/make_test_corpus.py")
        print("  Official corpus: https://tone.lib.msu.edu/")
        sys.exit(1)

    # Baseline guard
    if mode == "baseline" and engine.baseline_exists(log_path):
        print("ERROR: baseline already anchored (day_number=0 row exists).")
        print("  Re-anchoring would destroy your Day-0 reference. Use --mode default instead.")
        sys.exit(1)

    # pygame init — hard stop on failure
    try:
        pygame.mixer.init()
    except Exception as e:
        print(f"ERROR: pygame audio init failed: {e}")
        print("  Run: pip install pygame")
        print("  Also verify Windows audio output is enabled.")
        sys.exit(1)

    weights   = cfg["weights"][mode]
    n_trials  = cfg["trial_counts"][mode]
    pause_ms  = cfg["feedback_pause_ms"]
    gate_cfg  = cfg["gate"]

    warmup_trials = engine.build_trial_set(corpus, 5, weights)
    main_trials   = engine.build_trial_set(corpus, n_trials, weights)

    print(f"\nHVPT — Day {day_number:02d} — {mode}")
    print(f"Corpus: {len(corpus)} files  |  {n_trials} scored trials + 5 warm-up")
    print("─" * 45)
    print("\n  [5 warm-up trials — unscored]")

    run_trials(warmup_trials, mode, day_number, pause_ms, scored=False)
    responses = run_trials(main_trials, mode, day_number, pause_ms, scored=True)

    scores = engine.score_session(responses)
    gates  = engine.check_gates(scores["accuracy_pct"], scores["t2t3_pct"], gate_cfg)

    # Print end report BEFORE any disk writes — data is never lost
    print_end_report(scores, gates, len(responses), mode, day_number, gate_cfg)

    today   = date.today().isoformat()
    csv_row = engine.format_csv_row(today, day_number, mode, len(responses), scores, gates)
    t_line  = engine.format_tracker_line(today, day_number, mode, scores, gates)

    try:
        append_csv(log_path, csv_row)
        print(f"  Logged → {log_path}")
    except Exception as e:
        print(f"  [warn] CSV write failed: {e}")

    try:
        append_tracker(tracker_path, t_line)
        print("  tracker.md updated")
    except Exception as e:
        print(f"  [warn] tracker append failed: {e}")

    pygame.mixer.quit()


if __name__ == "__main__":
    main()
