n = int(input())

result = 0
for num in range(1, n+1):
    if len(str(num)) <= 2: result += 1
    else:
        is_as = True
        for i in range(1, len(str(num))-1):
            if int(str(num)[i]) - int(str(num)[i-1]) != int(str(num)[i+1]) - int(str(num)[i]):
                is_as = False
                break
        if is_as: result += 1
print(result)
