import sys
input = sys.stdin.readline


def find(parent, x):
    if parent[x] == x:
        return x
    parent[x] = find(parent, parent[x])
    return parent[x]


def union(parent, x, y):
    x = find(parent, x)
    y = find(parent, y)
    parent[y] = x


N, L, R = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
cnt = 0

while True:
    group = list(range(N * N))
    flag = False

    for r in range(N):
        for c in range(N):
            cur = A[r][c]
            for mr, mc in zip([1, -1, 0, 0], [0, 0, 1, -1]):
                nr = r + mr
                nc = c + mc
                if 0 <= nr < N and 0 <= nc < N:
                    if L <= abs(A[r][c] - A[nr][nc]) <= R:
                        if find(group, N * r + c) == find(group, N * nr + nc):
                            continue
                        union(group, N * r + c, N * nr + nc)
                        flag = True
    if not flag:
        break
    sum_list = [0] * (N * N)
    counter = [0] * (N * N)
    for i in range(len(group)):
        g = find(group, i)
        sum_list[g] += A[i // N][i % N]
        counter[g] += 1

    for i in range(len(group)):
        g = find(group, i) 
        A[i // N][i % N] = sum_list[g] // counter[g]
    cnt += 1
print(cnt)