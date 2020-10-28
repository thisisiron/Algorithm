import sys
from math import inf
input = sys.stdin.readline


N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]

for k in range(N):
    for i in range(N):
        for j in range(N):
            if graph[i][j] == 0:
                graph[i][j] = graph[i][k] * graph[k][j]

for r in graph:
    for c in r:
        print(c, end=" ")
    print()