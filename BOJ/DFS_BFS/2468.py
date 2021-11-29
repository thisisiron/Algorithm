import sys
from collections import deque
input = sys.stdin.readline


dy = (0, 0, 1, -1)
dx = (1, -1, 0, 0)


def bfs(y, x):
    
    q = deque()
    q.append((y, x))
    visited[y][x] = 1
    
    while q:
        y, x = q.popleft()
        
        for d in range(4):
            ny = dy[d] + y
            nx = dx[d] + x

            if ny >= N or ny < 0 or nx >= N or nx < 0 or visited[ny][nx]:
                continue
            if board[ny][nx] <= h:
                continue

            q.append((ny, nx))
            visited[ny][nx] = 1


N = int(input())
board = []
max_high = 1
for _ in range(N):
    a = [int(x) for x in input().split()]
    tmp = max(a)
    if tmp > max_high:
        max_high = tmp
    board.append(a)

mx = 0

for h in range(max_high):

    visited = [[0] * N for _ in range(N)]
    cnt = 0
    
    for i in range(N):
        for j in range(N):
            if not visited[i][j] and board[i][j] > h:
                bfs(i, j)
                cnt += 1
    if mx < cnt:
        mx = cnt

print(mx)