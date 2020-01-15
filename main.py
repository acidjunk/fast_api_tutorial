from operator import itemgetter

from fastapi import FastAPI

from utils import find

app = FastAPI()

fake_items_db = [
    {"item_id": "abcd", "item_name": "Foo"},
    {"item_id": "1234", "item_name": "Bar"},
    {"item_id": "5678", "item_name": "Baz"},
]


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/items/{item_id}")
async def read_item(item_id):
    return find(fake_items_db, "item_id", item_id)


@app.get("/numbers{number_id}")
async def read_number(number_id: int):
    return {"number_id": number_id}


@app.get("/items/")
async def read_items(skip: int = 0, limit: int = 10):
    return fake_items_db[skip : skip + limit]
