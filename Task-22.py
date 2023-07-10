import random

array = [random.randint(1, 10) for x in range(10)]

sum = 0

for i in array:
    sum +=i

print(sum)