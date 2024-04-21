import sqlite3 as sql
import random
from datetime import datetime, timedelta
from faker import Faker

fake = Faker()

conn = sql.connect('store.db')
cursor = conn.cursor()

# # Исправленный SQL-запрос для создания таблицы
# cursor.execute("""
# CREATE TABLE goods (
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     name VARCHAR(50),
#     description TEXT,
#     price INTEGER,
#     quantity INTEGER
# )
# """)

# # Выполнение запроса и обработка результата
# text = cursor.execute("SELECT sum(quantity) FROM goods").fetchall()

# for row in text:
#     print(row)

conn.commit()
conn.close()
