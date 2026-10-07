# Portfolio site: instructions for AI assistants

This is a student's Quarto portfolio. Its purpose is to show a real person's real skills to employers and graduate programs. Everything on it must be true and must be something the student can explain in an interview.

## Rules that override everything else

1. **Never invent facts.** Do not make up projects, results, metrics, employers, courses, awards, or skills. If you need a fact, ask the student. If they do not know it, leave a `TODO` comment instead of guessing.
2. **Keep the student's voice.** Suggest edits and explain why. Do not rewrite whole pages unprompted. Prefer plain, specific sentences over marketing language.
3. **Teach while you work.** When you make a change, say in one or two sentences what you did and why, so the student learns the Quarto or writing idea behind it.
4. **Ask before big changes.** Confirm before deleting pages, changing `_quarto.yml` structure, or adding dependencies.
5. **Only claim skills that a project demonstrates.** The Skills page is generated from project `categories`, so every skill needs a project behind it.

## Layout

| Path | Purpose |
|---|---|
| `index.qmd` | Home page. Shows projects marked `featured: true`. |
| `about.qmd` | About page. Student writes this. |
| `projects/<slug>/index.qmd` | One folder per project. The core of the portfolio. |
| `posts/<slug>/index.qmd` | Optional writing (what they learned, how they work). |
| `skills.qmd` | Skills page; a filterable listing of projects by `categories`. |
| `_quarto.yml` | Site title, navbar, links. |
| `_brand.yml` | Colors and fonts. |
| `scripts/check_site.py` | Checks for leftover placeholders and thin projects. |
| `scripts/brand.py` | Previews brand presets, checks color contrast, applies a preset to `_brand.yml`. |
| `.agents/skills/` | Task playbooks for Codex and other agents (see below). Plain markdown, so any tool can read them. |
| `guide/` | Student-facing guide to working with AI. |

## Project page contract

Every `projects/<slug>/index.qmd` has this frontmatter:

```yaml
title: "Plain-language title"
description: "One sentence: what it is and the result."
date: "YYYY-MM-DD"
categories: [Python, Polars, Data Visualization]   # these ARE the skills; keep names consistent across projects
featured: true            # optional, max 3 across the site
repo: https://github.com/...
tools: [polars, lets-plot]
image: thumbnail.png      # optional but strongly recommended
```

Body sections, in order: **The problem**, **My approach**, **The work**, **The result**, **What I learned**, **Links**. The result must include at least one concrete number or finding.

Reuse existing category names exactly (check other projects first). `Python` and `python` would be two different skills.

## Commands

```bash
uv sync                                  # install Python dependencies (once)
uv run quarto preview                    # live preview at localhost
uv run quarto render                     # full build into docs/
uv run python scripts/check_site.py      # portfolio checklist
```

Computed output is frozen in `_freeze/` and committed, so CI does not run code. After changing a code cell, re-render locally and commit `_freeze/`.

## Publishing

Pushing to `main` runs `.github/workflows/publish.yml`, which deploys to GitHub Pages. Pages must be set to "GitHub Actions" in repo settings, under Pages.

## Skills

Playbooks live in `.agents/skills/<name>/SKILL.md`: `setup-portfolio`, `new-project`, `new-post`, `portfolio-review`, `polish-writing`, `brand-site`, `check-site`. If your tool does not load skills automatically, read the matching file and follow it.

## Optional: marimo

`_extensions/marimo-team/marimo` is installed for interactive pages. Use it only if the student asks for interactivity. Use ```` ```{python.marimo} ```` cells; see https://github.com/marimo-team/quarto-marimo.
