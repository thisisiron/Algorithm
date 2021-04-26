import sys
import heapq
input = sys.stdin.readline


V, E = map(int, input().split())
K = int(input())
graph = {} 
for _ in range(E):
    u, v, w = map(int, input().split())
    graph.setdefault(u, []).append((v, w))

q = [] 
dists = [float('inf')] * (V + 1)
dists[K] = 0
q.append((0, K))

while q:
    cur_w, cur = heapq.heappop(q) 
    
    if dists[cur] < cur_w:
        continue

    if cur not in graph:
        continue
    
    for nxt, w in graph[cur]:
        if dists[nxt] > dists[cur] + w:
            dists[nxt] = dists[cur] + w
            heapq.heappush(q, (dists[cur] + w, nxt))

for i in range(1, V + 1):
    print(dists[i] if dists[i] != float('inf') else 'INF')