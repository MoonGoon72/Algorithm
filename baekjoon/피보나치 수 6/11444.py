n = int(input())
matrix = [[1, 1], [1, 0]]

def mul_matrix(mat1, mat2):
    result = [[0] * 2 for _ in range(2)]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                result[i][j] += mat1[i][k] * mat2[k][j]
                result[i][j] %= 1_000_000_007
    return result
    
def power(M, num):
    if num == 0:
        return [[1, 0], [0, 1]]
    elif num == 1:
        return M
    else:
        tmp = power(M, num // 2)
        if num % 2 == 0:
            return mul_matrix(tmp, tmp)
        else:
            return mul_matrix(mul_matrix(tmp, tmp), M)

answer = power(matrix, n)
print(answer[0][1])