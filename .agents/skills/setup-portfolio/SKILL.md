---
name: setup-portfolio
description: First-run setup for a new student portfolio. Interviews the student, then replaces the template placeholders in _quarto.yml, index.qmd, about.qmd. Use when the student says "set up my portfolio" or when check_site.py reports placeholders.
---

# Set up the portfolio

Goal: turn the template into the student's site without inventing anything about them.

1. Run `uv run python scripts/check_site.py` to see what is still a placeholder.
2. Interview the student, **one or two questions at a time**, and wait for answers:
   - Full name and how they want it displayed.
   - GitHub username, LinkedIn URL, and the GitHub repo name for this site.
   - One sentence: what are they studying and what kind of work do they want?
   - Who is the audience: employers, grad schools, clients?
   - Which projects do they already have, even rough ones? (These feed `new-project`.)
3. Edit `_quarto.yml` (title, site-url as `https://<username>.github.io/<repo>`, github/linkedin links), `index.qmd` (title, subtitle, intro), and `about.qmd` links. Use only what they told you.
4. For the About body, give them a short outline and let them write it. Offer to polish it afterward with `polish-writing`.
5. Remind them to replace `profile.jpg` with their own photo, or remove the image line from `about.qmd`.
6. Run `uv run quarto preview` and tell them to look at the site.
7. Explain the next step: add a first real project with `new-project`, then delete the sample under `projects/example-penguin-analysis/`.

Do not touch `projects/` or `posts/` in this skill.
