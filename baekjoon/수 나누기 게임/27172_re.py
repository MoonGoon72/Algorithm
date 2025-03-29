import sys
input = sys.stdin.readline
MILLION = 1_000_000

n = int(input())
cards = list(map(int, input().split()))

arr = [0] + [0] * MILLION
is_appear = [False] + [False] * MILLION

for card in cards:
    is_appear[card] = True

for card in cards:
    i = 2
    num = card * i
    while num <= MILLION:
        if is_appear[num]:
            arr[card] += 1
            arr[num] -= 1
        i += 1
        num = card * i

result = []
for i in range(n):
    result.append(arr[cards[i]])
print(*result)