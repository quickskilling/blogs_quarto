---
name: new-post
description: Scaffold a new blog post under posts/. Use when the student wants to write about something they learned, a decision they made, or a tutorial.
---

# Add a post

Posts are optional. They show how the student thinks. Projects show what they built.

1. Ask: what is the one thing a reader should take away? Who is it for?
2. Create `posts/<slug>/index.qmd` (slug: lowercase, hyphens) with this frontmatter and `draft: true`:

```yaml
---
title: ""
description: ""
author: "<name from _quarto.yml>"
date: "<today, YYYY-MM-DD>"
categories: []
draft: true
---
```

3. Propose a short outline (problem, what I tried, what worked, takeaway). Let the student write the content; offer to react to drafts.
4. Remove `draft: true` only when the student says it is ready to publish.
5. If the post uses code, add `jupyter: python3` and render locally so `_freeze/` is updated.
