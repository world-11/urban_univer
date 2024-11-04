from fastapi import FastAPI, status, HTTPException, Body, Request, Form
from fastapi.responses import HTMLResponse
from typing import List, Annotated
from pydantic import BaseModel
from fastapi.templating import Jinja2Templates

app = FastAPI()


templates = Jinja2Templates(directory='.venv/templates')


users = []

class User(BaseModel):
    id: int = None
    username: str
    age: int

@app.get('/', response_class=HTMLResponse)
async def get_all_users(request: Request) -> HTMLResponse:
    return templates.TemplateResponse("users.html", {"request": request, "users": users})

@app.get('/users/{user_id}', response_class=HTMLResponse)
async def list_users(request: Request, user_id: int) -> HTMLResponse:
    try:
        return templates.TemplateResponse("users.html", {"request": request, "users": users[user_id]})
    except:
        raise HTTPException(status_code=404, detail='User not found')

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