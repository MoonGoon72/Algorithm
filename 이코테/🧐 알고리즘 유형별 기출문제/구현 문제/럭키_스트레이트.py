import sys
input = sys.stdin.readline

def calc(str):
    tmp = 0
    for s in str:
        tmp += int(s)
    return tmp

n = input().strip()
length = len(n)
left = n[:length // 2]
right = n[length // 2:]

print("LUCKY") if calc(left) == calc(right) else print("READY")