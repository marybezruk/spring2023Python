import time

data_base = [
    {
        'time': time.time(),
        'name': 'Jack',
        'text': 'Привет всем!'
    },
    {
        'time': time.time(),
        'name': 'Mary',
        'text': 'Здраво!'
    }
]


def send_message(name, text):
    message = {
        'time': time.time(),
        'name': name,
        'text': text
    }
    data_base.append(message)


send_message('123', '123')
send_message('123', '456')
send_message('123', '789')

'''for message in data_base:
    print(message['time'], message['name'])
    print(message['text'])
    print()'''


def get_messages(after):
    result = []
    for message in data_base:
        if message['time'] > after:
            result.append(message)
    return result