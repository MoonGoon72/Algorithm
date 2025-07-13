import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

n = int(input())
inorder = list(map(int, input().split())) # left, mid, right
postorder = list(map(int, input().split())) # left, right, mid
idx_map = { value: index for index, value in enumerate(inorder) }
tree = []

# postorder의 마지막 원소를 통해 root 값을 찾기
# 미리 만들어둔 map을 사용하여 inorder의 root 위치 찾기
# inorder의 root를 기준으로 왼쪽 서브트리와 오른쪽 서브트리를 분할 정복하기

def build_preorder(in_start, in_end, post_start, post_end):
    if in_start > in_end or post_start > post_end:
        return
    
    root = postorder[post_end]
    print(root, end=" ")
    
    in_root_index = idx_map[root]
    left_size = in_root_index - in_start

    build_preorder(in_start, in_root_index - 1, post_start, post_start + left_size - 1)
    build_preorder(in_root_index + 1, in_end, post_start + left_size, post_end - 1)

build_preorder(0, n - 1, 0, n - 1)