import sys 
from collections import deque
input = sys.stdin.readline


N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [0] * (N + 1)
cnt = 0
for i in range(1, N + 1):
    if visited[i]:
        continue
    queue = deque()
    queue.append(i)
    visited[i] = 1
    while queue:
        cur = queue.popleft()

        for nxt in graph[cur]:
            if not visited[nxt]:
                queue.append(nxt)
                visited[nxt] = 1
    cnt += 1

print(cnt)