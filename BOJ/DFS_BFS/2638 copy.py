import sys
from collections import deque
input = sys.stdin.readline


def bfs(i, j):
    global visited
    queue = deque()
    queue.append((i, j))
    visited[i][j] = 1

    removed = []
    while queue:
        i, j = queue.popleft()

        for mi, mj in zip(dy, dx):
            ni = i + mi
            nj = j + mj
            if 0 <= ni < N and 0 <= nj < M and not visited[ni][nj]:
                if grid[ni][nj] == 0:
                    queue.append((ni, nj))
                else:
                    print(i, j, '->', ni, nj, ':', grid[ni][nj])
                    removed.append((ni, nj))
                visited[ni][nj] = 1
    return removed


dy = [-1, 1, 0, 0]
dx = [0, 0, 1, -1]
N, M = map(int, input().split())
grid = []
for i in range(N):
    row = list(map(int, input().split()))
    grid.append(row)

cnt = 0

while True:
    visited = [[0] * M for _ in range(N)]
    removed = bfs(0, 0)
    print(removed)

    if not removed:
        break

    for ri, rj in removed:
        grid[ri][rj] = 0
    cnt += 1

    print(grid)

print(cnt)