import sys
input = sys.stdin.readline

s = input()
stack = []
tmp = 1
answer = 0
is_closed = False

for c in s:
    if c == "(":
        tmp *= 2
        stack.append(c)
        is_closed = False
    elif c == "[":
        tmp *= 3
        stack.append(c)
        is_closed = False
    elif c == ")":
        if not stack or stack[-1] != "(":
            answer = 0
            break
        stack.pop()
        if not is_closed:
            answer += tmp
            is_closed = True
        tmp //= 2
    elif c == "]":
        if not stack or stack[-1] != "[":
            answer = 0
            break
        stack.pop()
        if not is_closed:
            answer += tmp
            is_closed = True
        tmp //= 3

if stack:
    answer = 0

print(answer)