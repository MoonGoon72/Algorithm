import sys
input = sys.stdin.readline

dp = [[[0 for _ in range(101)] for _ in range(101)] for _ in range(101)]

def get_dp(a, b, c):
    a += 50
    b += 50
    c += 50
    if dp[a][b][c] == 0:
        return None
    else:
        return dp[a][b][c]

def update_dp(a, b, c, v):
    a += 50
    b += 50
    c += 50
    dp[a][b][c] = v

def recursion(a, b, c):
    value = get_dp(a, b, c)
    if value is not None:
        return value

    if a <= 0 or b <= 0 or c <= 0:
        update_dp(a, b, c, 1)
        return 1
    
    if a > 20 or b > 20 or c > 20:
        value = recursion(20, 20, 20)
        update_dp(a, b, c, value) 
        return value
    
    if a < b and b < c:
        value = recursion(a, b, c-1) + recursion(a, b-1, c-1) - recursion(a, b-1, c)
        update_dp(a, b, c, value)
        return value

    value = recursion(a-1, b, c) + recursion(a-1, b-1, c) + recursion(a-1, b, c-1) - recursion(a-1, b-1, c-1)
    update_dp(a, b, c, value)
    return value

while True:
    a, b, c = map(int, input().split())
    if a == b == c == -1: break
    value = recursion(a, b, c)
    print(f'w({a}, {b}, {c}) = {value}')
