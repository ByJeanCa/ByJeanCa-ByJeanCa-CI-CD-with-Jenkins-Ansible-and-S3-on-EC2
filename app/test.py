import os
import pytest
from app import app
from unittest.mock import patch
from werkzeug.datastructures import FileStorage

# Mock de entorno para evitar errores si falta S3_BUCKET
@pytest.fixture
def client(monkeypatch):
    monkeypatch.setenv('S3_BUCKET', 'bucket-test')
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

# ✅ Test GET de la página con mocking del listado de S3
@patch('app.s3.list_objects_v2')
def test_get_upload_page(mock_list_objects, client):
    mock_list_objects.return_value = {
        'Contents': [
            {'Key': 'archivo1.txt'},
            {'Key': 'foto.jpg'}
        ]
    }
    response = client.get('/')
    assert response.status_code == 200
    assert b'Subir archivo' in response.data
    assert b'archivo1.txt' in response.data
    assert b'foto.jpg' in response.data

# ✅ Test POST de subida con mocking de upload_fileobj y list_objects_v2
@patch('app.s3.upload_fileobj')
@patch('app.s3.list_objects_v2')
def test_post_upload_file(mock_list_objects, mock_upload, client):
    mock_list_objects.return_value = {'Contents': []}
    data = {
        'file': (open(__file__, 'rb'), 'testfile.py')
    }
    response = client.post('/', data=data, content_type='multipart/form-data')

    # ✅ Validaciones mínimas sin modificar la app
    assert response.status_code == 200
    assert b'Subir archivo' in response.data  # Confirmamos que volvió al formulario
    mock_upload.assert_called_once()

