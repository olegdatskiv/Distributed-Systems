from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

class Message(BaseModel):
    text: str

class MessageId(BaseModel):
    message_id: int

MESSAGE_STORE = {} #created messages will be stored in a dict

class Master:
    def __init__(self):
        self._log = {}

    def get_last_message_id(self):
        if len(self._log) == 0:
            return 0
        return len(self._log) - 1

    def append_msg(self, msg: str):
        prev_id = self.get_last_message_id()
        self._log[prev_id + 1] = msg

    def list_msgs(self):
        return list(self._log.values())

MASTER = Master()

@app.get("/")
async def get_main():
    return "This is a master node"

@app.post('/append_msg')
async def append_msg(msg: Message):
    print('im here!')
    MASTER.append_msg(msg.text)
    return 'ok'

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
    return len(MESSAGE_STORE)-1
    # return "Whoops"

# post a message
@app.post("/messages/{message_id}")
async def create_message(message_id: int, message_text: str):
    message_dict = {}
    message_dict['id'] = message_id
    message_dict['text'] = message_text

    MESSAGE_STORE.update({message_id:message_dict}) #does not work like that - why?

    return f'Successfully created a message\n {message_dict}'