from data_create import name_data, surname_data, phone_data, email_data
from db_connect import create_connection, create_cur


def input_data():
    cur = create_cur()
    conn = create_connection()
    name = name_data()
    surname = surname_data()
    phone = phone_data()
    email = email_data()
    var = int(input("Сохранить данные? \n 1 - Да \n 2 - Нет \n"))

    if var == 1:
        cur.execute(f"INSERT INTO users (name, surname, phone, email) VALUES ('{name}', '{surname}', '{phone}', '{email}');")
        conn.commit()
        conn.close()

def print_data():
    var = int(input("Выберете вариант \n 1 - Показать все контакты \n 2 - Введите Фамилию \n"))
    cur = create_cur()
    conn = create_connection()
    if var == 1:
        cur.execute("SELECT * FROM users;")
        print(cur.fetchall())
    elif var == 2:
        surname = surname_data()
        cur.execute(f"SELECT * FROM users WHERE surname = '{surname}';")
        print(cur.fetchall())
    conn.close()

def update_data():
    pass

def delete_data():
    conn = create_connection()
    cur = create_cur()
    print("Какой контакт хотите удалить? Выберите фамилию")
    surname = surname_data()
    cur.execute(f"DELETE FROM users WHERE surname='{surname}';")
    conn.commit()
    conn.close()
