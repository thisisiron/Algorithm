import sys
from collections import deque
input = sys.stdin.readline


t = int(input())

for _ in range(t):
    N = int(input())
    parent = {}
    children = {}

    for _ in range(N - 1):
        a, b = [int(x) for x in input().split()]
        parent[b] = a
        children.setdefault(a, []).append(b)
    
    root = 1
    while parent.get(root) != None:
        root = parent[root]
    
    depth = {}
    queue = deque()
    level = 1
    queue.append((root, level))

    while queue:
        cur, level = queue.popleft()
        depth[cur] = level 

        if children.get(cur) == None:
            continue

        for child in children[cur]:
            queue.append((child, level + 1))

    a, b = [int(x) for x in input().split()]

    while depth[a] != depth[b] or a != b:
        if depth[a] > depth[b]:
            a = parent[a]
        elif depth[a] < depth[b]:
            b = parent[b]
        else:
            a = parent[a]
            b = parent[b]
        
    print(a)