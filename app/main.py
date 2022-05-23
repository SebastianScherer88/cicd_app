# -*- coding: utf-8 -*-
"""
Created on Sat May 21 11:52:04 2022

@author: bettmensch
"""

import uvicorn
from fastapi import FastAPI
import os

app = FastAPI()


def generate_message():
    
    return "Hello!"

@app.get("/")
def read_root():
    generate_message()
    return {"message": generate_message()}


@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=int(os.environ.get('PORT', 8080)))
