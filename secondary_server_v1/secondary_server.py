from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Message(BaseModel):
    id: int
    text: str


class Secondary:
    def __init__(self):
        self._log = {}

    def append_msg(self, msg: Message):
        self._log[msg.id] = msg.text
        print(f"Message #{self._log[msg.id]} appended to secondary node 1")

    def list_msgs(self):
        return list(self._log.values())


SECONDARY = Secondary()


@app.get("/")
async def get_main():
    return "This is a secondary node"


@app.post('/append_msg')
async def append_msg(msg: Message):
    print('im here!')
    SECONDARY.append_msg(msg)
    return 'secondary-1: ok'


@app.get('/list_msgs')
async def list_msgs():
    return SECONDARY.list_msgs()
