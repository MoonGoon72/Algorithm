import sys
input = sys.stdin.readline

n = int(input())
arr = sorted(list(map(int, input().split())))
answer = (0, 0, 0)
summation = int(3e9 + 1)

def two_pointer():
    global summation, answer
    for i in range(n):
        fixed = i
        left = fixed + 1
        right = n - 1
        
        while left < right:
            tmp = arr[left] + arr[fixed] + arr[right]
            if abs(tmp) < abs(summation):
                summation = tmp
                answer = (arr[fixed], arr[left], arr[right])
            if tmp > 0:
                right -= 1
            elif tmp < 0:
                left += 1
            else:
                print(arr[fixed], arr[left], arr[right])
                sys.exit(0)
    return

two_pointer()
print(*answer)