import sqlite3

connection = sqlite3.connect('Products.db')
cursor = connection.cursor()

def initiate_db():
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Products(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    description TEXT,
    price INTEGER NOT NULL
    )
    ''')

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