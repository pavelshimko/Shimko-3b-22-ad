arr = input()

arr = arr.split(",")
arr = [int(x) for x in arr]

min = arr[0]

for i in arr:
    if i < min:
        min = i

print(min)