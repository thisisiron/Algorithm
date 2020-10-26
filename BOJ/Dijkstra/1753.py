import sys 
from math import inf
import heapq
input = sys.stdin.readline


V, E = map(int, input().split())
start = int(input())

graph = [[] for _ in range(V + 1)]
for i in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

distance = [inf] * (V + 1)
queue = [(0, start)]
distance[start] = 0

while queue:
    w, now = heapq.heappop(queue) 

    if distance[now] < w:
        continue

    for next_node, next_w in graph[now]:
        cost = w + next_w 
        if cost < distance[next_node]:
            distance[next_node] = cost
            heapq.heappush(queue, (cost, next_node))

for i in range(1, V + 1):
    if distance[i] == inf:
        print('INF')
    else:
        print(distance[i])