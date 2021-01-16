import sys
input = sys.stdin.readline


def dfs(cur, idx):
    for nxt in graph[idx]:
        if not check[cur][nxt]:
            check[cur][nxt] = 1
            check[nxt][cur] = 1
            dfs(cur, nxt)


N, M = map(int, input().split())
graph = [[] * (N + 1) for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)

check = [[0] * (N + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
    check[i][i] = 1
    dfs(i, i)

cnt = 0
for row in check:
    if row == [0] + [1] * N:
        cnt += 1

print(cnt)