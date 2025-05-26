import sys
input = sys.stdin.readline

n = int(input())
students = []
for _ in range(n):
    students.append(input().split())

students.sort(key=lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))
for i in range(n):
    print(students[i][0])