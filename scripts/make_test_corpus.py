# scripts/make_test_corpus.py
"""
One-shot script: generate tiny synthetic WAV files named in Tone Perfect format.
Used as the build-phase corpus sample until the official MSU corpus arrives.
Run from the repo root: python scripts/make_test_corpus.py
"""
import math
import struct
import wave
from pathlib import Path

SAMPLE_RATE = 22050
DURATION_MS = 800  # 0.8 s — long enough for pygame to play before keypress

# Cover all 4 tones, 3 syllables, 3 speakers (36 files — enough to exercise every code path)
SYLLABLES = ["ba", "ma", "fan"]
TONES = [1, 2, 3, 4]
SPEAKERS = ["FV1", "FV2", "MV1"]

# Distinct frequencies per tone so they're not all identical (helps manual QA)
TONE_FREQ = {1: 300, 2: 400, 3: 250, 4: 350}


def make_wav(path, frequency):
    n = int(SAMPLE_RATE * DURATION_MS / 1000)
    with wave.open(str(path), "w") as f:
        f.setnchannels(1)
        f.setsampwidth(2)
        f.setframerate(SAMPLE_RATE)
        for i in range(n):
            v = int(32767 * math.sin(2 * math.pi * frequency * i / SAMPLE_RATE))
            f.writeframes(struct.pack("<h", v))


def main():
    out = Path(__file__).parent.parent / "corpus" / "tone_perfect"
    out.mkdir(parents=True, exist_ok=True)

    created = 0
    for syllable in SYLLABLES:
        for tone in TONES:
            for speaker in SPEAKERS:
                fname = f"{syllable}{tone}_{speaker}_MP3.wav"
                fpath = out / fname
                make_wav(fpath, TONE_FREQ[tone])
                created += 1

    print(f"Created {created} synthetic WAV files in {out}")
    print("These are build-phase placeholders. Swap in the official Tone Perfect MP3s on arrival.")


if __name__ == "__main__":
    main()
