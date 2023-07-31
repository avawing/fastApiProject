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


#fail
def test_get_user():
    response = client.get('/users/1')
    assert response.status_code == 200


#fail
def test_delete_user():
    response = client.delete('/users/1')
    assert response.status_code == 200


def test_create_user():
    data = {"first_name": "Fred", "last_name": "fredderton", "email": "fred@george.com", "has_loan": True,
            "has_other_loan": False}

    response = client.post('/users/', json=data)
    assert response.status_code == 200


def test_update_user():
    data = {"first_name": "Fred", "last_name": "fredderton", "email": "bobtastic@bob.com", "has_loan": True,
            "has_other_loan": False}
    response = client.put('/users/2', json=data)
    assert response.status_code == 200





