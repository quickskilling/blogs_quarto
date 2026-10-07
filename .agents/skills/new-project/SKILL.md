---
name: new-project
description: Scaffold a new portfolio project page by interviewing the student about work they actually did. Use when the student wants to add or turn existing work (a class assignment, repo, analysis) into a project page.
---

# Add a project

A project page is evidence. Build it from what the student really did.

1. **Ask**, a couple of questions at a time:
   - What is the project, and where is the code or data (repo, notebook, folder)? Read it if you have access.
   - What problem or question was it answering? Who cared?
   - What did *they* do versus what was given to them (group work, starter code)?
   - What tools and methods did they use?
   - What was the result? Push for a number or concrete finding.
   - What was hard, and what would they do differently?
2. **Pick a slug** (lowercase, hyphens) and create `projects/<slug>/index.qmd` following the contract in `AGENTS.md`.
3. **Categories are skills.** List existing categories with: `grep -h -A1 "^categories" projects/*/index.qmd`. Reuse names exactly; add a new one only for a skill the project truly demonstrates.
4. Fill the sections from their answers. Where an answer is missing, write a `<!-- TODO: ... -->` comment, not a guess.
5. If the project has analysis code, put it in `{python}` cells so readers can see it, or link to the repo if it is large. Set `jupyter: python3`.
6. Suggest a thumbnail: a chart from the project is best. Save it as `projects/<slug>/thumbnail.png` and set `image:`.
7. Render with `uv run quarto render projects/<slug>/index.qmd`, then run `uv run python scripts/check_site.py` and fix what it flags for this project.
8. Tell the student which claims on the page they should be able to explain out loud, and ask them to read it for accuracy.

Never state a result the student did not give you.
