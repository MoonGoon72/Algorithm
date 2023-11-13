import sys
input = sys.stdin.readline

n = int(input())

# 자리 수 계산
num_len = len(str(n))

result = 0

for i in range(num_len):
    divider = (9 * (10 ** i))
    
    if n < divider:
        result += (i + 1) * n
        break
    else:
        n -= divider
        result += (i + 1) * (9 * (10 ** i)) # 9, 90, 900, 9000 ... 에 각각 1개 2개 3개씩 증가함
print(result)