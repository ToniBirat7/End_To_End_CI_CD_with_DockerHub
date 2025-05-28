from app import app_flask as app
import pytest

def test_hello_world():
  """Test the hello_world route."""
  with app.test_client() as client:
    response = client.get('/')
    assert response.status_code == 200
    assert response.data == b'Hello, World! This is a Flask app running in a Docker container.'
  