# Quarto Portfolio Template (AI-assisted)

A template for building a data science portfolio with [Quarto](https://quarto.org), Python, and an AI coding assistant. You end with a live website that shows your projects, your skills, and how you think.

## Quick start

1. **Use this template.** On GitHub click *Use this template*, then *Create a new repository* (name it something like `portfolio`). Clone it.
2. **Install tools** (once):
   - [uv](https://docs.astral.sh/uv/): `curl -LsSf https://astral.sh/uv/install.sh | sh` (Windows: `powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"`)
   - [Quarto](https://quarto.org/docs/download/) 1.9 or newer. Check with `quarto check`.
   - An AI coding assistant. This course uses Codex.
3. **Install dependencies:** `uv sync`
4. **Preview the site:** `uv run quarto preview`
5. **Open your assistant in this folder** and say: *"Use the setup-portfolio skill."*
6. **Publish:** push to `main`. In your repo go to *Settings, Pages, Source* and choose **GitHub Actions**. Your site appears at `https://<username>.github.io/<repo>`.

## What you build

| Page | Purpose |
|---|---|
| Home | Short pitch and your 3 featured projects |
| Projects | One page per project: problem, approach, result |
| Skills | Filter projects by skill. Every skill is backed by evidence |
| Writing | Optional posts about what you learned |
| About | Who you are and how to reach you |

## Working with AI

Skills (playbooks) live in `.agents/skills/`. Ask your assistant to use them by name:

| Skill | Use it to |
|---|---|
| `setup-portfolio` | Replace the template placeholders with your info |
| `new-project` | Turn work you did into a project page |
| `new-post` | Start a blog post |
| `polish-writing` | Get editing feedback in your own voice |
| `brand-site` | Pick colors and fonts from vetted presets, with a contrast check |
| `portfolio-review` | Get a hiring-manager critique |
| `check-site` | Verify the site is ready to publish |

Read [guide/ai-workflow.md](guide/ai-workflow.md) first. The rule is simple: the AI helps you write and debug, but every claim on the site must be true and something you can explain.

`AGENTS.md` holds the rules the assistant follows (never invent facts, keep your voice, teach as it goes).

## Daily commands

```bash
uv run quarto preview                 # live preview
uv run quarto render                  # build to docs/
uv run python scripts/check_site.py   # leftover placeholders, thin projects
```

Code output is saved in `_freeze/`. Commit it so the publish workflow does not need to execute your code. If you change a code cell, re-render locally first.

## Customizing

- Colors and fonts: `_brand.yml`
- Site title, nav, links: `_quarto.yml`
- Extra CSS: `styles.css`

## Optional: interactive pages with marimo

The [marimo Quarto extension](https://github.com/marimo-team/quarto-marimo) is installed in `_extensions/`. Use `{python.marimo}` cells in a project page if you want reactive widgets. Not needed for a good portfolio.

## History

The previous version of this repo (a plain Quarto blog with a marimo post script) is on the `historical` branch.
