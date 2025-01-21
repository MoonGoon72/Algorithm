import sys
input = sys.stdin.readline

n = int(input())
parts = sorted(list(map(int, input().split())))
m = int(input())
wants = list(map(int, input().split()))

def binary_search(parts, part, start, end):
    if start > end:
        return "no"
    mid = (start + end) // 2
    if parts[mid] == part:
        return "yes"
    elif parts[mid] > part:
        return binary_search(parts, part, start, end - 1)
    else:
        return binary_search(parts, part, mid + 1, end)

for part in wants:
    print(binary_search(parts, part, 0, len(parts) - 1), end=" ")

"""
5
8 3 7 9 2
3
5 7 9
"""