import sys, itertools
input = sys.stdin.readline

n = int(input())
data = []

for i in range(n):
    line = list(map(int, input().split()))
    data.append(line)

def stat(lst, data):
    count = 0
    for i in range(n//2):
        x = lst[i]
        for j in range(n//2):
            y = lst[j]
            count += data[x][y]
    return count

answer = int(1e9)

combinations = itertools.combinations([i for i in range(n)], n // 2)
for combination in combinations:
    opposite = [i for i in range(n) if i not in list(combination)]
    left = stat(list(combination), data)
    right = stat(opposite, data)
    answer = min(answer, abs(left - right))

print(answer)