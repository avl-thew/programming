from pypika import Query, Table, JoinType, functions as fn
import sqlite3

conn = sqlite3.connect('biggeek.db')
cursor = conn.cursor()

phones = Table('phones')
specs = Table('specs')

def id_phones_specs(conn):
    query = (
        Query.from_(phones)
        .join(specs, JoinType.left)
        .on(phones.id == specs.phone_id)
        .select(
            phones.name,
            phones.manufacturer,
            phones.price,
            specs.country,
            specs.os,
            specs.color,
            specs.storage,
            specs.processor,
            specs.camera
        )
    )
    cursor = conn.cursor()
    cursor.execute(query.get_sql())
    result = cursor.fetchall()
    print(result)

def LEFT_JOIN(conn):
    manufacturer = 'Apple'
    query = (
        Query.from_(phones)
        .join(specs, JoinType.left)
        .on(phones.id == specs.phone_id)
        .select(
            phones.name,
            phones.manufacturer,
            phones.price,
            specs.country,
            specs.os,
            specs.color,
            specs.storage,
            specs.processor,
            specs.camera
        )
        .where(phones.manufacturer == manufacturer)
    )
    cursor = conn.cursor()
    cursor.execute(query.get_sql())
    result = cursor.fetchall()
    print(result)

def by_phone(conn):
    query = (
        Query.from_(phones)
        .select(phones.manufacturer, fn.Count(phones.id))
        .groupby(phones.manufacturer)
    )
    cursor = conn.cursor()
    cursor.execute(query.get_sql())
    result = cursor.fetchall()
    print(result)

def by_specs(conn):
    query = (
        Query.from_(phones)
        .select(
            phones.manufacturer,
            fn.Min(phones.price),
            fn.Max(phones.price),
            fn.Avg(phones.price)
        )
        .groupby(phones.manufacturer)
    )
    cursor = conn.cursor()
    cursor.execute(query.get_sql())
    result = cursor.fetchall()
    print(result)

def by_color(conn):
    query = (
        Query.from_(specs)
        .select(specs.color, fn.Count(specs.phone_id))
        .groupby(specs.color)
    )
    cursor = conn.cursor()
    cursor.execute(query.get_sql())
    result = cursor.fetchall()
    print(result)

print("Введите цифру:")
print("1. Запрос с JOIN:")
print("2. Запрос с JOIN для телефонов определенного производителя:")
print("3. Запрос с агрегирующей функцией:")
print("4. Запрос с группировкой:")
print("5. Запрос с агрегирующей функцией для цветов телефонов:")

while True:
    try:
        button_user = int(input("Введите значение кнопки (1, 2, 3, 4 или 5): "))
        if button_user == 1:
            id_phones_specs(conn)
        elif button_user == 2:
            LEFT_JOIN(conn)
        elif button_user == 3:
            by_phone(conn)
        elif button_user == 4:
            by_specs(conn)
        elif button_user == 5:
            by_color(conn)
        else:
            print("Некорректное значение, введите 1, 2, 3, 4 или 5")
    except ValueError:
        print("Ожидается число. Попробуйте еще раз.")
