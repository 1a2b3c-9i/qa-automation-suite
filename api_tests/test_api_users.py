"""
Test Suite: REST API Testing
Target: https://reqres.in/api
Covers: GET, POST, PUT, DELETE, status codes, response schema, negative cases
"""

import requests

BASE_URL = "https://reqres.in/api"
HEADERS = {"x-api-key": "reqres-free-v1"}  # required by reqres.in's free tier


def test_get_single_user_success():
    """TC_API_01: Verify GET request for an existing user returns 200 with correct schema."""
    response = requests.get(f"{BASE_URL}/users/2", headers=HEADERS)
    assert response.status_code == 200

    data = response.json()["data"]
    assert data["id"] == 2
    assert "email" in data
    assert "first_name" in data


def test_get_user_not_found():
    """TC_API_02: Verify GET request for a non-existent user returns 404."""
    response = requests.get(f"{BASE_URL}/users/9999", headers=HEADERS)
    assert response.status_code == 404


def test_post_create_user():
    """TC_API_03: Verify POST request creates a new user and returns 201 with an id."""
    payload = {"name": "Niveditha", "job": "QA Engineer"}
    response = requests.post(f"{BASE_URL}/users", json=payload, headers=HEADERS)

    assert response.status_code == 201
    data = response.json()
    assert data["name"] == "Niveditha"
    assert data["job"] == "QA Engineer"
    assert "id" in data
    assert "createdAt" in data


def test_put_update_user():
    """TC_API_04: Verify PUT request updates an existing user's details."""
    payload = {"name": "Niveditha", "job": "Senior QA Engineer"}
    response = requests.put(f"{BASE_URL}/users/2", json=payload, headers=HEADERS)

    assert response.status_code == 200
    data = response.json()
    assert data["job"] == "Senior QA Engineer"
    assert "updatedAt" in data


def test_delete_user():
    """TC_API_05: Verify DELETE request removes a user and returns 204 No Content."""
    response = requests.delete(f"{BASE_URL}/users/2", headers=HEADERS)
    assert response.status_code == 204


def test_post_create_user_missing_field():
    """TC_API_06 (Negative test): Verify POST with an empty payload is still handled gracefully."""
    response = requests.post(f"{BASE_URL}/users", json={}, headers=HEADERS)
    assert response.status_code == 201  # reqres accepts empty payload — documents actual API behavior
    data = response.json()
    assert "id" in data  # even with no fields, an id should be generated


def test_get_users_list_pagination():
    """TC_API_07: Verify paginated list endpoint returns expected structure and page size."""
    response = requests.get(f"{BASE_URL}/users?page=2", headers=HEADERS)
    assert response.status_code == 200

    body = response.json()
    assert body["page"] == 2
    assert len(body["data"]) > 0
    assert "total_pages" in body
