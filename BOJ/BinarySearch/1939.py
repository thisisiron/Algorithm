import sys
from collections import deque
input = sys.stdin.readline


def bfs(mid):
    visited = [0 for _ in range(N + 1)]
    q = deque()
    q.append(V)
    visited[V] = 1

    while q:
        cur = q.popleft()
        
        if cur == W:
            return True
        
        for nxt, w in graph[cur]:
            if not visited[nxt] and mid <= w:
                q.append(nxt)
                visited[nxt] = 1
    return False


N, M = map(int, input().split())
graph = {}
for _ in range(M):
    A, B, C = map(int, input().split())
    graph.setdefault(A, []).append([B, C])
    graph.setdefault(B, []).append([A, C])

V, W = map(int, input().split())

left, right = 1, 1000000000
while left <= right:
    mid = (left + right) // 2

    if bfs(mid):
        left = mid + 1
    else:
        right = mid - 1
print(right)