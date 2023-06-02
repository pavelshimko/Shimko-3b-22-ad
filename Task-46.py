try:
    with open("text.txt", 'w') as file:
        file.write('Hello, world!')
        file.close()
except Exception as e:
    print(f"Возникла ошибка: {e}")