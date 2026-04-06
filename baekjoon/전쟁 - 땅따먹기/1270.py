from collections import defaultdict
import sys
input = sys.stdin.readline

n = int(input())

def whos_ground(dict, soldiers, l):
    for soldier in soldiers:
        if dict[str(soldier)] > l // 2:
            return soldier
    return "SYJKGW"

for _ in range(n):
    data = list(map(int, input().rstrip().split()))
    l = data[0]
    soldiers = data[1:]
    count = defaultdict(int)
    for solider in soldiers:
        count[str(solider)] += 1
    print(whos_ground(count, set(soldiers), l))
