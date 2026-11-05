# Architecture — Current Sprint: Sprint 4

> **Living document.** Updated each sprint. See `docs/checkpoints/` for snapshots.  
> **Last updated:** S4_1

---

## Sprint 3 → Sprint 4 Evolution

Sprint 3 introduced `TaskService` as the business logic layer. Sprint 4 goes one level deeper — introducing the **repository pattern** that separates `TaskService` from any specific persistence backend.

### Sprint 3 State
```
HTTP Request → Route → TaskService → TaskStorage → tasks.json
```

## Sprint 4 Layered Architecture

```
HTTP Request
    ↓
Blueprint Route (routes/tasks.py)        ← HTTP only — unchanged
    ↓
TaskService (services/task_service.py)   ← business logic — unchanged interface
    ↓
ITaskRepository (repositories/base.py)   ← interface contract — NEW
    ↓
FileTaskRepository  OR  DatabaseTaskRepository
    ↓
tasks.json          OR  tasks.db (SQLite)
```

## Key Changes from Sprint 3 to Sprint 4

| Aspect | Sprint 3 | Sprint 4 |
|--------|----------|----------|
| **Persistence dependency** | `TaskService(TaskStorage)` | `TaskService(ITaskRepository)` |
| **Interface contract** | None — duck typing | `ITaskRepository` ABC |
| **Backends available** | File only | File (S4_1) + Database (S4_2) |
| **Mock in tests** | Hand-rolled `MockTaskService` | `mocker.MagicMock()` via pytest-mock |
| **CLI** | Present | **Removed** — tightly coupled, untestable |
| **UI** | None | Flask templates + Jinja2 (S4_2) |
| **CI pipeline** | 3 jobs, runs on PR **and** on merge | 1 job, runs on PR only |

## CLI Retirement — SQA Decision

The CLI called `load_tasks()` and `save_tasks()` directly — bypassing `TaskService` entirely. It could not be tested through any designed interface.

**Lesson:** Code that cannot participate in the architecture's testing seams is a maintenance liability. The CLI's functionality is fully covered by the API — retirement is the correct SQA decision.

## CI Pipeline

`.github/workflows/python-app.yml` — tuned in S4_1 to run once per PR (SQA CI Pipeline Tune-Up, mitigates RISK-CI-01)

| Aspect | Setting |
|--------|---------|
| **Trigger** | `pull_request` to `main` only — no run on merge |
| **Skipped when** | Only `**.md`, `docs/**` or `images/**` files change |
| **Jobs** | One job — *Lint, type-check, test* |
| **Steps (in order)** | ruff → mypy → start Flask → pytest with coverage → stop Flask; a failed step skips the rest, except the stop step (`if: always()`) |
| **Teardown** | `Stop Flask server` step from S3_2 retained — runs even on failure |
| **Safety cap** | `timeout-minutes: 10` |
| **Cost** | ~1–2 billed minutes per PR (was ~6) |

## Test Architecture

```
tests/
├── conftest.py                    # client fixture + reset_tasks (API-based S4+)
│                                  # MockTaskService REMOVED — mocker used instead
├── api/
│   └── test_tasks_api.py          # E2E via requests — unchanged
├── repositories/
│   └── test_file_task_repository.py  # RF010 contract tests
├── storage/
│   └── test_task_storage.py       # Raw I/O tests — unchanged
└── tasks/
    └── test_routes_with_mock.py   # Rewritten: mocker.MagicMock() (RF012)
```
