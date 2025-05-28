import sys, heapq
input = sys.stdin.readline

n = int(input())
queue = []
for _ in range(n):
    heapq.heappush(queue, int(input()))

answer = 0
while len(queue) > 1:
    first = heapq.heappop(queue)
    second = heapq.heappop(queue)
    summation = first + second
    answer += summation
    heapq.heappush(queue, summation)

print(answer)