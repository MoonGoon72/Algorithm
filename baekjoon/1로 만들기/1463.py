INF = float("inf")
number = int(input())

arr = [INF for _ in range(number + 1)]

arr[1] = 0

for i in range(2, number + 1, 1):
    tmp = INF
    if i % 3 == 0: tmp = min(tmp, arr[i // 3])
    if i % 2 == 0: tmp = min(tmp, arr[i // 2])
    tmp = min(tmp, arr[i - 1]) + 1
    arr[i] = tmp

print(arr[number])
