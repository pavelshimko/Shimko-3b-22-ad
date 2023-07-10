import random

r = int(input())

array = [random.randint(1, 10) for x in range(10)]
print(array)

if r in array:
    print(f"Число найдено в массиве")
else:
    print(f"Число не найдено в массиве")