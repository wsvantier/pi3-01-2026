import pytest
from pi3_01_2026.app import create_app

@pytest.fixture
def client():
    app = create_app()
    app.config["TESTING"] = True

    with app.test_client() as client:
        yield client


def test_estoque_status_code(client):
    response = client.get('/')
    assert response.status_code == 200

def test_genero_status_code(client):
    response = client.get('/genero')
    assert response.status_code == 200

def test_consumo_status_code(client):
    response = client.get('/consumo')
    assert response.status_code == 200
