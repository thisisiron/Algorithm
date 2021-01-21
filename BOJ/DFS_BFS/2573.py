import sys
from collections import deque
input = sys.stdin.readline


dy = (-1, 1, 0, 0)
dx = (0, 0, -1, 1)


def bfs(y, x):
    queue = deque()
    queue.append((y, x))
    visited[y][x] = 1

    while queue:
        y, x = queue.popleft()
        cnt = 0
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if 0 <= ny < R and 0 <= nx < C:
                if iceberg[ny][nx] == 0 and not visited[ny][nx]:
                    cnt += 1      
                elif not visited[ny][nx]:
                    visited[ny][nx] = 1
                    queue.append((ny, nx))
        iceberg[y][x] = max(iceberg[y][x] - cnt ,0)
                    

R, C = map(int, input().split())

iceberg = [[int(x) for x in input().split()] for _ in range(R)]

year = 0
while True:
    num = 0
    visited = [[0] * C for _ in range(R)]
    for r in range(R):
        for c in range(C):
            if iceberg[r][c] and not visited[r][c]:
                bfs(r, c)
                num += 1

    if num >= 2:
        break 
    elif num == 0:
        year = 0
        break
    year += 1
print(year)