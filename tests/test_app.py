from app import app_flask as app
import pytest

def test_hello_world():
  """Test the hello_world route."""
  with app.test_client() as client:
    response = client.get('/')
    assert response.status_code == 200
    assert response.data == b'Hello, World! This is a Flask app running in a Docker container.'
    assert response.content_type == 'text/html; charset=utf-8'
    assert response.headers['Content-Length'] == '64'
    assert response.headers['Server'] == 'Werkzeug/2.0.1 Python/3.8.10'
    assert response.headers['Date'] is not None # Date header is set by Flask 
    assert response.headers['Content-Type'] == 'text/html; charset=utf-8'
    assert response.headers['Content-Length'] == '64'   
    assert response.headers['Server'] == 'Werkzeug/2.0.1 Python/3.8.10'
    assert response.headers['X-Content-Type-Options'] == 'nosniff'
    assert response.headers['X-Frame-Options'] == 'DENY'
    assert response.headers['X-XSS-Protection'] == '1; mode=block'
    assert response.headers['Strict-Transport-Security'] == 'max-age=31536000; includeSubDomains'
    assert response.headers['Cache-Control'] == 'no-cache, no-store, must-revalidate'
    assert response.headers['Pragma'] == 'no-cache'
    assert response.headers['Expires'] == '0'
    assert response.headers['Content-Security-Policy'] == "default-src 'self'; script-src 'self'; style-src 'self'; img-src 'self'; font-src 'self'; frame-ancestors 'none';"
    assert response.headers['Referrer-Policy'] == 'no-referrer'
    assert response.headers['Feature-Policy'] == "geolocation 'none'; microphone 'none'; camera 'none'; fullscreen 'self'; payment 'none';"
    assert response.headers['Access-Control-Allow-Origin'] == '*'
    assert response.headers['Access-Control-Allow-Methods'] == 'GET, POST, PUT, DELETE, OPTIONS'
    assert response.headers['Access-Control-Allow-Headers'] == 'Content-Type, Authorization, X-Requested-With'
    assert response.headers['Access-Control-Allow-Credentials'] == 'true' 