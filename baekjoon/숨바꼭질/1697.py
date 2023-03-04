from collections import deque

def bfs(node):
    queue = deque([node])

    while queue:
        now = queue.popleft()
        # visited[now] 가 0 이면 아직 방문하지 않음
        if now == brother:
            print(visited[now])
            break
        for next_node in (now -1 , now + 1, now * 2):
            # 다음 방문 위치가 범위 안에 있는지 확인하고, visited[next_node]가 0이면 아직 방문하지 않았으므로 추가해줌
            if 0 <= next_node < 100001 and not visited[next_node]:
                visited[next_node] = visited[now] + 1
                queue.append(next_node)


subin, brother = map(int, input().split(' '))
visited = [0 for _ in range(100001)]
result = 0
bfs(subin)