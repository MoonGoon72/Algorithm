# pypy로 제출함
import sys
input = sys.stdin.readline

m = int(input())
s = set()

def calc(txt):
    global s
    arr = txt.split()
    op, num = arr[0], int(arr[1]) if len(arr) > 1 else None
    if num:
        if op == "add":
            s.add(num)
        elif op == "remove":
            s.discard(num)
        elif op == "check":
            print("1") if num in s else print("0")
        elif op == "toggle":
            s.discard(num) if num in s else s.add(num)
    else:
        if op == "all":
            s = set(str(i) for i in range(1, 21))
        else:  # empty 의 경우
            s = set()
    
    

for _ in range(m):
    calc(input().rstrip())
