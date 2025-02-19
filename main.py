from fastapi import FastAPI, HTTPException, Depends, status
from pydantic import BaseModel
from typing import Annotated

import models
from database import engine, SessionLocal
from sqlalchemy.orm import Session

app = FastAPI()
models.Base.metadata.create_all(bind=engine)

class PostBase(BaseModel):
    title : str
    content : str
    user_id : int

class UserBase(BaseModel):
    username : str
    email: str

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]

@app.post("/posts/", status_code=status.HTTP_201_CREATED)
async def create_post(post: PostBase, db: db_dependency):
    db_post = models.Post(**post.dict())
    db.add(db_post)
    db.commit()

@app.get("/posts/{post_id}", status_code=status.HTTP_200_OK)
async def read_post(post_id: int, db: db_dependency):
    post = db.query(models.Post).filter(models.Post.id==post_id).first()
    if post is None:
        raise HTTPException(status_code=404,detail=f"Post {post_id} was not found!")
    return post


@app.post("/users/", status_code=status.HTTP_201_CREATED)
async def create_user(user: UserBase, db: db_dependency):
    db_user = models.User(**user.dict())
    db.add(db_user)
    db.commit()

@app.get("/users/{user_id", status_code=status.HTTP_200_OK )
async def read_user(user_id: int, db: db_dependency):
    user = db.query(models.User).filter(models.User.id==user_id).first()
    if user is None:
        raise HTTPException(status_code=404,detail=f"User {user_id} is not found!")
    return user

@app.get("/posts",status_code=status.HTTP_200_OK)
async def read_users(db: db_dependency):
    posts = db.query(models.Post).all()
    
    if posts is None:
        raise HTTPException(status_code=404,detail=f"No posts!")
    return posts

@app.get("/users",status_code=status.HTTP_200_OK)
async def read_users(db: db_dependency):
    users = db.query(models.User).all()
    if users is None:
        raise HTTPException(status_code=404,detail=f"No users!")
    return users



    
