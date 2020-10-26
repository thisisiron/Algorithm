import sys 
from math import inf
import heapq
input = sys.stdin.readline


N, M, X = map(int, input().split())

graph = [[] for _ in range(N + 1)]
rev_graph = [[] for _ in range(N + 1)]
for _ in range(M):
    s, e, t = map(int, input().split())
    graph[s].append((e, t))
    rev_graph[e].append((s, t))
    

def dijkstra(graph, start):
    distances = [inf] * (N + 1)
    distances[start] = 0
    queue = [(0, start)]

    while queue:
        now_t, now_v = heapq.heappop(queue)

        if now_t > distances[now_v]:
            continue

        for next_v, next_t in graph[now_v]:
            cost = now_t + next_t 
            if cost < distances[next_v]:
                distances[next_v] = cost
                heapq.heappush(queue, (cost, next_v))

    return distances


x_dist = dijkstra(graph, X)
rev_x_dist = dijkstra(rev_graph, X)

ans = 0
for i in range(1, N + 1):
    if i == X:
        continue
    if ans < rev_x_dist[i] + x_dist[i]:
        ans = rev_x_dist[i] + x_dist[i] 

print(ans)