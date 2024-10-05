import sqlite3

connection = sqlite3.connect('Products.db')
cursor = connection.cursor()

def initiate_db():
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Products(
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT,
    price INTEGER NOT NULL
    )
    ''')
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Users(
    id INTEGER PRIMARY KEY,
    username NOT NULL,
    email NOT NULL,
    age INTEGER NOT NULL,
    balance INTEGER NOT NULL
    )
    ''')


def add_user(username, email, age):
    cursor.execute("INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)",
                   (username, email, age, 1000))
    connection.commit()


def is_included(username):
    cursor.execute("SELECT username FROM Users WHERE username=?", [username])
    res = cursor.fetchall()
    # print(res)
    if res == []:
        return False
    else:
        return True

def get_all_products():
    cursor.execute('''
    SELECT * FROM Products
    ''')
    result = cursor.fetchall()
    return result

def records():
    cursor.execute("INSERT INTO Products (title, description, price) VALUES (?, ?, ?)",
                        (f'Паста', 'Приготовлена по итальянскому рецепту', 130))
    cursor.execute("INSERT INTO Products (title, description, price) VALUES (?, ?, ?)",
                        (f'Баранье мясо', 'Свежее мясо', 1000))
    cursor.execute("INSERT INTO Products (title, description, price) VALUES (?, ?, ?)",
                        (f'Молочный микс', 'Молочное ассорти', 1300))
    cursor.execute("INSERT INTO Products (title, description, price) VALUES (?, ?, ?)",
                        (f'Дары востока', 'Орехи, сухофрукты', 890))
    connection.commit()
# connection.close()