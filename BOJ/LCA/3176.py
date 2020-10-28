import sys
from collections import deque
from math import log2
from math import inf
input = sys.stdin.readline


N = int(input())
graph = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

MAX = int(log2(N) + 1)

root = 1
depth = [-1] * (N + 1)
parent = [[[0, 0, 0] for _ in range(MAX)] for _ in range(N + 1)]   # ie. [parent, min, max]

queue = deque()
queue.append(root)
depth[root] = 0 

while queue:
    cur_node = queue.popleft()
    
    for child, dist in graph[cur_node]:
        if depth[child] == -1:
            depth[child] = depth[cur_node] + 1
            parent[child][0][0] = cur_node
            parent[child][0][1] = dist
            parent[child][0][2] = dist
            queue.append(child)

for j in range(MAX - 1):
    for i in range(1, N + 1):
        parent[i][j + 1][0] = parent[parent[i][j][0]][j][0]
        parent[i][j + 1][1] = min(parent[i][j][1], parent[parent[i][j][0]][j][1])
        parent[i][j + 1][2] = max(parent[i][j][2], parent[parent[i][j][0]][j][2])

K = int(input())
for _ in range(K):
    d, e = map(int, input().split())

    if depth[d] > depth[e]:
        d, e = e, d
    
    diff = depth[e] - depth[d]

    shortest = inf
    longest = 0

    j = 0
    while diff:
        if diff % 2:
            shortest = min(shortest, parent[e][j][1])
            longest = max(longest, parent[e][j][2])
            e = parent[e][j][0]
        diff //= 2 
        j += 1
    
    if e == d:
        print(shortest, longest)
        continue
    
    for j in range(MAX - 1, -1, -1):
        if parent[e][j][0] != parent[d][j][0]:
            shortest = min(shortest, parent[e][j][1], parent[d][j][1])
            longest = max(longest, parent[e][j][2], parent[d][j][2])
            e = parent[e][j][0]
            d = parent[d][j][0]
    shortest = min(shortest, parent[e][j][1], parent[d][j][1])
    longest = max(longest, parent[e][j][2], parent[d][j][2])
    print(shortest, longest)