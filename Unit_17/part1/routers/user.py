from fastapi import APIRouter, Depends, status, HTTPException
from app.models import *
from sqlalchemy.orm import Session
from app.backend.db_depends import get_db
from app.backend import db
from typing import Annotated
from sqlalchemy import insert, delete
from app.schemas import CreateUser, UpdateUser
from slugify import slugify
from sqlalchemy import select, update

router = APIRouter(prefix='/user', tags=['user'])


@router.get("/all")
async def all_users(db: Annotated[Session, Depends(get_db)]):
    users = db.scalars(select(User)).all()
    return users


@router.get("/user_id")
async def user_by_id(db: Annotated[Session, Depends(get_db)], user_id: int):
    user = db.scalars(select(User).where(User.id == user_id)).all()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'User with ID={user_id} not found'
        )
    else:
        return user


@router.post("/create")
async def create_user(db: Annotated[Session, Depends(get_db)], create_user: CreateUser):
    db.execute(insert(User).values(username=create_user.username,
                                   firstname=create_user.firstname,
                                   lastname=create_user.lastname,
                                   age=create_user.age,
                                   slug=slugify(create_user.username)))
    db.commit()
    return {
        "status_code": status.HTTP_201_CREATED,
        "transaction": "successful"
    }


@router.put("/update")
async def update_user(db: Annotated[Session, Depends(get_db)], user_id: int, update_user: UpdateUser):
    users = db.scalar(select(User).where(User.id == user_id))
    if not users:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'User with ID={user_id} not found'
        )
    db.execute(update(User).where(User.id == user_id).values(
        firstname=update_user.firstname,
        lastname=update_user.lastname,
        age=update_user.age))
    db.commit()
    return {
        "status_code": status.HTTP_200_OK,
        "transaction": "User update successful"
    }


@router.delete("/delete")
async def delete_user(db: Annotated[Session, Depends(get_db)], user_id: int):
    users = db.scalars(select(User).where(User.id == user_id)).all()
    if not users:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'User with ID={user_id} not found')
    db.execute(delete(User).where(User.id == user_id)).all()
    db.commit()
    return {
        "status_code": status.HTTP_200_OK,
        "transaction": "User delete is successful"
    }

