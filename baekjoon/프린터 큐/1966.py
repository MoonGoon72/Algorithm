from collections import deque
T = int(input())
for _ in range(T):
    N, M = map(int, input().split(' '))
    queue = deque()
    
    arr = list(map(int, input().split(' ')))
    for i in range(N):
        queue.append((arr[i], i))

    count = 0
    while True:
        if queue[0][0] == max(queue, key=lambda x : x[0])[0]:
            count += 1
            _, num = queue.popleft()
            if num == M:
                print(count)
                break
        else: queue.append(queue.popleft())
