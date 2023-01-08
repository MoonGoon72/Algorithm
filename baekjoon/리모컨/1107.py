# 다시 풀어볼 것

channel = int(input())
buttonNum = int(input())
channelLen = len(str(channel))

def remoteController():
    result = abs(100 - channel)
    for nums in range(1000001):
        nums = str(nums)
        for i in range(len(nums)):
            # 누를 수 없는 수면 다음 수를 찾는다
            if int(nums[i]) in brokenButtons:
                break
            # 모든 숫자를 누를 수 있으면 그 수에서 +나 - 버튼으로 이동하여 원하는 채널로 이동하는 총 입력수를 측정하고 더 작은수를 result에 넣어 갱신한다.
            elif i == len(nums) -1:
                result = min(result, abs(channel - int(nums)) + len(nums))
    print(result)

if buttonNum != 0:
    brokenButtons = list(map(int, input().split(" ")))
    remoteController()
else:
    brokenButtons = []
    remoteController()
