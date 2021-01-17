import sys
from collections import deque
N, M = map(int, input().split())


# dy = [-1, 1, 0, 0]
# dx = [0, 0, -1, 1]

# board = [[int(x) for x in input()] for _ in range(N)]
board = [input() for _ in range(N)]
visited = [[[0] * M for _ in range(N)] for _ in range(2)]
visited[1][0][0] = 1
visited[0][0][0] = 1

queue = deque()
chance = 1
cnt = 1
queue.append((0, 0, chance, cnt))


def bfs():
    while queue:
        y, x, chance, cnt = queue.popleft()

        if y == N - 1 and x == M - 1:
            return cnt

        for nx, ny in [[x - 1, y], [x + 1, y], [x, y - 1], [x, y + 1]]:

            if 0 <= ny < N and 0 <= nx < M:
                if not visited[chance][ny][nx]:
                    if board[ny][nx] == '1' and chance == 1:
                        queue.append((ny, nx, chance - 1, cnt + 1))
                        visited[chance - 1][ny][nx] = 1
                    elif board[ny][nx] == '0':
                        queue.append((ny, nx, chance, cnt + 1))
                        visited[chance][ny][nx] = 1
    return -1


if (N, M) == (1, 1):
    print(1)
else:
    print(bfs())