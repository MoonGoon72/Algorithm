import copy

operators = [' ', '+', '-']

def rec(now, ans):
    if now == n + 1:
        calc(ans)
        return
    else:
        for operator in operators:
            rec(now+1, ans+operator+str(now))

def calc(ans):
    tmp = ans.replace(' ', '')
    if eval(tmp) == 0:
        result.append(ans)

T = int(input())
for _ in range(T):
    result = []
    n = int(input())
    rec(2, '1')
    result.append(' ')
    print(*result, sep='\n')
