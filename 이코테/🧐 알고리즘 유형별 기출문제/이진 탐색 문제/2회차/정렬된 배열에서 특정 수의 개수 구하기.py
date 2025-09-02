def bisect_left(x, start, end, data):
    if start > end:
        return None
    mid = (start + end) // 2
    
    if (mid == 0 or data[mid - 1] < x) and data[mid] == x:
        return mid
    elif data[mid] >= x:
        return bisect_left(x, start, mid - 1, data)
    else:
        return bisect_left(x, mid + 1, end, data)

def bisect_right(x, start, end, data):
    if start > end:
        return None
    mid = (start + end) // 2

    if (mid == len(data) - 1 or data[mid + 1] > x) and data[mid] == x:
        return mid
    elif data[mid] <= x:
        return bisect_right(x, mid + 1, end, data)
    else:
        return bisect_right(x, start, mid - 1, data)
    
n, x = map(int, input().split())
data = list(map(int, input().split()))

l, r = bisect_left(x, 0, n - 1, data), bisect_right(x, 0, n - 1, data)

if l == None or r == None:
    print(-1)
else:
    print(r - l + 1)

