from collections import deque
import sys
input = sys.stdin.readline


def bfs(cur, mode):
    q = deque()
    q.append((cur, 0))
    visited = [0] * n
    visited[cur] = 1
    res = [0, 0]
    while q:
        cur, cur_w = q.popleft()
        if res[0] < cur_w:
            res[0] = cur_w
            res[1] = cur  
        for nxt_w, nxt in graph[cur]:
            if not visited[nxt]:
                visited[nxt] = 1 
                q.append((nxt, cur_w + nxt_w))
    return res[mode]


n = int(input())
graph = [[] for _ in range(n)]

for i in range(n-1):
    x, y, w = map(int, input().split())
    graph[x-1].append([w, y-1])
    graph[y-1].append([w, x-1])
print(bfs(bfs(0, 1), 0))