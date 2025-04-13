data = input().strip()

def solution(data):
    num = 0
    arr = []
    for s in data:
        if s < "A":
            num += int(s) 
        else:
            arr.append(s)
    arr.sort()
    if num > 0:
        arr.append(str(num))
    return arr

print("".join(solution(data)))