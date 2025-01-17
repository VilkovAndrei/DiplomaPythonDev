FROM python:3.11

WORKDIR /library_app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .