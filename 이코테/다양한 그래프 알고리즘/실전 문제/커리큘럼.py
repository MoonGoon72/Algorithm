from collections import deque
import sys, copy
input = sys.stdin.readline

n = int(input())
indegree = [0] * (n + 1)
graph = [[] for _ in range(n + 1)]
time = [0] * (n + 1)

for i in range(1, n + 1):
    lecture = list(map(int, input().split()))
    lecture.pop()
    time[i] = lecture[0]
    for x in lecture[1:]:
        graph[x].append(i)
        indegree[i] += 1

def topology_sort():
    result = copy.deepcopy(time)
    q = deque()
    
    for i in range(1, n + 1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()
        for i in graph[now]:
            result[i] = max(result[i], result[now] + time[i])
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)
    
    for i in range(1, n + 1):
        print(result[i])

topology_sort()

"""
5
10 -1
10 1 -1
4 1 -1
4 3 1 -1
3 3 -1

10
20
14
18
17
"""