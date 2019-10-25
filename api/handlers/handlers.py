from aiohttp import web


async def index_handler(request: web.Request):
    return web.FileResponse('client/dist/index.html')
