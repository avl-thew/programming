import sqlite3 as sql

conn = sql.connect('store.db')
cursor = conn.cursor()

cursor.execute("SELECT * FROM goods")
rows = cursor.fetchall()

cursor.execute("SELECT * FROM orders")
rows = cursor.fetchall()

cursor.execute("SELECT * FROM customers")
rows = cursor.fetchall()

index_order = input("Введите индекс заказа:")
sql_one = "SELECT * FROM orders WHERE id={}".format(index_order)
text = cursor.execute(sql_one).fetchall()

if text:
    row = text[0] 

    for i, val in enumerate(row):  
        if i == 0:
            print("id заказа: " + str(val))
        if i == 1:
            print("Дата заказа: " + str(val))
        if i == 2:
            print("Статус заказа: " + str(val))
        if i == 3:
            for good in val.split(", "):
                sql_two = "SELECT name FROM goods WHERE id='{}'".format(str(good))
                text2 = cursor.execute(sql_two).fetchall()
                product_names = ", ".join([item[0] for item in text2])
                print("Выбранные товары: {}".format(product_names))
        if i == 4:
            sql_three = "SELECT * FROM customers WHERE id='{}'".format(val) 
            text3 = cursor.execute(sql_three).fetchall()  
            print("ID пользователя: {}".format(text3))
    i+=1
# for row in text[0]:
#     print(row)
