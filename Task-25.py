number = int(input())

dividers = []

for i in range(1, number + 1):
    s = number % i
    if s ==0:
        dividers.append(i)

if [1, number] == dividers:
    print("Число простое")
else:
    print("Число не простое")