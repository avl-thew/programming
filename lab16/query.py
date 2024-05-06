import sqlite3

conn = sqlite3.connect('database.db')

cursor = conn.cursor()

cursor.execute(
"""create table galaxies (
    id integer primary key,
    galaxy varchar(50) not null,
    type varchar(50),
    grp varchar(50),
    note text
);"""
)

cursor.execute(
"""create table distances (
    id integer primary key,
    galaxy_id integer,
    light_years real,
    parsecs real,
    absolute_magnitude real,
    magnitude real,
    FOREIGN KEY (galaxy_id) REFERENCES galaxies(id)
);"""
)

conn.commit()
conn.close()