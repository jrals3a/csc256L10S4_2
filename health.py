# app/routes/health.py

from flask import Blueprint, Response, jsonify


health_bp = Blueprint("health", __name__)

@health_bp.route("/api/health")
def health_check() -> tuple[Response, int]:

    """
    Health check endpoint to verify that the API is running.
    """
    return jsonify({"status": "ok"}), 200
