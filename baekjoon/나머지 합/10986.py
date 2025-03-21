import sys
input = sys.stdin.readline

def prefix_sum():
    global answer
    for i in range(1, n + 1):
        prefix[i] = prefix[i - 1] + numbers[i]
        remainder = prefix[i] % m
        answer += remainders[remainder]
        remainders[remainder] += 1
    return

n, m = map(int, input().split())
numbers = [0] + list(map(int, input().split()))
answer = 0
prefix = [0] * (n + 1)
remainders = [0] * (m)
remainders[0] = 1 # 나머지 0은 k까지의 부분합이 나누어 떨어졌을 때
prefix_sum()

print(answer)