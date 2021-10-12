import requests
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--host', default='http://127.0.0.1:8000')

    args = parser.parse_args()
    while True:
        msg = input("Enter GET msg:")
        resp = requests.get(f'{args.host}')
        if resp.status_code != 200:
            print("Failed to GET: URL=[{args.host}], status_code={resp.status_code}")
        else:
            print("Response:", resp.content)