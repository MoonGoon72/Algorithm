import sys
input = sys.stdin.readline

def get_primes():
    primes = [True] * 10001
    for i in range(2, 101):
        if primes[i]:
            idx = i
            while i * idx < 10001:
                primes[i * idx] = False
                idx += 1
    return primes

def get_partition(n, primes):
    for a in range(n // 2, 1, -1):
        if not primes[a]:
            continue
        if not primes[n - a]:
            continue
        return a, n - a
    return 0, 0

def solution():
    t = int(input())
    primes = get_primes()

    for _ in range(t):
        n = int(input())
        a, b = get_partition(n, primes)
        print(a, b)

solution()