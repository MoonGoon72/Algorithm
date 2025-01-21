import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

n, b = map(int, input().split())
matrix = []

for _ in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)

def matrix_mul(a, b):
    new_matrix = []
    for i in range(n):
        tmp_a = a[i]
        tmp_arr = []
        for j in range(n):    
            tmp = 0
            for k in range(n):
                tmp += tmp_a[k] * b[k][j]
            tmp %= 1000
            tmp_arr.append(tmp)
        new_matrix.append(tmp_arr)
    return new_matrix

def matrix_pow(matrix, exp):
    if exp == 1:
        return [[element % 1000 for element in row] for row in matrix]
    elif exp % 2 == 0:
        half_pow = matrix_pow(matrix, exp // 2)
        return matrix_mul(half_pow, half_pow)
    return matrix_mul(matrix, matrix_pow(matrix, exp - 1))

result = matrix_pow(matrix, b)
for row in result:
    print(*row)