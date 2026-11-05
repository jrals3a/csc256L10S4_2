# Test Cases — Current Sprint: Sprint 4

> **Living document.** Updated each sprint. See `docs/checkpoints/` for snapshots.  
> **Last updated:** S4_1

---

Test cases for US000–US004. Each case maps to acceptance criteria in `tt_user_stories.md`.

---

## US000 — Initial Setup & Validation

### TC-US000-001: pytest Runs Successfully

| Field | Detail |
|-------|--------|
| **ID** | TC-US000-001 |
| **Description** | Verify pytest can discover and run tests |
| **Type** | Automated |
| **Steps** | Run `uv run pytest -v` |
| **Expected** | Tests collected and passed |

### TC-US000-002: create_app() Returns Flask Instance

| Field | Detail |
|-------|--------|
| **ID** | TC-US000-002 |
| **Description** | Verify app factory returns valid Flask app |
| **Type** | Automated |
| **Expected** | `isinstance(app, Flask)` is True |

### TC-US000-003: Flask Returns 404 Without Routes

| Field | Detail |
|-------|--------|
| **ID** | TC-US000-003 |
| **Description** | Verify app returns 404 at root before routes registered |
| **Type** | Automated |
| **Expected** | `GET /` returns 404 |

### TC-US000-004: Flask Application Runs Locally

| Field | Detail |
|-------|--------|
| **ID** | TC-US000-004 |
| **Description** | Verify Flask starts without errors |
| **Type** | Manual |
| **Steps** | Run `uv run python -m app` in terminal |
| **Expected** | App starts; terminal shows running on `http://127.0.0.1:5000` |

---

## US001 — Health Check Endpoint

### TC-US001-001: Health Check Returns 200 + JSON

| Field | Detail |
|-------|--------|
| **ID** | TC-US001-001 |
| **Description** | `GET /api/health` returns 200 and `{"status": "ok"}` |
| **Type** | Automated |
| **Expected** | status_code == 200; body == `{"status": "ok"}` |

---

## US002 — Add Task via API

### TC-US002-001: Add Valid Task

| Field | Detail |
|-------|--------|
| **ID** | TC-US002-001 |
| **User Story** | US002: Add a task via POST /api/tasks |
| **Description** | When a valid title and description are provided, the API accepts the task and returns it with an auto-assigned ID |
| **Type** | Automated (Integration) |
| **Steps** | Send POST request to `/api/tasks` with JSON: `{"title": "Buy Milk", "description": "2% and whole"}` |
| **Expected Result** | 201 Created; response includes `{"id": 1, "title": "Buy Milk", "description": "2% and whole"}` |
| **Acceptance Criteria** | Status code is 201; response JSON includes all three fields (id, title, description) |

### TC-US002-002: Empty Title Returns 400

| Field | Detail |
|-------|--------|
| **ID** | TC-US002-002 |
| **Description** | When title is an empty string, the API rejects with 400 Bad Request |
| **Type** | Automated (Integration) |
| **Steps** | Send POST to `/api/tasks` with `{"title": "", "description": "Empty title"}` |
| **Expected Result** | 400 Bad Request; error message mentions "title" |
| **Acceptance Criteria** | Status code is 400; empty/whitespace-only titles are rejected |

### TC-US002-003: Missing Title Returns 400

| Field | Detail |
|-------|--------|
| **ID** | TC-US002-003 |
| **Description** | When title field is completely missing, the API rejects with 400 |
| **Type** | Automated (Integration) |
| **Steps** | Send POST to `/api/tasks` with `{"description": "No title provided"}` |
| **Expected Result** | 400 Bad Request; error message mentions "title" |
| **Acceptance Criteria** | Status code is 400; missing title field is caught and rejected |

### TC-US002-004: Empty Request Returns 400

| Field | Detail |
|-------|--------|
| **ID** | TC-US002-004 |
| **Description** | When request body is empty JSON `{}`, the API rejects with 400 |
| **Type** | Automated (Integration) |
| **Steps** | Send POST to `/api/tasks` with `{}` |
| **Expected Result** | 400 Bad Request |
| **Acceptance Criteria** | Status code is 400; completely empty requests are caught |

---

## US003 — View Tasks

### TC-US003-001: View Tasks When None Exist

| Field | Detail |
|-------|--------|
| **ID** | TC-US003-001 |
| **User Story** | US003: View all tasks via GET /api/tasks |
| **Description** | When no tasks exist, GET /api/tasks returns empty list |
| **Type** | Automated (Integration) |
| **Steps** | Send GET to `/api/tasks` when task list is empty |
| **Expected Result** | 200 OK; response is `[]` |
| **Acceptance Criteria** | Status code is 200; response is valid JSON array; length is 0 |

### TC-US003-002: View Tasks When Tasks Exist

| Field | Detail |
|-------|--------|
| **ID** | TC-US003-002 |
| **Description** | When tasks exist, GET /api/tasks returns all tasks |
| **Type** | Automated (Integration) |
| **Steps** | Create 2 tasks via POST, then GET `/api/tasks` |
| **Expected Result** | 200 OK; array length is 2; all fields present |
| **Acceptance Criteria** | Status code is 200; array contains all added tasks with id, title, description |

### TC-US003-003: Invalid HTTP Method Returns 405

| Field | Detail |
|-------|--------|
| **ID** | TC-US003-003 |
| **Description** | PUT /api/tasks returns 405 Method Not Allowed |
| **Type** | Automated (Integration) |
| **Steps** | Send PUT to `/api/tasks` with valid JSON body |
| **Expected Result** | 405 Method Not Allowed |
| **Acceptance Criteria** | Status code is 405; no task is created or modified |

---

## US004 — CLI Interface

### TC-US004-001: CLI Add Task

| Field | Detail |
|-------|--------|
| **ID** | TC-US004-001 |
| **Description** | CLI prompts for task and stores it |
| **Type** | Manual |
| **Expected** | Task stored in memory; confirmation printed |

### TC-US004-002: CLI View Tasks

| Field | Detail |
|-------|--------|
| **ID** | TC-US004-002 |
| **Description** | CLI displays all stored tasks |
| **Type** | Manual |
| **Expected** | Tasks listed with id, title, description |

### TC-US004-003: CLI Menu Loop

| Field | Detail |
|-------|--------|
| **ID** | TC-US004-003 |
| **Description** | CLI menu allows add/view/quit |
| **Type** | Manual |
| **Expected** | Menu loops; Quit exits cleanly |

---

## US005 — Mark Task Complete

### TC-US005-001: Mark Task Complete with Valid ID
| Field | Detail |
|-------|--------|
| **ID** | TC-US005-001 |
| **Type** | Automated |
| **Steps** | Send `PUT /api/tasks/1` |
| **Expected** | 200 OK; task with `completed: true` |

### TC-US005-002: Mark Non-Existent Task
| Field | Detail |
|-------|--------|
| **ID** | TC-US005-002 |
| **Type** | Automated |
| **Steps** | Send `PUT /api/tasks/999` |
| **Expected** | 404 Not Found with error JSON |

---

## US007 — Delete Task

### TC-US007-001: Delete Existing Task
| Field | Detail |
|-------|--------|
| **ID** | TC-US007-001 |
| **Type** | Automated |
| **Steps** | Send `DELETE /api/tasks/1` |
| **Expected** | 200 OK; `{"message": "Task deleted"}` |

### TC-US007-002: Verify Task Removed from List
| Field | Detail |
|-------|--------|
| **ID** | TC-US007-002 |
| **Type** | Automated |
| **Steps** | Send `GET /api/tasks` after deletion |
| **Expected** | Deleted task not in response array |

### TC-US007-003: Delete Non-Existent Task
| Field | Detail |
|-------|--------|
| **ID** | TC-US007-003 |
| **Type** | Automated |
| **Steps** | Send `DELETE /api/tasks/999` |
| **Expected** | 404 Not Found with error JSON |

---

## US011 — Persist Tasks

### TC-US011-001: Save and Load Tasks
| Field | Detail |
|-------|--------|
| **ID** | TC-US011-001 |
| **Type** | Automated |
| **Steps** | `save_tasks()` then `load_tasks()` |
| **Expected** | Tasks match what was saved |

### TC-US011-002: Empty Task List Returns []
| Field | Detail |
|-------|--------|
| **ID** | TC-US011-002 |
| **Type** | Automated |
| **Steps** | `save_tasks([])` then `load_tasks()` |
| **Expected** | Returns empty list |

---

## US015 — Error Handling

### TC-US015-001: Missing Title Returns 400
| Field | Detail |
|-------|--------|
| **ID** | TC-US015-001 |
| **Type** | Automated |
| **Steps** | `POST /api/tasks` with `{}` |
| **Expected** | 400; `{"error": "Title is required"}` |

### TC-US015-002: Non-Existent Task Returns 404
| Field | Detail |
|-------|--------|
| **ID** | TC-US015-002 |
| **Type** | Automated |
| **Steps** | `PUT /api/tasks/999` |
| **Expected** | 404 Not Found; `{"error": "Not Found"}` |

---

## RF003 — Test Structure Refactor

### TC-RF003-001: pytest Discovers All Tests in Subfolders
| Field | Detail |
|-------|--------|
| **ID** | TC-RF003-001 |
| **Type** | Automated |
| **Steps** | Run `uv run pytest -v` from project root |
| **Expected** | All test files in tasks/, storage/, error/, health/ discovered and run |

### TC-RF003-002: conftest.py Fixtures Available Without Import
| Field | Detail |
|-------|--------|
| **ID** | TC-RF003-002 |
| **Type** | Automated |
| **Steps** | Run any test file that uses client fixture without local fixture definition |
| **Expected** | Tests pass without ImportError or fixture-not-found errors |

### TC-RF003-003: reset_tasks Fixture Clears State Between Tests
| Field | Detail |
|-------|--------|
| **ID** | TC-RF003-003 |
| **Type** | Automated |
| **Steps** | Run full test suite — verify no test depends on state from a prior test |
| **Expected** | All 21 tests pass; no order-dependent failures |

---

## RF004 — Task Class

### TC-RF004-001: Task Instantiates with Correct Attributes
| Field | Detail |
|-------|--------|
| **ID** | TC-RF004-001 |
| **Type** | Automated (Unit) |
| **Steps** | `task = Task(id=1, title="Buy milk", description="2%")` |
| **Expected** | `task.id == 1`, `task.title == "Buy milk"`, `task.completed == False` |

### TC-RF004-002: mark_complete() Sets completed to True
| Field | Detail |
|-------|--------|
| **ID** | TC-RF004-002 |
| **Type** | Automated (Unit) |
| **Steps** | Create task, call `task.mark_complete()` |
| **Expected** | `task.completed == True` |

### TC-RF004-003: Task completed Defaults to False
| Field | Detail |
|-------|--------|
| **ID** | TC-RF004-003 |
| **Type** | Automated (Unit) |
| **Steps** | Create `Task(id=1, title="Test")` without completed argument |
| **Expected** | `task.completed == False` |

### TC-RF004-004: to_dict() Returns Correct Dictionary
| Field | Detail |
|-------|--------|
| **ID** | TC-RF004-004 |
| **Type** | Automated (Unit) |
| **Steps** | `task = Task(id=1, title="Buy milk", description="2%")` then `task.to_dict()` |
| **Expected** | Returns `{"id": 1, "title": "Buy milk", "description": "2%", "completed": False}` |

---

## RF005 — TaskService

### TC-RF005-001: add_task() Returns Task with Correct Fields
| Field | Detail |
|-------|--------|
| **ID** | TC-RF005-001 |
| **Type** | Automated (Unit) |
| **Steps** | `service.add_task("Buy milk", "2%")` |
| **Expected** | Returns task with `title="Buy milk"`, `completed=False`, `id` assigned |

### TC-RF005-002: get_tasks() Returns Empty List Initially
| Field | Detail |
|-------|--------|
| **ID** | TC-RF005-002 |
| **Type** | Automated (Unit) |
| **Steps** | `service.get_tasks()` on fresh service |
| **Expected** | Returns `[]` |

### TC-RF005-003: complete_task() Sets completed to True
| Field | Detail |
|-------|--------|
| **ID** | TC-RF005-003 |
| **Type** | Automated (Unit) |
| **Steps** | Add task, call `service.complete_task(task_id)` |
| **Expected** | Task `completed == True` |

### TC-RF005-004: delete_task() Removes Task
| Field | Detail |
|-------|--------|
| **ID** | TC-RF005-004 |
| **Type** | Automated (Unit) |
| **Steps** | Add task, call `service.delete_task(task_id)` |
| **Expected** | Task no longer in `service.get_tasks()` |

---

## RF008 — Automated API Tests (requests)

### TC-RF008-001: POST /api/tasks Returns 201
| Field | Detail |
|-------|--------|
| **ID** | TC-RF008-001 |
| **Type** | Automated (E2E) |
| **Steps** | `requests.post("http://127.0.0.1:5000/api/tasks", json={"title": "Test"})` |
| **Expected** | 201 Created; task JSON in response |

### TC-RF008-002: GET /api/tasks Returns 200
| Field | Detail |
|-------|--------|
| **ID** | TC-RF008-002 |
| **Type** | Automated (E2E) |
| **Expected** | 200 OK; array of tasks |

### TC-RF008-003: PUT /api/tasks/<id> Returns 200
| Field | Detail |
|-------|--------|
| **ID** | TC-RF008-003 |
| **Type** | Automated (E2E) |
| **Expected** | 200 OK; task with `completed: true` |

### TC-RF008-004: DELETE /api/tasks/<id> Returns 200
| Field | Detail |
|-------|--------|
| **ID** | TC-RF008-004 |
| **Type** | Automated (E2E) |
| **Expected** | 200 OK; `{"message": "Task deleted"}` |

---

## RF008 — MockTaskService Route Tests (Hand-Rolled)

### TC-RF008-009: MockTaskService Injected via create_app(service=)
| Field | Detail |
|-------|--------|
| **ID** | TC-RF008-009 |
| **Type** | Automated (Unit) |
| **Steps** | Pass `MockTaskService()` to `create_app(service=mock)` in test fixture |
| **Expected** | Routes use mock service — no file I/O; tests run in isolation |

### TC-RF008-010: POST /api/tasks with MockTaskService Returns 201
| Field | Detail |
|-------|--------|
| **ID** | TC-RF008-010 |
| **Type** | Automated (Unit) |
| **Steps** | POST `/api/tasks` via Flask test client with `MockTaskService` injected |
| **Expected** | 201 Created; task stored in mock memory — no tasks.json written |

### TC-RF008-011: GET /api/tasks with MockTaskService Returns Empty List
| Field | Detail |
|-------|--------|
| **ID** | TC-RF008-011 |
| **Type** | Automated (Unit) |
| **Steps** | GET `/api/tasks` via Flask test client with fresh `MockTaskService` injected |
| **Expected** | 200 OK; `[]` returned |

---

## SQA Tooling Review — mypy Type Checking

### TC-MYPY-001: mypy Clean on app/ After Annotations
| Field | Detail |
|-------|--------|
| **ID** | TC-MYPY-001 |
| **Type** | Automated (Static) |
| **Steps** | `uv run mypy app/` after all S3_2 annotations applied |
| **Expected** | `Success: no issues found in N source files` |

### TC-MYPY-002: mypy CI Job Passes on main
| Field | Detail |
|-------|--------|
| **ID** | TC-MYPY-002 |
| **Type** | Automated (CI) |
| **Steps** | Push to main — observe `type-check` job in GitHub Actions |
| **Expected** | `type-check` job passes; green checkmark in Actions tab |

---

## CI Pipeline — Teardown

### TC-CI-001: Flask Server Stopped After CI Tests
| Field | Detail |
|-------|--------|
| **ID** | TC-CI-001 |
| **Type** | Automated (CI) |
| **Steps** | Open a PR — observe the `test` job in GitHub Actions |
| **Expected** | `Stop Flask server` step passes; **Post Install uv** completes in seconds (not a 5-minute timeout); job green |

---

## RF009 — ITaskRepository Interface

### TC-RF009-001: ITaskRepository Cannot Be Instantiated Directly
| Field | Detail |
|-------|--------|
| **ID** | TC-RF009-001 |
| **Type** | Automated (Unit) |
| **Steps** | Attempt `ITaskRepository()` |
| **Expected** | `TypeError` raised — abstract class cannot be instantiated |

### TC-RF009-002: FileTaskRepository Is Recognized as ITaskRepository
| Field | Detail |
|-------|--------|
| **ID** | TC-RF009-002 |
| **Type** | Automated (Unit) |
| **Steps** | `isinstance(FileTaskRepository(), ITaskRepository)` |
| **Expected** | `True` |

---

## RF010 — FileTaskRepository

### TC-RF010-001: add_task() Returns Dict with Correct Fields
| Field | Detail |
|-------|--------|
| **ID** | TC-RF010-001 |
| **Type** | Automated (Contract) |
| **Steps** | `repo.add_task("Buy milk", "2%")` |
| **Expected** | Returns dict with `id`, `title`, `description`, `completed: False` |

### TC-RF010-002: get_all_tasks() Returns Empty List Initially
| Field | Detail |
|-------|--------|
| **ID** | TC-RF010-002 |
| **Type** | Automated (Contract) |
| **Steps** | Fresh `FileTaskRepository()` → `repo.get_all_tasks()` |
| **Expected** | Returns `[]` |

### TC-RF010-004: complete_task() Sets completed to True
| Field | Detail |
|-------|--------|
| **ID** | TC-RF010-004 |
| **Type** | Automated (Contract) |
| **Steps** | Add task → `repo.complete_task(task_id)` |
| **Expected** | Returns task dict with `completed: True` |

### TC-RF010-008: clear_tasks() Removes All Tasks
| Field | Detail |
|-------|--------|
| **ID** | TC-RF010-008 |
| **Type** | Automated (Contract) |
| **Steps** | Add 3 tasks → `repo.clear_tasks()` → `repo.get_all_tasks()` |
| **Expected** | Returns `[]` |

> The lab's `test_file_task_repository.py` has eight RF010 contract tests (TC-RF010-001 through 008). The four above are representative; the IDs match the test docstrings.

---

## RF012 — pytest-mock Route Tests

### TC-RF012-001: POST /api/tasks with mocker Returns 201
| Field | Detail |
|-------|--------|
| **ID** | TC-RF012-001 |
| **Type** | Automated (Unit) |
| **Steps** | `mocker.MagicMock()` injected → POST `/api/tasks` |
| **Expected** | 201 Created; no file I/O |

### TC-RF012-005: mocker Verifies Route Delegates to Service with Correct Args
| Field | Detail |
|-------|--------|
| **ID** | TC-RF012-005 |
| **Type** | Automated (Unit) |
| **Steps** | POST `/api/tasks` with mocker → `mock.add_task.assert_called_once_with(...)` |
| **Expected** | Assertion passes — confirms route delegates to service with the request's arguments |

> The lab's `test_routes_with_mock.py` has seven RF012 tests (TC-RF012-001 through 007). The two above are representative; the IDs match the test docstrings.

---

## RF013 — CLI Retirement

### TC-RF013-001: Full Test Suite Passes After CLI Removal
| Field | Detail |
|-------|--------|
| **ID** | TC-RF013-001 |
| **Type** | Automated (Regression) |
| **Steps** | `uv run python -m pytest -v` after CLI retirement PR merged |
| **Expected** | All tests pass — CLI removal has no effect on test suite |

### TC-RF013-002: cli/ Directory No Longer Exists
| Field | Detail |
|-------|--------|
| **ID** | TC-RF013-002 |
| **Type** | Manual (Verification) |
| **Steps** | After the CLI retirement PR merges, `ls cli` on `main` (or browse the repo on GitHub) |
| **Expected** | `cli/` does not exist; no remaining imports or references to `cli` in the codebase |

---

## SQA — CI Pipeline Tune-Up

### TC-SQA-002: CI Runs on the PR, Not on Merge
| Field | Detail |
|-------|--------|
| **ID** | TC-SQA-002 |
| **Type** | Manual (CI verification) |
| **Steps** | Merge the `ci/pipeline-tune-up` PR → Actions tab → filter **Python application** |
| **Expected** | The PR run is the newest run; no "Merge pull request" run appears after it |

### TC-SQA-003: One Job Runs All Checks in Order
| Field | Detail |
|-------|--------|
| **ID** | TC-SQA-003 |
| **Type** | Manual (CI verification) |
| **Steps** | Open the PR's **Lint, type-check, test** check → expand steps |
| **Expected** | Lint (ruff), Type check (mypy), Flask start/wait, Test (pytest), Stop Flask server steps all green in one job |

### TC-SQA-004: Docs/Image-Only PR Skips CI
| Field | Detail |
|-------|--------|
| **ID** | TC-SQA-004 |
| **Type** | Manual (CI verification) |
| **Steps** | Open a PR that changes only files in `docs/` or `images/` (e.g. this assignment's docs PR) |
| **Expected** | No Python application check runs on the PR |
