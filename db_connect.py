import sqlite3 as sl
from sqlite3 import Error

def create_connection():
    connection = None
    try:
        connection = sl.connect("phonebook.db")
    except Error as e:
        print(f"Произошла ошибка '{e}' ")
    
    return connection

def create_cur():
    connection = create_connection()
    cur = connection.cursor()
    
    return cur
