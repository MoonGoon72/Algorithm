n, k = map(int, input().split(' '))

arr = [i for i in range(n+1)]
result = []
for i in range(2, n + 1):
    if arr[i] != 0:
        for j in range(i, n+1, i):
            if arr[j] != 0:
                result.append(j)
                arr[j] = 0
            if len(result) == k:
                print(result[-1])
                exit()