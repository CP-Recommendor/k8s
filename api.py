from quart import Quart, request
import aiohttp

app = Quart(__name__)

@app.before_serving
async def startup():
    app.client = aiohttp.ClientSession()

@app.route('/hello')
async def world():
    return 'Hello, world!'

@app.route('/')
async def hello():
    return 'Hello,'