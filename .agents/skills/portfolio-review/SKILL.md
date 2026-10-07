---
name: portfolio-review
description: Review the whole portfolio as a skeptical hiring manager and give prioritized, honest feedback. Use when the student asks for a review or before sharing the site.
---

# Review the portfolio

Read-only. Do not edit files; produce feedback.

1. Run `uv run python scripts/check_site.py` and read `index.qmd`, `about.qmd`, `_quarto.yml`, and every `projects/*/index.qmd`.
2. Pretend you have 90 seconds. Answer, from the site alone:
   - What does this person do, and for whom?
   - What is the single strongest piece of evidence?
   - Which claims have no proof behind them?
3. Report in this order:
   - **Top 3 fixes** by impact, each with the exact file and a concrete suggestion.
   - **Per project:** is there a clear problem, a result with a number, visible code or a repo link, and a thumbnail? Quote the weakest sentence.
   - **Skills page:** any category with fewer than one real project behind it, or inconsistent names.
   - **What is already good.** Be specific.
4. Flag anything that looks inflated, vague ("passionate", "utilized"), or that you cannot verify. Ask the student whether it is true rather than assuming.
5. Finish by suggesting which skill to run next (`new-project`, `polish-writing`, `check-site`).
