import sys
from collections import deque
input = sys.stdin.readline


dy = (0, 0, 1, -1, 1, -1, 1, -1)
dx = (1, -1, 0, 0, 1, -1, -1, 1)


while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break

    island = []
    for r in range(h):
        island.append([int(x) for x in input().split()])

    q = deque()
    cnt = 0
    visited = [[0] * w for _ in range(h)]
    for i in range(h):
        for j in range(w):
            if island[i][j] and not visited[i][j]:
                q.append((i, j))
                while q:
                    y, x = q.popleft()

                    for k in range(8):
                        ny = y + dy[k]
                        nx = x + dx[k]
                        if ny < 0 or ny >= h or nx < 0 or nx >= w or island[ny][nx] == 0:
                            continue

                        if not visited[ny][nx]:
                            q.append((ny, nx))
                            visited[ny][nx] = 1
                cnt += 1
    print(cnt)