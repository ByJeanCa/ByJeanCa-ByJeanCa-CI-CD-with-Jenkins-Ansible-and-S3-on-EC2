from flask import Flask, request, render_template
import os
import boto3

app = Flask(__name__)

s3 = boto3.client('s3')

BUCKET_NAME = os.getenv('S3_BUCKET')

@app.route('/', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        file = request.files['file']
        s3.upload_fileobj(file, BUCKET_NAME, file.filename)
        return 'Archivo subido exitosamente a S3.'
    return render_template('upload.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
