from fastapi import FastAPI, status, HTTPException, Body
from typing import List, Annotated
from pydantic import BaseModel

app = FastAPI()
users = []

class User(BaseModel):
    id: int = None
    username: str
    age: int

@app.get('/users')
async def list_users() -> List[User]:
    return users

@app.post('/user/{username}/{age}')
async def create_user(username: str, age: int) -> str:
    user_id = (users[-1].id + 1) if users else 1
    new_user = User(id=user_id, username=username, age=age)
    users.append(new_user)
    return f"User {new_user} is registered"

@app.put('/user/{user_id}/{username}/{age}')
async def update_user(user_id: int, username: str, age: int) -> User:
    up_user = next((user for user in users if user.id == user_id), None)
    if up_user is None:
        raise HTTPException(status_code=404, detail="User was not found")
    else:
        up_user.username = username
        up_user.age = age
        return up_user

@app.delete('/user/{user_id}')
async def delete_message(user_id: int) -> str:
    del_user = next((user for user in users if user.id == user_id), None)
    if del_user is None:
        raise HTTPException(status_code=404, detail="User was not found")
    else:
        users.remove(del_user)
        return f"User with ID {user_id} has been deleted."