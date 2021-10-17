# Distributed-Systems

## How to run master node:

`uvicorn master_main:app`

## How to run secondary node:

`uvicorn secondary_main:app`

## How to access master node:

Use `python client_main.py`.

## How to run from docker all nodes

In CMD run:

` $ docker-compose up --build `

In new CMD tab run client from your local venv

` python client_main.py `