from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

app = FastAPI()


@app.get('/')
def read_root():
    return {'msg': 'hello fastapi'}


@app.get('/test')
def read_test():
    return {'msg': 'hello fastapi test'}


@app.get('/items/{item_id}')
def read_item(item_id: int, q: str | None = None):
    return {'item_id': item_id, 'q': q}


if __name__ == '__main__':
    uvicorn.run("main:app", host='0.0.0.0', port=8400, reload=True)
