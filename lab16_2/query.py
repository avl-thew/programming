import sqlite3

conn = sqlite3.connect('biggeek.db')

cursor = conn.cursor()

cursor.execute(
    """create table phones (
    id integer primary key,
    name varchar(50) not null,
    manufacturer varchar(50),
    price integer
);"""
)

cursor.execute(
    """create table specs (
    id integer primary key,
    phone_id integer,
    country varchar(50),
    os varchar(50),
    color varchar(50),
    storage varchar(50),
    processor varchar(50),
    camera varchar(50),
    FOREIGN KEY (phone_id) REFERENCES phones(id)
);"""
)

# cursor.execute(
#     """drop table models;
# """
# )


# res = cursor.execute(
#     "select name, processor, camera from specs join phones on specs.phone_id = phones.id order by processor;").fetchall()
# for row in res:
#     print(row)
conn.commit()
conn.close()
