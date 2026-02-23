import sys
input = sys.stdin.readline

n = int(input())
req = list(map(int, input().split()))
m = int(input())

total = sum(req)

def calc(budget):
    tmp = 0
    for v in req:
        tmp += min(v, budget)
    return tmp <= m

def binary_search(s, e):
    answer = 0
    while s <= e:
        mid = (s + e) // 2
        if calc(mid):
            s = mid + 1
            answer = mid
        else:
            e = mid - 1
    return answer

if total <= m:
    print(max(req))
else:
    avg = m // n
    answer = binary_search(avg, m)
    print(answer)
