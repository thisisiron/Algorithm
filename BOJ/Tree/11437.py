import sys
from collections import deque
input = sys.stdin.readline


n = int(input())
adj = {}

for _ in range(n - 1):
    a, b = [int(x) for x in input().split()]
    adj.setdefault(a, []).append(b)
    adj.setdefault(b, []).append(a)

root = 1
depth = [-1] * (n + 1)
parent = [-1] * (n + 1)

queue = deque()
queue.append(root)
depth[root] = 0 

while queue:
    cur_node = queue.popleft()
    
    for child in adj[cur_node]:
        if depth[child] == -1:
            depth[child] = depth[cur_node] + 1
            parent[child] = cur_node
            queue.append(child)

m = int(input())
for _ in range(m):
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