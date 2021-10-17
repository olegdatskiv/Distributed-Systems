# Distributed-Systems

Note that for everything to work smoothly, secondary nodes must be run on certain host/port.
## How to run master node:

`uvicorn master_main:app`

## How to run secondary nodes:
`uvicorn secondary_main:app`

Add parameters `--host 127.0.0.2 --port 8081` when running one secondary node and `--host 127.0.0.3 --port 8082` for another

## How to access master node through client:
Run `client_main.py`

Then follow on-screen instructions.