from collections import deque
import sys
input = sys.stdin.readline

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

def check(y, x):
    return 1 <= y <= n and 1 <= x <= n

n = int(input())
k = int(input())

apples = []
for _ in range(k):
    r, c = map(int, input().split())
    apples.append((r, c))

l = int(input())
moves = []
for _ in range(l):
    x, c = map(str, input().split())
    moves.append((int(x), c))

def solution():
    queue = deque()
    y, x = 1, 1
    d = 0
    next_move = 0
    answer = 0
    queue.append((y, x))
    while True:
        answer += 1
        y, x = y + dy[d], x + dx[d]
        
        # 충돌 여부 체크
        if not check(y, x) or (y, x) in queue:
            return answer

        # 사과 여부 확인
        if (y, x) not in apples:
            queue.popleft()
        else:
            apples.remove((y, x))
        queue.append((y, x))
        
        # 방향 전환 여부 확인
        if next_move < len(moves) and moves[next_move][0] == answer:
            if moves[next_move][1] == "D":
                d = (d + 1) % 4
            else:
                d = d - 1 if d > 0 else 3
            next_move += 1

print(solution())