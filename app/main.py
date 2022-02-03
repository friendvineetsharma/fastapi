from typing import List
from fastapi import FastAPI, Response, status, HTTPException, Depends
import psycopg2
from psycopg2.extras import RealDictCursor
import time
from sqlalchemy.orm import Session
from . import models, schemas, utils
from .database import engine, get_db
from .routers import post, user, auth




models.Base.metadata.create_all(bind = engine)

app = FastAPI()


while True:
    try:
        conn = psycopg2.connect(host='localhost', database='fastapi', user='postgres', password='database', cursor_factory=RealDictCursor)
        cursor = conn.cursor()
        print("Database connection was successfull!")
        break
    except Exception as error:
        print("Connecting to database failed")
        print("Error: ", error)
        time.sleep(2)

# my_posts = [{"title": "title of post 1","content": "content of post 1","id": 1},
# {"title": "favorite foods","content": "I like healthy food","id": 2}]

# def find_index_post(id):
#     for i, p in enumerate(my_posts):
#         if p['id'] == id:
#             return  i


@app.get("/")
def root():
    return {"message": "Hello Everyone"}

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)