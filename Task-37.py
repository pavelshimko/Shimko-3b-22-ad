import random

a = [random.randint(1, 100) for x in range(10)]
print(a)
first_min = min(a)
a.remove(first_min)
second_min = min(a)

print(f"Самое наименьшее {first_min}, второе наименьшее {second_min}")
