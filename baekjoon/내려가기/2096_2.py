import sys
input = sys.stdin.readline

n = int(input())

left = [0, 0]
mid = [0, 0]
right = [0, 0]

for _ in range(n):
    a, b, c = map(int, input().split())
    l_min = min(left[0], mid[0])
    l_max = max(left[1], mid[1])

    m_min = min(left[0], mid[0], right[0])
    m_max = max(left[1], mid[1], right[1])

    r_min = min(mid[0], right[0])
    r_max = max(mid[1], right[1])

    left = [l_min + a, l_max + a]
    mid = [m_min + b, m_max + b]
    right = [r_min + c, r_max + c]

max_value = max(left[1], mid[1], right[1])
min_value = min(left[0], mid[0], right[0])
print(max_value, min_value)
