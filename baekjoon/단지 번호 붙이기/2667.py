from collections import deque
import sys
input = sys.stdin.readline

size = int(input())

graph = [list(map(int, input().rstrip())) for _ in range(size)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
    queue = deque()
    totalGroup = []
    groupSize = int(0)
    for i in range(size):
        for j in range(size):
            if(graph[i][j] != 0):
                queue.append((i,j))
                graph[i][j] = 0
                groupSize = 1
            while queue:
                a, b = queue.popleft()
                
                for k in range(4):
                    nx = a + dx[k]
                    ny = b + dy[k]
                    if (nx >= 0 and ny >= 0 and nx <= (size-1) and ny <= (size-1) and graph[nx][ny] == 1):
                        graph[nx][ny] = 0
                        groupSize+=1
                        queue.append((nx, ny))
            if groupSize != 0: 
                totalGroup.append(groupSize)
                groupSize = 0
    totalGroup.sort()
    print(len(totalGroup))
    print(*totalGroup, sep='\n')

bfs()