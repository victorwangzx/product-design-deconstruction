#!/usr/bin/env python3
"""Overlay Chinese handwritten-style labels and leader lines on a sketch image."""

from __future__ import annotations

import argparse
import json
import math
import re
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


DEFAULT_FONTS = [
    "/Users/admin/Library/Fonts/AlimamaDongFangDaKai-Regular.ttf",
    "/Users/admin/Library/Fonts/AlimamaDongFangDaKai.ttf",
    "/System/Library/Fonts/Supplemental/STKaiti.ttf",
    "/System/Library/Fonts/Supplemental/Kaiti.ttc",
    "/System/Library/Fonts/Hiragino Sans GB.ttc",
    "/System/Library/Fonts/STHeiti Medium.ttc",
    "/System/Library/Fonts/Supplemental/Arial Unicode.ttf",
    "/System/Library/Fonts/Supplemental/STKaiti.ttf",
    "/System/Library/Fonts/Supplemental/Kaiti.ttc",
    "/System/Library/Fonts/Supplemental/NotoSansKaithi-Regular.ttf",
    "/Users/admin/Library/Fonts/AlimamaShuHeiTi-Bold.otf",
    "/System/Library/Fonts/PingFang.ttc",
]

DEFAULT_ENGLISH_ALLOWLIST = {
    "AI",
    "AR",
    "VR",
    "CMF",
    "PCB",
    "LED",
    "USB",
    "Type-C",
    "PP",
    "ABS",
    "PC",
    "PET",
    "EVA",
    "IPX",
}


def load_font(size: int, font_path: str | None = None) -> ImageFont.FreeTypeFont:
    candidates = [font_path] if font_path else []
    candidates.extend(DEFAULT_FONTS)
    for candidate in candidates:
        if candidate and Path(candidate).exists():
            return ImageFont.truetype(candidate, size=size)
    return ImageFont.load_default()


def text_size(draw: ImageDraw.ImageDraw, text: str, font: ImageFont.ImageFont) -> tuple[int, int]:
    bbox = draw.textbbox((0, 0), text, font=font)
    return bbox[2] - bbox[0], bbox[3] - bbox[1]


def draw_soft_line(draw: ImageDraw.ImageDraw, p1: tuple[int, int], p2: tuple[int, int], color: tuple[int, int, int, int]) -> None:
    draw.line([p1, p2], fill=color, width=2)
    angle = math.atan2(p2[1] - p1[1], p2[0] - p1[0])
    for delta in (2.5, -2.5):
        end = (
            int(p2[0] - 12 * math.cos(angle + delta)),
            int(p2[1] - 12 * math.sin(angle + delta)),
        )
        draw.line([p2, end], fill=color, width=2)


def parse_allowlist(value: str | None) -> set[str]:
    allowlist = set(DEFAULT_ENGLISH_ALLOWLIST)
    if value:
        allowlist.update(part.strip() for part in value.split(",") if part.strip())
    return allowlist


def validate_language(labels: list[dict], allowlist: set[str], strict_chinese: bool) -> None:
    if not strict_chinese:
        return
    latin_pattern = re.compile(r"[A-Za-z][A-Za-z0-9+.-]*")
    errors = []
    for index, item in enumerate(labels, start=1):
        text = item.get("text", "")
        for match in latin_pattern.findall(text):
            if match not in allowlist:
                errors.append(f"label {index} contains non-allowed English token: {match}")
    if errors:
        raise ValueError(
            "Chinese-label policy failed. Use Chinese labels, or pass --allow-english for true industry terms.\n"
            + "\n".join(errors)
        )


def render_labels(
    image_path: Path,
    labels_path: Path,
    output_path: Path,
    font_path: str | None,
    font_size: int,
    canvas_size: tuple[int, int] | None,
    allowlist: set[str],
    strict_chinese: bool,
) -> None:
    base = Image.open(image_path).convert("RGBA")
    offset_x = 0
    offset_y = 0
    scale = 1.0
    if canvas_size:
        canvas_w, canvas_h = canvas_size
        scale = min(canvas_w / base.width, canvas_h / base.height)
        new_size = (int(base.width * scale), int(base.height * scale))
        resized = base.resize(new_size, Image.LANCZOS)
        canvas = Image.new("RGBA", canvas_size, (255, 255, 255, 255))
        offset_x = (canvas_w - new_size[0]) // 2
        offset_y = (canvas_h - new_size[1]) // 2
        canvas.alpha_composite(resized, (offset_x, offset_y))
        base = canvas
    overlay = Image.new("RGBA", base.size, (255, 255, 255, 0))
    draw = ImageDraw.Draw(overlay)
    font = load_font(font_size, font_path)
    small_font = load_font(max(18, int(font_size * 0.75)), font_path)

    labels = json.loads(labels_path.read_text(encoding="utf-8"))
    validate_language(labels, allowlist, strict_chinese)
    ink = (32, 32, 32, 235)
    muted = (92, 92, 92, 210)
    paper = (255, 255, 255, 205)

    for i, item in enumerate(labels, start=1):
        text = item["text"]
        x, y = item["xy"]
        x = x * scale + offset_x
        y = y * scale + offset_y
        anchor = item.get("anchor")
        number = item.get("number", i)
        size = int(item.get("font_size", font_size))
        item_font = load_font(size, font_path)

        if anchor:
            ax, ay = anchor
            ax = ax * scale + offset_x
            ay = ay * scale + offset_y
            draw_soft_line(draw, (int(x), int(y + size * 0.45)), (int(ax), int(ay)), muted)

        tw, th = text_size(draw, text, item_font)
        pad_x, pad_y = int(size * 0.38), int(size * 0.25)
        box = [x - pad_x, y - pad_y, x + tw + pad_x, y + th + pad_y]
        if box[0] < 0 or box[1] < 0 or box[2] > base.width or box[3] > base.height:
            raise ValueError(f"label {i} is outside canvas bounds: {text}")
        draw.rounded_rectangle(box, radius=8, fill=paper, outline=(35, 35, 35, 90), width=1)
        draw.text((x, y), text, fill=ink, font=item_font)

        if item.get("show_number", True):
            r = max(11, int(size * 0.42))
            cx, cy = int(x - pad_x - r - 6), int(y + th / 2)
            draw.ellipse([cx - r, cy - r, cx + r, cy + r], outline=ink, width=2)
            nw, nh = text_size(draw, str(number), small_font)
            draw.text((cx - nw / 2, cy - nh / 2 - 1), str(number), fill=ink, font=small_font)

    result = Image.alpha_composite(base, overlay).convert("RGB")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    result.save(output_path, quality=95)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", required=True, type=Path, help="Base no-text sketch image")
    parser.add_argument("--labels", required=True, type=Path, help="JSON list of label objects")
    parser.add_argument("--output", required=True, type=Path, help="Output image path")
    parser.add_argument("--font", default=None, help="Optional Chinese handwriting/kaiti font path")
    parser.add_argument("--font-size", type=int, default=34)
    parser.add_argument("--canvas", default=None, help="Optional final canvas, such as 1080x1920")
    parser.add_argument("--allow-english", default=None, help="Comma-separated extra allowed English terms")
    parser.add_argument("--no-strict-chinese", action="store_true", help="Allow arbitrary English in labels")
    args = parser.parse_args()
    canvas_size = None
    if args.canvas:
        w, h = args.canvas.lower().split("x", 1)
        canvas_size = (int(w), int(h))
    render_labels(
        args.input,
        args.labels,
        args.output,
        args.font,
        args.font_size,
        canvas_size,
        parse_allowlist(args.allow_english),
        not args.no_strict_chinese,
    )


if __name__ == "__main__":
    main()
