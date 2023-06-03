arr = [(1, 2), (3, 4), (-1, 5), (6, -3)]

distances = []

for i in arr:
    x = i[0]
    y = i[1]
    distance = (x**2 + y**2) ** (1/2)
    distances.append(distance)

distances.sort()
print(distances)