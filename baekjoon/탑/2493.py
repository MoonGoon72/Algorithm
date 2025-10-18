import sys
input = sys.stdin.readline

n = int(input())
towers = list(map(int, input().split()))

def my_solution():
    dp = [0] * n

    for i in range(1, n):
        if towers[i - 1] > towers[i]:
            dp[i] = i
        else:
            left = dp[i - 1]
            while left > 0:
                if towers[left - 1] > towers[i]:
                    break
                else:
                    left = dp[left - 1]
            dp[i] = left

    print(*dp)

def use_stack():
    stack = []
    answer = []
    for i, e in enumerate(towers):
        is_appended = False
        while stack:
            if stack[-1][1] > e:
                answer.append(stack[-1][0])
                stack.append((i + 1, e))
                is_appended = True
                break
            else:
                stack.pop()
        
        if not is_appended:
            answer.append(0)
            stack.append((i + 1, e))
    print(*answer)

use_stack()