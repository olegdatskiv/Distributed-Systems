FROM python:3.7

RUN apt-get update && apt-get install -y netcat

RUN mkdir -p /usr/src/app/
WORKDIR /usr/src/app/

COPY . /usr/src/app/
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8001

CMD ["uvicorn", "main_server:app", "--host", "127.0.0.1", "--port", "8001"]