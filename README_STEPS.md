# S4_2 Agile Documentation Update: what's here and what's left for you

## What I built

| Path | What it is |
|---|---|
| `task-tracker/` | Local repo, continuing from the S4_1 assignment repo (same history). Phases 1–8 applied as written, except for the deviations listed below. |
| `task-tracker/docs/checkpoints/s4_1/` | Phase 1: 7-file snapshot of the S4_1 living docs |
| `task-tracker/docs/living/` | `architecture`, `test_plan`, `test_cases`, `api_reference`, `class_diagram`, `erd` updated to `Last updated: S4_2`, plus the **new** `user_journey.md`. `sprint_plan.md` is untouched (frozen, still `S4_1`). |
| `task-tracker/images/s4/kahsai-S4_2-agile-docs.md` | PDF template, renamed, with name and date filled in. Repo URL and screenshots are yours. |
| `diffs/` | `git diff` per file for the PR, so you can see what each "Files Changed" screenshot should look like |

History: branches `docs/s4_1-checkpoint` and `docs/s4-2-update`, merged `--no-ff`. The merges are a **local simulation**.
Nothing is pushed, no PR or issue exists on GitHub, and no screenshot has been taken.

## Important: timing

The assignment says to do this **after the S4_2 Lab**. These docs describe code from that lab (`DatabaseTaskRepository`, `app/routes/ui.py`, templates, `db_client` fixture). That code doesn't exist in this repo, because I haven't been given the S4_2 lab. Do the lab first, or at least be aware the docs are ahead of the code. If you send me the S4_2 lab files I can build it too.

## Deviations from the instructions

1. **OBJ numbers collide again.** The assignment adds OBJ-27/28/29, but your test plan already has OBJ-27 (CLI retirement), OBJ-28 (regression) and OBJ-28a (CI). I used **OBJ-29, OBJ-30, OBJ-31** in the same order and wording, and updated the template captions in your copy. Find-and-replace if your instructor wants the literal numbers.
2. **TC-US000-003 is already taken.** The test cases file already defines TC-US000-003 as "Flask Returns 404 Without Routes". The assignment adds a TC-US000-003 "GET / Redirects to /tasks/new" at the end. I added it as instructed and marked the old entry "*(superseded in S4_2 — see TC-US000-003 under Web UI)*", so the ID isn't ambiguous.
3. **API reference is pasted verbatim, but a few lines don't match the actual API.** I checked them against `app/routes/tasks.py`. You may want to flag this to your instructor or fix it in a later PR:
   - Reset returns `{"message": "Tasks reset successfully"}`; the doc says `"Tasks reset"`.
   - A missing title returns `{"error": "Title is required"}`; the doc says `"Title is required and cannot be empty"`.
   - `PUT /api/tasks/<id>` ignores the body; the doc shows a `{"completed": true}` body.
   - Task responses include `"completed"`, and the doc's examples omit it.
   - A missing description is not a 400 (it is optional).
4. **ERD calls `Task` a "dataclass".** In your code, `app/models/task.py` is a plain class. Pasted as given.
5. **`docs/living/readme.md`** already lists `user_journey.md` (from the starter), so no change was needed there.

## Screenshot map (take these yourself, from your PR's Files Changed tab)

PR title: `[s4_2] docs: Sprint 4 agile documentation updates`. Save everything into `images/s4/`.

| # | Save as | File in the PR | Should be visible |
|---|---|---|---|
| 1 | `s4_2_architecture_diff.png` | `architecture.md` | S4_2 stack, new files, `create_app()` selection |
| 2 | `s4_2_test_plan_diff.png` | `test_plan.md` | New objectives (OBJ-29/30/31 in your numbering) and the SQLAlchemy tools row |
| 3 | `s4_2_test_cases_diff.png` | `test_cases.md` | RF011 and web UI cases |
| 4 | `s4_2_api_reference_diff.png` | `api_reference.md` | Full-file replacement; Web UI Routes section |
| 5 | `s4_2_class_diagram_diff.png` | `class_diagram.md` | S4_2 Additions |
| 6 | `s4_2_erd_diff.png` | `erd.md` | Full-file replacement; Mermaid entity and `tasks table` |
| 7 | `s4_2_user_journey.png` | `user_journey.md` | New file, all green |

The API reference and ERD diffs are long. Capture what the template asks for (Web UI Routes; Mermaid entity and table), scrolling if needed.

## Doing it in your real repo

1. `docs/s4_1-checkpoint`: copy your current `docs/living/*.md` to `docs/checkpoints/s4_1/` (Phase 1 commands). PR `[s4_2] docs: S4_1 checkpoint snapshot`. Do not delete the branch.
2. `docs/s4-2-update`: bring in the six updated docs and `user_journey.md` from `task-tracker/docs/living/`, one commit each. They were edited onto my S4_1 versions, so a straight copy matches only if your S4_1 docs are the same. Otherwise re-apply the phases from the assignment.
3. One PR: `[s4_2] docs: Sprint 4 agile documentation updates`. Wait for CI, merge, don't delete the branch.
4. Phase 10 (yours on GitHub.com): close the four S4_2 sub-issues with the exact comments in the assignment. **Leave the Epic open** (RF014 is pending).
5. Export `kahsai-S4_2-agile-docs.md` to PDF, rename it `kahsai-S4_2-agile-docs.pdf`, and submit it on Blackboard under **S4_2 Agile Documentation**.
6. S4_2 Reflection & Learning is a separate assignment.
