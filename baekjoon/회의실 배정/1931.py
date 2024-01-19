import sys
input = sys.stdin.readline

n = int(input())

meeting = []
for _ in range(n):
    a, b = map(int, input().split())
    meeting.append((a, b))

meeting.sort(key= lambda x: (x[1], x[0]))
schedule = []


for i in meeting:
    if schedule == []:
        schedule.append(i)
    else:
        if schedule[-1][1] <= i[0]:
            schedule.append(i)
print(len(schedule))
