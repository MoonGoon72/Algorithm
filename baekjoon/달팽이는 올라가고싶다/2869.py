import sys
import math
input = sys.stdin.readline
A, B, V = map(int, input().split())
m = 0
day = (V-B)/(A-B)
print(math.ceil(day))