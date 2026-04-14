import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    sounds = map(str, input().rstrip().split())
    sound = input().rstrip()
    sound_set = set()
    while sound != 'what does the fox say?':
        data = sound.split(' ')
        sound_set.add(data[-1])
        sound = input().rstrip()
    result = []
    for s in sounds:
        if s not in sound_set:
            result.append(s)
    print(*result)