import sys
input = sys.stdin.readline

n = int(input())
numbers = list(map(int, input().split()))
plus, minus, mul, div = map(int, input().split())

min_answer = int(1e9)
max_answer = int(-1e9)

def update_min_max(total):
    global min_answer, max_answer
    min_answer = min(min_answer, total)
    max_answer = max(max_answer, total)

def dfs(depth, total, plus, minus, mul, div):
    if depth == n:
        update_min_max(total)
    if plus > 0:
        dfs(depth + 1, total + numbers[depth], plus - 1, minus, mul, div)
    if minus > 0:
        dfs(depth + 1, total - numbers[depth], plus, minus - 1, mul, div)
    if mul > 0:
        dfs(depth + 1, total * numbers[depth], plus, minus, mul - 1, div)
    if div > 0:
        if total < 0:
            dfs(depth + 1, -(-(total) // numbers[depth]), plus, minus, mul, div - 1)
        else:
            dfs(depth + 1, int(total // numbers[depth]), plus, minus, mul, div - 1)

dfs(1, numbers[0], plus, minus, mul, div)

print(max_answer)
print(min_answer)