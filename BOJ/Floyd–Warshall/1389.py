import sys
from math import inf
input = sys.stdin.readline


N, M = map(int, input().split())
graph = [[inf] * N for _ in range(N)]

for _ in range(M):
    A, B = map(int, input().split())
    graph[A - 1][B - 1] = 1
    graph[B - 1][A - 1] = 1

for k in range(N):
    for i in range(N):
        for j in range(N):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
        
mn = inf
for i, row in enumerate(graph):
    row[i] = 0
    res = sum(row)
    if mn > res:
        ans = i + 1 
        mn = res
print(ans)