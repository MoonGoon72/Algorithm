import sys
input = sys.stdin.readline

s = input().rstrip()
answer = 0
pipe = 0

# 파이프 개수를 증가시키고
# 레이저를 맞으면 파이프 개수많큼 answer를 증가시킴
# 파이프가 끝나면 answer + 1

for i in range(len(s)):
    if s[i] == "(":
        if s[i+1] == "(":
            pipe += 1
    else:
        if s[i-1] == "(":
            answer += pipe
        else:
            pipe -= 1
            answer += 1
print(answer)
