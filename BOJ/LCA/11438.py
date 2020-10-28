import sys
from math import log2
from collections import deque
input = sys.stdin.readline


n = int(input())
MAX = int(log2(n) + 1)
adj = {}

for _ in range(n - 1):
    a, b = map(int, input().split())
    adj.setdefault(a, []).append(b)
    adj.setdefault(b, []).append(a)

root = 1
depth = [-1] * (n + 1)
parent = [[-1] * MAX for _ in range(n + 1)]

queue = deque()
queue.append(root)
depth[root] = 0 

while queue:
    cur_node = queue.popleft()
    
    for child in adj[cur_node]:
        if depth[child] == -1:
            depth[child] = depth[cur_node] + 1
            parent[child][0] = cur_node
            queue.append(child)

for j in range(MAX - 1):
    for i in range(1, n + 1):
        if parent[i][j] != -1:
            parent[i][j + 1] = parent[parent[i][j]][j]

m = int(input())
for _ in range(m):
    a, b = map(int, input().split())

    if depth[a] < depth[b]:
        a, b = b, a
    
    diff = depth[a] - depth[b]

    j = 0
    while diff:
        if diff % 2:
            a = parent[a][j]
        diff //= 2
        j += 1

    if a != b:
        for j in range(MAX - 1, -1, -1):
            if parent[a][j] != -1 and parent[a][j] != parent[b][j]:
                a = parent[a][j]
                b = parent[b][j]
        a = parent[a][0]
    print(a)