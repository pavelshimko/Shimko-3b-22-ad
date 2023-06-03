import os

extension = input()

try:
    list_of_files = os.listdir(r'C:\Users\Pavel Shimko\PycharmProjects\Shimko-3b-22-ad')
    files = 0
    for i in list_of_files:
        if i.split(".", 1)[1] == extension:
            files += 1
    print(f"Список файлов с заданным расширением {extension}: {files}")
except NotADirectoryError:
    print("Ошибка")
