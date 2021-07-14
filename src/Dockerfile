FROM python:3.8-slim-buster
WORKDIR /sdu
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY ./simple-dropbox-uploader .
ENTRYPOINT ["python3",  "simple-dropbox-uploader.py" ]
