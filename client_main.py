#%%
import requests
import argparse

class Client:
    def __init__(self, host: str = 'http://127.0.0.1:8000'):
        self.host = host

    def prepare_output(self, response: requests.Response):
        if response.status_code == 200:
            return f'{response.status_code}: {response.text}'
        else:
            return f'{response.status_code}: {response.reason}'
    
    def append_msg(self, msg: str):
        return self.prepare_output(requests.post(f'{self.host}/append_msg', json={'text': msg}))

    def list_msgs(self):
        resp = requests.get(f'{self.host}/list_msgs')
        return self.prepare_output(resp)

#%%
if __name__ == '__main__':
    client = Client()
    
    parser = argparse.ArgumentParser()
    parser.add_argument('--host', default='http://127.0.0.1:8000') #define the default host address

    args = parser.parse_args()

    while True:
        operation = int(input("Please select operation: (1) POST (2) GET:"))
        if operation == 1:
            message_text = input("Type your message here and press Return")
            print(client.append_msg(message_text))

        elif operation == 2:
            print(client.list_msgs())