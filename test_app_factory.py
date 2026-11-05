# tests/test_app_factory.py
from flask import Flask

from app import create_app


def test_create_app_returns_flask_instance():
    """
    TC-US000-002: create_app() returns valid Flask app instance.
    """
    app = create_app()
    assert isinstance(app, Flask)


def test_app_returns_404_when_no_routes_defined():
    """
    TC-US000-003: Flask returns 404 at root before routes are added.
    """
    app = create_app()
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 404
