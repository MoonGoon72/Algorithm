import sys, heapq
input = sys.stdin.readline

n = int(input())
min_heap = []
max_heap = []
# max_heap + min_heap 순서로 정렬된다고 생각하기
# [1, 2, 3, 4, 5]는 [1, 2, 3], [4, 5] 로 나눈다고 생각해보면
# 3이 중앙값이고, 중앙값을 기준으로 왼쪽을 보면 [2, 1]이고 (최대 힙)
# 오른쪽을 보면 [4, 5] (최소 힙)
# 그렇기 때문에 최대 힙이 최소 힙보다 같거나 1 크게 유지하면서, 중앙값을 갱신해줄 수 있다.
for i in range(n):
    num = int(input())
    if not max_heap or num <= -max_heap[0]:
        heapq.heappush(max_heap, -num)
    else:
        heapq.heappush(min_heap, num)
    if len(min_heap) > len(max_heap):
        heapq.heappush(max_heap, -heapq.heappop(min_heap))
    elif len(min_heap) + 1 < len(max_heap):
        heapq.heappush(min_heap, -heapq.heappop(max_heap))
    print(-max_heap[0])