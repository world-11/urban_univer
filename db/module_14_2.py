import sqlite3

connection =  sqlite3.connect('not_telegram.db')
cursor = connection.cursor()

# удаление таблицы
# cursor.execute(('''DROP TABLE Users'''))

# создание таблицы
cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY AUTOINCREMENT,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER NOT NULL
)
''')

# создание индекса
cursor.execute("CREATE INDEX IF NOT EXISTS idx_email ON Users(email)")

# удаление записей
# cursor.execute("DELETE FROM Users WHERE balance = ?", (1000,))

# добавление записей
# for i in range(10):
#     cursor.execute("INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)",
#                    (f'user{i+1}', f'example{i+1}@gmail.com', (i+1)*10, 1000))

#обновление баланса
# i = 1
# while i <= 10:
#  cursor.execute("UPDATE Users SET balance = ? WHERE id = ?",
#                    (500, f'{i}'))
#  i += 2

#удаление каждой 3 записи, начиная с 1
# i = 1
# while i <= 10:
#  cursor.execute("DELETE FROM Users WHERE id = ?",
#                    (f'{i}',))
#  i += 3

#выборка
# cursor.execute("SELECT username, email, age, balance FROM Users WHERE age != ?", (60,))
# users = cursor.fetchall()
# for user in users:
#  print(f'Имя: {user[0]} | Почта: {user[1]} | Возраст: {user[2]} | Баланс: {user[3]}')

# cursor.execute("DELETE FROM Users WHERE id = ?", (6,))
cursor.execute("SELECT COUNT(*) FROM Users")
count = cursor.fetchone()[0]
cursor.execute("SELECT SUM(balance) FROM Users")
sum_balance = cursor.fetchone()[0]
avg_balance = sum_balance / count
print(count, sum_balance, avg_balance)

# users = cursor.fetchall()
# for user in users:
#  print(f'Имя: {user[0]} | Почта: {user[1]} | Возраст: {user[2]} | Баланс: {user[3]}')

connection.commit()
connection.close()