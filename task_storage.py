# app/services/task_storage.py
import os
import json
from typing import Any

TASKS_FILE = os.path.join("app", "data", "tasks.json")

def load_tasks() -> list[dict[str, Any]]:
    """Load tasks from the JSON file or return an empty list on failure."""
    try:
        with open(TASKS_FILE, "r") as file:
            return json.load(file)  # type: ignore[no-any-return]
    except (FileNotFoundError, json.JSONDecodeError, IOError):
        return []

def save_tasks(tasks: list[dict[str, Any]]) -> None:
    """Write the task list to the JSON file, ensuring directory exists."""
    os.makedirs(os.path.dirname(TASKS_FILE), exist_ok=True)
    try:
        with open(TASKS_FILE, "w") as file:
            json.dump(tasks, file, indent=2)
    except IOError as e:
        print(f"[Warning] Error saving tasks: {e}")
        
# ── Dependency Injection Infrastructure ────────────────────────────────────
# TaskStorage wraps the existing load_tasks/save_tasks functions to enable
# dependency injection. The original functions remain unchanged.

class TaskStorage:
    """Storage interface for task persistence.

    Wraps load_tasks() / save_tasks() functions for dependency injection.
    Allows TaskService to be tested with mock storage by swapping this class.
    """

    def load_tasks(self) -> list[dict[str, Any]]:

        """Load tasks using the underlying load_tasks function."""
        return load_tasks()

    def save_tasks(self, tasks: list[dict[str, Any]]) -> None:

        """Save tasks using the underlying save_tasks function."""
        save_tasks(tasks)

# Singleton instance — injected into TaskService in create_app()
task_storage = TaskStorage()
