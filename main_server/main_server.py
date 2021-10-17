from fastapi import FastAPI
from pydantic import BaseModel
import requests

app = FastAPI()


class Message(BaseModel):
    text: str


class MessageToNode(BaseModel):
    id: int = None
    text: str = None


MESSAGE_STORE = {}  # created messages will be stored in a dict


class Master:
    def __init__(self, host_node_v1: str = 'http://127.0.0.2:8081', host_node_v2: str = 'http://127.0.0.3:8082'):
        self._log = {}
        self._host_node_v1 = host_node_v1
        self._host_node_v2 = host_node_v2

    def get_last_message_id(self):
        return len(self._log) - 1

    def append_msg(self, msg: str):
        prev_id = self.get_last_message_id()
        print(prev_id)
        self._log[prev_id + 1] = msg
        data = MessageToNode()
        data.id = prev_id + 1
        data.text = msg
        requests.post(f"{self._host_node_v1}/append_msg", json={"id": data.id, "text":data.text})
        requests.post(f"{self._host_node_v2}/append_msg", json={"id": data.id, "text":data.text})
        return f"Posted message '{data.text}' with id {data.id} on secondary nodes 1 and 2 successfully"

    def list_msgs(self):
        msgs_list = [f'{k}: {v}' for k, v in self._log.items()]
        return msgs_list


MASTER = Master()


@app.get("/")
async def get_main():
    return "This is a master node"


@app.post('/append_msg')
async def append_msg(msg: Message):
    r = MASTER.append_msg(msg.text)
    return r


@app.get('/list_msgs')
async def list_msgs():
    return MASTER.list_msgs()


# a method to get message by its id
@app.get("/messages/message/{message_id}")
async def read_message(message_id: int):
    if message_id in MESSAGE_STORE:
        return MESSAGE_STORE[message_id]
    else:
        return "Message with this id does not exist"


# a method to get an id of a latest message (to assign a new id to a new message)
@app.get("/messages/last_message_id")
async def get_last_message_ind() -> int:
    # get the len of our message storage 
    print('last_message_id called, returns:', len(MESSAGE_STORE) - 1)
    return len(MESSAGE_STORE) - 1


# post a message
@app.post("/messages/{message_id}")
async def create_message(message_id: int, message_text: str):
    message_dict = {}
    message_dict['id'] = message_id
    message_dict['text'] = message_text

    MESSAGE_STORE.update({message_id: message_dict})  # does not work like that - why?

    return f'Successfully created a message\n {message_dict}'
