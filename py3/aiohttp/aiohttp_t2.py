# coding=utf-8

# Environment requirement:
#   Python 3.5+
#   aiohttp

import asyncio
from aiohttp import web

async def index(request):
    await asyncio.sleep(0.5)
    return web.Response(body=b'<h1>Index</h1>')

async def hello(request):
    await asyncio.sleep(0.5)
    text = '<h1>hello, {name}!</h1>'.format(name=request.match_info['name'])
    return web.Response(body=text.encode('utf-8'))

async def init(loop):
    app = web.Application(loop=loop)
    app.router.add_get('/', index)
    app.router.add_get('/{name}', hello)
    port = 8001
    server = await loop.create_server(app.make_handler(), '127.0.0.1', port)
    print('Server started at http://127.0.0.1:{port}...'.format(port=port))
    return server

loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()