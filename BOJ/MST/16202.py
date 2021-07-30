import sys
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


N, M, K = map(int, input().split())

edges = []
for i in range(1, M + 1):
    x, y = map(int, input().split())
    edges.append((i, x - 1, y - 1))

answer = []
for k in range(K):
    ans = 0
    cnt = 0
    root = [i for i in range(N)]
    rank = [1 for i in range(N)]
    for c, a, b in edges[k:]:
        if find(a) != find(b):
            union(a, b)
            cnt += 1
            ans += c
        if cnt == N - 1:
            answer.append(ans)
            break
    else:
        answer.append(0)
print(*answer)