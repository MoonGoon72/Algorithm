import sys
input = sys.stdin.readline

n, m = map(int, input().split())
ttoks = list(map(int, input().split()))

start = 0
end = max(ttoks)
mid = (start + end) // 2

def cutting(h):
    total = 0
    for ttok in ttoks:
        total += max(0, ttok - h)
    return True if total >= m else False
        
while start <= end:
    if cutting(mid):
        start = mid + 1
    else:
        end = mid - 1
    mid = (start + end) // 2

print(mid)