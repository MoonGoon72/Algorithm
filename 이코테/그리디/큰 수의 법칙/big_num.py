n, m, k = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
first = arr[-1]
second = arr[-2]

def solution(m, k):
    result = 0
    # M이 10,000개 이하의 경우
    while True:
        for _ in range(k):
            if m == 0:
                break
            result += first
            m -= 1
        if m == 0:
            break
        result += second
        m -= 1
    return result

def solution2(m, k):
    first_count = int(m / (k + 1)) * k
    first_count += m % (k + 1)
    second_count = m - first_count
    total = first * first_count + second * second_count
    return total

print(solution(m, k))
print(solution2(m, k))