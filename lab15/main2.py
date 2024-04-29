#pip install requests bs4
import sqlite3
from bs4 import BeautifulSoup
import requests

def get_html(url):
    r = requests.get(url)
    return r.text

def create_connection():
    conn = sqlite3.connect('buildings.db')
    return conn

def create_table(conn):
 
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS buildings
        (id INTEGER PRIMARY KEY,
        rank TEXT,
        building TEXT,
        city TEXT,
        height TEXT,
        numberoffloors TEXT,
        year TEXT,
        typ TEXT)''')
        conn.commit()

import re
def insert_building(conn, rank, building, city, height, numberoffloors, year, typ):
        height_value = re.findall(r'\d+', height)
        if height_value:
            height_numeric = float(height_value[0])
        else:
            height_numeric = 0
        cursor = conn.cursor()
        cursor.execute('''INSERT INTO buildings (rank, building, city, height, numberoffloors, year, typ)
        VALUES (?, ?, ?, ?, ?, ?, ?)''', (rank, building, city, height_numeric, numberoffloors, year, typ))
        conn.commit()
 
# def print_buildings(conn):
#     cursor = conn.cursor()
#     cursor.execute("SELECT * FROM buildings")
#     rows = cursor.fetchall()
#     for row in rows:
#         print(row)

# def by_typ(conn):
#     cursor = conn.cursor()
#     cursor.execute("SELECT typ, COUNT(*) as building_count FROM buildings GROUP BY typ")
#     rows = cursor.fetchall()
#     for row in rows:
#         print(row)

# def by_city(conn):
#     cursor = conn.cursor()
#     cursor.execute("SELECT city, COUNT(*) as building_count FROM buildings GROUP BY city")
#     rows = cursor.fetchall()
#     for row in rows:
#         print(row)
        
# def by_50(conn):
#     cursor = conn.cursor()
#     cursor.execute("SELECT SUM(height) as total_height FROM (SELECT height FROM buildings ORDER BY height DESC LIMIT 50)")
#     rows = cursor.fetchall()
#     for row in rows:
#         print(row)
               

def main():
    url = 'https://ru.wikipedia.org/wiki/%D0%A1%D0%BF%D0%B8%D1%81%D0%BE%D0%BA_%D1%81%D0%B0%D0%BC%D1%8B%D1%85_%D0%B2%D1%8B%D1%81%D0%BE%D0%BA%D0%B8%D1%85_%D0%B7%D0%B4%D0%B0%D0%BD%D0%B8%D0%B9_%D0%B8_%D1%81%D0%BE%D0%BE%D1%80%D1%83%D0%B6%D0%B5%D0%BD%D0%B8%D0%B9_%D0%BC%D0%B8%D1%80%D0%B0'
    html = get_html(url)
    soup = BeautifulSoup(html, 'html.parser')
    table = soup.find('table', {'class': 'wikitable'})
    conn = create_connection()
    
    create_table(conn)

    for row in table.find_all('tr')[1:]:
        columns = row.find_all('td')
        if columns:
            rank = columns[0].get_text(strip=True)
            building = columns[1].find('a').get_text(strip=True)
            city = columns[3].get_text(strip=True)
            height = columns[4].get_text(strip=True)
            numberoffloors = columns[5].get_text(strip=True)
            year = columns[6].get_text(strip=True)
            typ = columns[7].get_text(strip=True)
            insert_building(conn, rank, building, city, height, numberoffloors, year, typ)
    # print_buildings(conn)
    # by_city(conn)
    # by_typ(conn)
    # by_50(conn)
    conn.close()



if __name__ == "__main__":
    main()
    
        