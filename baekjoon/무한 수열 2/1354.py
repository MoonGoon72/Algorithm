from collections import defaultdict
n, p, q, x, y = map(int, input().split())

dp = defaultdict(int)
dp[0] = 1

def calc(i):
    if i <= 0: return dp[0]
    if dp[i] != 0: return dp[i]

    first = i//p - x
    second = i//q - y
    result = calc(first) + calc(second)
    dp[i] = result
    return result

answer = calc(n)
print(answer)
