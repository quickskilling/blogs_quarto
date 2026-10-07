#!/usr/bin/env python3
"""Preview, check, and apply brand presets for the site.

Usage:
    uv run python scripts/brand.py preview        # build and open a page showing every preset
    uv run python scripts/brand.py check          # contrast check of the current _brand.yml
    uv run python scripts/brand.py apply <id>     # write a preset to _brand.yml
"""
import html
import subprocess
import sys
import webbrowser
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
PRESETS = ROOT / ".agents/skills/brand-site/presets.yml"
BRAND = ROOT / "_brand.yml"
OUT = ROOT / ".brand-preview/index.html"
AA = 4.5


def load_presets() -> list[dict]:
    return yaml.safe_load(PRESETS.read_text())["presets"]


def resolve(brand: dict) -> dict[str, str]:
    """Return foreground, background, primary as hex, resolving palette names."""
    color = brand["color"]
    palette = color.get("palette", {})
    out = {}
    for key in ("foreground", "background", "primary"):
        val = color.get(key)
        if val is None:
            continue
        out[key] = palette.get(val, val)
    out.setdefault("background", "#ffffff")
    return out


def luminance(hex_color: str) -> float:
    h = hex_color.lstrip("#")
    r, g, b = (int(h[i:i + 2], 16) / 255 for i in (0, 2, 4))
    lin = lambda c: c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4
    return 0.2126 * lin(r) + 0.7152 * lin(g) + 0.0722 * lin(b)


def contrast(a: str, b: str) -> float:
    la, lb = sorted((luminance(a), luminance(b)), reverse=True)
    return (la + 0.05) / (lb + 0.05)


def pairs(brand: dict) -> list[tuple[str, float]]:
    c = resolve(brand)
    bg = c["background"]
    result = []
    if "foreground" in c:
        result.append(("text on background", contrast(c["foreground"], bg)))
    if "primary" in c:
        result.append(("links/accent on background", contrast(c["primary"], bg)))
        # Buttons and the navbar put text on the primary color: use whichever of white/black reads better.
        best = max(contrast("#ffffff", c["primary"]), contrast("#000000", c["primary"]))
        result.append(("text on accent (buttons)", best))
    return result


def cmd_check() -> int:
    brand = yaml.safe_load(BRAND.read_text())
    bad = 0
    for label, ratio in pairs(brand):
        ok = ratio >= AA
        bad += not ok
        print(f"{'ok  ' if ok else 'FAIL'} {ratio:5.2f}:1  {label}")
    print("\nWCAG AA needs 4.5:1 for normal text." + ("" if not bad else f" {bad} pair(s) too low."))
    return 1 if bad else 0


def cmd_apply(pid: str) -> int:
    for p in load_presets():
        if p["id"] == pid:
            header = "# Written by scripts/brand.py from preset '%s'. Edit freely.\n" % pid
            BRAND.write_text(header + yaml.safe_dump(p["brand"], sort_keys=False, allow_unicode=True))
            print(f"Wrote {BRAND.relative_to(ROOT)} from preset '{pid}'. Run: uv run quarto preview")
            return 0
    print(f"No preset '{pid}'. Choices: " + ", ".join(p["id"] for p in load_presets()))
    return 1


def card(p: dict) -> str:
    b = p["brand"]
    c = resolve(b)
    t = b["typography"]
    head = t["headings"]["family"]
    base = t["base"]
    badges = "".join(
        f'<span class="b {"ok" if r >= AA else "bad"}">{html.escape(l)}: {r:.1f}:1</span>'
        for l, r in pairs(b)
    )
    fg, bg, pr = c["foreground"], c["background"], c["primary"]
    on_pr = "#ffffff" if contrast("#ffffff", pr) >= contrast("#000000", pr) else "#000000"
    return f"""
<section class="card" style="background:{bg};color:{fg};font-family:'{base}',sans-serif">
  <div class="tag">{html.escape(p['id'])}</div>
  <h2 style="font-family:'{head}',serif;font-weight:{t['headings'].get('weight', 700)}">{html.escape(p['name'])}</h2>
  <p class="mood">{html.escape(p['mood'])}</p>
  <p>I analyze data and communicate what it means. <a href="#" style="color:{pr}">See my projects</a>.</p>
  <span class="btn" style="background:{pr};color:{on_pr}">View projects</span>
  <div class="sw">
    <i style="background:{fg}" title="text"></i><i style="background:{bg};border:1px solid #8884" title="background"></i><i style="background:{pr}" title="accent"></i>
  </div>
  <p class="fonts">{html.escape(head)} + {html.escape(base)}</p>
  <div>{badges}</div>
</section>"""


def cmd_preview() -> int:
    presets = load_presets()
    fams = {f["family"] for p in presets for f in p["brand"]["typography"]["fonts"]}
    link = "https://fonts.googleapis.com/css2?" + "&".join(
        f"family={f.replace(' ', '+')}:wght@400;600;700" for f in sorted(fams)
    ) + "&display=swap"
    page = f"""<!doctype html><html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1"><title>Brand presets</title>
<link rel="stylesheet" href="{link}">
<style>
body{{margin:0;padding:24px;font-family:system-ui,sans-serif;background:#eef0f3;color:#111}}
h1{{margin:0 0 4px}} .lead{{margin:0 0 20px;color:#444}}
.grid{{display:grid;gap:16px;grid-template-columns:repeat(auto-fit,minmax(280px,1fr))}}
.card{{padding:20px;border-radius:10px;border:1px solid #0002}}
.card h2{{margin:.2em 0}} .tag{{font:12px monospace;opacity:.7}} .mood{{opacity:.85}}
.btn{{display:inline-block;padding:8px 14px;border-radius:6px;font-weight:600}}
.sw{{margin:14px 0 6px}} .sw i{{display:inline-block;width:28px;height:28px;border-radius:50%;margin-right:6px}}
.fonts{{font-size:13px;opacity:.8;margin:4px 0 8px}}
.b{{display:inline-block;font:11px system-ui;padding:2px 6px;border-radius:4px;margin:2px 4px 2px 0;background:#fff;color:#111}}
.ok{{outline:1px solid #16a34a}} .bad{{outline:2px solid #dc2626}}
</style></head><body>
<h1>Pick a starting point</h1>
<p class="lead">Five vetted brand presets. Green outlines mean the contrast is readable (WCAG AA). Tell your assistant the id you like, or ask for a mix.</p>
<div class="grid">{''.join(card(p) for p in presets)}</div></body></html>"""
    OUT.parent.mkdir(exist_ok=True)
    OUT.write_text(page)
    print(f"Wrote {OUT.relative_to(ROOT)}")
    webbrowser.open(OUT.as_uri())
    return 0


def main() -> int:
    args = sys.argv[1:]
    if args[:1] == ["preview"]:
        return cmd_preview()
    if args[:1] == ["check"]:
        return cmd_check()
    if len(args) == 2 and args[0] == "apply":
        return cmd_apply(args[1])
    print(__doc__)
    return 2


if __name__ == "__main__":
    sys.exit(main())
