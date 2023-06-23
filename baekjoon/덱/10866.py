import sys
input = sys.stdin.readline
n = int(input())
queue = []

def deque(order):
    global queue
    if order[0] == 'push_front':
        queue.insert(0, order[1])
    elif order[0] == 'push_back':
        queue.insert(len(queue), order[1])
    elif order[0] == 'pop_front':
        if not queue:
            print(-1)
        else:
            print(queue.pop(0))
    elif order[0] == 'pop_back':
        if not queue:
            print(-1)
        else:
            print(queue.pop(-1))
    elif order[0] == 'size':
        print(len(queue))
    elif order[0] == 'empty':
        print(0) if queue else print(1)
    elif order[0] == 'front':
        if not queue: print(-1)
        else: print(queue[0])
    elif order[0] == 'back':
        if not queue: print(-1)
        else: print(queue[-1])

for _ in range(n):
    order = list(map(str, input().split()))
    deque(order)