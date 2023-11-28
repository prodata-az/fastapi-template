FROM python:3.9.18-slim

WORKDIR /square

COPY requirements.txt /square/requirements.txt

RUN pip install -r requirements.txt

COPY src /square/src

CMD ["python", "-m", "src.app"]
