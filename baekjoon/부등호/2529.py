import sys
input = sys.stdin.readline

k = int(input())
data = list(map(str, input().split()))
answer = []

# 넘겨받을 파라미터: 현재 부등호 관계 어디까지인지, 누적된 수
def backtracking(depth, acc):
    if depth == k:
        answer.append(''.join(map(str, acc)))
        return
    
    for i in range(10):
        if i in set(acc): continue

        if data[depth] == '<':
            if acc[-1] < i:
                backtracking(depth+1, acc + [i])
        else:
            if acc[-1] > i:
                backtracking(depth+1, acc + [i])

for i in range(10):
    backtracking(0, [i])

print(answer[-1])
print(answer[0])