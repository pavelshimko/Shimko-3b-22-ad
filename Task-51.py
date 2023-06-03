arr1 = [24, 36, 48, 60]
arr2 = [12, 18, 24, 36, 72]

mutual_array = []
mutual_array.extend(arr1)
mutual_array.extend(arr2)

mutual_array.sort()

biggest_number = mutual_array.pop()
mutual_array.insert(len(mutual_array), biggest_number)

common_denominators = []

biggest_number_denominators = []

for i in range(1, biggest_number + 1):
    n = biggest_number % i
    if n == 0:
        biggest_number_denominators.append(i)

biggest_number_denominators.sort()

for d in biggest_number_denominators:
    arr = []
    for i in mutual_array:
        n = i % d
        if n == 0:
            arr.append(d)
        if len(arr) == len(mutual_array):
            common_denominators.append(d)

common_denominators.sort()

biggest_common_denominator = common_denominators.pop()
print(biggest_common_denominator)