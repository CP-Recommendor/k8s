from model import Model
from request import ModelRequest
from quart import Quart, request
import aiohttp

#from fastapi import FastAPI, Body
app = Quart(__name__)
#app.client = aiohttp.ClientSession()
#app = FastAPI()

@app.before_serving
async def startup():
    app.client = aiohttp.ClientSession()


@app.route('/hello')
async def home():
    return 'Welcome to the Quark application!'

@app.route('/translate', methods=['POST'])
async def translate():
    try:
        data = await request.get_json()
        req = ModelRequest(**data)
        model = Model(app)
        return await model.inference(req)
    except Exception as e:
        return e
