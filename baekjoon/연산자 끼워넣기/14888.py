import sys
input = sys.stdin.readline

n = int(input())
data = list(map(int, input().split()))
add, sub, mul, div = list(map(int, input().split()))
min_value = int(1e9)
max_value = int(-1e9)

def dfs(i, value):
    global add, sub, mul, div, min_value, max_value
    
    if i == n:
        min_value = min(min_value, value)
        max_value = max(max_value, value)
        return
    if add > 0:
        add -= 1
        dfs(i + 1, value + data[i])
        add += 1
    if sub > 0:
        sub -= 1
        dfs(i + 1, value - data[i])
        sub += 1
    if mul > 0:
        mul -= 1
        dfs(i + 1, value * data[i])
        mul += 1
    if div > 0:
        div -= 1
        dfs(i + 1, int(value / data[i]))
        div += 1

dfs(1, data[0])
print(max_value)
print(min_value)