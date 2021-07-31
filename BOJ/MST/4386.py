import sys
import heapq
input = sys.stdin.readline


def find(x):
    if x != root[x]:
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


n = int(input())
stars = []
for i in range(n):
    x, y = map(float, input().split())
    stars.append((x, y))

q = []
for i in range(n - 1):
    for j in range(i + 1, n):
        dist = ((stars[i][0] - stars[j][0]) ** 2 + (stars[i][1] - stars[j][1]) ** 2) ** .5
        heapq.heappush(q, (dist, i, j))

root = [i for i in range(n)]
rank = [1 for i in range(n)]

cnt = 0
ans = 0
while cnt < n - 1:
    dist, a, b = heapq.heappop(q)
    if find(a) != find(b):
        union(a, b)
        cnt += 1
        ans += dist

print(f"{ans:.3}")