import sys
input = sys.stdin.readline

def two_pointer():
    global answer, summation
    for i in range(n):
        fixed = arr[i]
        start = i + 1
        end = n - 1

        while start < end:
            tmp = fixed + arr[start] + arr[end]
            if tmp == 0:
                answer = (fixed, arr[start], arr[end])
                return
            if abs(tmp) < abs(summation):
                answer = (fixed, arr[start], arr[end])
                summation = tmp
            if tmp < 0:
                start += 1
            elif tmp > 0:
                end -= 1

n = int(input())
arr = sorted(list(map(int, input().split())))
answer = (0, 0, 0)
summation = int(3e9 + 1)

two_pointer()
print(*answer)