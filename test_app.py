"""Tests for hello-flask-sz Flask application."""

import pytest
from app import app


@pytest.fixture
def client():
    """Create a test client for the app."""
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_welcome_returns_json(client):
    """Test GET / returns JSON with welcome message."""
    # Arrange
    expected_message = "Welcome to hello-flask-sz"

    # Act
    resp = client.get("/")

    # Assert
    assert resp.status_code == 200
    assert resp.content_type == "application/json"
    assert resp.get_json()["message"] == expected_message


def test_welcome_returns_200(client):
    """Test GET / returns status code 200."""
    # Act
    resp = client.get("/")

    # Assert
    assert resp.status_code == 200


def test_health_returns_ok(client):
    """Test GET /health returns status ok."""
    # Act
    resp = client.get("/health")

    # Assert
    assert resp.status_code == 200
    assert resp.get_json()["status"] == "ok"


def test_health_returns_200(client):
    """Test GET /health returns status code 200."""
    # Act
    resp = client.get("/health")

    # Assert
    assert resp.status_code == 200


def test_health_json_format(client):
    """Test GET /health returns proper JSON content-type."""
    # Act
    resp = client.get("/health")

    # Assert
    assert resp.content_type == "application/json"
    assert isinstance(resp.get_json(), dict)


def test_welcome_json_structure(client):
    """Test GET / returns proper JSON structure."""
    # Act
    resp = client.get("/")
    data = resp.get_json()

    # Assert
    assert isinstance(data, dict)
    assert "message" in data
    assert isinstance(data["message"], str)
