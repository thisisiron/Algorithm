import sys
from collections import deque
input = sys.stdin.readline


def bfs(i, j):
    global visited
    queue = deque()
    queue.append((i, j))
    visited[i][j] = 1

    while queue:
        i, j = queue.popleft()

        for mi, mj in zip(dy, dx):
            ni = i + mi
            nj = j + mj
            if 0 <= ni < N and 0 <= nj < M and not visited[ni][nj]:
                if grid[ni][nj] == 0:
                    queue.append((ni, nj))
                    visited[ni][nj] = 1
                else:
                    grid[ni][nj] += 1


dy = [-1, 1, 0, 0]
dx = [0, 0, 1, -1]
N, M = map(int, input().split())
grid = []
cheeze = 0
for i in range(N):
    row = list(map(int, input().split()))
    for x in row:
        if x == 1:
            cheeze += 1
    grid.append(row)

cnt = 0

while cheeze >= 1:
    visited = [[0] * M for _ in range(N)]
    bfs(0, 0)

    for i in range(N):
        for j in range(M):
            if grid[i][j] >= 3:
                grid[i][j] = 0
                cheeze -= 1
            elif grid[i][j] == 2:
                grid[i][j] = 1
    cnt += 1

print(cnt)