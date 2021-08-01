import sys
import heapq
ipnut = sys.stdin.readline


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


N, M, t = map(int, input().split())

city = []
for i in range(M):
    a, b, c = map(int, input().split())
    heapq.heappush(city, (c, a - 1, b - 1))

root = [i for i in range(N)]
rank = [1 for i in range(N)]
cnt = 0
ans = 0
while cnt < N - 1:
    c, a, b = heapq.heappop(city)
    if find(a) != find(b):
        union(a, b)

        ans += c + cnt * t
        cnt += 1
print(ans)