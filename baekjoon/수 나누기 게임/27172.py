import sys
input = sys.stdin.readline

n = int(input())
cards = list(map(int, input().split()))
scores = [0] * n
is_here = [False] * 1_000_001
arr = [0] * 1_000_001
for card in cards:
    is_here[card] = True

for card in cards:
    j = 2
    num = card * j
    while num < 1_000_001:
        if is_here[num]:
            arr[card] += 1
            arr[num] -= 1
        j += 1
        num = card * j

for i in range(n):
    scores[i] = arr[cards[i]]

print(*scores)