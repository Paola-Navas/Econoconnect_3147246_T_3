import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_register_user():
    payload = {"id": 1, "username": "jess", "password": "password1"}
    response = client.post("/register", data=payload)
    assert response.status_code == 200
    assert response.json()["msg"] == "Usuario registrado"

def test_register_existing_user():
    payload = {"id": 1, "username": "jess", "password": "password1"}
    response = client.post("/register", data=payload)
    assert response.status_code == 400
    assert response.json()["detail"] == "El usuario ya existe"

def test_login_success():
    payload = {"username": "jess", "password": "password1"}
    response = client.post("/login", data=payload)
    assert response.status_code == 200
    assert response.json() == {"Inicio de sesión": "jess"}

def test_login_wrong_password():
    payload = {"username": "jess", "password": "wrongpass"}
    response = client.post("/login", data=payload)
    assert response.status_code == 400
    assert response.json()["detail"] == "La contraseña no es correcta"

def test_get_user():
    response = client.get("/user/jess")
    assert response.status_code == 200
    data = response.json()
    assert data["username"] == "jess"
