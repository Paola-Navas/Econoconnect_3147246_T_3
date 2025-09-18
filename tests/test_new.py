import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_create_news():
    payload = {
        "title": "Noticia de prueba",
        "summary": "Un resumen breve",
        "content": "Contenido de la noticia",
        "author": "David"
    }
    response = client.post("/news/create", json=payload)
    assert response.status_code == 201
    data = response.json()
    assert data["title"] == payload["title"]
    assert data["published"] is False
    assert "id" in data

def test_get_drafts_contains_created_news():
    response = client.get("/news/drafts")
    assert response.status_code == 200
    drafts = response.json()
    assert any(news["title"] == "Noticia de prueba" for news in drafts)

def test_publish_news():
    response = client.post("/news/1/publish")
    assert response.status_code == 200
    data = response.json()
    assert data["published"] is True
    assert data["published_at"] is not None

def test_get_published_contains_news():
    response = client.get("/news/")
    assert response.status_code == 200
    published = response.json()
    assert any(news["id"] == 1 and news["published"] for news in published)

def test_publish_nonexistent_news():
    response = client.post("/news/999/publish")
    assert response.status_code == 404
    assert response.json()["detail"] == "Noticia no encontrada"
