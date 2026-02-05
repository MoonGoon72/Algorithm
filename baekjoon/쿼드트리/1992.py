import sys
input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().rstrip())) for _ in range(n)]

def summation(y, x, k):
    count = 0
    for i in range(k):
        count += sum(arr[y+i][x:x+k])
    return count

def solution(y, x, k):
    answer = ""
    tmp = summation(y, x, k)
    if tmp == 0:
        return "0"
    elif tmp == k ** 2:
        return "1"
    else:
        nk = k//2
        a = solution(y, x, nk)
        b = solution(y, x+nk, nk)
        c = solution(y+nk, x, nk)
        d = solution(y+nk, x+nk, nk)
        answer = "(" + a + b + c + d + ")"
    return answer

result = solution(0, 0, n)
print(result)