import sys
input = sys.stdin.readline


V, E = map(int, input().split())

graph = [[float('inf')] * V for _ in range(V)] 
for _ in range(E):
    a, b, c = map(int, input().split())
    graph[a - 1][b - 1] =  c

for k in range(V):
    for i in range(V):
        for j in range(V):
            if graph[i][j] > graph[i][k] + graph[k][j]:
                graph[i][j] = graph[i][k] + graph[k][j]
                
mn = float('inf')
for i in range(V):
    for j in range(V):
        if mn > graph[i][j] + graph[j][i]:
            mn = graph[i][j] + graph[j][i]
print(mn if mn != float('inf') else -1)