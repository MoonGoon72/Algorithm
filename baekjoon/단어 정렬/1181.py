import sys
input = sys.stdin.readline
n = int(input())
dict = []
for _ in range(n):
    str = input().strip()
    dict.append(str)
#중복 제거를 위해 set으로 한변 변환해줌
dict = list(set(dict))
dict.sort()
dict.sort(key=lambda x: len(x))  #길이별로 정렬

print(*dict, sep='\n')