import sys
input = sys.stdin.readline

n = int(input())
limits = list(map(int, input().split()))
m = int(input())
weights = list(map(int, input().split()))
limits.sort(reverse=True)
weights.sort(reverse=True)

def solution():
    count = 0
    loaded = 0
    if limits[0] < weights[0]:
        return -1

    while loaded < m:
        count += 1
        i = 0
        for c in limits:
            while i < m:
                if weights[i] == -1:
                    i += 1
                    continue
                if weights[i] <= c:
                    loaded += 1
                    weights[i] = -1
                    i += 1
                    break
                else:
                    i += 1
                    continue
    return count

answer = solution()
print(answer)
