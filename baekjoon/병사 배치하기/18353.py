import sys, bisect
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
arr.reverse()
lis = []

for i in range(n):
    if len(lis) == 0:
        lis.append(arr[i])
        continue
    if lis[-1] < arr[i]:
        lis.append(arr[i])
    else:
        idx = bisect.bisect_left(lis, arr[i])
        lis[idx] = arr[i]

print(n - len(lis))