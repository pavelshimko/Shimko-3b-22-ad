length = 10

seq = [1, 1]

for i in range(length - len(seq)):
    seq.append(seq[i] + seq[i + 1])

print(seq)