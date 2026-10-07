---
name: check-site
description: Build the site and check it is ready to publish. Renders, runs the portfolio checklist, and verifies links. Use before pushing or when something looks broken.
---

# Check the site

1. Run `uv run python scripts/check_site.py`. Group the output into: placeholders, project problems, site-level problems.
2. Run `uv run quarto render` and read any warnings or errors. Fix errors; explain warnings.
3. Check that `_freeze/` is up to date: `git status --short _freeze`. If tracked files are modified or untracked after the render, tell the student to commit them.
4. Look for broken internal links and missing images: search rendered output in `docs/` for `404`-prone paths, and confirm each `image:` in frontmatter exists.
5. Confirm `site-url` in `_quarto.yml` matches `https://<username>.github.io/<repo>`.
6. Report a short checklist: pass, fix before publishing, or nice to have. Offer to fix the mechanical items; leave content decisions to the student.
7. Reminder if they have never published: repo Settings, Pages, Source set to "GitHub Actions".
