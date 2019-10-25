import socketio


sio = socketio.AsyncServer()

@sio.event
def connect(sid, environ):
    print('connect ', sid)

@sio.event
def disconnect(sid):
    print('disconnect ', sid)

@sio.event
def login(sid, data):
    print(sid, data)