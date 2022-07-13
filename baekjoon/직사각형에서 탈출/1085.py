import sys
input = sys.stdin.readline

x, y, w, h = map(int, input().split())

if(x <= w-x):
    xMin=x
else:
    xMin = w-x

if(y <= h-y):
    yMin = y
else:
    yMin = h-y

if(xMin <= yMin):
    print(xMin)
else:
    print(yMin)