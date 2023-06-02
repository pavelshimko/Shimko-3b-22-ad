import os

list_of_files = os.listdir(r'C:\Users\Pavel Shimko\PycharmProjects\Shimko-3b-22-ad')

if 'text.txt' in list_of_files:
    print("Файл существует")
else:
    print("Файл не найден")