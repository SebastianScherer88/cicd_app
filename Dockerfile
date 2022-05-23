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
COPY ./tests /repository/tests

# 
CMD ["python", "app/main.py"]
