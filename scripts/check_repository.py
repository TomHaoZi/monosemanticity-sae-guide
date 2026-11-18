#!/usr/bin/env python3
"""Check local documentation links, slide coverage, and PPTX structure."""

import json
import re
import sys
import zipfile
from pathlib import Path
from urllib.parse import unquote, urlsplit
from xml.etree import ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
NS = {"p": "http://schemas.openxmlformats.org/presentationml/2006/main"}
ERRORS = []


def fail(message):
    ERRORS.append(message)


def check_links():
    pattern = re.compile(r"!?\[[^\]\n]*\]\(([^\n)]+)\)")
    for document in sorted(ROOT.rglob("*.md")):
        if ".git" in document.relative_to(ROOT).parts:
            continue
        content = document.read_text(encoding="utf-8")
        if re.search(r"/Users/|/tmp/|file://|gh[pousr]_[A-Za-z0-9]{16,}", content):
            fail(f"Private path or credential pattern: {document.relative_to(ROOT)}")
        for raw in pattern.findall(content):
            target = raw.strip().split(' "', 1)[0].strip("<>")
            parsed = urlsplit(target)
            if parsed.scheme or parsed.netloc or not parsed.path:
                continue
            resolved = (document.parent / unquote(parsed.path)).resolve()
            if not resolved.is_relative_to(ROOT):
                fail(f"Link leaves repository: {document.relative_to(ROOT)} -> {target}")
            elif not resolved.exists():
                fail(f"Missing link: {document.relative_to(ROOT)} -> {target}")


def check_slides():
    slides = json.loads((ROOT / "data/slides.json").read_text(encoding="utf-8"))
    if [slide.get("slide") for slide in slides] != list(range(1, 19)):
        fail("Slide metadata must cover pages 1–18 in order.")
    for slide in slides:
        number = slide["slide"]
        if not 150 <= len(slide["script"]) <= 300:
            fail(f"Slide {number}: spoken script must be 150–300 characters.")
        if not (ROOT / f"assets/slides/slide-{number:02d}.png").is_file():
            fail(f"Slide {number}: preview is missing.")
        for source in slide["source"].splitlines():
            parsed = urlsplit(source)
            if parsed.hostname != "transformer-circuits.pub" or not parsed.fragment:
                fail(f"Slide {number}: expected an original-paper section link.")
    presentation = ROOT / "reports/sae-experiments.pptx"
    with zipfile.ZipFile(presentation) as package:
        broken = package.testzip()
        if broken:
            fail(f"PPTX ZIP integrity error: {broken}")
        document = ET.fromstring(package.read("ppt/presentation.xml"))
        slide_ids = document.find("p:sldIdLst", NS)
        if slide_ids is None or len(slide_ids) != 18:
            fail("PPTX must contain 18 slides.")
        size = document.find("p:sldSz", NS)
        if size is None or (int(size.get("cx", "0")), int(size.get("cy", "0"))) != (12192000, 6858000):
            fail("PPTX must use the expected 16:9 slide dimensions.")
        notes = [name for name in package.namelist()
                 if re.fullmatch(r"ppt/notesSlides/notesSlide\d+\.xml", name)]
        if len(notes) != 18:
            fail("PPTX must have notes for all 18 slides.")
    manuscript = (ROOT / "docs/speaker-notes.md").read_text(encoding="utf-8")
    if len(re.findall(r"^## 第 \d+ 页", manuscript, re.M)) != 18:
        fail("Manuscript must contain 18 slide sections.")
    if len(re.findall(r"^### Q\d+", manuscript, re.M)) != 6:
        fail("Manuscript must contain 6 Q&A items.")


def main():
    for name in ["README.md", "LICENSE", "THIRD_PARTY_NOTICES.md", "CITATION.cff",
                 "docs/concepts.md", "docs/experiment-notes.md", "docs/references.md"]:
        if not (ROOT / name).is_file():
            fail(f"Required repository file is missing: {name}")
    check_links()
    check_slides()
    if ERRORS:
        print("\n".join(f"ERROR: {error}" for error in ERRORS), file=sys.stderr)
        raise SystemExit(1)
    print("Repository checks passed: local links, 18 previews, manuscript, sources, PPTX and notes.")


if __name__ == "__main__":
    main()
