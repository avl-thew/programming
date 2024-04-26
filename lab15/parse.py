import locale
from datetime import datetime
from typing import Optional

import bs4
import requests
from icecream import ic
from pprint import pprint
from db_api import create_sqlite_connection, execute_query, execute_read_query



locale.setlocale(locale.LC_ALL, "ru_RU.UTF-8")

def get_html(url) -> Optional[str]:
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    return None


def parse_date(date_str: str) -> datetime:
    return datetime.strptime(date_str, "%d %B %Y").date()



def parse_natural_reserves(url: str) -> list[dict]:
    html = get_html(url)
    soup = bs4.BeautifulSoup(html, "html.parser")
    table = soup.find("tbody")
    rows = table.find_all("tr")

    data = []

    for row in rows[1:]:
        for cell in row.find_all("td"):
            span = cell.find("span", class_="noprint")
            if span:
                span.clear()
        cells = [cell.text.strip().replace(u'\xa0','').split("[")[0].split("ГПЗ")[0] for cell in row.find_all("td")]
        

        if len(cells) == 7:
            location = cells[2]
            area_i = 3
        if len(cells) == 6:
            area_i = 2
        fnd_date_i = area_i + 1


        data_dict = {
            "name": cells[1],
            "location": location,
            "area": float(cells[area_i].replace(",", ".")),
            "fnd_date": parse_date(cells[fnd_date_i]),
        }
        data.append(data_dict)
    return data


URL = "https://ru.wikipedia.org/wiki/%D0%A1%D0%BF%D0%B8%D1%81%D0%BE%D0%BA_%D0%B7%D0%B0%D0%BF%D0%BE%D0%B2%D0%B5%D0%B4%D0%BD%D0%B8%D0%BA%D0%BE%D0%B2_%D0%A0%D0%BE%D1%81%D1%81%D0%B8%D0%B8"


CREATE_LOCATIONS = """CREATE TABLE IF NOT EXISTS locations (
    loc_id integer PRIMARY KEY AUTOINCREMENT,
    name text NOT NULL
);"""


CREATE_RESERVES = """CREATE TABLE IF NOT EXISTS reserves (
    id integer PRIMARY KEY AUTOINCREMENT,
    name text NOT NULL,
    loc_id integer NOT NULL,
    area real NOT NULL,
    fnd_date datetime NOT NULL,
    FOREIGN KEY (loc_id) REFERENCES locations(loc_id) 
);"""


INSERT_LOCATION = """INSERT INTO locations (name) VALUES (:location);"""


INSERT_RESERVE = """INSERT INTO reserves (name, loc_id, area, fnd_date) VALUES
(:name, :loc_id, :area, :fnd_date);"""


if __name__ == "__main__":
    
    conn = create_sqlite_connection("reserves.db")

    execute_query(conn, "DROP TABLE locations;")
    execute_query(conn, "DROP TABLE reserves;")
    execute_query(conn, CREATE_LOCATIONS)
    execute_query(conn, CREATE_RESERVES)


    data = parse_natural_reserves(URL)

    for d in data:
        q_res = execute_read_query(conn, "SELECT loc_id FROM locations WHERE name = :location;", d)
        if q_res:
            d["loc_id"] = q_res[0][0]
        else:
            execute_query(conn, INSERT_LOCATION, d)
            d["loc_id"] = execute_read_query(conn, "SELECT loc_id FROM locations WHERE name = :location;", d)[0][0]
        
        execute_query(conn, INSERT_RESERVE, d)
    
    pprint(execute_read_query(conn, "SELECT * FROM reserves;"))
    ic(execute_read_query(conn, "SELECT * FROM locations;"))
    
