import sys
input = sys.stdin.readline

n = int(input())

arr = line = list(map(int, input().split()))
minAnswers = arr
maxAnswers = arr

def check(x):
    return 0 <= x < 3

for _ in range(1, n):
    line = list(map(int, input().split()))
    maxAnswers = [line[0] + max(maxAnswers[0], maxAnswers[1]), line[1] + max(maxAnswers[0], maxAnswers[1], maxAnswers[2]), line[2] + max(maxAnswers[1], maxAnswers[2])]
    minAnswers = [line[0] + min(minAnswers[0], minAnswers[1]), line[1] + min(minAnswers[0], minAnswers[1], minAnswers[2]), line[2] + min(minAnswers[1], minAnswers[2])]

print(max(maxAnswers), min(minAnswers))