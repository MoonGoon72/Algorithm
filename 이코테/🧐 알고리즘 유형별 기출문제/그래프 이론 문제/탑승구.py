# 공항
# boj.kr/10755

import sys
input = sys.stdin.readline

def find(x):
    if gates[x] != x:
        gates[x] = find(gates[x])
    return gates[x]

def union(x, y):
    px, py = find(x), find(y)
    if px == py:
        return
    
    if px < py:
        gates[py] = px
    else:
        gates[px] = py
    return


g = int(input())
p = int(input())
gates = [i for i in range(g + 1)]

planes = []
for _ in range(p):
    planes.append(int(input()))

count = 0
for x in planes:
    px = find(x)
    if px == 0:
        break
    union(px, px - 1)
    count += 1

print(count)