number = input()
try:
    number = float(number)
    number = number ** 2
    print(number)
except Exception as e:
    print('Ошибка')
