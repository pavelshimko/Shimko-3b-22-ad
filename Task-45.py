file_name = input()
try:
    with open(file_name, 'r') as file:
        data = file.read()
        print(data)
        file.close()
except FileNotFoundError:
    print("Ошибка!")
except Exception:
    print("Ошибка!")