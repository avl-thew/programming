import sqlite3 as sql
import random
from datetime import datetime, timedelta
from faker import Faker

fake = Faker()

conn = sql.connect('store.db')
cursor = conn.cursor()

# Создание таблиц
cursor.execute("""
    CREATE TABLE IF NOT EXISTS goods (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name VARCHAR(50),
        description TEXT,
        price INTEGER,
        quantity INTEGER
    )
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS customers (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name VARCHAR(50),
        address TEXT,
        phone_number TEXT,
        email TEXT
    )
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS orders (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        date TEXT,
        status INTEGER,
        goods TEXT,
        customer_id INTEGER
    )
""")


for _ in range(20):
    cursor.execute(
        "INSERT INTO goods (name, price, quantity, description) VALUES (?, ?, ?, ?)",
        (fake.word(), random.randint(100, 10000), random.randint(0, 50), fake.sentence())
    )


for _ in range(20):
    cursor.execute(
        "INSERT INTO customers (name, address, phone_number, email) VALUES (?, ?, ?, ?)",
        (fake.name(), fake.address(), fake.phone_number(), fake.email())
    )

for _ in range(20):
    start_date = datetime(2024, 1, 1)
    end_date = datetime(2024, 4, 19)
    random_date = start_date + timedelta(
        seconds=random.randint(0, int((end_date - start_date).total_seconds())))
    random_goods = []
    for _ in range(random.randint(1, 5)):
        random_num = random.randint(1, 4)
    
        if random_num == 1:
            status = "ОБРАБАТЫВАЕТСЯ "
        if random_num == 2:
            status = "СОБИРАЕТСЯ"
        if random_num == 3:
            status = "В ПУТИ"
        if random_num == 4:
            status = "НА СКЛАДЕ"
        if random_num == 5:
            status = "ПОЛУЧЕН"
        random_goods.append(random.randint(1, 20))
    cursor.execute(
        "INSERT INTO orders (date, status, goods, customer_id) VALUES (?, ?, ?, ?)",
        (str(random_date), status, str(random_goods)[1:-1], random.randint(1, 20))
    )


# text = cursor.execute("SELECT sum(quantity) FROM goods").fetchall()
# text = cursor.execute("SELECT * FROM orders WHERE customer_id=17 AND status=2").fetchall()

# for row in text[0]:
#     print(row)

# SELECT * FROM goods
# SELECT * FROM customers WHERE id>10;
# SELECT * FROM orders WHERE customer_id=17;
# SELECT * FROM orders WHERE customer_id=17 AND status=2;
# SELECT sum(quantity) from goods

conn.commit()
# conn.close()
