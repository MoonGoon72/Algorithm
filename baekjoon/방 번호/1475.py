import math
n = input()

arr = []

result = 0

for i in n:
    arr.append(int(i))

for num in range(10):
    if num == 6 or num == 9: continue
    result = max(result, arr.count(num))

tmp = 0
tmp += arr.count(6)
tmp += arr.count(9)

tmp = math.ceil(tmp / 2)

result = max(result, tmp)

print(result)
