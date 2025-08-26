import sys
input = sys.stdin.readline

n = int(input())
data = list(map(int, input().split()))
data.sort()
mid = n // 2
if n % 2  == 0:
    print(data[mid - 1])
else:
    print(data[mid])
# 쉬운 방법은 data[(n-1)//2]를 하면 위 두 상황 모두 반영됨