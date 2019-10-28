from aiohttp import web

import socketio
from api.handlers.handlers import index_handler
from api.handlers.websockets import sio


app = web.Application()
sio.attach(app)

app.add_routes([
	web.get('/', index_handler),
	web.static('/', 'client/dist')
])

web.run_app(app)
