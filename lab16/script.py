import sqlite3
# pip install --upgrade pypika
from pypika import Query, Table, functions as fn

conn = sqlite3.connect('database.db')
cursor = conn.cursor()

# Запрос к таблице galaxies
cursor.execute("SELECT * FROM galaxies")
galaxies_rows = cursor.fetchall()

# Запрос к таблице distances
cursor.execute("SELECT * FROM distances")
distances_rows = cursor.fetchall()

galaxies = Table('galaxies')
distances = Table('distances')

def id_galaxies_distances(conn):
    query = Query.from_(galaxies).join(distances).on(galaxies.id == distances.galaxy_id).select(galaxies.galaxy, distances.light_years)
    cursor = conn.cursor()
    cursor.execute(query.get_sql())
    result = cursor.fetchall()
    print(result)

def LEFT_JOIN(conn):
    query = Query.from_(galaxies).left_join(distances).on(galaxies.id == distances.galaxy_id).select(galaxies.galaxy, distances.light_years)
    cursor = conn.cursor()
    cursor.execute(query.get_sql())
    result = cursor.fetchall()
    print(result)

def by_type(conn):
    query = Query.from_(galaxies).select(fn.Count('*'))
    cursor = conn.cursor()
    cursor.execute(query.get_sql())
    result = cursor.fetchall()
    print(result)
    
def absolute_tude(conn):
    query = Query.from_(distances).select(fn.Count('*'))
    cursor = conn.cursor()
    cursor.execute(query.get_sql())
    result = cursor.fetchall()
    print(result)

def limit_distances(conn):
    query = Query.from_(galaxies).select(fn.Count('*')).group_by(galaxies.type)
    cursor = conn.cursor()
    cursor.execute(query.get_sql())
    result = cursor.fetchall()
    print(result)



print("Введите цифру:")
print("1.Запрос на объединение таблиц galaxies и distances по id галактики:")
print("2.Запрос на объединение таблиц galaxies и distances с использованием LEFT JOIN:")
print("3.Запрос на выборку всех галактик в БД:")
print("4.Запрос на выборку всех дистанций в БД:")
print("5.Запрос на наиболее популярный тип галактики:")

while True:
    try:
        button_user = int(input("Введите значение кнопки (1, 2, 3, 4 или 5):"))
        if button_user == 1:
            id_galaxies_distances(conn)
        elif button_user == 2:
            LEFT_JOIN(conn)
        elif button_user == 3:
            by_type(conn)
        elif button_user == 4:
            absolute_tude(conn)
        elif button_user == 5:
            limit_distances(conn)
        else:
            print("Некорректное значение, введите 1, 2, 3, 4 или 5")
    except ValueError:
        print("Ожидается число. Попробуйте еще раз.")