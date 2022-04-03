import sys
from collections import deque
input = sys.stdin.readline


dy = (0, 0, -1, 1)
dx = (-1, 1, 0, 0)


def check(y, x):
    visited[y][x] = 1

    queue = deque()
    queue.append((y, x))

    while queue:
        y, x = queue.popleft()

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            
            if ny >= H or ny < 0 or nx >= W or nx < 0 or grassland[ny][nx] == '.':
                continue

            if visited[ny][nx]:
                continue

            queue.append((ny, nx))
            visited[ny][nx] = 1


T = int(input())
for _ in range(T):
    H, W = map(int, input().split())

    grassland = [[x for x in input()] for _ in range(H)]
    visited = [[0] * W for _ in range(H)]

    cnt = 0
    for h in range(H):
        for w in range(W):
            if grassland[h][w] == '#' and not visited[h][w]:
                check(h, w)
                cnt += 1

    print(cnt)