from collections import deque, defaultdict
import sys
input = sys.stdin.readline

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
wall = '*'
empty_space = '.'
document = '$'

def initial_setting(h, w, data, keys, closed_doors, answer):
    start_points = []
    for i in range(w):
        if data[0][i] != wall:
            if data[0][i] == empty_space:
                start_points.append((0, i))
            elif data[0][i] == document:
                start_points.append((0, i))
                answer += 1
                data[0][i] = empty_space
            elif is_key(data[0][i]):
                start_points.append((0, i))
                key = data[0][i]
                keys.append(key)
                doors = closed_doors[key.upper()]
                
                for door in doors:
                    start_points.append((door[0], door[1]))
                closed_doors[key.upper()] = []
            elif is_door(data[0][i]):
                closed_doors[data[0][i]].append((0, i))
        if data[h - 1][i] != wall:
            if data[h - 1][i] == empty_space:
                start_points.append((h - 1, i))
            elif data[h - 1][i] == document:
                start_points.append((h - 1, i))
                answer += 1
                data[h - 1][i] = empty_space
            elif is_key(data[h - 1][i]):
                start_points.append((h - 1, i))
                key = data[h - 1][i]
                keys.append(key)
                doors = closed_doors[key.upper()]
                
                for door in doors:
                    start_points.append((door[0], door[1]))
                closed_doors[key.upper()] = ()
            elif is_door(data[h - 1][i]):
                closed_doors[data[h - 1][i]].append((h - 1, i))
    for i in range(h):
        if data[i][0] != wall:
            if data[i][0] == empty_space:
                start_points.append((i, 0))
            elif data[i][0] == document:
                start_points.append((i, 0))
                answer += 1
                data[i][0] = empty_space
            elif is_key(data[i][0]):
                start_points.append((i, 0))
                key = data[i][0]
                keys.append(key)
                doors = closed_doors[key.upper()]

                for door in doors:
                    start_points.append((door[0], door[1]))
                closed_doors[key.upper()] = []
            elif is_door(data[i][0]):
                closed_doors[data[i][0]].append((i, 0))
        if data[i][w - 1] != wall:
            if data[i][w - 1] == empty_space:
                start_points.append((i, w - 1))
            elif data[i][w - 1] == document:
                start_points.append((i, w - 1))
                answer += 1
                data[i][w - 1] = empty_space
            elif is_key(data[i][w - 1]):
                start_points.append((i, w - 1))
                key = data[i][w - 1]
                keys.append(key)
                doors = closed_doors[key.upper()]

                for door in doors:
                    start_points.append((door[0], door[1]))
                closed_doors[key.upper()] = []
            elif is_door(data[i][w - 1]):
                closed_doors[data[i][w - 1]].append((i, w - 1))

    return start_points, keys, closed_doors, answer

def get_keys(key_string):
    if key_string == '0':
        keys = []
    else:
        keys = list(key_string)
    return keys

def check(y, x, h, w):
    return 0 <= y < h and 0 <= x < w

def is_door(x):
    return ord('A') <= ord(x) <= ord('Z')

def is_key(x):
    return ord('a') <= ord(x) <= ord('z')

test_case = int(input())
for _ in range(test_case):
    h, w = map(int, input().split())
    data = [list(input().rstrip()) for _ in range(h)]
    visited = [[False] * w for _ in range(h)]
    keys = get_keys(input().strip())
    closed_doors = defaultdict(list)
    answer = 0
    start_points, keys, closed_doors, answer = initial_setting(h, w, data, keys, closed_doors, answer)

    for key in keys:
        for door in closed_doors[key.upper()]:
            start_points.append(door)
            data[door[0]][door[1]] = empty_space

    queue = deque(start_points)
    while queue:
        y, x = queue.popleft()
        visited[y][x] = True
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if not check(ny, nx, h, w): continue

            if data[ny][nx] == wall: continue
            
            if visited[ny][nx]: continue
            
            elif data[ny][nx] == empty_space:
                queue.append((ny, nx))
                visited[ny][nx] = True
            elif data[ny][nx] == document:
                answer += 1
                data[ny][nx] = empty_space
                queue.append((ny, nx))
                visited[ny][nx] = True
            elif is_door(data[ny][nx]):
                door = data[ny][nx]
                key = door.lower()
                if key in keys:
                    queue.append((ny, nx))
                    data[ny][nx] = empty_space
                    visited[ny][nx] = True
                else:
                    closed_doors[door].append((ny, nx))
            elif is_key(data[ny][nx]):
                queue.append((ny, nx))
                key = data[ny][nx]
                keys.append(key)
                visited[ny][nx] = True
                # 키를 찾았는데 잠겼던 문이 있음
                doors = closed_doors[key.upper()]
                for door in doors:
                    queue.append(door)
                    data[door[0]][door[1]] = empty_space
                    visited[door[0]][door[1]] = True
                closed_doors[key.upper()] = []
    print(answer)
