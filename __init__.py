# app/__init__.py

from flask import Flask, Response, jsonify
from app.routes.tasks import tasks_bp
from app.routes.health import health_bp
from app.services.task_service import TaskService
from app.services.task_storage import task_storage


def create_app(service: object = None) -> Flask:

    """
    US015 — Global error handlers returning JSON.
    Tested in: tests/error/test_error_handling.py
    """
    app = Flask(__name__)

    # Register Blueprints
    app.register_blueprint(tasks_bp)
    app.register_blueprint(health_bp)
    # Dependency Injection — inject TaskService with TaskStorage
    # Routes access the service via current_app.task_service
    # Use injected service if provided, otherwise default to TaskService with real storage
    if service is None:
        service = TaskService(task_storage)
    app.task_service = service  # type: ignore[attr-defined]




    # Global error handler for 400 Bad Request
    @app.errorhandler(400)
    def bad_request(error: Exception) -> tuple[Response, int]:
        return jsonify({"error": "Bad Request"}), 400

    @app.errorhandler(404)
    def not_found(error: Exception) -> tuple[Response, int]:
        return jsonify({"error": "Not Found"}), 404

    return app

