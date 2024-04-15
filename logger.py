from data_create import name_data, surname_data, phone_data, email_data
from main import cur,conn

def input_data():
    name = name_data()
    surname = surname_data()
    phone = phone_data()
    email = email_data()

    var = int(input("Сохранить данные? \n 1 - Да \n 2 - Нет \n"))

    if var == 1:
        string = f"INSERT INTO users (name, surname, phone, email) VALUES ('{name}', '{surname}', '{phone}', '{email}');"
        cur.execute(string)
        conn.commit()

def print_data():
    var = int(input("Выберете вариант \n 1 - Показать все контакты \n 2 - Введите Фамилию \n"))
    if var == 1:
        cur.execute("SELECT * FROM users;")
        print(cur.fetchall())
    elif var == 2:
        surname = surname_data()
        cur.execute(f"SELECT * FROM users WHERE surname = {surname};")
        print(cur.fetchall())

def update_data():
    pass

def delete_data():
    pass