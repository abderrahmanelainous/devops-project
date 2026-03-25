import pytest
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home(client):
    response = client.get('/')
    assert response.status_code == 200
    data = response.get_json()
    assert data['status'] == 'running'
    assert data['version'] == '2.0.0'
    assert data['author'] == 'Abderrahman Elainous'

def test_health(client):
    response = client.get('/health')
    assert response.status_code == 200
    data = response.get_json()
    assert data['status'] == 'healthy'
    assert 'timestamp' in data
    assert 'hostname' in data

def test_info(client):
    response = client.get('/info')
    assert response.status_code == 200
    data = response.get_json()
    assert data['app'] == 'flask-devops-api'

def test_status(client):
    response = client.get('/status')
    assert response.status_code == 200
    data = response.get_json()
    assert data['cluster'] == 'K3s on AWS EC2'
    assert data['nodes'] == 2
    assert data['pipeline'] == 'GitHub Actions'
