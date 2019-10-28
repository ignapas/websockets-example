import socketio

from entities.Chat import Chat

sio = socketio.AsyncServer()
chat = Chat()
msg_id = 1

@sio.event
def connect(sid, environ):
    print('connect ', sid)

@sio.event
def disconnect(sid):
    print('disconnect ', sid)

@sio.event
def login(sid, data):
    print('login', sid, data)
    chat.clients[sid] = data
    return { 'data': True }

@sio.on('chatCreated')
def chat_created(sid, data):
    print('chat_created', sid)
    return { 'data': chat.messages }

@sio.event
async def message(sid, data):
    print('message', sid, data)
    global msg_id
    msg = {
        'id': msg_id,
        'author': chat.clients[sid],
        'text': data
    }
    chat.messages.append(msg)
    msg_id += 1
    await sio.emit('newMessage', { 'data': msg })
    return { 'data': msg }