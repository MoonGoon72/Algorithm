import sys
input = sys.stdin.readline

s = input().rstrip()
bomb = input().rstrip()
bomb_length = len(bomb)
end = bomb[bomb_length - 1]

def solution():
    stack = []
    for char in s:
        stack.append(char)
        if len(stack) >= bomb_length:
            if "".join(stack[-bomb_length:]) == bomb:
                del stack[-bomb_length:]
    if len(stack) == 0:
        return "FRULA"
    else:
        return "".join(stack)
print(solution())