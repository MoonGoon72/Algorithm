steps = [(-2, -1), (-2, 1), (2, -1), (2, 1), (1, -2), (1, 2), (-1, 2), (-1, -2)]

def movable(col, row):
    return 0 <= col < 8 and 0 <= row < 8

def solution(point):
    count = 0
    n = ord("a")
    row = ord(point[0]) - n
    col = int(point[1]) - 1
    for step in steps:
        ny, nx = row - step[0], col - step[1]
        if movable(ny, nx): 
            count += 1
    return count

point = input()
print(solution(point=point))
