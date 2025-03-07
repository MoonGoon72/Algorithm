import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

# dp 테이블을 정의를 잘 생각해봅시다.
# d[i] 는 i까지 왔을 때 최대 값이다. arr[i]를 포함하지 않고 arr[i - 1]까지의 최대값이 될 수도 있다는 뜻
d = [0] * 100

d[0] = arr[0]
d[1] = max(arr[0], arr[1])

for i in range(2, n):
    d[i] = max(d[i - 1], d[i - 2] + arr[i])

print(d[n - 1])