from collections import deque
n, k = map(int, input().split())
queue = deque()
queue.append(n)
time = 0
# 수빈이가 동생보다 앞에있어서 뒤로만 가면 되는 경우
if n > k :
    print(n-k)

while (n != k):
    n = n * 2
    time += 1
    if (n - 1 > k):
        n = queue.pop()
        n -= 1
        queue.append(n)
    elif (n - 1 == k):
        n -= 1
        time += 1
        
print(time)