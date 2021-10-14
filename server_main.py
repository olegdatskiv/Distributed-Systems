from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

class Message(BaseModel):
    id: int
    text: str
    additional: Optional[str] = None

message_store = {} #created messages will be stored in a dict


@app.get("/")
async def get_main():
    return "This is a test"

# a method to get message by its id
@app.get("/messages/{message_id}")
async def read_message(message_id: int):
    if message_id in message_store:
        return message_store[message_id]
    else:
        return "Message with this id does not exist"

# a method to get an id of a latest message (to assign a new id to a new message)
@app.get("/messages/last_message_id")
async def get_last_message_ind(m_store = message_store):
    # get the len of our message storage 
    return len(m_store)-1
    # return "Whoops"

# post a message
@app.post("/messages/{message_id}")
async def create_message(message_id: int, message_text: str, message: Message, message_store = message_store):
    message_dict = message.dict()
    message_dict['id'] = message_id
    message_dict['text'] = message_text

    message_store.update({message_id:message_dict}) #does not work like that - why?
    
    return f'Successfully created a message\n {message_dict}'