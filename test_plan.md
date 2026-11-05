# Test Plan — Current Sprint: Sprint 4

> **Living document.** Updated each sprint. See `docs/checkpoints/` for snapshots.  
> **Last updated:** S4_1

---

## Purpose

This document outlines the testing strategy for the TaskTracker project, currently covering Sprint 1 user stories US000–US004.

## Test Objectives

| ID | Objective | Success Metric |
|----|-----------|----------------|
| OBJ-1 | Validate environment and app factory (US000) | All sanity tests pass; Flask app initializes |
| OBJ-2 | Validate health check endpoint (US001) | `GET /api/health` returns 200 + `{"status": "ok"}` |
| OBJ-3 | Verify task creation with validation (US002) | `POST /api/tasks` returns 201 for valid; 400 for invalid |
| OBJ-4 | Verify task retrieval (US003) | `GET /api/tasks` returns 200 + JSON array |
| OBJ-5 | Validate CLI interface (US004) | Add/view/menu via terminal with correct output |
| OBJ-6 | Regression safety via CI | All tests pass in GitHub Actions on every push and PR |
| OBJ-7 | Verify task creation with input validation (US002) | `POST /api/tasks` returns 201 for valid; 400 for invalid; error messages are clear |
| OBJ-8 | Verify task retrieval for all states (US003) | `GET /api/tasks` returns 200 + JSON array; handles empty state and invalid methods |
| OBJ-9 | Verify RF001: Routes accessible via Blueprints | All endpoints work through registered blueprints |
| OBJ-10 | Verify RF002: JSON file persistence | Tasks persist to `data/tasks.json` |
| OBJ-11 | Verify US005: Mark task complete | `PUT /api/tasks/<id>` updates `completed` status |
| OBJ-12 | Verify US007: Delete task | `DELETE /api/tasks/<id>` removes task |
| OBJ-13 | Verify US011: Task persistence | All CRUD operations save to JSON file |
| OBJ-14 | Verify US015: Error handling | All errors return consistent JSON format |
| OBJ-15 | Regression testing | All Sprint 1 features still work |
| OBJ-16 | Verify Task class attributes and behavior (RF004) | `Task` instantiates correctly; `mark_complete()` works |
| OBJ-17 | Verify TaskService CRUD methods (RF005) | All four methods return correct results |
| OBJ-18 | Verify TaskStorage wrapper (RF006A) | `load_tasks()` and `save_tasks()` work via wrapper |
| OBJ-19 | Verify dependency injection (RF006B/C) | Routes use `current_app.task_service` |
| OBJ-20 | Verify E2E API behavior via requests (RF008) | All CRUD endpoints return correct responses |
| OBJ-21 | Verify MockTaskService isolation (RF008) | Unit tests run without file I/O |
| OBJ-22 | Regression — all Sprint 2 endpoints still work | All existing tests pass after refactor |
| OBJ-23 | SQA Tooling Review — mypy configuration verified and enforced | `uv run mypy app/` returns `Success: no issues found` |
| OBJ-24 | Verify `ITaskRepository` ABC defines the correct interface | ABC importable; concrete classes satisfy all abstract methods |
| OBJ-25 | Verify `FileTaskRepository` satisfies `ITaskRepository` contract | All contract tests pass |
| OBJ-26 | Verify `pytest-mock` route tests equivalent to hand-rolled mock | Same assertions, mocker fixture used |
| OBJ-27 | Verify CLI retirement does not break existing tests | Full test suite passes after `cli/` removed |
| OBJ-28 | Regression — all Sprint 3 tests pass after refactor | All existing tests pass unchanged |
| OBJ-28a | Verify CI pipeline runs the same checks once per PR | One run per PR, none on merge; lint → type-check → test steps all run; image/docs-only PRs skip CI |

## Test Scope

### In Scope
* Flask app factory and environment (US000)
* Health check API (US001)
* Add task via API with validation (US002)
* View tasks via API (US003)
* CLI add/view/menu (US004)
* Task creation via POST /api/tasks with validation (US002)
* Task retrieval via GET /api/tasks for all states (US003)
* Input validation: required fields, error handling
* Edge cases: empty list, invalid HTTP methods
* Mark task complete via PUT /api/tasks/<id> (US005)
* Delete task via DELETE /api/tasks/<id> (US007)
* JSON file persistence — all CRUD operations (US011)
* Global error handling — 400 and 404 (US015)
* Regression: all Sprint 1 endpoints unchanged
* Task class unit tests — RF004
* TaskService CRUD unit tests — RF005
* TaskStorage wrapper unit tests — RF006A
* Dependency injection integration tests — RF006B/C
* E2E requests-based API tests — RF008
* MockTaskService for isolated route tests — RF008
* Regression: all Sprint 2 tests pass after refactor
* `ITaskRepository` ABC — RF009
* `FileTaskRepository` contract tests — RF010
* pytest-mock route tests — RF012
* CLI retirement verification — RF013
* CI pipeline tune-up verification — [SQA] (RISK-CI-01)
* Regression: all Sprint 3 tests pass unchanged

### Out of Scope
* Persistent storage (Sprint 2+)
* Authentication / authorization
* Performance testing
* UI testing (Sprint 4+)

## CI Test Execution Strategy

- **When CI runs:** on every pull request to `main`; not on merge (the PR run already tested the merge result)
- **What runs, in order:** ruff → mypy → Flask server → pytest with coverage → Stop Flask server — a failed step skips the rest; the stop step always runs (`if: always()`, carried over from S3_2)
- **What does not trigger CI:** changes to only `**.md`, `docs/**`, or `images/**`
- **Exit criterion:** all CI steps green on the PR before merge
- **Constraint:** shared GitHub Actions minutes budget — see RISK-CI-01

## Test Types and Tools

| Type | Tool | When Used |
|------|------|-----------|
| Automated (Unit/API) | pytest | Every branch; required for CI |
| Code Coverage | pytest-cov | Every CI run |
| CI Validation | GitHub Actions | Every pull request to `main` (not on merge — see CI Test Execution Strategy) |
| Manual | curl / Postman / CLI | Validating endpoints manually |

## SQA Tools

| Tool | Command | Scope |
|------|---------|-------|
| pytest | `uv run pytest -v` | All tests |
| coverage | `uv run pytest --cov=app` | Production code |
| ruff | `uv run ruff check .` | Full codebase |
| bandit | `uv run bandit -r app/` | Production code |
| pre-commit | `uv run pre-commit run --all-files` | Planned — activated in S5_2 (RF017) with ruff, bandit, and mypy hooks |
| mypy | `uv run mypy app/` | `disallow_untyped_defs = true`; `exclude = ["tests/", "setup_browsers.py"]` in `[tool.mypy]`; production code only |
| pytest-mock | `mocker.MagicMock()` | Replaces hand-rolled `MockTaskService` from Sprint 3 |
| GitHub Actions | `python-app.yml` | One job on each PR: ruff → mypy → pytest. Tuned in S4_1 — no run on merge; image/docs-only PRs skip CI |

## Pass/Fail Criteria

* All automated tests pass locally and in CI
* Code coverage ≥ 80% for `app/` module
* Manual tests produce expected output
* All automated tests for US002 and US003 pass locally and in CI
* Input validation tests verify 400 responses for invalid data
* All test cases documented with clear acceptance criteria

---

## RF003 — Test Organization Strategy (S2_2 Delta)

### conftest.py Shared Fixtures
Located at `tests/conftest.py`. Provides fixtures to ALL test files automatically:
- `client` — creates Flask test client with `TESTING=True`
- `reset_tasks` — clears `tasks.json` before/after each test (`autouse=True`)
- Reset strategy: File-only reset (`save_tasks([])`) — no API route needed for Sprint 2

> **Note:** When database is introduced (Sprint 4+), `reset_tasks` will need `POST /api/tasks/reset` route instead. Comment planted in `conftest.py` to flag this.

### test_tasks.py Deprecation
Original `tests/test_tasks.py` split into focused files:
- `tests/tasks/test_add_task.py` — TC-US002 cases
- `tests/tasks/test_get_tasks.py` — TC-US003 cases

File deleted after split to prevent duplicate test execution.

## Risks

### RISK-CI-01 — CI Minutes Budget Exhaustion

- **Identified:** S3_1 — the GitHub Actions usage report at the end of S2_2 showed the class's shared 3,000-minute pool fully used
- **Impact:** High — when the pool runs out, CI stops for every student until the monthly reset, so no PR can be verified
- **Likelihood:** High — Sprint 4 and 5 labs add more PRs and heavier workflows (Playwright, Robot Framework)
- **Root cause:** Pipeline design, not usage — 3 jobs × 2 triggers (PR + merge) ≈ 6 billed minutes per PR
- **Planned mitigation:** Sprint 4 (S4_1) — run CI on pull requests only, in one job; skip image-only changes
- **Monitoring:** Organization usage report reviewed monthly
- **Status:** Mitigated in S4_1 — [SQA] CI Pipeline Tune-Up (PR-only, single job, images ignored). Continue monthly monitoring.

---

## SQA Tooling Review — S3_2 Delta

### What Changed and Why

The `type-check` CI job running `uv run mypy .` was already present in `python-app.yml` from Sprint 2. The SQA tooling review in S3_2 revealed it wasn't properly configured — no `[tool.mypy]` section existed in `pyproject.toml`. mypy was running with defaults, silently passing even unannotated code.

**Actions taken:**
1. Added `[tool.mypy]` to `pyproject.toml` with `ignore_missing_imports = true`
2. Annotated `Task` class with full PEP 484 type hints
3. Tightened to `disallow_untyped_defs = true` — 20 errors found across 5 files
4. Fixed all 20 errors; mypy clean on `app/`
5. Added `exclude = ["tests/", "setup_browsers.py"]` — production code only

No CI command change was needed — `pyproject.toml` is the control. SQA manages scope through configuration, not CI commands.

### Boundary Decision

mypy is scoped to `app/` only via `exclude` in `pyproject.toml`. Test files use pytest fixtures and dynamic patterns that mypy flags — not because they are bugs, but because pytest's dynamic patterns are a known mypy limitation. Enforcing types on production code while leaving test implementation flexible is the majority professional practice.

**Impact:** All future PRs must pass `uv run mypy app/` in CI. Unannotated functions in `app/` will block merges.

---

## CI Pipeline Finding — S3_2 Delta

### What Was Found

When the `test` job was extended to start a Flask server for E2E tests, SQA/DevOps found that CI could fail **even when every test passed**. The failing step was **Post Install uv** (setup-uv's cache cleanup), which timed out after exactly 5 minutes with exit code 2.

**Root cause:** The Flask server was started with `uv run` and never stopped, so the running process held uv's cache and the cleanup could not finish (missing **teardown**). The workflow does not pin a uv version, so a newer uv release (0.13.0) changed cleanup behavior and exposed the problem (**environment drift**).

### Actions Taken

| Action | When | Status |
|--------|------|--------|
| Added `Stop Flask server` step with `if: always()` to the `test` job | S3_2 | ✅ Done — immediate fix |
| Logged issue `CI: pin uv version in GitHub Actions workflows` (#N) | S3_2 | 🔓 Open |
| Pin uv version on every `setup-uv` step | S4_3 | ⏳ Planned — permanent fix |

### Risk

| Risk | Likelihood | Impact | Mitigation |
|------|-----------|--------|------------|
| Unpinned CI tools (uv) change behavior between runs and break CI with no code change | Medium | High — all PRs blocked | Teardown step added (S3_2); version pinning planned (S4_3, issue #N) |
