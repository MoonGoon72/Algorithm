import sys
input = sys.stdin.readline

n, t = map(int, input().rstrip().split())
times = [0] * (1001)
for _ in range(n):
    k = int(input().rstrip())
    for _ in range(k):
        s, e = map(int, input().rstrip().split())
        for time in range(s+1, e+1):
            times[time] += 1

s, e = 0-1, t-1
max_time = 0
ans_s, ans_e = s, e

for i in range(1001 - t):
    s += 1
    e += 1
    summation = sum(times[s+1: e+1])
    if summation > max_time:
        max_time = summation
        ans_s, ans_e = s, e

print(ans_s, ans_e)
