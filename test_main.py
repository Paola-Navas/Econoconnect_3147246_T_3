import unittest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

class TestRegister(unittest.TestCase):

    def setUp(self):
        # Registrar un usuario base para las pruebas
        client.post("/register", data={"id": 1, "username": "testuser", "password": "password123"})

    def test_register_success(self):
        response = client.post("/register", data={"id": 2, "username": "newuser", "password": "password123"})
        self.assertEqual(response.status_code, 200)

    def test_register_short_password(self):
        response = client.post("/register", data={"id": 3, "username": "testuser", "password": "short"})
        self.assertEqual(response.status_code, 400)

    def test_register_long_password(self):
        response = client.post("/register", data={"id": 4, "username": "testuser", "password": "toolongpassword123"})
        self.assertEqual(response.status_code, 400)

    def test_register_existing_user(self):
        response = client.post("/register", data={"id": 1, "username": "testuser", "password": "password123"})
        self.assertEqual(response.status_code, 400)

class TestLogin(unittest.TestCase):

    def setUp(self):
        # Registrar un usuario base para las pruebas
        client.post("/register", data={"id": 1, "username": "testuser", "password": "password123"})

    def test_login_success(self):
        response = client.post("/login", data={"username": "testuser", "password": "password123"})
        self.assertEqual(response.status_code, 200)

    def test_login_wrong_password(self):
        response = client.post("/login", data={"username": "testuser", "password": "wrongpassword"})
        self.assertEqual(response.status_code, 400)

    def test_login_nonexistent_user(self):
        response = client.post("/login", data={"username": "nonexistent", "password": "password123"})
        self.assertEqual(response.status_code, 400)

if __name__ == "__main__":
    unittest.main()