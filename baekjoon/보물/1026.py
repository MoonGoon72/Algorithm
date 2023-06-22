n = int(input())

A = list(map(int, input().split(' ')))
B = list(map(int, input().split(' ')))

result = 0

for _ in range(n):
    a_min = A.pop(A.index(min(A)))
    b_max = B.pop(B.index(max(B)))
    result += a_min * b_max

print(result)