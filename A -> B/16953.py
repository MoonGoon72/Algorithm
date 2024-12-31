import sys
input = sys.stdin.readline

a, b = map(int, input().split())

def dfs(depth, num):
    if num > b: return -1
    elif num == b: return depth

    result = dfs(depth + 1, num * 2) 
    
    if result == -1:
        result = dfs(depth + 1, num * 10 + 1)

        if result != -1:
            return result
    return result

answer = dfs(1, a)
print(answer)