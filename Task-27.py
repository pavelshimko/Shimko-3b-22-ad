import random

array = [random.randint(1, 100) for x in range(10)]

for i in array:
    if i % 2 == 0:
        print(f"{i} - число четное")