import sys
import heapq
input = sys.stdin.readline


def dijkstra(graph, start):
    q = [(0, start)]
    dists = [float('inf')] * (N + 1)
    dists[start] = 0

    while q:
        cur_w, cur = heapq.heappop(q)
        
        if dists[cur] < cur_w:
            continue
        
        if cur not in graph:
            continue

        for nxt, nxt_w in graph[cur]:
            cost = dists[cur] + nxt_w
            if dists[nxt] > cost:
                dists[nxt] = cost
                heapq.heappush(q, (cost, nxt))
    return dists


N, E = map(int, input().split())

graph = {} 
for _ in range(E):
    a, b, c = map(int, input().split())
    graph.setdefault(a, []).append((b, c))
    graph.setdefault(b, []).append((a, c))

v1, v2 = map(int, input().split())

a = dijkstra(graph, v1)
b = dijkstra(graph, v2)
ans = min(a[1] + b[N], a[N] + b[1]) + a[v2]

print(ans if ans != float('inf') else -1)