#!/usr/bin/env python3
"""Generate the slide gallery from checked-in metadata; standard library only."""

import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def render_gallery(slides):
    lines = [
        "# 18 页幻灯片与逐页口播",
        "",
        "[返回首页](../README.md) · [下载可编辑 PPT](../reports/sae-experiments.pptx) · "
        "[完整演讲稿、详细解析与 Q&A](speaker-notes.md)",
        "",
        "16 页正文与 2 页附录。建议总时长约 26 分 20 秒，含读图与停顿。"
        "每页口播与 PPT 备注对应，公式及方法细节见完整解析。",
        "",
        "## 页面导航",
        "",
    ]
    for slide in slides:
        number = slide["slide"]
        lines.append(f'- [{number:02d} · {slide["title"]}](#slide-{number:02d})')
    lines.extend(["", "---", ""])
    for slide in slides:
        number = slide["slide"]
        lines.extend([
            f'<a id="slide-{number:02d}"></a>',
            "",
            f'## {number:02d} · {slide["title"]}',
            "",
            f'![第 {number} 页：{slide["title"]}](../assets/slides/slide-{number:02d}.png)',
            "",
            f'建议用时：{slide["seconds"]} 秒。',
            "",
            slide["script"],
            "",
            "原文定位：",
            "",
        ])
        for source in slide["source"].splitlines():
            if source.strip():
                fragment = source.rsplit("#", 1)[-1]
                lines.append(f"- [{fragment}]({source.strip()})")
        lines.extend(["", "[回到导航](#页面导航)", "", "---", ""])
    lines.extend([
        "## 图片与许可",
        "",
        "预览页中的论文原图归原权利人所有，原创中文讲解与配置采用 MIT。"
        "详见 [第三方材料说明](../THIRD_PARTY_NOTICES.md)。",
        "",
        "本页由 `scripts/build_docs.py` 从 `data/slides.json` 生成。",
        "",
    ])
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="Check without changing files")
    args = parser.parse_args()
    slides = json.loads((ROOT / "data/slides.json").read_text(encoding="utf-8"))
    expected = render_gallery(slides)
    target = ROOT / "docs/slides.md"
    if args.check:
        if not target.exists() or target.read_text(encoding="utf-8") != expected:
            raise SystemExit("Gallery is stale. Run: python3 scripts/build_docs.py")
        print("Slide gallery is up to date.")
    else:
        target.write_text(expected, encoding="utf-8")
        print("Generated docs/slides.md")


if __name__ == "__main__":
    main()
