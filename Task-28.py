a = 100
b = 17

def calculator(a, b, mode = '+'):
    if mode == '+':
        return a + b
    elif mode == '-':
        return a - b
    elif mode == '/':
        return a / b
    elif mode == '*':
        return a * b

g = calculator(a, b, '*')
print(g)