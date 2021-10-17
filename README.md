# Distributed-Systems

Note that for everything to work smoothly, secondary nodes must be run on certain host/port.
## How to run master node:

`uvicorn master_main:app`

## How to run secondary nodes:
`uvicorn secondary_main:app`

If running without docker, add parameters `--host 127.0.0.2 --port 8081` when running one secondary node and `--host 127.0.0.3 --port 8082` for another

## How to access master node through client:
Run `client_main.py`

Use `python client_main.py`.

## How to run from docker all nodes

In CMD run:

` $ docker-compose up --build `

In new CMD tab run client from your local venv

` python client_main.py `
