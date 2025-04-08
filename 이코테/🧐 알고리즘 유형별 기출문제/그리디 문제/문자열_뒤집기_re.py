data = input()
counts = [0, 0]

if data[0] == "0":
    counts[0] += 1
else:
    counts[1] += 1
for i in range(len(data) - 1):
    if data[i] != data[i + 1]:
        counts[int(data[i + 1])] += 1

print(min(counts))