import sys
input = sys.stdin.readline


def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]


def union(x, y):
    x = find(x)
    y = find(y)

    if x == y:
        return
    
    if rank[x] < rank[y]:
        parent[x] = y
    else:
        parent[y] = x

        if rank[x] == rank[y]:
            rank[x] += 1


N = int(input())
planets = [list(map(int, input().split())) for _ in range(N)]

edges = []

for i in range(N):
    for j in range(i + 1, N):
        edges.append((planets[i][j], i, j))
edges.sort()

parent = [i for i in range(N)]
rank = [1] * N

ans = 0
for cost, a, b in edges:

    if find(a) != find(b):
        union(a, b)
        ans += cost

print(ans)