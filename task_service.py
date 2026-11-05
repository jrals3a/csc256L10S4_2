# app/services/task_service.py
from typing import Any
from .task_storage import load_tasks, save_tasks
from app.models.task import Task


class TaskService:
    """Service layer for task management operations.

    HYBRID ARCHITECTURE PATTERN:
    Supports both dependency injection AND direct function calls.

    - Unit Tests: TaskService(storage=None) → calls load_tasks()/save_tasks() directly
    - Integration: TaskService(task_storage) → calls injected storage.load_tasks()/save_tasks()

    NOTE: This hybrid approach is intentional for Sprint 3 learning.
    Sprint 4 will clean this up to use ONLY dependency injection.
    """

    def __init__(self, storage: Any = None) -> None:

        self.storage = storage
        # Load tasks from storage and convert to Task objects
        self._tasks: list[Task] = []
        for t in self._load_tasks():
            self._tasks.append(
                Task(
                    id=t["id"],
                    title=t["title"],
                    description=t.get("description", ""),
                    completed=t.get("completed", False),
                )
            )

    def _load_tasks(self) -> list[dict[str, Any]]:
        """Load tasks using injected storage or direct functions."""
        if self.storage:
            return self.storage.load_tasks()  # type: ignore[attr-defined]
        return load_tasks()

    def _save_tasks(self, tasks: list[dict[str, Any]]) -> None:
        """Save tasks using injected storage or direct functions."""
        if self.storage:
            self.storage.save_tasks(tasks)  # type: ignore[attr-defined]
        else:
            save_tasks(tasks)

    def get_all_tasks(self) -> list[dict[str, Any]]:
        """Return all tasks as dicts (for JSON serialization)."""
        return [t.to_dict() for t in self._tasks]

    def get_tasks(self) -> list[dict[str, Any]]:
        """Return all tasks — alias for get_all_tasks().

        Returns:
            list: List of all task dictionaries
        """
        return self.get_all_tasks()

    def add_task(self, title: str, description: str = "") -> dict[str, Any]:
        """Add a new task with auto-incrementing ID."""
        if not title or not str(title).strip():
            raise ValueError("Title cannot be empty")

        next_id = max((task.id for task in self._tasks), default=0) + 1
        new_task = Task(
            id=next_id,
            title=title,
            description=description if description is not None else "",
        )
        self._tasks.append(new_task)
        self._save_tasks([t.to_dict() for t in self._tasks])
        return new_task.to_dict()

    def complete_task(self, task_id: int) -> dict[str, Any] | None:
        """Mark a task as completed."""
        for task in self._tasks:
            if task.id == task_id:
                task.completed = True
                self._save_tasks([t.to_dict() for t in self._tasks])
                return task.to_dict()
        return None

    def delete_task(self, task_id: int) -> dict[str, Any] | None:
        """Delete a task from the system."""
        for i, task in enumerate(self._tasks):
            if task.id == task_id:
                deleted_task = self._tasks.pop(i)
                self._save_tasks([t.to_dict() for t in self._tasks])
                return deleted_task.to_dict()
        return None

    def clear_tasks(self) -> None:
        """Clear all tasks from storage and in-memory list."""
        self._tasks = []
        self._save_tasks([])
