import sys, math
input = sys.stdin.readline

n = int(input())
answer = 0

if n == 1:
    print(0)
    exit(0)

def prime_numbers(num):
    tmp = [False, False] + [True for _ in range(num - 1)]
    n_sqrt = int(math.sqrt(num)) +1 
    for i in range(2, n_sqrt):
        if not tmp[i]:
            continue
        
        counter = 2
        while i * counter <= num:
            if tmp[i * counter]:
                tmp[i * counter] = False
            counter += 1
    return tmp

primes = prime_numbers(n)

start = 2
end = 2
summation = start

while start <= end:
    if summation == n:
        answer += 1
        summation -= start
        start += 1
        while start <= n and primes[start] == False:
            start += 1
    elif summation < n:
        end += 1
        while end <= n and primes[end] == False:
            end += 1
        if end > n:
            break
        summation += end
    elif summation > n:
        summation -= start
        start += 1
        while start <= n and primes[start] == False:
            start += 1

print(answer)