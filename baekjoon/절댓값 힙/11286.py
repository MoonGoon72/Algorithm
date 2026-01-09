import sys, heapq
input = sys.stdin.readline

n = int(input())
heap = []

for _ in range(n):
    op = int(input())
    if op == 0:
        if len(heap) == 0:
            print(0)
        else:
            v, sign = heapq.heappop(heap)
            print(v * sign)
    else:
        heapq.heappush(heap, (abs(op), 1 if op > 0 else -1))
