import sys, heapq
input = sys.stdin.readline

n = int(input())
min_heap = []
max_heap = []

for _ in range(n):
    num = int(input())
    if not max_heap or num < -max_heap[0]:
        heapq.heappush(max_heap, -num)
        if len(max_heap) > len(min_heap) + 1:
            heapq.heappush(min_heap, -heapq.heappop(max_heap))
    else:
        heapq.heappush(min_heap, num)
        if len(min_heap) > len(max_heap):
            heapq.heappush(max_heap, -heapq.heappop(min_heap))
    print(-max_heap[0])
