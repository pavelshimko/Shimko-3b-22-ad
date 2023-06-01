"""
Имя существующего файла для проверки кода - тест
"""
file_name = input()
if file_name:
    try:
        with open(file_name, 'r') as file:
            data = file.read()
            print(data)
    except FileNotFoundError:
        print("Ошибка!")
    except ValueError:
        print("Ошибка!")
else:
    print("Ошибка!")