N, M = map(int, input().split(' '))

tmp = []

def bfs():
    if M == len(tmp):
        print(' '.join(map(str, tmp)))
        return
    for i in range(1, N + 1):
        if i not in tmp:
            tmp.append(i)
            bfs()
            tmp.pop()
bfs()