import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N, M = map(int, input().split(' '))
numbers = sorted(list(map(int, input().split(' '))))
answer = []

def dfs(n, s, lst):
    if n == M:
        answer.append(lst)
        return
    
    prev = 0
    for i in range(s, N):
        if prev != numbers[i]:
            prev = numbers[i]
            dfs(n+1, i, lst+[numbers[i]])

dfs(0, 0, [])

for lst in answer:
    print(*lst)