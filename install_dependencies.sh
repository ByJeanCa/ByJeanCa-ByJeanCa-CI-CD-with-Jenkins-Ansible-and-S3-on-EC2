#!/bin/bash

echo "Instalando Python y pip con microdnf..."

microdnf update -y && \
microdnf install -y python3 python3-pip

echo "Instalando dependencias de Python..."

pip3 install --no-cache-dir flask boto3 python-dotenv pytest

echo "Listo: Python + dependencias instaladas correctamente."
