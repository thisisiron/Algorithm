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

    if parent[x] < parent[y]:
        parent[x] = y
    else:
        parent[y] = x


V, E = map(int, input().split())
edges = []
for _ in range(E):
    a, b, c = map(int, input().split())
    edges.append((c, a, b))

edges.sort()
parent = [i for i in range(V + 1)]

ans = 0
cnt = 0
while cnt < V - 1:
    c, a, b = edges.pop(0)
    if find(a) != find(b):
        union(a, b)

        cnt += 1
        ans += c
print(ans)