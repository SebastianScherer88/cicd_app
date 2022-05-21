# -*- coding: utf-8 -*-
"""
Created on Sat May 21 11:58:13 2022

@author: bettmensch
"""


FROM python:3.10.4

# 
WORKDIR /repository

# 
COPY ./requirements.txt /repository/requirements.txt

# 
RUN pip install --no-cache-dir --upgrade -r /repository/requirements.txt

# 
COPY ./app /repository/app

# 
CMD ["python", "main.py"]
