import sys
input = sys.stdin.readline

n, c = map(int, input().split())
houses = []
for _ in range(n):
    houses.append(int(input()))
houses.sort()

def solution():
    start = 1
    end = houses[n - 1] - houses[0]
    answer = 0
    while start <= end:
        mid = (start + end) // 2
        value = houses[0]
        count = 1
        for i in range(1, n):
            if houses[i] - value >= mid:
                value = houses[i]
                count += 1
        if count >= c:
            answer = mid
            start = mid + 1
        else:
            end = mid - 1
    print(answer)

solution()