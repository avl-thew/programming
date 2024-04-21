import sqlite3 as sql
import random
from datetime import datetime, timedelta
from faker import Faker

fake = Faker()

conn = sql.connect('store.db')
cursor = conn.cursor()

create table goods (\
    id integer primary key autoincrement,\
    name varchar(50),\
    description text,\
    price integer,\
    quantity integer)

create table customers (\
    id integer primary key autoincrement,\
    name varchar(50),\
    address text,\
    phone_number text,\
    email text)

create table orders (\
    id integer primary key autoincrement,\
    date text,\
    status integer,\
    goods text,\
    customer_id integer)

for _ in range(20):
    cursor.execute(
        f"insert into goods (name, price, quantity, description) values ('\
        {fake.word()}', {random.randint(100, 10000)}, {random.randint(0, 50)}, {fake.sentence()});")

for _ in range(20):
    cursor.execute(
        f"insert into customers (name, address, phone_number, email) values ('\
        {fake.name()}', '{fake.address()}', '{fake.phone_number()}', '{fake.email()}');")
    
for _ in range(20):
    start_date = datetime(2024, 1, 1)
    end_date = datetime(2024, 4, 19)
    random_date = start_date + timedelta(
        seconds=random.randint(0, int((end_date - start_date).total_seconds())))
    random_goods = []
    for _ in range(random.randint(1, 5)):
        random_goods.append(random.randint(1, 20))
    cursor.execute(
        f"insert into orders (date, status, goods, customer_id) values ('\
        {str(random_date)}', {random.randint(1, 5)}, '{str(random_goods)[1:-1]}' ,{random.randint(1, 20)});")


# Выполнение запроса и обработка результата
text = cursor.execute("SELECT sum(quantity) FROM goods").fetchall()

for row in text:
    print(row)

conn.commit()
# conn.close()
