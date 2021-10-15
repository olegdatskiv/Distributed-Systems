from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

class Message(BaseModel):
    id: int
    text: str
    additional: Optional[str] = None

class MessageId(BaseModel):
    message_id: int

MESSAGE_STORE = {} #created messages will be stored in a dict


@app.get("/")
async def get_main():
    return "This is a master node"

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