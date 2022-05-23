# -*- coding: utf-8 -*-
"""
Created on Mon May 23 22:21:14 2022

@author: bettmensch
"""

import requests
import os
import pytest
from app.main import generate_message

port=int(os.environ.get('PORT', 8080))


def test_root():
    response = requests.get(f'http://127.0.0.1:{port}/')
    assert response.status_code == 200
    assert response.json() == {"message": generate_message()}

@pytest.mark.parametrize('item_id',[1,10,-1,200])
def test_item_endpoint(item_id):
    response = requests.get(f'http://127.0.0.1:{port}/items/{item_id}')
    assert response.status_code == 200
    assert response.json() == {"item_id": item_id}