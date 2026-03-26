from itertools import permutations
import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

# permutations 사용
def solution1():
    def calc(data):
        s = 0
        for i in range(n-1):
            s += abs(data[i] - data[i+1])
        return s

    answer = 0
    for comb in permutations(arr, n):
        tmp = calc(comb)
        answer = tmp if answer < tmp else answer
    print(answer)

# 재귀 & recursion으로 직접 구현
def solution2():
    def calc(data):
        s = 0
        for i in range(n-1):
            s += abs(data[i] - data[i+1])
        return s
    answer = 0

    def permutation(data, depth):
        nonlocal answer
        if depth == n:
            tmp = calc(data)
            answer = max(answer, tmp)
            return
        
        for i in range(depth, n):
            data[depth], data[i] = data[i], data[depth]
            permutation(data, depth + 1)
            data[depth], data[i] = data[i], data[depth]
    permutation(arr, 0)
    print(answer)

if __name__ == "__main__":
    # solution1()
    solution2()