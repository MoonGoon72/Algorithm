channel = input()
buttonNum = int(input())
channelLen = len(str(channel))
brokenButtons = list(map(int, input().split(" ")))
totalPress = 0

for i in range(channelLen, 0, -1):
    tmpNum = channelLen // (10 ** i)
    if tmpNum not in brokenButtons:
        totalPress += 1
    else:
        
