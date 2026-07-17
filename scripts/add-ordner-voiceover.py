#!/usr/bin/env python3
"""Generate German VO (edge-tts) and mux onto ordner-service.mp4."""

from __future__ import annotations

import asyncio
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

import edge_tts

ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / "assets"
VIDEO = ASSETS / "ordner-service.mp4"
OUT = ASSETS / "ordner-service.mp4"
VOICE_MP3 = ASSETS / "ordner-service-vo.mp3"

# Calm male DE voice – Conrad works well for Makler-Ton
VOICE = "de-DE-ConradNeural"
RATE = "-5%"
PITCH = "-2Hz"

# Timed lines aligned to tightened ~26s cut
LINES: list[tuple[float, str]] = [
    (0.25, "Versicherungsunterlagen – oft über Jahre verteilt."),
    (3.7, "Sie bringen den Ordner. Wir übernehmen."),
    (7.2, "Wir prüfen Ihren Bestand, finden Lücken und bessere Alternativen."),
    (12.2, "Aus Chaos wird Ordnung."),
    (16.2, "Alles landet digital in Ihrem persönlichen Kundenportal."),
    (21.3, "Ordner-Service: einmalig 49 Euro."),
]

VIDEO_DUR = 26.0


def find_ffmpeg() -> str:
    exe = shutil.which("ffmpeg")
    if exe:
        return exe
    winget = Path.home() / "AppData/Local/Microsoft/WinGet/Packages"
    if winget.exists():
        hits = list(winget.glob("**/ffmpeg.exe"))
        if hits:
            return str(hits[0])
    raise SystemExit("ffmpeg nicht gefunden.")


async def synth_line(text: str, out_path: Path) -> None:
    communicate = edge_tts.Communicate(text, VOICE, rate=RATE, pitch=PITCH)
    await communicate.save(str(out_path))


def probe_duration(ffmpeg: str, path: Path) -> float:
    # ffprobe via ffmpeg -i is messy; use ffprobe if available
    probe = shutil.which("ffprobe")
    if probe:
        r = subprocess.run(
            [
                probe,
                "-v",
                "error",
                "-show_entries",
                "format=duration",
                "-of",
                "default=noprint_wrappers=1:nokey=1",
                str(path),
            ],
            capture_output=True,
            text=True,
            check=True,
        )
        return float(r.stdout.strip())
    # fallback: parse ffmpeg stderr
    r = subprocess.run([ffmpeg, "-i", str(path)], capture_output=True, text=True)
    for part in r.stderr.split():
        if part.startswith("Duration"):
            continue
    import re

    m = re.search(r"Duration: (\d+):(\d+):(\d+\.\d+)", r.stderr)
    if not m:
        raise RuntimeError(f"Dauer nicht lesbar: {path}")
    h, mi, s = int(m.group(1)), int(m.group(2)), float(m.group(3))
    return h * 3600 + mi * 60 + s


async def build_vo_track(tmp: Path, ffmpeg: str) -> Path:
    parts: list[Path] = []
    for i, (start, text) in enumerate(LINES):
        clip = tmp / f"line_{i:02d}.mp3"
        print(f"  TTS [{start:5.1f}s] {text[:48]}…")
        await synth_line(text, clip)
        dur = probe_duration(ffmpeg, clip)
        # delay in ms for adelay (must be applied to both channels for stereo;
        # edge-tts outputs mono – adelay works on each channel listed)
        delayed = tmp / f"delayed_{i:02d}.wav"
        delay_ms = int(round(start * 1000))
        subprocess.run(
            [
                ffmpeg,
                "-y",
                "-i",
                str(clip),
                "-af",
                f"aformat=sample_rates=48000:channel_layouts=mono,adelay={delay_ms},apad=whole_dur={VIDEO_DUR}",
                "-t",
                str(VIDEO_DUR),
                str(delayed),
            ],
            check=True,
            capture_output=True,
        )
        parts.append(delayed)
        print(f"         Dauer {dur:.1f}s")

    # mix all delayed lines
    mixed = tmp / "vo_mixed.wav"
    cmd = [ffmpeg, "-y"]
    for p in parts:
        cmd += ["-i", str(p)]
    n = len(parts)
    # soft compression + slight loudness normalize
    filters = (
        f"amix=inputs={n}:normalize=0:dropout_transition=0,"
        f"dynaudnorm=f=75:g=15,"
        f"loudnorm=I=-16:TP=-1.5:LRA=11,"
        f"aresample=48000"
    )
    cmd += ["-filter_complex", filters, "-t", str(VIDEO_DUR), str(mixed)]
    subprocess.run(cmd, check=True, capture_output=True)

    # also export mp3 archive next to video
    subprocess.run(
        [ffmpeg, "-y", "-i", str(mixed), "-codec:a", "libmp3lame", "-q:a", "3", str(VOICE_MP3)],
        check=True,
        capture_output=True,
    )
    return mixed


def mux(ffmpeg: str, video: Path, audio: Path, out: Path) -> None:
    tmp_out = out.with_suffix(".tmp.mp4")
    subprocess.run(
        [
            ffmpeg,
            "-y",
            "-i",
            str(video),
            "-i",
            str(audio),
            "-map",
            "0:v:0",
            "-map",
            "1:a:0",
            "-c:v",
            "copy",
            "-c:a",
            "aac",
            "-b:a",
            "192k",
            "-ar",
            "48000",
            "-ac",
            "2",
            "-shortest",
            "-movflags",
            "+faststart",
            str(tmp_out),
        ],
        check=True,
    )
    tmp_out.replace(out)


async def main() -> int:
    if not VIDEO.exists():
        raise SystemExit(f"Video fehlt: {VIDEO} – zuerst build-ordner-video.py ausführen.")
    ffmpeg = find_ffmpeg()
    print(f"Stimme: {VOICE} ({RATE})")
    with tempfile.TemporaryDirectory(prefix="ordner-vo-") as td:
        tmp = Path(td)
        audio = await build_vo_track(tmp, ffmpeg)
        print("Muxe Audio auf Video…")
        mux(ffmpeg, VIDEO, audio, OUT)
    size = OUT.stat().st_size / (1024 * 1024)
    print(f"Fertig: {OUT} ({size:.1f} MB) + {VOICE_MP3.name}")
    return 0


if __name__ == "__main__":
    sys.exit(asyncio.run(main()))
