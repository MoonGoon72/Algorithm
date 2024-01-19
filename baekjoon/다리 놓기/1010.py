import sys
import math
input = sys.stdin.readline

t = int(input())

def calcSite(n, m):
    result = math.comb(m, n)
    print(result)
    return

for _ in range(t):
    n, m = map(int, input().split())
    calcSite(n, m)
