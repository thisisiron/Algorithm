import sys
input = sys.stdin.readline


n = int(input())
m = int(input())
graph = [[float('inf')] * n for _ in range(n)] 
for _ in range(m):
    a, b, c = map(int, input().split())
    if graph[a - 1][b - 1] > c: 
        graph[a - 1][b - 1] = c

for k in range(n):
    for i in range(n):
        for j in range(n):
            if graph[i][j] > graph[i][k] + graph[k][j]:
                graph[i][j] = graph[i][k] + graph[k][j]

for i in range(n):
    graph[i][i] = 0

for row in graph:
    for val in row:
        if val == float('inf'):
            print(0, end=' ')
        else:
            print(val, end=' ')
    print()