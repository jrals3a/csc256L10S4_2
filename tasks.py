# app/routes/tasks.py
from flask import Blueprint, Response, current_app, jsonify, request


# Dependency Injection complete:
# All routes use current_app.task_service — no direct storage imports.
# This enables mock storage, database swapping, and cleaner testing.

tasks_bp = Blueprint('tasks', __name__, url_prefix='/api/tasks')

@tasks_bp.route('/reset', methods=['POST'])
def reset_tasks() -> tuple[Response, int]:
    """Development endpoint to reset all tasks."""
    current_app.task_service.clear_tasks()  # type: ignore[attr-defined]
    return jsonify({"message": "Tasks reset successfully"}), 200


@tasks_bp.route('', methods=['POST'])
def add_task() -> tuple[Response, int]:
    """POST /api/tasks — Create a new task."""
    data = request.get_json() or {}
    title = data.get("title")
    if not data or "title" not in data or not title or str(title).strip() == "":
        return jsonify({"error": "Title is required"}), 400
    description = data.get("description", "")
    new_task = current_app.task_service.add_task(title, description)  # type: ignore[attr-defined]
    return jsonify(new_task), 201


@tasks_bp.route('', methods=['GET'])
def list_tasks() -> tuple[Response, int]:
    """GET /api/tasks — Return all tasks."""
    tasks = current_app.task_service.get_all_tasks()  # type: ignore[attr-defined]
    return jsonify(tasks), 200


@tasks_bp.route("/<int:task_id>", methods=["PUT"])
def complete_task(task_id: int) -> tuple[Response, int]:
    """PUT /api/tasks/<id> — Mark a task as complete."""
    updated_task = current_app.task_service.complete_task(task_id)  # type: ignore[attr-defined]
    if updated_task:
        return jsonify(updated_task), 200
    return jsonify({"error": "Task not found"}), 404


@tasks_bp.route("/<int:task_id>", methods=["DELETE"])
def delete_task(task_id: int) -> tuple[Response, int]:
    """DELETE /api/tasks/<id> — Delete a task."""
    deleted_task = current_app.task_service.delete_task(task_id)  # type: ignore[attr-defined]
    if deleted_task:
        return jsonify({"message": "Task deleted"}), 200
    return jsonify({"error": "Task not found"}), 404

