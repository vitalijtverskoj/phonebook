import sqlite3 as sl
from easygui import *
from user_interface import interface

# создание подключения к БД
conn = sl.connect("phonebook.db")

# создание курсора - основного объекта выполнения SQL кода
cur = conn.cursor()

# создадим таблицу users, если она не создана
cur.execute("""
            CREATE TABLE IF NOT EXISTS users
            (
            id INTEGER PRIMARY KEY,
            name TEXT,
            surname TEXT,
            phone INTEGER,
            email TEXT
            );
            """)

interface()