t = int(input())

def moving(s, e):
    distance = e - s
    n = 0
    
    while True:
        if distance <= n * (n+1):
            break
        n += 1
    
    if distance <= n ** 2:
        print(2 * n - 1)
    else:
        print(2 * n)

for _ in range(t):
    s, e = map(int, input().split())
    moving(s, e)