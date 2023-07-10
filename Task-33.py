string = input()

unique = set(string.lower())

freq = 0
for i in unique:
    for s in string:
        if i == s:
            freq += 1
    print(f"Частота буквы {i}: {freq}")
    freq = 0
