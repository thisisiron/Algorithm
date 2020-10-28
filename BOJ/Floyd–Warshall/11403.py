import sys
from math import inf
input = sys.stdin.readline


def floyd_warshall(graph):
    N = len(graph)
    for k in range(N):
        for i in range(N):
            for j in range(N):
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])


N = int(input())
graph = [[x if x == 1 else inf for x in map(int, input().split()) ] for _ in range(N)]

floyd_warshall(graph)
for r in graph:
    for c in r:
        print(1 if c != inf else 0, end=" ")
    print()