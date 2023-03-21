import pytest
from app import app
from flask.testing import FlaskClient

@pytest.fixture
def client() -> FlaskClient:
    app.config['TESTING'] = True
    client = app.test_client()
    yield client
    
def test_index(client: FlaskClient):
    rv = client.get('/')
    assert rv.status_code == 200
    assert rv.json == {'message': 'Hello, World!'}