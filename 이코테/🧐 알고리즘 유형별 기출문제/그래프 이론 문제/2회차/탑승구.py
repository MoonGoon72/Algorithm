# https://www.acmicpc.net/problem/10775

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

g, p = int(input()), int(input())
gates = [i for i in range(g + 1)] 
planes = []

def union(px, py):
    gates[px] = py

def find(x):
    if gates[x] != x:
        gates[x] = find(gates[x])
    return gates[x]

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