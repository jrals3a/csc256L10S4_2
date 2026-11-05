# Task Tracker — User Story Backlog


### Iteration Key

- 👤 **Individual Lab** — Completed in Individual Labs

---

> [!NOTE]
> **On engineering refactors:** technical refactors like "introduce a service
> layer" or "add file persistence" aren't customer requirements — they're
> engineering decisions about *how* to build what the customer already agreed to.
> They're intentionally not tracked in this document. See
> `s6_architecture.md` → **How This Architecture Evolved** for that history.

---

## Sprint 1

### US000 — Initial Setup & Validation 👤

**As a developer**, I want to validate the development environment and project scaffolding so I can begin development with confidence.

**Owner:** Dev | **Sprint:** 1 | **Status:** Planned

**Notes:** Ensures local dev environment, GitHub setup, and virtual environment are working. Mirrors the real-world "first commit" milestone in full-stack teams. Introduces pytest and lays the groundwork for TDD.

**Acceptance Criteria:**
- [ ] Repository can be cloned and opened in VS Code
- [ ] Virtual environment activates; `uv sync` installs all dependencies successfully
- [ ] Test framework executes correctly with `uv run pytest`

---

### US001 — Health Check Endpoint 👤

**As a developer or QA engineer**, I want a `/api/health` endpoint that returns system status in JSON, and I want this tested automatically using GitHub Actions, so I can ensure the server is running and verify tests on every push.

**Owner:** Dev | **Sprint:** 1 | **Status:** Planned

**Notes:** Introduces the first API route and automates testing via GitHub Actions CI. A realistic real-world feature that supports monitoring and validates that infrastructure is running — a first step in DevOps pipelines.

**Acceptance Criteria:**
- [ ] `GET /api/health` returns `{"status": "ok"}`
- [ ] Response includes HTTP 200 status code
- [ ] Endpoint has automated test using pytest
- [ ] CI is configured to run the test on every push to main

---

### US002 — Add Task via API 👤

**As a user**, I want to add a new task with a description to my to-do list so I can track tasks. If I forget to enter a task name, I should receive an error so I don't create empty tasks.

**Owner:** Dev | **Sprint:** 1 | **Status:** Planned

**Notes:** Introduces the first POST route and begins enforcing data validation with meaningful API responses. Students use both pytest and manual tools (curl/Postman) to test input validation and persistence. Forms the basis for all future task logic. This requirement's underlying implementation moves into a service layer in Sprint 3 — the requirement and acceptance criteria below are unchanged.

**Acceptance Criteria:**
- [ ] `POST /api/tasks` accepts a JSON body with a task title
- [ ] Task is added to an in-memory list
- [ ] Title field is required; request fails with 400 if missing or empty
- [ ] Whitespace-only title is rejected with 400
- [ ] Valid requests return 201 and include the new task in JSON
- [ ] All logic is covered by unit tests

---

### US003 — View Tasks (List) 👤

**As a user**, I want to view a list of all my tasks so that I can see each task's details.

**Owner:** Dev | **Sprint:** 1 | **Status:** Planned

**Notes:** Introduces the first GET route and the concept of system state. Tests both empty and populated task states. Lays the foundation for understanding JSON structure and return codes. The `completed` field is not part of the initial task object — it is introduced later with US005. This requirement's underlying implementation moves into a service layer in Sprint 3 — the requirement and acceptance criteria below are unchanged.

**Acceptance Criteria:**
- [ ] `GET /api/tasks` returns a JSON array of all tasks
- [ ] Each task includes `id`, `title`, and `description`
- [ ] Endpoint returns 200 with correct structure even when task list is empty
- [ ] Tests validate response structure and content for both empty and populated states

---

### US004 — Add and View Tasks via CLI 👤

**As a user**, I want to add and view tasks using a CLI menu so I can interact with the app from the terminal without using a browser or Postman.

**Owner:** Dev | **Sprint:** 1 | **Status:** Planned

**Notes:** Provides a terminal-based way to manually test task creation and retrieval before the web UI exists. The CLI uses the same in-memory task store as the API — no file persistence yet. Covers add, view, and a menu loop. File persistence is introduced later with US006.

*Consolidates: US027 (View Task Report), US028 (CLI Menu UI)*

**Acceptance Criteria:**
- [ ] CLI prompts for task title and description
- [ ] Task added to in-memory list (no file persistence yet)
- [ ] Confirmation message displayed after successful add
- [ ] CLI displays all stored tasks with `id`, `title`, and `description`
- [ ] Menu provides numbered options: Add / View / Quit
- [ ] Menu loops until user selects Quit
- [ ] Quit exits the CLI cleanly

---

## Sprint 2

### US005 — Mark Task Complete 👤

**As a user**, I want to mark a task as completed so I can focus on remaining tasks.

**Owner:** Dev | **Sprint:** 2 | **Status:** Planned

**Notes:** This requirement's underlying implementation moves into a service layer in Sprint 3 — the requirement and acceptance criteria below are unchanged.

**Acceptance Criteria:**
- [ ] A completed task's `completed` field is set to `true`
- [ ] `PUT /api/tasks/<id>` marks the specified task complete
- [ ] Invalid task IDs return a 404 error
- [ ] Changes are saved to `data/tasks.json`
- [ ] Unit tests cover valid and invalid use cases

---

### US006 — CLI: Add Task with Persistence 👤

**As a user**, I want to add a task using the CLI so I can manually test the logic and persistence before transitioning to the web UI.

**Owner:** Dev | **Sprint:** 2 | **Status:** Planned

**Notes:** Extends US004 (in-memory CLI) by adding file persistence via `data/tasks.json`. Complete US004 before starting US006. In the current curriculum, this isn't delivered as its own dedicated phase — it's folded into a Sprint 2 storage persistence refactor. The CLI is an interim manual testing tool and learning aid — it will be deprecated when the web UI and Playwright automation are introduced later.

**Acceptance Criteria:**
- [ ] User can enter a task title and optional description via CLI prompt
- [ ] Task is persisted to `data/tasks.json`
- [ ] CLI confirms success with a message and task ID
- [ ] Errors are shown if input is invalid (e.g., blank title)
- [ ] Tasks persist between CLI sessions (read from JSON file on startup)

---

### US007 — Remove Task 👤

**As a user**, I want to delete a task from my list to keep it up to date.

**Owner:** Dev | **Sprint:** 2 | **Status:** Planned

**Notes:** This requirement's underlying implementation moves into a service layer in Sprint 3 — the requirement and acceptance criteria below are unchanged.

**Acceptance Criteria:**
- [ ] `DELETE /api/tasks/<id>` deletes the specified task
- [ ] Nonexistent task IDs return 404
- [ ] Deleted tasks no longer appear in the list
- [ ] Changes are saved to `data/tasks.json`
- [ ] Unit tests cover valid and invalid deletions

---

### US011 — Persist Tasks 👤

**As a user**, I want tasks saved between sessions so I don't lose my list.

**Owner:** Dev | **Sprint:** 2 | **Status:** Planned

**Acceptance Criteria:**
- [ ] Tasks are saved to `data/tasks.json`
- [ ] Tasks are loaded from the file on app startup
- [ ] Adding, editing, or deleting a task updates the file
- [ ] File is formatted as a valid JSON array
- [ ] Functionality is covered by integration tests

---

### US015 — API Error Handling 👤

**As a developer**, I want consistent JSON error responses for all API errors so clients can handle failures predictably.

**Owner:** Dev | **Sprint:** 2 | **Status:** Planned

**Acceptance Criteria:**
- [ ] Create a global error handler using `@app.errorhandler`
- [ ] All 400, 404, and 500 errors return a JSON body like `{"error": "Message here"}`
- [ ] Errors are logged or printed for debugging
- [ ] Tests verify that error format is consistent for expected error cases

---

## Sprint 3

> [!NOTE]
> Not every lab in a sprint introduces a new story — some labs focus on testing
> technique or tooling using functionality that already exists.

### US012 — Add Task via Web Form 👤

**As a user**, I want to add tasks through a web form interface so I can use the application easily without using Postman or CLI.

**Owner:** Frontend/Dev | **Sprint:** 4 | **Status:** Planned

**Acceptance Criteria:**
- [ ] Create a simple HTML form for task creation (title and description)
- [ ] Submitting the form with valid input sends a POST request to `/tasks/new`
- [ ] The form handles and displays error messages when title is missing
- [ ] On success, the new task is visible in the updated list or a success message is shown
- [ ] UI is tested using Playwright to verify valid and invalid input handling

---

### US036 — Form Validation and Feedback (Web) 👤

**As a user**, I want real-time validation and feedback when submitting forms with errors so that I can understand and correct mistakes before resubmitting.

**Owner:** Frontend/Backend | **Sprint:** 4 | **Status:** Planned

**Acceptance Criteria:**
- [ ] Form fields enforce required input (e.g., non-empty title)
- [ ] Invalid input is blocked on both frontend and backend
- [ ] Errors are clearly shown near the relevant fields
- [ ] User input is retained after validation failure
- [ ] The user is guided to fix the issue and try again

---

### US033 — User Journey: Manual Task Workflow 👤

**As a user**, I want to manually complete a full task workflow so I can validate that the app supports typical task management behavior.

**Owner:** User | **Sprint:** 4 | **Status:** Planned

**Notes:** Applies to either CLI or Web UI. Intended to simulate a realistic user workflow for exploratory testing. Documented with screenshots as part of manual UI verification.

**Acceptance Criteria:**
- [ ] I can add a task via CLI or Web UI
- [ ] I can mark that task complete
- [ ] I can view the completed task in the task list, visually distinguished (e.g., strikethrough)
- [ ] I can delete the task
- [ ] Each step provides appropriate feedback (e.g., success message or redirect)

---

## Sprint 5

### US031 — Show Current Time via External API 👤

**As a user**, I want to view the current time for my selected timezone so I can track tasks across different regions or validate time-based information.

**Owner:** Dev | **Sprint:** 5 | **Status:** Planned

**Notes:** Requires integration with a public API (TimeAPI.io). Displayed via a dedicated `/time` page and used internally for report timestamping. Introduces mocking external APIs during testing (`MockHTTPClient`, `MockTimeService`).

**Acceptance Criteria:**
- [ ] A new route `/api/time` returns the current time as JSON
- [ ] Uses `requests.get()` to fetch time from an external API
- [ ] Handles network errors or invalid responses gracefully
- [ ] Unit test uses mocking to simulate external API response
- [ ] Current time is displayed on the Web UI via a dedicated `/time` page

---

### US039 — View Current Time in Web UI

**As a user**, I want to view the current time and see it reflected in the Task Summary.

**Owner:** Frontend/Backend/DevOps | **Sprint:** 5 | **Status:** Planned

---

### US040 — Acceptance Test for Task Workflow

**As a QA tester**, I want to validate the full task workflow using Robot Framework acceptance test cases so that I can ensure the app behaves as expected from a user perspective.

**Owner:** QA | **Sprint:** 5 | **Status:** Planned

**Notes:** Uses Robot Framework with `RequestsLibrary` (HTTP-level API acceptance tests, not browser-driven).

**Acceptance Criteria:**
- [ ] Robot Framework tests validate the full task workflow
- [ ] Tests cover creation, completion, and deletion
- [ ] All tests pass in CI

---

## Sprint 6

### US037 — Limit Task Title and Description Length

**As a user**, I want task titles and descriptions to have reasonable length limits so that the interface remains clean and readable.

**Owner:** Dev | **Sprint:** 6 | **Status:** Planned

**Acceptance Criteria:**
- [ ] `validate_task_title_length(title)` raises `ValidationError("Title must be 100 characters or fewer")` when title exceeds 100 characters
- [ ] `validate_description_length(description)` raises `ValidationError("Description must be 500 characters or fewer")` when description exceeds 500 characters
- [ ] `validate_description_length(None)` does not raise — description is optional
- [ ] `POST /api/tasks` with a 101-character title returns `400` with `{"error": "Title must be 100 characters or fewer"}`
- [ ] `POST /api/tasks` with a 501-character description returns `400` with `{"error": "Description must be 500 characters or fewer"}`
- [ ] `POST /api/tasks` with title exactly 100 characters returns `201` — boundary passes
- [ ] `POST /api/tasks` with description exactly 500 characters returns `201` — boundary passes
- [ ] `add_task.html` title input has `maxlength="100"` attribute
- [ ] `add_task.html` description input has `maxlength="500"` attribute
- [ ] Character counter below title input shows `0/100` on page load and updates live as user types
- [ ] Character counter below description input shows `0/500` on page load and updates live as user types
- [ ] Existing tasks longer than the limits are not affected — grandfathered (validators only called on `add_task()`)

**Status:** Sprint 6 — full feature slice implemented independently in a single lab (S6)

---

## Backlog

> Stories below are documented requirements that have not yet been implemented in any
> individual lab. They are candidates for future sprints.

> [!NOTE]
> Not every story below has fully elaborated acceptance criteria yet — some are
> single-line stubs. That's normal for a backlog; a story doesn't need full detail
> until it's actually being planned. Once a story is pulled into a sprint, writing
> complete, testable acceptance criteria is the **first action** — before any code
> is written, not something filled in after the fact.

### US008 — Tag Tasks (Assign Category)
**As a user**, I want to assign category tags to each task (e.g., "work", "personal") when creating or editing tasks so I can organize my task list.

**Status:** Backlog

---

### US009 — Edit Task Title
**As a user**, I want to edit a task's title so I can correct or update information.

**Acceptance Criteria:**
- [ ] `PUT /api/tasks/<id>` allows updating the title of an existing task
- [ ] Empty or missing title returns a 400 error
- [ ] Nonexistent IDs return 404
- [ ] Changes persist in `data/tasks.json`
- [ ] Endpoint is tested for success and error cases

**Status:** Backlog

---

### US010 — Assign Due Date
**As a user**, I want to assign a due date to each task so I can track deadlines.

**Status:** Backlog

---

### US013 — Search Tasks
**As a user**, I want to search tasks by keyword.

**Status:** Backlog

---

### US016 — Filter Tasks by Status
**As a user**, I want to filter tasks by complete/incomplete.

**Status:** Backlog

---

### US017 — Responsive UI
**As a user**, I want the task list to look good on mobile.

**Status:** Backlog

---

### US018 — View Task List (UI)
**As a user**, I want to see a table of tasks in the browser.

**Notes:** Not implemented as its own phase — general task-list rendering is covered
inline as part of US012's web form work in Sprint 4, but this story's specific acceptance
criteria (dedicated table view, empty-state handling) were never built out separately.

**Acceptance Criteria:**
- [ ] Tasks are rendered in a table format in the browser
- [ ] Each task displays: Title, Description, and Completion Status
- [ ] Completed tasks are visually distinguishable (e.g., checkbox, strikethrough, or ✅)
- [ ] The page updates when tasks are added, modified, or deleted
- [ ] Table is rendered using Jinja2 and Flask templates
- [ ] UI gracefully handles empty task lists (e.g., shows "No tasks yet.")
- [ ] Manual testing confirms task list matches data in JSON file
- [ ] Automated UI tests (Playwright) validate expected rendering

**Status:** Backlog

---

### US019 — Add Tags to Tasks
**As a user**, I want to tag tasks with categories.

**Status:** Backlog

---

### US020 — User Registration
**As a new user**, I want to register with a username/password to create an account.

**Status:** Backlog

---

### US021 — Secure Session Management
**As a logged-in user**, I want my session to persist securely.

**Status:** Backlog

---

### US022 — User Logout
**As a logged-in user**, I want to log out and terminate my session.

**Status:** Backlog

---

### US023 — Password Validation & Errors
**As a user**, I want clear messages if login or registration fails.

**Status:** Backlog

---

### US024 — Filter Tasks by Tag
**As a user**, I want to filter tasks by tag so I can quickly view only relevant items.

**Status:** Backlog

---

### US025 — Overdue Task Alerts
**As a user**, I want the system to highlight or notify me when a task is overdue so I don't miss important tasks.

**Status:** Backlog

---

### US026 — Task Menu UI
**As a user**, I want a menu on the web page that lets me navigate to add, edit, delete, complete, and view tasks so I can easily access all core features from one place.

**Notes:** Not implemented as its own phase in any current lab.

**Acceptance Criteria:**
- [ ] A navigation menu is displayed with links to: Add Task, View Tasks, and Reports
- [ ] Menu clearly indicates which section is active (e.g., highlight, underline)
- [ ] Navigation works across views/pages without breaking functionality
- [ ] Menu is responsive and accessible (keyboard-friendly, screen-reader-friendly)
- [ ] Playwright test validates clickable navigation between sections

**Status:** Backlog

---

### US029 — CLI: Mark Task Complete
**As a user**, I want to mark a task as complete via CLI so I can validate completion manually.

**Notes:** Referenced in Sprint 3's overview reading list ("review Sprint 3 stories") but
never implemented as an actual lab phase.

**Acceptance Criteria:**
- [ ] User can select a task by ID from the CLI and mark it as completed
- [ ] CLI provides visual confirmation when a task is marked complete
- [ ] If a non-existent ID is entered, an error message is shown: "Task not found."
- [ ] If no tasks exist, the CLI shows: "No tasks available to complete."
- [ ] Updated task state is saved in the JSON file (`completed: true`)
- [ ] Marked tasks remain visible in the list with a visual cue like `[X]` or `✔`
- [ ] All state changes persist and are visible across CLI and API views
- [ ] CLI supports marking multiple tasks in sequence without restarting the app
- [ ] Automated CLI tests verify marking a valid task updates JSON correctly
- [ ] Automated CLI tests verify invalid task ID triggers appropriate error

**Status:** Backlog

---

### US030 — CLI: Delete Task
**As a user**, I want to delete a task via CLI so I can validate deletion manually.

**Status:** Backlog

---

### US032 — BDD Test for Task Workflow
**As a QA tester**, I want to validate the full task workflow using BDD scenarios so that I can ensure the app behaves as expected from a user perspective.

**Notes:** Uses Behave with Gherkin syntax — Behave is not used anywhere in the
current curriculum. BDD-style acceptance testing was superseded by Robot Framework
(US040, Sprint 5).

**Acceptance Criteria:**
- [ ] BDD tests simulate creation, completion, and reporting
- [ ] Written in Gherkin and executed via `behave`
- [ ] Includes at least 1 end-to-end scenario

**Status:** Backlog — likely superseded by US040, not actively planned

---

### US034 — CI Automation for Task Features
**As a DevOps or QA engineer**, I want all automated tests to run in CI so I can catch errors or regressions before release.

**Notes:** Not implemented as its own phase — general CI automation is covered by
a Sprint 4 tooling/CI lab, but that lab isn't tied to this specific story.

**Acceptance Criteria:**
- [ ] Run unit tests (pytest) with test coverage report
- [ ] Run API tests using requests or Postman collection
- [ ] Run UI tests using Playwright
- [ ] Run BDD acceptance tests via Robot Framework or Behave
- [ ] Ensure all stages run in GitHub Actions and fail if any test fails

**Status:** Backlog

---

### US035 — API Testing Automation (requests)
**As a QA engineer**, I want to write automated API tests using the requests library so I can verify endpoint behavior without manual tools.

**Notes:** Referenced in Sprint 3's overview reading list ("review Sprint 3 stories") but
never implemented as an actual lab phase. Complements Postman and curl tests.

**Acceptance Criteria:**
- [ ] Write test scripts using `requests` to test core API routes
- [ ] Cover at least: `POST /api/tasks`, `GET /api/tasks`, `PUT /api/tasks/<id>`, `DELETE /api/tasks/<id>`
- [ ] Include both positive and negative test cases
- [ ] Save scripts in `/tests/api/` and integrate with pytest
- [ ] Document how to run and interpret the results

**Status:** Backlog

---

### US038 — Batch Task Creation
**As a user**, I want to add multiple tasks in sequence without being redirected to the task list after each one so that I can efficiently batch-create tasks during planning sessions.

**Acceptance Criteria:**
- [ ] After submitting a task, user is offered: "Add Another Task" or "View Task List"
- [ ] "Add Another Task" stays on the form, clears fields, and shows a success message
- [ ] "View Task List" redirects as current behavior

**Status:** Backlog

---

### US041 — View Deleted Task Count in Report

**As a user**, I want to see how many tasks I have deleted in the report summary so I can track my full task activity including completed and removed items.

**Acceptance Criteria:**
- [ ] Report page shows a "Deleted" count alongside Pending and Completed
- [ ] Deleted tasks are soft-deleted — marked as deleted, not removed from data
- [ ] `GET /report` includes `deleted_count` in template context
- [ ] Deleted tasks do not appear in the active task list
- [ ] `DELETE /api/tasks/<id>` sets `deleted=True` instead of removing the record

**Notes:**
- Requires soft delete: new `deleted` field on Task model
- Requires repository changes: `delete_task()` updates flag instead of removing
- Requires migration: existing data must be handled

**Status:** Backlog — emerged from Sprint 5 stakeholder demo; requires soft delete implementation

---

> **Note:** US014, US027, and US028 have been removed from the backlog. US014 was merged into US012. US027 and US028 were merged into US004.
