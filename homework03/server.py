from flask import Flask, request, abort
import time
from datetime import datetime

app = Flask(__name__)
data_base = []


@app.route("/")
def hello():
    return "Hello, World 123!"


@app.route("/status")
def status():
    stat = 'Статус: True, Приложение: Эрик-Мессенджер, Дата: ' + str(datetime.now().strftime('%d.%m.%Y')) + ', Время: ' + str(datetime.now().strftime('%H:%M:%S')) + ',  Всего сообщений: ' + str(len(data_base)) +',  Пользователи: ' + str(len(set([data_base[i]['name'] for i in range(len(data_base))])))
    # return {
    #     'status': True,
    #     'name': 'Messenger',
    #     'time': datetime.now().strftime('%Y/%m/%d %H:%M:%S'),
    #     'messages': len(data_base),
    #     'users': len(set([data_base[i]['name'] for i in range(len(data_base))]))
    # }
    return stat

@app.route("/send", methods=['POST'])
def send_message():
    data = request.json

    if not isinstance(data, dict):
        return abort(400)
    if set(data.keys()) != {'name', 'text'}:
        return abort(400)
    if 'name' not in data or 'text' not in data:
        return abort(400)

    name = data['name']
    text = data['text']

    if not isinstance(name, str) or \
            not isinstance(text, str) or \
            name == '' or text == '':
        return abort(400)

    if text == '/commands':
        message = {
            'time': time.time(),
            'name': 'Bot',
            'text': 'Команды: /commands - выводит список команд, /help - выводит как пользоваться мессенджером',
        }
    elif text == '/help':
        message = {
            'time': time.time(),
            'name': 'Bot',
            'text': 'Введите имя и текст, затем нажмите кнопку',
        }
    else:
        message = {
            'time': time.time(),
            'name': name,
            'text': text,
        }
    data_base.append(message)
    return {'ok': True}



@app.route("/messages")
def get_messages():
    result = []

    try:
        after = float(request.args['after'])
    except:
        return abort(400)

    for message in data_base:
        if message['time'] > after:
            result.append(message)
            if len(result) >= 100:
                break

    return {'messages': result}


app.run()
