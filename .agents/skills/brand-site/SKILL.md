---
name: brand-site
description: Theme and brand the portfolio (colors, fonts, base theme, logo, small CSS tweaks). Shows five vetted presets first, then interviews the student. Use when the student wants to restyle the site, change colors or fonts, or says "make it look like me".
---

# Brand the site

Goal: a site that looks intentional and stays readable. Branding is edited in `_brand.yml` (colors, fonts), `_quarto.yml` (base theme, logo, favicon, navbar) and `styles.css` (small tweaks). Do not touch page content.

1. **Show the presets before asking anything.** Run `uv run python scripts/brand.py preview`. It opens a page with five vetted options (`.agents/skills/brand-site/presets.yml`). Tell the student to look at it, then ask which id they like best, or whether they want none of them.
2. **Interview, one or two questions at a time**, only after they have seen the presets:
   - Which preset is closest, and what would they change (a color, a font, light vs dark)?
   - Any required colors or a logo (school, employer, personal brand)? Do they have the right to use the logo?
   - What impression should an employer get: clean, creative, technical, warm?
3. **Apply the starting point.** `uv run python scripts/brand.py apply <id>` writes `_brand.yml`. For changes beyond the preset, edit `_brand.yml` by hand and explain each value in a sentence.
4. **Always check contrast.** Run `uv run python scripts/brand.py check`. Every line must say `ok` (4.5:1, WCAG AA). If one fails, darken the accent on a light background (or lighten it on a dark one) and re-run. Never ship a failing pair.
5. **Optional pieces**, only if asked:
   - Base theme: the `theme:` list in `_quarto.yml` is `[cosmo, brand]`. Another Bootswatch theme (`flatly`, `lux`, `journal`, ...) can replace `cosmo`; keep `brand` last so their colors win.
   - Logo and favicon: put the image in the project, then set `logo` in `_brand.yml` and `favicon` under `website:` in `_quarto.yml`.
   - Small CSS in `styles.css`: card radius, link underline, spacing. Keep it under about 20 lines and comment each rule.
6. **Preview and iterate.** Run `uv run quarto preview` and change one thing at a time. Explain what each change did so they learn the idea behind it.
7. **Finish.** Run `uv run python scripts/brand.py check` once more and tell them to commit `_brand.yml`, `_quarto.yml` and `styles.css`.

Rules:
- One accent color. Restraint reads as professional.
- Do not add fonts beyond two families, or any dependency, without asking. Google fonts via `_brand.yml` only.
- Do not use a logo or image the student does not have rights to.
- Do not edit `projects/`, `posts/`, `index.qmd`, or `about.qmd`.
- Slides in `guide/` use the same `_brand.yml`, so tell the student the deck changes too.
