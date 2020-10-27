import sys 
import heapq
from math import inf
input = sys.stdin.readline


def dijkstra(graph, start):
    distances = [inf] * (N + 1)
    distances[start] = 0
    q = [(0, start)]

    while q:
        cur_d, cur_n = heapq.heappop(q)

        if cur_d > distances[cur_n]:
            continue

        for next_n, next_d  in graph[cur_n]:
            new_d = cur_d + next_d
            if new_d < distances[next_n]:
                distances[next_n] = new_d
                heapq.heappush(q, (new_d, next_n))
    return distances


N, E = map(int, input().split())
graph = [[] for _ in range(N + 1)]

for _ in range(E):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

v1, v2 = map(int, input().split())

ans = 0
ans2 = 0

first = dijkstra(graph, v1)
second = dijkstra(graph, v2)
ans = min(first[1] + second[N], second[1] + first[N]) + first[v2]

print(ans if ans != inf else -1)