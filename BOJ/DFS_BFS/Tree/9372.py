import sys
from collections import deque
input = sys.stdin.readline


t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    adj = {}

    for _ in range(m):
        a, b = map(int, input().split())
        adj.setdefault(a, []).append(b)
        adj.setdefault(b, []).append(a)
    
    visited = [0] * (n + 1)
    queue: deque = deque()
    queue.append(a)
    cnt: int = 0

    while queue:
        start = queue.popleft()
        visited[start] = 1

        for next_node in adj[start]:
            if not visited[next_node]:
                queue.append(next_node)
                visited[next_node] = 1
                cnt += 1

    print(cnt)