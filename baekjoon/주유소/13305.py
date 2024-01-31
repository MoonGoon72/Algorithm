import sys
input = sys.stdin.readline

n = int(input())
distance = list(map(int, input().split(' ')))
cost = list(map(int, input().split(' ')))

result = 0
tmp = cost[0]

for node in range(n - 1):
    if tmp <= cost[node]: # 현재 도시의 기름 값이 다음 도시의 기름 값보다 싸거나 같으면 계속 유지
        result += tmp * distance[node]
    else: # 현재 도시의 기름 값이 다음 도시의 기름 값보다 비싸면 다음 도시까지 거리만큼만 기름 사고 다음 도시에서 추가 구매
        result += cost[node] * distance[node]
        tmp = cost[node]
print(result)
