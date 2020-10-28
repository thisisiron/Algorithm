import sys
from collections import deque
from math import log2
input = sys.stdin.readline


N = int(input())
MAX = int(log2(N)) + 1 
adj = {}

for _ in range(N - 1):
    u, v, w = map(int, input().split())
    adj.setdefault(u, []).append((v, w))
    adj.setdefault(v, []).append((u, w))

root = 1
depth = [-1] * (N + 1)
parents = [[-1] * MAX for _ in range(N + 1)]
dist = [0] * (N + 1)

queue = deque()
queue.append(root)
depth[root] = 0

while queue:
    now = queue.popleft()

    for child, w in adj[now]:
        if depth[child] == -1:
            depth[child] = depth[now] + 1 
            dist[child] = dist[now] + w
            parents[child][0] = now
            queue.append(child)

for j in range(MAX - 1):
    for i in range(1, N + 1):
        if parents[i][j] != -1:
            parents[i][j + 1] = parents[parents[i][j]][j]

M = int(input())

for _ in range(M):
    a, b = map(int, input().split())

    answer = dist[a] + dist[b]

    if depth[a] < depth[b]:
        a, b = b, a
    
    diff = depth[a] - depth[b]

    j = 0
    while diff:
        if diff % 2:
            a = parents[a][j]
        diff //= 2
        j += 1

    if a != b:
        for j in range(MAX - 1, -1, -1):
            if parents[a][j] != -1 and parents[a][j] != parents[b][j]:
                a = parents[a][j]
                b = parents[b][j]
        a = parents[a][0]
    answer -= (dist[a] * 2)

    print(answer)