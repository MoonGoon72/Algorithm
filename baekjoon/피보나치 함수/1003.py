import sys
input = sys.stdin.readline

testCase = int(input())
table = list([] for _ in range(41))
table[0] = [1,0]
table[1] = [0,1]
def fibonacci(num):
    if num < 2:
        return table[num]
    if table[num] != []:
        return table[num]
    table[num] = [fibonacci(num-1)[0] + fibonacci(num-2)[0], fibonacci(num-1)[1] + fibonacci(num-2)[1]]
    return table[num]

for _ in range(testCase):
    num = int(input())
    print(fibonacci(num)[0], fibonacci(num)[1])
