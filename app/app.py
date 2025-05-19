from flask import Flask, request, render_template
from werkzeug.utils import secure_filename
import os
import boto3

app = Flask(__name__)

s3 = boto3.client('s3')
BUCKET_NAME = os.getenv('S3_BUCKET')

@app.route('/', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        file = request.files['file']
        if file.filename:
            filename = secure_filename(file.filename)
            s3.upload_fileobj(file, BUCKET_NAME, filename)
    
    # Obtener lista de archivos en el bucket
    response = s3.list_objects_v2(Bucket=BUCKET_NAME)
    files = [obj['Key'] for obj in response.get('Contents', [])]

    return render_template('upload.html', files=files)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
