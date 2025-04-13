data = input().strip()

def solution(data):
    num = 0
    arr = []
    for s in data:
        if s < "A": # 혹은 s.isAlpha() 로 알파벳 여부 판단 가능
            num += int(s) 
        else:
            arr.append(s)
    arr.sort()
    if num > 0:
        arr.append(str(num))
    return arr

print("".join(solution(data)))