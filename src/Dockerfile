FROM python:3.8-slim-buster
WORKDIR /sdu
ENV environment default_env_value
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
ENTRYPOINT [ "python3",  "simple-dropbox-uploader.py" ]
