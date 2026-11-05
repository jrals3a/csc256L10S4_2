# Sprint Plan — Current Sprint: Sprint 4

> **Living document.** Updated each sprint. See `docs/checkpoints/` for snapshots.  
> **Last updated:** S4_1

---

# Sprint 4 Planning

Sprint 4 introduces the **repository pattern** — a professional software design technique that decouples `TaskService` from any specific persistence backend. By defining a formal `ITaskRepository` interface, the application can swap between file storage, a database, or a test double without changing any business logic or route code. Sprint 4 also introduces `pytest-mock` as the professional standard for mock-based testing, retires the CLI, and introduces the web UI.

## 1. Sprint Goals

### S4_1 — Repository Pattern and pytest-mock
- 🔁 **RF009** — Define `ITaskRepository` ABC: formal interface contract
- 🔁 **RF010** — Implement `FileTaskRepository`: wraps `TaskStorage`, implements `ITaskRepository`
- 🔁 **RF012** — Replace hand-rolled `MockTaskService` with `pytest-mock` (`mocker` fixture)
- 🔁 **RF013** — Retire CLI: tightly coupled to file storage, cannot participate in repository pattern
- 🛠️ **[SQA] CI Pipeline Tune-Up** — run CI once per PR in one job; skip image-only changes (mitigates RISK-CI-01)

### S4_2 — Database Repository and Web UI
- 🔁 **RF011** — Implement `DatabaseTaskRepository`: SQLAlchemy-backed
- ✅ **US012** — Add Task via Web Form: Flask templates, Jinja2
- ✅ **US036** — Form Validation and Feedback
- ✅ **US033** — User Journey: Manual Task Workflow via Web UI

## 2. User Stories in Scope

* **US012** — Add Task via Web Form (S4_2)
* **US033** — Manual Task Workflow via Web UI (S4_2)
* **US036** — Form Validation and Feedback (S4_2)

## 3. Test Planning Overview

- **TDD:** Write repository contract tests BEFORE implementing `FileTaskRepository`
- **Contract testing:** Same test suite runs against `FileTaskRepository` (S4_1) and `DatabaseTaskRepository` (S4_2)
- **Coverage:** ≥ 80%
- **Tools:** `pytest`, `pytest-cov`, `pytest-mock`, `requests`, `mypy`, `ruff`, `bandit`

## 4. Tools and Technologies

| Tool | Purpose | Notes |
|------|---------|-------|
| `pytest` | Test runner | `uv run python -m pytest -v` |
| `pytest-cov` | Coverage | ≥ 80% |
| `pytest-mock` | Route mock testing | `mocker.MagicMock()` — replaces hand-rolled `MockTaskService` |
| `requests` | E2E API tests | Unchanged from Sprint 3 |
| `mypy` | Type checking | Already enforced — `disallow_untyped_defs = true` |
| `SQLAlchemy` | ORM for DB repository | S4_2 only |
| `GitHub Actions` | CI — 1 job, PR-only | lint → type-check → test as steps; tuned in S4_1 to cut Actions minutes (RISK-CI-01) |

## 5. Technical Design

### Repository Pattern Architecture

```
HTTP Request
    ↓
Blueprint Route (routes/tasks.py)        ← unchanged
    ↓
TaskService (services/task_service.py)   ← accepts ITaskRepository
    ↓
ITaskRepository (repositories/base.py)   ← interface contract
    ↓
FileTaskRepository  OR  DatabaseTaskRepository
```

### Swappable Backends

```python
create_app()              → FileTaskRepository()      → tasks.json
create_app(use_db=True)   → DatabaseTaskRepository()  → tasks.db
mocker.MagicMock()        → no I/O at all (tests)
```

## 6. Sprint-Level Completion Criteria

- [ ] `ITaskRepository` ABC importable; concrete classes satisfy all abstract methods
- [ ] `FileTaskRepository` passes all repository contract tests
- [ ] Route tests pass using `mocker.MagicMock()` — `MockTaskService` fully removed
- [ ] All Sprint 3 tests pass without modification
- [ ] CLI removed; no broken imports
- [ ] `uv run mypy app/` clean
- [ ] Coverage ≥ 80%
- [ ] GitHub Actions green on all merged PRs
- [ ] CI runs once per PR (no run on merge), in one job; image-only and docs-only PRs skip CI

## 7. Definition of Done

- [ ] All acceptance criteria met
- [ ] TDD approach — contract tests written before implementation
- [ ] All tests pass locally and in CI
- [ ] PR merged to main via GitHub Flow — every change reaches `main` through a PR (CI does not run on direct pushes)
- [ ] No regressions from Sprint 3
