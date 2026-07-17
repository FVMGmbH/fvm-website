#!/usr/bin/env python3
"""Build Ordner-Service promo video (~40s, 16:9) from story stills."""

from __future__ import annotations

import math
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

from PIL import Image, ImageDraw, ImageFilter, ImageFont

ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / "assets"
OUT = ASSETS / "ordner-service.mp4"

W, H = 1920, 1080
FPS = 30

# Shot list aligned to Drehbuch (seconds)
SHOTS = [
    {
        "src": "ordner-01-chaos.jpg",
        "dur": 5.0,
        "zoom": "in",
        "lines": ["Versicherungsunterlagen –", "oft über Jahre verteilt."],
    },
    {
        "src": "ordner-02-uebergabe.jpg",
        "dur": 5.0,
        "zoom": "out",
        "lines": ["Sie bringen den Ordner.", "Wir übernehmen."],
    },
    {
        "src": "ordner-03-pruefen.jpg",
        "dur": 8.0,
        "zoom": "in",
        "lines": ["Wir prüfen Bestand, Lücken", "und bessere Alternativen."],
    },
    {
        "src": "ordner-04-ordnen.jpg",
        "dur": 7.0,
        "zoom": "pan",
        "lines": ["Aus Chaos wird Ordnung."],
    },
    {
        "src": "ordner-06-portal.jpg",
        "dur": 8.0,
        "zoom": "in",
        "lines": ["Alles digital in Ihrem", "persönlichen Kundenportal."],
    },
    {
        "src": "__endcard__",
        "dur": 7.0,
        "zoom": "hold",
        "lines": [],  # text baked into endcard
    },
]


def find_ffmpeg() -> str:
    exe = shutil.which("ffmpeg")
    if exe:
        return exe
    raise SystemExit("ffmpeg nicht gefunden – bitte installieren und PATH neu laden.")


def load_font(size: int, bold: bool = False) -> ImageFont.FreeTypeFont | ImageFont.ImageFont:
    candidates = [
        r"C:\Windows\Fonts\segoeuib.ttf" if bold else r"C:\Windows\Fonts\segoeui.ttf",
        r"C:\Windows\Fonts\arialbd.ttf" if bold else r"C:\Windows\Fonts\arial.ttf",
        r"C:\Windows\Fonts\calibrib.ttf" if bold else r"C:\Windows\Fonts\calibri.ttf",
    ]
    for path in candidates:
        if Path(path).exists():
            return ImageFont.truetype(path, size)
    return ImageFont.load_default()


def cover_crop(img: Image.Image, tw: int, th: int) -> Image.Image:
    src = img.convert("RGB")
    sw, sh = src.size
    scale = max(tw / sw, th / sh)
    nw, nh = int(sw * scale), int(sh * scale)
    src = src.resize((nw, nh), Image.Resampling.LANCZOS)
    left = (nw - tw) // 2
    top = (nh - th) // 2
    return src.crop((left, top, left + tw, top + th))


def make_endcard() -> Image.Image:
    img = Image.new("RGB", (W, H), (10, 26, 47))
    draw = ImageDraw.Draw(img)

    # soft radial glow
    glow = Image.new("RGB", (W, H), (10, 26, 47))
    gdraw = ImageDraw.Draw(glow)
    for i, alpha in enumerate(range(40, 0, -2)):
        r = 420 + i * 18
        c = (21, 51, 86)
        gdraw.ellipse([W // 2 - r, H // 2 - r - 80, W // 2 + r, H // 2 + r - 80], fill=c)
    glow = glow.filter(ImageFilter.GaussianBlur(48))
    img = Image.blend(img, glow, 0.55)
    draw = ImageDraw.Draw(img)

    logo_path = ASSETS / "fvm-logo.png"
    if logo_path.exists():
        logo = Image.open(logo_path).convert("RGBA")
        lw = 340
        ratio = lw / logo.width
        logo = logo.resize((lw, max(1, int(logo.height * ratio))), Image.Resampling.LANCZOS)
        img.paste(logo, ((W - logo.width) // 2, 160), logo)

    title_f = load_font(54, bold=True)
    price_f = load_font(72, bold=True)
    sub_f = load_font(32, bold=False)
    cta_f = load_font(28, bold=False)

    def center_text(text: str, y: int, font, fill=(238, 243, 249)):
        bbox = draw.textbbox((0, 0), text, font=font)
        tw = bbox[2] - bbox[0]
        draw.text(((W - tw) // 2, y), text, font=font, fill=fill)

    center_text("Ordner-Service", 430, title_f, (255, 255, 255))
    center_text("einmalig 49 €", 510, price_f, (51, 183, 172))
    center_text("Einstieg für Neukunden · FVM GmbH Rockenhausen", 600, sub_f, (174, 191, 208))

    # gold hairline
    draw.rectangle([W // 2 - 40, 660, W // 2 + 40, 662], fill=(203, 161, 78))

    center_text("fvm-website.pages.dev  ·  06361 / 7744", 700, cta_f, (203, 161, 78))
    return img


def draw_subtitle(base: Image.Image, lines: list[str]) -> Image.Image:
    if not lines:
        return base
    frame = base.copy()
    overlay = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    draw = ImageDraw.Draw(overlay)
    font = load_font(46, bold=True)

    # measure block
    padd_x, padd_y, gap = 28, 18, 8
    widths, heights = [], []
    for line in lines:
        bbox = draw.textbbox((0, 0), line, font=font)
        widths.append(bbox[2] - bbox[0])
        heights.append(bbox[3] - bbox[1])
    block_w = max(widths) + padd_x * 2
    block_h = sum(heights) + gap * (len(lines) - 1) + padd_y * 2
    x0 = (W - block_w) // 2
    y0 = H - 160 - block_h

    # soft dark plate for readability
    draw.rounded_rectangle(
        [x0, y0, x0 + block_w, y0 + block_h],
        radius=14,
        fill=(8, 16, 28, 150),
    )

    y = y0 + padd_y
    for i, line in enumerate(lines):
        tw = widths[i]
        tx = x0 + (block_w - tw) // 2
        # shadow
        draw.text((tx + 2, y + 2), line, font=font, fill=(0, 0, 0, 180))
        draw.text((tx, y), line, font=font, fill=(255, 255, 255, 245))
        y += heights[i] + gap

    return Image.alpha_composite(frame.convert("RGBA"), overlay).convert("RGB")


def ken_burns_frame(src: Image.Image, t: float, dur: float, mode: str) -> Image.Image:
    """t in [0,1] progress. Slight zoom/pan for documentary feel."""
    # work on oversized canvas then crop
    scale_start, scale_end = 1.0, 1.08
    if mode == "out":
        scale_start, scale_end = 1.08, 1.0
    elif mode == "hold":
        scale_start, scale_end = 1.0, 1.0
    elif mode == "pan":
        scale_start, scale_end = 1.06, 1.06

    scale = scale_start + (scale_end - scale_start) * t
    # pan left→right for pan mode
    ox = 0.0
    if mode == "pan":
        ox = (t - 0.5) * 0.06  # ±3% of width
    elif mode == "in":
        ox = t * 0.02
    elif mode == "out":
        ox = (1 - t) * 0.02

    bw, bh = int(W * scale) + 4, int(H * scale) + 4
    canvas = cover_crop(src, bw, bh)
    cx = canvas.width / 2 + ox * W
    cy = canvas.height / 2
    left = int(cx - W / 2)
    top = int(cy - H / 2)
    left = max(0, min(left, canvas.width - W))
    top = max(0, min(top, canvas.height - H))
    return canvas.crop((left, top, left + W, top + H))


def write_shot_frames(shot: dict, out_dir: Path, start_idx: int) -> int:
    if shot["src"] == "__endcard__":
        src = make_endcard()
    else:
        path = ASSETS / shot["src"]
        if not path.exists():
            raise SystemExit(f"Fehlendes Asset: {path}")
        src = Image.open(path)

    n = int(round(shot["dur"] * FPS))
    for i in range(n):
        t = i / max(n - 1, 1)
        # ease in-out
        te = 0.5 - 0.5 * math.cos(math.pi * t)
        frame = ken_burns_frame(src, te, shot["dur"], shot["zoom"])
        # slight subtitle fade in first 0.4s / out last 0.35s
        lines = shot["lines"]
        if lines:
            fade = 1.0
            if t < 0.08:
                fade = t / 0.08
            elif t > 0.92:
                fade = (1 - t) / 0.08
            if fade > 0.05:
                frame = draw_subtitle(frame, lines)
                if fade < 0.99:
                    # blend with non-subtitled for fade
                    plain = ken_burns_frame(src, te, shot["dur"], shot["zoom"])
                    frame = Image.blend(plain, frame, fade)
        out_path = out_dir / f"frame_{start_idx + i:06d}.jpg"
        frame.save(out_path, "JPEG", quality=88, optimize=True)
        if i % 30 == 0:
            print(f"  frame {start_idx + i}/{start_idx + n - 1}", flush=True)
    return n


def encode_mp4(frames_dir: Path, out_path: Path, ffmpeg: str) -> None:
    # soft ambient bed: very quiet filtered noise (optional, under speech-less cut)
    # Keep silent for cleaner subtitle-only version – user can add music later.
    cmd = [
        ffmpeg,
        "-y",
        "-framerate",
        str(FPS),
        "-i",
        str(frames_dir / "frame_%06d.jpg"),
        "-c:v",
        "libx264",
        "-preset",
        "medium",
        "-crf",
        "20",
        "-pix_fmt",
        "yuv420p",
        "-movflags",
        "+faststart",
        "-an",
        str(out_path),
    ]
    print("ffmpeg encode…", flush=True)
    subprocess.run(cmd, check=True)


def main() -> int:
    ffmpeg = find_ffmpeg()
    total_dur = sum(s["dur"] for s in SHOTS)
    print(f"Baue Ordner-Service Video ({total_dur:.0f}s, {W}x{H} @ {FPS}fps)…")

    with tempfile.TemporaryDirectory(prefix="ordner-vid-") as tmp:
        tmp_path = Path(tmp)
        idx = 0
        for n, shot in enumerate(SHOTS, 1):
            label = shot["src"] if shot["src"] != "__endcard__" else "endcard"
            print(f"[{n}/{len(SHOTS)}] {label} ({shot['dur']}s)")
            idx += write_shot_frames(shot, tmp_path, idx)

        encode_mp4(tmp_path, OUT, ffmpeg)

    size_mb = OUT.stat().st_size / (1024 * 1024)
    print(f"Fertig: {OUT} ({size_mb:.1f} MB, {idx / FPS:.1f}s)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
