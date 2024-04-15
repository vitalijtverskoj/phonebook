from logger import input_data, print_data

def interface():
    print("Телефонный справочник! \n 1 - Показать контакты \n 2 - Добавить контакты "
          "\n 3 - Изменить контакты \n 4 - Удалить контакты \n ")
    command = input("Введите число ")

    while command not in ['1', '2', '3', '4']:
        print("Неправильный ввод")
        command = input("Введите число ")

    if command == 1:
        input_data()
    elif command == 2:
        print_data()

interface()