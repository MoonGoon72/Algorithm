import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())

    people = []
    for i in range(n):
        a, b = map(int, input().split())
        people.append((a, b))
    people.sort(key=lambda x: x[0])

    minimum = people[0][1]
    count = 0

    for _, b in people:
        if minimum < b:
            count += 1
        else:
            minimum = b
    print(n-count)