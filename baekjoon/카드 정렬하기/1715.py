import sys, heapq
input = sys.stdin.readline

n = int(input())
queue = []
for _ in range(n):
    heapq.heappush(queue, int(input()))

count = 0
while len(queue) > 1:
    val1, val2 = heapq.heappop(queue), heapq.heappop(queue)
    new_val = val1 + val2
    count += new_val
    heapq.heappush(queue, new_val)

print(count)
