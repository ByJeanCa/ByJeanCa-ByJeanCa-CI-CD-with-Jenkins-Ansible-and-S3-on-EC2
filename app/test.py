import os
import pytest
from app import app
from unittest.mock import patch

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_get_upload_page(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'Subir archivo' in response.data or b'input' in response.data

@patch('app.s3.upload_fileobj')
def test_post_upload_file(mock_upload, client):
    data = {
        'file': (open(__file__, 'rb'), 'testfile.py')
    }
    response = client.post('/', data=data, content_type='multipart/form-data')
    assert response.status_code == 200
    assert b'Archivo subido exitosamente' in response.data
    mock_upload.assert_called_once()
