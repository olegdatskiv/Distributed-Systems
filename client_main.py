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
    print(client.list_msgs())
    print(client.append_msg('m1'))
    print(client.append_msg('m2'))
#     print(client.list_msgs())
    # parser = argparse.ArgumentParser()
    # parser.add_argument('--host', default='http://127.0.0.1:8000') #define the default host address
#%%
    # args = parser.parse_args()
    # while True:
    #     operation = int(input("Please select operation: (1) POST (2) GET:"))
    #     if operation == 1:
            
    #         message_text = input("Type your message here and press Return")

    #         last_msg_id = requests.get(f'{args.host}/messages/last_message_id').text
            
    #         print("THIS IS LAST MSG ID:", last_msg_id)
            
    #         new_msg_id = int(last_msg_id)+1
            
    #         payload = {'message_id':new_msg_id, 'message_text':message_text}
            
    #         resp = requests.post(f'{args.host}/messages/{new_msg_id}', data = payload)
            
    #         if resp.status_code != 200:
    #             print(f"Failed to POST: URL={args.host}, status_code={resp.status_code}")
    #         else:
    #             print("Response:", resp.content)

    #     elif operation == 2:
    #         msg_id = input("Enter msg id here:")
    #         resp = requests.get(f'{args.host}/messages/{msg_id}')
    #         if resp.status_code != 200:
    #             print(f"Failed to GET: URL={args.host}, status_code={resp.status_code}")
    #         else:
    #             print("Response:", resp.content)