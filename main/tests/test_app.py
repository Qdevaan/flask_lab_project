import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from app import app   # now Python can find app.py

def test_home():
    client = app.test_client()
    response = client.get('/')
    assert response.status_code == 200

def test_health():
    client = app.test_client()
    response = client.get('/health')
    assert b"OK" in response.data
