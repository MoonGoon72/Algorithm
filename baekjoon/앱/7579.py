import sys
input = sys.stdin.readline

n, m = map(int, input().split())
mems = [0] + list(map(int, input().split()))
costs = [0] + list(map(int, input().split()))

max_cost = sum(costs)
result = max_cost
dp = [[0] * (max_cost + 1) for _ in range(n + 1)]

for i in range(1, n + 1): # 모든 앱을 순회
    mem, cost = mems[i], costs[i]
    for j in range(max_cost + 1): # 특정 비용일 때 메모리 획득량
        if j < cost:
            dp[i][j] = dp[i-1][j] # 앱을 재실행할 cost가 모자라서 삭제 못함 (선택 안함)
            continue
        
        dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - cost] + mem) # 선택 안함 vs 선택함
        if dp[i][j] >= m: # 원하는 만큼 메모리를 획득
            result = min(result, j) # 했을 때 현재 cost j가 제일 작은지
        
print(result)