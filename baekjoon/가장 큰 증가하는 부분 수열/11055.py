from copy import deepcopy
import sys
input = sys.stdin.readline

n = int(input())
seq = list(map(int, input().split()))

def bis(seq):
    dp = deepcopy(seq)
    for i in range(1, n):
        for j in range(i):
            if seq[i] <= seq[j]:
                continue
            dp[i] = max(dp[i], dp[j] + seq[i])
    return max(dp)

print(bis(seq))