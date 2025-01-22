import sys
input = sys.stdin.readline

n = int(input())
sequence = list(map(int, input().split()))
lis = [1] * n
lds = [1] * n

def get_lis():
    global lis
    for i in range(n):
        for j in range(i):
            if sequence[i] > sequence[j]:
                lis[i] = max(lis[i], lis[j] + 1)
    return
def get_lds():
    global lds
    for i in range(n - 1, -1, -1):
        for j in range(n - 1, i, -1):
            if sequence[i] > sequence[j]:
                lds[i] = max(lds[i], lds[j] + 1)
    return

def solution():
    get_lis()
    get_lds()

    result = 0
    for i in range(n):
        result = max(result, lis[i] + lds[i] - 1)
    return result

answer = solution()
print(answer)