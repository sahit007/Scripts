from typing import Union

from fastapi import FastAPI

app = FastAPI();


@app.get("/")
def read_root():
    return {'data':{'name': 'Sahit',"surname":"burada"}}

@app.get("/meow")
def read_root():
    return {'data':{'file': 'https://purr.objects-us-east-1.dream.io/i/hni_0073.jpg'}}


@app.get("/items/{item_id}")
def read_item(item_id: int, query: Union[str, None] = None):
    return {"item_id": item_id, "query": query
    }

@app.get('/about')
def about():
    return {'data':'about page'}