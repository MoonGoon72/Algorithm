import sys
input = sys.stdin.readline

n = int(input())
lst = list(map(int, input().split()))

def two_pointer():
    left_idx = 0
    right_idx = n - 1
    answer = abs(lst[left_idx] + lst[right_idx])
    ans_left = left_idx
    ans_right = right_idx

    while left_idx < right_idx:
        tmp = lst[left_idx] + lst[right_idx]

        if abs(tmp) < answer:
            ans_left = left_idx
            ans_right = right_idx
            answer = abs(tmp)
        
        if tmp < 0:
            left_idx += 1
        
        if tmp > 0:
            right_idx -= 1

        if tmp == 0:
            break
    
    print(lst[ans_left], lst[ans_right])

def binary_search():
    answer = float('inf')
    ans_left, ans_right = 0, 0

    for i in range(n - 1):
        current = lst[i]
        start = i + 1
        end = n - 1

        while start <= end:
            mid = (start + end) // 2
            tmp = current + lst[mid]
            
            if abs(tmp) < answer:
                answer = abs(tmp)
                ans_left, ans_right = i, mid

                if answer == 0:
                    break
            
            if tmp < 0:
                start = mid + 1
            else:
                end = mid - 1
    print(lst[ans_left], lst[ans_right])


# two_pointer()
binary_search()