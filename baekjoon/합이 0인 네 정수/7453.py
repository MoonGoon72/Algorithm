from collections import defaultdict
import sys
input = sys.stdin.readline

n = int(input())
A, B, C, D = [], [], [], []
for _ in range(n):
    a, b, c, d = map(int, input().split())
    A.append(a)
    B.append(b)
    C.append(c)
    D.append(d)

dict = defaultdict(int)

for a in A:
    for b in B:
        dict[a + b] += 1

answer = 0
for c in C:
    for d in D:
        target = -(c + d)
        if target in dict:
            answer += dict[target]

print(answer)