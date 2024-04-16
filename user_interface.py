from logger import input_data, print_data, update_data, delete_data

def interface():
    print("Телефонный справочник! \n 1 - Показать контакты \n 2 - Добавить контакты "
          "\n 3 - Изменить контакты \n 4 - Удалить контакты \n 5 - Выход \n")
    
    while True:
        try:
            command = int(input("Выберите вариант "))
        except ValueError:
            print("Выберете один из 4-х вариантов")
            continue
        if command in [1, 2, 3, 4]:
            if command == 1:
                print_data()
            elif command == 2:
                input_data()
            elif command == 3:
                update_data()
            elif command == 4:
                delete_data()
            elif command == 5:
                break
            print("Телефонный справочник! \n 1 - Показать контакты \n 2 - Добавить контакты "
                    "\n 3 - Изменить контакты \n 4 - Удалить контакты \n 5 - Выход \n")
        else:
            print("Выберете один из 4-х вариантов")
