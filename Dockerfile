FROM python:3.6

WORKDIR /app

COPY ./ ./

RUN pip install --upgrade pip; \
    pip install -r requirements.txt;