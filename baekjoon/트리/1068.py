from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
childs = [[] for _ in range(n)]
data = list(map(int, input().strip().split()))
isLeaf = [True] * n
root = 0
for i in range(n):
    if data[i] == -1:
        isLeaf[i] = False
        root = i
    else:
        childs[data[i]].append(i)
        isLeaf[data[i]] = False

node = int(input())
if node == root:
    print(0)
    exit(0)
isLeaf[node] = False

parent = data[node]
childs[parent].remove(node)

if len(childs[parent]) == 0:
    isLeaf[parent] = True

queue = deque()
queue.append(node)

while queue:
    now = queue.popleft()
    for nxt in childs[now]:
        queue.append(nxt)
        isLeaf[nxt] = False

count = 0
for i in range(n):
    if isLeaf[i]:
        count += 1

print(count if count != 0 else 1)