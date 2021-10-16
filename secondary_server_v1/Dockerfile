FROM tiangolo/uvicorn-gunicorn:python3.8-slim

RUN apt-get update && apt-get install -y netcat

RUN mkdir -p /usr/src/app/
WORKDIR /usr/src/app/

COPY . /usr/src/app/
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8002

CMD ["uvicorn", "secondary_main:app", "--host", "127.0.0.3", "--port", "8003"]