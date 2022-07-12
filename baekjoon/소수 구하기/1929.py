import sys
import math
input = sys.stdin.readline

m,n = map(int, input().split())

for i in range(m, n+1):
    if i == 1 : continue
    for j in range(2,int(math.sqrt(i))+1):  # 1보다 큰 수의 약수유무 판단위해 +1
        if (i%j == 0):
            break
    else:
        print(i)
