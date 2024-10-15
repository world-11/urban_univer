from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI()

@app.get("/")
async def main() -> str:
    return "Главная страница"

@app.get("/user/admin")
async def admin() -> str:
    return "Вы вошли как администратор"

@app.get("/user/{user_id}")
async def id(user_id: Annotated[int, Path(min_length=1, max_length=100, description="Enter User ID", example=1)]) -> str:
    return f"Вы вошли, как пользователь № {user_id}"

@app.get("/user/{username}/{age}")
async def id_person(username: Annotated[str, Path(min_length=5, max_length=20, description="Enter username", example='UrbanUser')] ,
                              age: Annotated[int, Path(ge=18, le=120, description="Enter age", example=24)]) -> str:
    return f"Информация о пользователе: имя: {username}, возраст: {age}"