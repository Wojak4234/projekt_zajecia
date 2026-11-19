import pytest
from app import app as fask_app


@pytest.fixture
def app():
    yield fask_app


@pytest.fixture
def client(app):
    return app.test_client()

def test_homepage(client):
    response = client.get('/')
    assert response.status_code == 200