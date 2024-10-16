from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI()
db_users = {"1": {"Ivan Ivanov": "35"}}

@app.get('/users')
async def dict_() -> dict:
    return db_users

@app.post('/user/{username}/{age}')
async def add_in_dict(username: Annotated[str, Path(min_length=3, max_length=10, description="Enter your username",
                                                    example="Ivan Ivanov")],
                           age: Annotated[int, Path(min_length=18, max_length=120, description="Enter your age",
                                                    example=18)]) -> str:
    current_index = str(int(max(db_users, key=int))+1)
    db_users[current_index] = {username: age}
    return f"User {current_index} is registered"

@app.put('/user/{user_id}/{username}/{age}')
async def upd_data(user_id: Annotated[int, Path(min_length=1, max_length=1000, description="Enter ID", example=1)],
                   username: Annotated[str, Path(min_length=3, max_length=10, description="Enter your username", example="Ivan Ivanov")],
                   age: Annotated[int, Path(min_length=18, max_length=120, description="Enter your age", example=18)]) -> str:
    db_users[user_id] = {username: age}
    return f"The user {user_id} is registered"

@app.delete('/user/{user_id}')
async def delete_(user_id: Annotated[str, Path(min_length=1, max_length=1000, description="Enter your ID", example="1")]) -> str:
    db_users.pop(user_id)
    return f"User {user_id} has been deleted"