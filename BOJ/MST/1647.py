import sys
import heapq
input = sys.stdin.readline


def find(x):
    if root[x] != x:
        root[x] = find(root[x])
    return root[x]


def union(x, y):
    x = find(x)
    y = find(y)

    if x == y:
        return 

    if rank[x] < rank[y]:
        root[x] = y
    else:
        root[y] = x

        if rank[x] == rank[y]:
            rank[x] += 1


N, M = map(int, input().split())
edges = []
for i in range(M):
    a, b, c = map(int, input().split()) 
    heapq.heappush(edges, (c, a - 1, b - 1))

root = [i for i in range(N)]
rank = [1 for i in range(N)]

ans = 0
cnt = 0

while cnt < N - 2:
    c, a, b = heapq.heappop(edges) 

    if find(a) != find(b):
        union(a, b)
        cnt += 1
        ans += c
print(ans)