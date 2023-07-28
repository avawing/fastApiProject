import json
from fastapi.testclient import TestClient
from api.main import app


client = TestClient(app)


def test_main():
    response = client.get('/')
    assert response.status_code == 200


def test_get_users():
    response = client.get('/users/')
    assert response.status_code == 200


def test_get_user():
    response = client.get('/users/1')
    assert response.status_code == 200


def test_delete_user():
    response = client.delete('/users/1')
    assert response.status_code == 200


def test_create_user_empty():
    response = client.post('/users/')
    assert response.status_code == 400


def test_create_user():
    data = {"first_name": "Fred"}
    response = client.post('/users', json=json.dumps(data))
    assert response.status_code == 400

    data["last_name"] = "fredderton"
    response = client.post('/users/', json=json.dumps(data))
    assert response.status_code == 400

    data["email"] = "fred@fred.com"
    response = client.post('/users/', json=json.dumps(data))
    assert response.status_code == 200


def test_update_user():
    data = {"first_name": "Robert", "last_name": "Robertington"}
    response = client.put('/users/1', json=json.dumps(data))
    assert response.status_code == 200





