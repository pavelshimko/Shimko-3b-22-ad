try:
    with open("text.txt", 'w') as file:
        file.write('Hello, world!')
except Exception as e:
    print(f"Возникла ошибка: {e}")