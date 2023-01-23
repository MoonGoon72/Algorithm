number = int(input())

result = 0

arr = [0 for _ in range(1000000)]


for i in range(1, 4, 1):
    arr[i] = 1

if number <= 3:
    print(arr[number])
else:
    for num in range(4, number + 1):
        if num % 6 == 0:  # 6의 배수일경우
            arr[num] = arr[num // 3] + arr[num // 2]
        elif num % 3 == 0:
            arr[num] = arr[num // 3] + 1
        elif num % 2 == 0:
            arr[num] = arr[num // 2] + 1
        else:
            arr[num] = arr[num - 1] + 1

    print(arr[number])
