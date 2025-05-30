import sys
input = sys.stdin.readline

def binary_search(arr, start, end):
    if start > end:
        return -1
    mid = (start + end) // 2
    if arr[mid] == mid:
        return mid
    elif arr[mid] < mid:
        return binary_search(arr, mid + 1, end)
    else:
        return binary_search(arr, start, mid - 1)

n = int(input())
data = list(map(int, input().split()))

print(binary_search(data, 0, n - 1))
"""
5
-15 -6 1 3 7
-> 3

7
-15 -4 2 8 9 13 15
-> 2

7
-15 -4 3 8 9 13 15
-> -1

"""