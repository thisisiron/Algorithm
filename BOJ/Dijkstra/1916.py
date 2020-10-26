import sys 
from math import inf
import heapq
input = sys.stdin.readline


N = int(input())
M = int(input())

graph = [[] for _ in range(N + 1)]
for _ in range(M):
    s, e, cost = map(int, input().split())
    graph[s].append((e, cost))

start, end = map(int, input().split())

total_cost = [inf] * (N + 1)
total_cost[start] = 0
queue = [(0, start)]

while queue:
    cur_cost, cur_v = heapq.heappop(queue)

    if cur_cost > total_cost[cur_v]:
        continue

    for next_v, next_cost in graph[cur_v]:
        cost = cur_cost + next_cost 
        if cost < total_cost[next_v]:
            total_cost[next_v] = cost
            heapq.heappush(queue, (cost, next_v))

print(total_cost[end])