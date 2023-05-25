from fastapi import FastAPI
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.requests import Request

app = FastAPI()
templates = Jinja2Templates(directory='templates')
app.mount('/static', StaticFiles(directory='static'), name='static')


@app.get('/', name='index')
async def index(request: Request):
    context = {
        'request': request
    }

    return templates.TemplateResponse('home/index.html', context=context)

if __name__ == '__main__':
    import uvicorn

    uvicorn.run(
        app='main:app',
        host='127.0.0.1',
        port=8000,
        log_level='info',
        reload=True
    )
