arr = [1, 2, 3, 2, 1]
arr_inverted = arr.copy()
arr_inverted.reverse()

if arr == arr_inverted:
    print("Массив является палиндромом")
else:
    print("Массив не является палиндромом")