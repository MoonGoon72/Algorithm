def solution_a():
    import itertools
    n, m = map(int, input().split())
    data = list(map(int, input().split()))

    comb = list(itertools.combinations(data, 2))
    result = list(filter(lambda x: x[0] != x[1], comb))
    print(len(result))

def solution_b():
    n, m = map(int, input().split())
    data = list(map(int, input().split()))
    array = [0] * 11
    
    for x in data:
        array[x] += 1
    
    result = 0
    for i in range(1, m + 1):
        n -= array[i]
        result += array[i] * n
    print(result)

solution_b()