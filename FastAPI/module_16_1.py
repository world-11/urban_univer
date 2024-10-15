from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def main() -> str:
    return "Главная страница"

@app.get("/user/admin")
async def admin() -> str:
    return "Вы вошли как администратор"

@app.get("/user/{user_id}")
async def id(user_id: int) -> str:
    return f"Вы вошли, как пользователь № {user_id}"

@app.get("/user")
async def id_person(username: str = 'Borya', age: int = 23) -> str:
    return f"Информация о пользователе: имя: {username}, возраст: {age}"