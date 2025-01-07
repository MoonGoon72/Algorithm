import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

preorder =[]
while True:
    try:
        value = int(input())
        preorder.append(value)
    except:
        break

def get_postorder(tree):
    if len(tree) == 0:
        return []
    mid = tree[0]
    left = []
    right = []
    
    for i in range(1, len(tree)):
        if tree[i] < mid:
            left.append(tree[i])
        else:
            right.append(tree[i])

    return get_postorder(left) + get_postorder(right) + [mid]

print("\n".join(map(str, get_postorder(preorder))))