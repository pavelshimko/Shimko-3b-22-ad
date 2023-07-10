import random

array = []

for i in range(10):
    array.append(random.randint(1, 100))

print(f"Максимальное число: {max(array)}")
print(f"Минимальное число: {min(array)}")