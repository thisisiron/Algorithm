import sys 
from math import inf
import heapq
input = sys.stdin.readline


N, M, X = map(int, input().split())

graph = [[] for _ in range(N + 1)]
for _ in range(M):
    s, e, t = map(int, input().split())
    graph[s].append((e, t))
    

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

ans = 0
for i in range(1, N + 1):
    if i == X:
        continue
    distances = dijkstra(graph, i)
    if ans < distances[X] + x_dist[i]:
        ans = distances[X] + x_dist[i] 

print(ans)