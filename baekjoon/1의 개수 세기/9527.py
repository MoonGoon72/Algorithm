import sys
input = sys.stdin.readline

a, b = map(int, input().split())

dp = [0] * 60
dp[1] = 1

for i in range(2, 60):
    dp[i] = 2 * dp[i - 1] + 2 ** (i - 1)

def binary_one_count(n):
    if n == 1:
        return 1
    elif n == 0:
        return 0
    k = 0
    while (1 << (k + 1)) <= n:
        k += 1

    return dp[k] + (n + 1 - 2 ** k) + binary_one_count(n - 2 ** k)

answer = binary_one_count(b) - binary_one_count(a - 1)
print(answer)
