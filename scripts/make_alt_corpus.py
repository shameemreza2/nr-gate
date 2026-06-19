# scripts/make_alt_corpus.py
"""
Temporary alternative corpus: Microsoft Edge TTS (zh-CN) recordings named in
Tone Perfect filename format. Produces real Mandarin speech with correct F0
tone contours — usable for HVPT training until the official corpus arrives.

Requires: pip install edge-tts
Run:      python scripts/make_alt_corpus.py

PHASE2-UPGRADE: When the official Tone Perfect corpus arrives via MSU FileDepot,
drop the MP3s flat into corpus/tone_perfect/ and delete this script.
The engine, config, runner, and all tests need zero changes on the swap.

NOTE: Synthetic .wav files from make_test_corpus.py (sine waves) must not be
mixed with this corpus during training. Delete *.wav before running HVPT.
"""
import asyncio
import sys
from pathlib import Path

# 10 syllables × 4 tones × 4 voices = 160 files.
# Characters chosen for unambiguous, standard pronunciation in each tone.
SYLLABLES = {
    "ba":   ("巴", "拔", "把", "爸"),   # bā bá bǎ bà
    "ma":   ("妈", "麻", "马", "骂"),   # mā má mǎ mà
    "fan":  ("番", "凡", "反", "饭"),   # fān fán fǎn fàn
    "da":   ("搭", "达", "打", "大"),   # dā dá dǎ dà
    "guo":  ("锅", "国", "果", "过"),   # guō guó guǒ guò
    "yi":   ("衣", "疑", "椅", "意"),   # yī yí yǐ yì
    "wang": ("汪", "王", "往", "旺"),   # wāng wáng wǎng wàng
    "ni":   ("妮", "泥", "你", "腻"),   # nī ní nǐ nì
    "jia":  ("家", "夹", "假", "嫁"),   # jiā jiá jiǎ jià
    "tu":   ("突", "图", "土", "吐"),   # tū tú tǔ tù
}

# 2 female (FV) + 2 male (MV) voices — matches Tone Perfect speaker code style
SPEAKERS = {
    "FV1": "zh-CN-XiaoxiaoNeural",
    "FV2": "zh-CN-XiaoyiNeural",
    "MV1": "zh-CN-YunxiNeural",
    "MV2": "zh-CN-YunjianNeural",
}

TOTAL = len(SYLLABLES) * 4 * len(SPEAKERS)  # 160


async def _generate_one(char: str, voice: str, path: Path, sem: asyncio.Semaphore) -> None:
    import edge_tts
    async with sem:
        tts = edge_tts.Communicate(char, voice)
        await tts.save(str(path))


async def main() -> None:
    try:
        import edge_tts  # noqa: F401
    except ImportError:
        print("ERROR: run  pip install edge-tts  first")
        sys.exit(1)

    out = Path(__file__).parent.parent / "corpus" / "tone_perfect"
    out.mkdir(parents=True, exist_ok=True)

    wav_files = list(out.glob("*.wav"))
    if wav_files:
        print(f"  [warn] {len(wav_files)} synthetic .wav files found in {out}")
        print("  These are sine-wave placeholders (make_test_corpus.py) — not speech.")
        print("  Delete them before training:  del corpus\\tone_perfect\\*.wav")
        print()

    sem = asyncio.Semaphore(5)
    pending = []
    labels = []
    for syllable, chars in SYLLABLES.items():
        for tone_idx, char in enumerate(chars, 1):
            for speaker_code, voice in SPEAKERS.items():
                fname = f"{syllable}{tone_idx}_{speaker_code}_MP3.mp3"
                fpath = out / fname
                if fpath.exists():
                    continue
                pending.append(_generate_one(char, voice, fpath, sem))
                labels.append(fname)

    if not pending:
        print(f"All {TOTAL} files already present in {out}. Nothing to do.")
        return

    print(f"Generating {len(pending)} / {TOTAL} files  "
          f"(10 syllables × 4 tones × 4 voices) ...")
    results = await asyncio.gather(*pending, return_exceptions=True)
    errors = [(labels[i], r) for i, r in enumerate(results) if isinstance(r, Exception)]
    if errors:
        for name, exc in errors[:3]:
            print(f"  [error] {name}: {exc}")
        if len(errors) > 3:
            print(f"  … and {len(errors) - 3} more")

    ok = len(pending) - len(errors)
    print(f"Done: {ok}/{len(pending)} files written to {out}")
    if errors:
        print(f"  {len(errors)} failed — re-run to retry (idempotent, skips existing files)")
    print()
    print("Corpus is TTS-generated speech — adequate for tone training until official")
    print("Tone Perfect corpus arrives. Drop official MP3s into the same folder.")


if __name__ == "__main__":
    asyncio.run(main())
