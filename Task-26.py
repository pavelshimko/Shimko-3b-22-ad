a = 120
b = 50

def get_dividers(number):
    dividers = []
    for i in range(1, number + 1):
        s = number % i
        if s == 0:
            dividers.append(i)
    return dividers

a_dividers = get_dividers(a)
b_dividers = get_dividers(b)
common_dividers = []
for i in a_dividers:
    if i in b_dividers:
        common_dividers.append(i)

for i in b_dividers:
    if i in a_dividers and i not in common_dividers:
        common_dividers.append(i)
common_dividers.remove(1)

if len(common_dividers) != 0:
    print(f"НОД равен {common_dividers[0]}")
else:
    print(f"Не нашлось общих делителей")
