FROM python:3.7

RUN apt-get update && apt-get install -y netcat

RUN mkdir -p /usr/src/app/
WORKDIR /usr/src/app/

COPY . /usr/src/app/
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8003

CMD ["uvicorn", "secondary_server:app", "--host", "127.0.0.2", "--port", "8002"]