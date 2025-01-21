import copy
origin = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

def selection_sort():
    array = copy.deepcopy(origin)
    for i in range(len(array)):
        min_index = i
        for j in range(i, len(array)):
            if array[min_index] > array[j]:
                min_index = j
        array[i], array[min_index] = array[min_index], array[i]
    return array

def insertion_sort():
    array = copy.deepcopy(origin)
    for i in range(len(array)):
        for j in range(i, 0, -1):
            if array[j] < array[j - 1]:
                array[j], array[j - 1] = array[j - 1], array[j]
            else:
                break
    return array

def quick_sort(array, start, end):
    if start >= end:
        return
    pivot = start
    left = start + 1
    right = end
    while left <= right:
        while left <= end and array[left] <= array[pivot]:
            left += 1
        while right > start and array[right] >= array[pivot]:
            right -= 1
        if left > right:
            array[right], array[pivot] = array[pivot], array[right]
        else:
            array[left], array[right] = array[right], array[left]
    quick_sort(array, start, right - 1)
    quick_sort(array, right + 1, end)
    return array

def quick_sort_for_python(array):
    if len(array) <= 1:
        return array

    pivot = array[0]
    tail = array[1:]

    left_side = [x for x in tail if x <= pivot]
    right_side = [x for x in tail if x > pivot]    
    return quick_sort_for_python(left_side) + [pivot] + quick_sort_for_python(right_side)

print(selection_sort())
print(insertion_sort())
array = copy.deepcopy(origin)
print(quick_sort(array, 0, len(origin) - 1))
array = copy.deepcopy(origin)
print(quick_sort_for_python(array))