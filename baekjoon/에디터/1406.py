import sys
from collections import deque
input = sys.stdin.readline

def solution():
    s = list(input().rstrip())
    m = int(input())

    l_q = deque(s)
    r_q = deque([])

    for _ in range(m):
        op = list(map(str, input().split()))
        
        if len(op) == 2:
            c = op[1]
            l_q.append(c)
        else:
            if op[0] == "L":
                if not l_q: continue
                c = l_q.pop()
                r_q.appendleft(c)
            elif op[0] == "D":
                if not r_q: continue
                c = r_q.popleft()
                l_q.append(c)
            else:  # B
                if not l_q: continue
                l_q.pop()
    print("".join(l_q + r_q))
solution()