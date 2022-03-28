import sys
input = sys.stdin.readline


N, M = map(int, input().split())
trees = []

right = 0
for tree in map(int, input().split()):
    trees.append(tree)
    if right < tree:
        right = tree

left = 0
ans = 0
while left <= right:
    mid = (left + right) // 2
    
    x = 0
    for tree in trees:
        if tree > mid:
            x += (tree - mid)
            
    if x < M:
        right = mid - 1
    else:
        ans = mid
        left = mid + 1

print(ans)