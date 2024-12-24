import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
s = input().strip()

pattern = "IOI"
i = count = result = 0

while i < m:
    if s[i:i+3] == pattern:
        count += 1
        i += 2
        if count == n:
            result += 1
            count -= 1
    else:
        count = 0
        i += 1

print(result)