# Working with an AI assistant on your portfolio

Your portfolio is evidence of what *you* can do. An AI assistant (Codex, in this course) is a fast collaborator, not a replacement for your judgment. These habits keep the site honest and keep you learning.

## The loop

1. **Give context.** Tell it the goal, the audience, and the files. The repo's `AGENTS.md` already explains the structure.
2. **Ask for a plan before changes** on anything bigger than a typo.
3. **Review every change** with `git diff` before you accept it. Read it. If you cannot explain a line, ask the assistant to explain it, or remove it.
4. **Run the checks**: `uv run python scripts/check_site.py`, then `uv run quarto preview`.
5. **Commit small.** One idea per commit makes mistakes easy to undo.

## What to ask for

| Good use | Example prompt |
|---|---|
| Set up | "Use the setup-portfolio skill." |
| Turn work into a page | "Use the new-project skill. My repo is ..." |
| Critique | "Use the portfolio-review skill. Be harsh." |
| Edit your writing | "Use polish-writing on projects/my-analysis/index.qmd. Give feedback first." |
| Understand code | "Explain what each line of this Quarto cell does." |
| Debug | "quarto render failed with this error. What does it mean, and what are two possible fixes?" |

## What not to do

- **Do not let it invent.** If a page says you improved accuracy by 12%, you must have measured that. Ask: "Which statements on this page did you not get from me?"
- **Do not paste generated text you have not read.** Employers can tell, and interviewers will ask about it.
- **Do not claim skills with no project behind them.** The Skills page is built from your project categories on purpose.
- **Do not paste secrets** (API keys, private data, other people's information) into a prompt or commit them.

## Be able to defend your site

Before sharing the link, pick any project and answer out loud, without notes:

1. What was the question and why did it matter?
2. What did you do, and what did you not do?
3. Why that method instead of another?
4. What would you do differently?

If you cannot, go back to the project and learn the part you skipped. That is the real value of the exercise.

## Disclose your use

Add one honest sentence to your About page or footer, for example: *"I use AI assistants for editing and debugging; the analysis and conclusions are my own."* Follow your course and employer policies.
