import sys
input = sys.stdin.readline

testCase = int(input())
for _ in range(testCase):
    col, row, n = map(int, input().split())
    if (n%col == 0):
        height = col*100
        horizental = int(n/col)
    else:
        height = int(n%col)*100
        horizental = int(n/col) + 1
    room = height + horizental
    print(room)
