import sys
from collections import deque
input = sys.stdin.readline


dy = (-1, 1, 0, 0)
dx = (0, 0, -1, 1)


N, M = map(int, input().split())
board = [input() for _ in range(N)]

visited = [[[0] * M for _ in range(N)] for _ in range(2)]
visited[1][0][0] = 1
visited[0][0][0] = 1

q = deque()
chance = 1
dist = 1
q.append((0, 0, chance, dist))

while q:
    y, x, chance, dist = q.popleft()

    if y == N - 1 and x == M - 1:
        res = dist 
        break

    for i in range(4):
        ny = dy[i] + y
        nx = dx[i] + x

        if 0 <= ny < N and 0 <= nx < M:
            if not visited[chance][ny][nx]:
                if board[ny][nx] == '1' and chance == 1:
                    q.append((ny, nx, chance - 1, dist + 1))
                    visited[chance - 1][ny][nx] = 1

                elif board[ny][nx] == '0':
                    q.append((ny, nx, chance, dist + 1))
                    visited[chance][ny][nx] = 1
else:
    res = -1

if 1 == N and 1 == M:
    print(1)
else:
    print(res)