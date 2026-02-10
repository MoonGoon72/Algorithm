from itertools import combinations
import sys
input = sys.stdin.readline

def solution1():
    while True:
        data = list(map(int, input().split()))
        if data[0] == 0:
            break
        data = data[1:]
        combs = list(combinations(data, 6))
        for comb in combs:
            print(" ".join(map(str, comb)))
        print()

def solution2():
    while True:
        data = list(map(int, input().split()))
        if data[0] == 0: break
        k = data[0]
        data = data[1:]
        backtracking(0, k, [], data)
        print()

def backtracking(idx, k, acc, arr):
    l = len(acc)
    # 6개를 만들면 출력한다.
    if l == 6:
        print(" ".join(map(str, acc)))
        return
    if idx == k: # 탈출 조건
        return
    
    # 현재 원소를 선택한다
    backtracking(idx+1, k, acc+[arr[idx]], arr)
    # 현재 원소를 선택하지 않는다.
    backtracking(idx+1, k, acc, arr)
solution2()