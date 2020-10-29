import sys
import heapq
from math import inf
input = sys.stdin.readline


i = 1
while True:
    N = int(input())
    if N == 0:
        break
    graph = [[int(x) for x in map(int, input().split())] for _ in range(N)]

    start = (0, 0)
    distances = [[inf] * N for _ in range(N)]
    q = [(graph[0][0], start)]

    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]

    while q:
        now_w, (now_y, now_x) = heapq.heappop(q)
        
        if now_w > distances[now_y][now_x]:
            continue
        for ny, nx in zip(dy, dx):
            new_y = now_y + ny
            new_x = now_x + nx
            if 0 <= new_y < N and 0 <= new_x < N:
                cost = now_w + graph[new_y][new_x]
                if cost < distances[new_y][new_x]:
                    distances[new_y][new_x] = cost
                    heapq.heappush(q, (cost, (new_y, new_x)))
    print(f"Problem {i}: {distances[-1][-1]}")
    i += 1