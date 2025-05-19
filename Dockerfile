FROM redhat/ubi9-minimal

WORKDIR /tests

COPY app/ .
COPY install_dependencies.sh .


RUN chmod +x install_dependencies.sh && ./install_dependencies.sh

EXPOSE 5000

CMD ["python3", "app.py"]
