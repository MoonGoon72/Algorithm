import sys
input = sys.stdin.readline
N = int(input())
list = list(int(input()) for _ in range(N))
list.sort()
print(*list, sep='\n')
