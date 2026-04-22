import sys
input = sys.stdin.readline

n, p = map(int, input().split())
stack = [[] for _ in range(7)]

count = 0
for _ in range(n):
    l, p = map(int, input().split())
    
    while True:
        if not stack[l]:
            stack[l].append(p)
            count += 1
            break
        top = stack[l][-1]
        if top == p:
            break
        elif top < p:
            stack[l].append(p)
            count += 1
            break
        else:
            stack[l].pop()
            count += 1
            continue
print(count)