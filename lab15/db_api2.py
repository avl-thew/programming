import sqlite3
from pathlib import Path
from sqlite3 import Error as DB_Error
from typing import Optional, Union


def create_sqlite_connection(
    db_path: Union[str, Path], print_info: bool = False
) -> Optional[sqlite3.Connection]:
    connection = None
    try:
        connection = sqlite3.connect(str(db_path))
        if print_info:
            print("Connection to sqlite3 database established")
    except DB_Error as exc:
        print(f"Connection failed: {exc}")
    return connection


def execute_query(
    connection: sqlite3.Connection,
    query: str,
    data: tuple = (),
    print_info: bool = False,
) -> None:
    cursor = connection.cursor()
    try:
        cursor.execute(query, data)
        connection.commit()
        if print_info:
            print("Query executed successfully")
    except DB_Error as exc:
        print(f"Query execution failed: {exc}")
    finally:
        cursor.close()


def execute_read_query(
    connection: sqlite3.Connection,
    query: str,
    data: tuple = (),
    print_info: bool = False,
) -> Optional[list]:
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query, data)
        result = cursor.fetchall()
        connection.commit()
        if print_info:
            print("Query executed successfully")
    except DB_Error as exc:
        print(f"Query execution failed: {exc}")
    finally:
        cursor.close()
    return result