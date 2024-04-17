import sqlite3 as sl
from data_create import name_data, surname_data, phone_data, email_data

def interface():

    print("Телефонный справочник! \n 1 - Показать контакты \n 2 - Добавить контакты "
          "\n 3 - Изменить контакты \n 4 - Удалить контакты \n 5 - Выход \n")
    
    while True:
        try:
            command = int(input("Выберите вариант "))
        except ValueError:
            print("Выберете один из 5-ти вариантов")
            continue
        if command in [1, 2, 3, 4, 5]:
            if command == 1:
                print_data()
            elif command == 2:
                input_data()
            elif command == 3:
                update_data()
            elif command == 4:
                delete_data()
            elif command == 5:
                conn.close()
                break
            print("Телефонный справочник! \n 1 - Показать контакты \n 2 - Добавить контакты "
                    "\n 3 - Изменить контакты \n 4 - Удалить контакты \n 5 - Выход \n")
        else:
            print("Выберете один из 5-ти вариантов")

def input_data():
    name = name_data()
    surname = surname_data()
    phone = phone_data()
    email = email_data()
    var = int(input("Сохранить данные? \n 1 - Да \n 2 - Нет \n"))

    if var == 1:
        cur.execute(f"INSERT INTO users (name, surname, phone, email) "
                    f"VALUES ('{name}', '{surname}', '{phone}', '{email}');")
        conn.commit()

def print_data():
    var = int(input("Выберете вариант \n 1 - Показать все контакты \n 2 - Введите Фамилию \n"))
    if var == 1:
        cur.execute("SELECT * FROM users;")
        print(cur.fetchall())
    elif var == 2:
        surname = surname_data()
        cur.execute(f"SELECT * FROM users WHERE surname = '{surname}';")
        print(cur.fetchall())

def update_data():
    print("Какой контакт хотите изменить? Введите фамилию")
    surname_upd = surname_data()
    print("Введите новые данные.")
    name = name_data()
    surname = surname_data()
    phone = phone_data()
    email = email_data()
    var = int(input("Сохранить данные? \n 1 - Да \n 2 - Нет \n"))

    if var == 1:
        cur.execute(f"UPDATE users SET name = '{name}', surname = '{surname}', "
                    f"phone = '{phone}', email = '{email}' WHERE surname = '{surname_upd}';")
        conn.commit()


def delete_data():
    print("Какой контакт хотите удалить? Выберите фамилию")
    surname = surname_data()
    cur.execute(f"DELETE FROM users WHERE surname='{surname}';")
    conn.commit()


conn = sl.connect("phonebook.db")
cur = conn.cursor()

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