file_name = input()
try:
    with open(file_name, 'r') as file:
        data = file.read()
        print(data)
except FileNotFoundError:
    print("Ошибка!")