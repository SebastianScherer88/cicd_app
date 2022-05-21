# -*- coding: utf-8 -*-
"""
Created on Sat May 21 11:52:04 2022

@author: bettmensch
"""

from typing import Union
import uvicorn
from fastapi import FastAPI
import os

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World!!"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=int(os.environ.get('PORT', 8080)))
