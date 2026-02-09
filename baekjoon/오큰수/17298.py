import sys
input = sys.stdin.readline

n = int(input())
data = list(map(int, input().strip().split()))
answer = [-1] * n
stack = []

for i in range(n):
    v = data[i]
    if not stack:
        stack.append((i, v))
        continue

    if stack[-1][1] >= v:
        stack.append((i, v))
    else:
        while stack and v > stack[-1][1]:
            idx, value = stack.pop()
            answer[idx] = v
        stack.append((i, v))

print(" ".join(map(str, answer)))