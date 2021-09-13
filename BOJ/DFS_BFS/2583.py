import sys
from collections import deque
input = sys.stdin.readline

dy = (1, -1, 0, 0)
dx = (0, 0, -1, 1)


def dfs(y, x):
    global board
    stack = deque()
    stack.append((y, x))
    size = 0
    board[y][x] = rectangle
    while stack:
        y, x = stack.pop()
        size += 1

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if ny < 0 or ny >= M or nx < 0 or nx >= N or board[ny][nx] != 0:
                continue

            stack.append((ny, nx))
            board[ny][nx] = rectangle

    return size


M, N, K = map(int, input().split())
board = [[0] * N for _ in range(M)]
rectangle = 1
for _ in range(K):
    lx, ly, rx, ry = map(int, input().split())

    for y in range(ly, ry):
        for x in range(lx, rx):
            board[y][x] = rectangle
    rectangle += 1

answer = []
for i in range(M):
    for j in range(N):
        if board[i][j] == 0:
            answer.append(dfs(i, j))

print(len(answer))
print(*sorted(answer))