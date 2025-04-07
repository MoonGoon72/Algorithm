data = input()

num = int(data[0])
for i in range(1, len(data)):
    a = int(data[i])
    if num <= 1 or a <= 1:
        num += a
    else:
        num *= a

print(num)
