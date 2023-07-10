
numbers = [x for x in range(1, 11)]

for i in numbers:
    table = [f'{i}x{x}={i*x}' for x in numbers]
    print(table)