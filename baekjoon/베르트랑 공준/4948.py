import sys
input = sys.stdin.readline

def get_prime_number(n):
    primes = [True] * (n + 1)
    primes[0] = False
    primes[1] = False
    arr = []

    for i in range(2, int(n ** 0.5) + 1):
        if not primes[i]: continue
        
        j = 2
        while True:
            nxt = i * j
            if nxt > n:
                break

            primes[nxt] = False
            j += 1

    for i in range(2, n + 1):
        if primes[i]:
            arr.append(i)
    return arr

while True:
    n = int(input())
    if n == 0:
        break

    primes = get_prime_number(2 * n)
    small_primes = get_prime_number(n)
    l = len(small_primes)
    r = len(primes)
    print(r - l)
