from fastapi import APIRouter, Depends, status, HTTPException
from app.models import *
from sqlalchemy.orm import Session
from app.backend.db_depends import get_db
from typing import Annotated
from sqlalchemy import insert, delete
from app.schemas import CreateTask, UpdateTask
from slugify import slugify
from sqlalchemy import select, update

router = APIRouter(prefix='/task', tags=['task'])


@router.get("/")
async def all_tasks(db: Annotated[Session, Depends(get_db)]):
    tasks = db.scalars(select(Task)).all()
    return tasks


#______________________

@router.get("/task_id")
async def task_by_id(db: Annotated[Session, Depends(get_db)], task_id: int):
    tasks = db.scalars(select(Task).where(Task.id == task_id)).all()
    if not tasks:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'Task with ID={task_id} not found'
        )
    return tasks


#-----------------------


@router.post("/create")
async def create_task(db: Annotated[Session, Depends(get_db)], create_task: CreateTask, user_id: int):
    db.execute(insert(Task).values(title=create_task.title,
                                   content=create_task.content,
                                   priority=create_task.priority,
                                   user_id=user_id,
                                   slug=slugify(create_task.title)))
    db.commit()
    return {
        "status_code": status.HTTP_201_CREATED,
        "transaction": "successful"
    }


#----------------------------


@router.put("/update")
async def update_task(db: Annotated[Session, Depends(get_db)], task_id: int, update_task: UpdateTask):
    task = db.scalar(select(Task).where(Task.id == task_id))
    if not task:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'Task with ID={task_id} not found'
        )
    db.execute(update(Task).where(Task.id == task_id).values(
        title=create_task.title,
        content=create_task.content,
        priority=create_task.priority))
    db.commit()
    return {
        "status_code": status.HTTP_200_OK,
        "transaction": "Task update successful"
    }


#---------------------------

@router.delete("/delete")
async def delete_task(db: Annotated[Session, Depends(get_db)], task_id: int):
    task = db.scalars(select(Task).where(Task.id == task_id))
    if not task:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'Task with ID={task_id} was deleted'
        )
    db.execute(delete(Task).where(Task.id == task_id))
    db.commit()
    return {
        "status_code": status.HTTP_200_OK,
        "transaction": "Task delete is successful"
    }
