import sys, heapq
input = sys.stdin.readline

n, k = map(int, input().split())
juwly = []
bags = []

for _ in range(n):
    m, v = map(int, input().split())
    juwly.append((m, v))
for _ in range(k):
    bags.append((int(input())))

juwly.sort()
bags.sort()
answer = 0
max_heap = []
j = 0

for bag in bags:
    while j < n and juwly[j][0] <= bag:
        heapq.heappush(max_heap, -juwly[j][1])
        j += 1
    
    if max_heap:
        answer += -heapq.heappop(max_heap)

print(answer)