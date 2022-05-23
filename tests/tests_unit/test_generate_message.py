# -*- coding: utf-8 -*-
"""
Created on Mon May 23 22:18:05 2022

@author: bettmensch
"""

from app.main import generate_message

def test_make_message():
    assert generate_message() == "Hello!"