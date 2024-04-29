import sqlite3 as sql

conn = sql.connect('buildings.db')
cursor = conn.cursor()

cursor.execute("SELECT * FROM buildings")
rows = cursor.fetchall()

def print_buildings(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM buildings")
    rows = cursor.fetchall()
    for row in rows:
        print(row)

def by_typ(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT typ, COUNT(*) as building_count FROM buildings GROUP BY typ")
    rows = cursor.fetchall()
    for row in rows:
        print(row)

def by_city(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT city, COUNT(*) as building_count FROM buildings GROUP BY city")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
        
def by_50(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT SUM(height) as total_height FROM (SELECT height FROM buildings ORDER BY height DESC LIMIT 50)")
    rows = cursor.fetchall()
    for row in rows:
        print(row)



print("Введите цифру:")
print("1.топ N стран по числу высоких зданий")
print("2.здания с группировкой по странам")
print("3.здания с группировкой по типам")
print("4.суммарная высота первых 50 зданий в км")

button_user = 0
while button_user != 4:

    button_user = int(input("Введите значение кнопки (1, 2, 3 или 4):"))
    if button_user == 1:
        print_buildings(conn)
    elif button_user == 2:
        by_typ(conn)
    elif button_user == 3:
        by_city(conn)
    elif button_user == 4:
        by_50(conn)
    else:
        print("Некорректное значение, введите 1, 2, 3, или 4")