import sys
input = sys.stdin.readline
people = []
n = int(input())
for _ in range(n):
    weight, height = map(int, input().split())
    people.append((weight,height))

for i in people:
    rank = 1 
    for j in people:
        if(i[0] < j[0] and i[1] < j[1]):
            rank+=1
    print(rank)
