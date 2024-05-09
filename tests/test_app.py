from app import app
import pytest


@pytest.fixture
def test_client():
    with app.test_client() as client:
        yield client


def test_index(test_client):
    response = test_client.get('/')
    assert response.status_code == 200
    assert b"Hello, World!" in response.data

