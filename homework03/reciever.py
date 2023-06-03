import requests
import time
from datetime import datetime
after = 0
def print_message(message):
    t = message['time']
    dt = datetime.fromtimestamp(t)
    dt = dt.strftime('%H:%M:%S')
    print(dt, message['name'])
    print(message['text'])
    print()

while True:
    response = requests.get(
        'http://127.0.0.1:5000/messages',
        params={'after': after}
    )
    messages = response.json()['messages']
    for message in messages:
        print_message(message)
        after = message['time']
    time.sleep(1)