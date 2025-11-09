# src/application/tests/app_test.py

from fastapi.testclient import TestClient
# Esta es la importación que corregimos antes
from src.application.app import app

client = TestClient(app)

# El nombre de la función debe empezar con "test_"
def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}

# El nombre de la función debe empezar con "test_"
def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"health": "ok"}

# El nombre de la función debe empezar con "test_"
def test_bye_endpoint():
    response = client.get("/bye")
    assert response.status_code == 200
    assert response.json() == {"msg": "Bye Bye"}