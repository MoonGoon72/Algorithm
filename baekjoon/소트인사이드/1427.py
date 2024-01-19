import sys
input = sys.stdin.readline

txt = list(str(input().rstrip()))
txt.sort(reverse=True)

print("".join(txt))
