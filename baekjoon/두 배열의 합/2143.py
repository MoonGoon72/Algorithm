from collections import defaultdict
import sys
input = sys.stdin.readline

def subarray_sum(arr):
    s = []
    prefix = [arr[0]]
    for i in range(1, len(arr)):
        prefix.append(prefix[i - 1] + arr[i])
    
    for i in range(len(arr)):
        for j in range(i, len(arr)):
            s.append(prefix[j] - (prefix[i - 1] if i > 0 else 0))
    return s

t = int(input())
n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))

count_a = defaultdict(int)

subarray_a = subarray_sum(a)
subarray_b = subarray_sum(b)

for num in subarray_a:
    count_a[num] += 1

result = 0

for num in subarray_b:
    result += count_a[t - num]

print(result)