from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import sqlite3
# Setup ChromeDriver
s=Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s)

# Open the Wikipedia page
url = "https://ru.wikipedia.org/wiki/%D0%A1%D0%BF%D0%B8%D1%81%D0%BE%D0%BA_%D0%B1%D0%BB%D0%B8%D0%B6%D0%B0%D0%B9%D1%88%D0%B8%D1%85_%D0%B3%D0%B0%D0%BB%D0%B0%D0%BA%D1%82%D0%B8%D0%BA"
driver.get(url)

table = driver.find_element(By.CLASS_NAME, 'wikitable')
rows = table.find_elements(By.TAG_NAME, 'tr')



database_name = 'database.db'



def remove_braces(string: str):
    index1 = string.find('[')
    index2 = string.find(']')
    string = string[:index1] + string[index2 + 1:]
    return string

data = []

# fill galaxies table

for row in rows[2:]:
    cols = row.find_elements(By.TAG_NAME, 'td')
    
    cols_text = [col.text for col in cols]
    if len(cols_text) == 10:
        data.append(
            {
                'galaxy': cols_text[2],
                'type': cols_text[3],
                'grp': cols_text[8],
                'note': cols_text[9]
            }
        )

for row in data:
    conn = sqlite3.connect(database_name)
    cur = conn.cursor()
    keys = ", ".join(row.keys())
    values = ""
    for index, value in enumerate(row.values()):
        values += f"'{value}'"
        if index < len(row.values()) - 1:
            values += ", "
    query_string = f"insert into galaxies ({keys}) values ({values});"
    try:
        cur.execute(query_string)
    except sqlite3.Error as e:
        print(e)
        print(query_string)

    conn.commit()
    conn.close()

# fill distances table

conn = sqlite3.connect(database_name)
cur = conn.cursor()

ids = [id[0] for id in cur.execute('select id from galaxies;').fetchall()]

print(ids)

rows = rows[2:]

dist_data = []

for i in range(len(ids)):
    cols = rows[i].find_elements(By.TAG_NAME, 'td')
    
    cols_text = [col.text for col in cols]
    if len(cols_text) == 10:
        dist_data.append(
            {
                'galaxy_id': ids[i],
                'light_years': cols_text[4],
                'parsecs': cols_text[5],
                'absolute_magnitude': cols_text[6],
                'magnitude': cols_text[7]
            }
        )

for row in dist_data:
    conn = sqlite3.connect(database_name)
    cur = conn.cursor()
    keys = ", ".join(row.keys())
    values = ""
    for index, value in enumerate(row.values()):
        values += f"'{value}'"
        if index < len(row.values()) - 1:
            values += ", "
    query_string = f"insert into distances ({keys}) values ({values});"
    while '[' in query_string:
        query_string = remove_braces(query_string)
    try:
        cur.execute(query_string)
    except sqlite3.Error as e:
        print(e)
        print(query_string)





    conn.commit()
    conn.close()


driver.quit()