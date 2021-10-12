from typing import Any, List, Optional

from fastapi import FastAPI

app = FastAPI()


class Logger:
    def __init__(self, msgs: List[str] = None):
        if msgs is None:
            self.msgs = []
        else:
            self.msgs = msgs
    
    def add_msg(self, msg: str) -> bool:
        self.msgs.append(msg)
        return True

    def list_msgs(self):
        return self.msgs

LOGGER = Logger()

@app.get("/")
def list_msgs():
    return LOGGER.list_msgs()

# if __name__ == '__main__':
