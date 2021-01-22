import sys
from collections import deque
input = sys.stdin.readline


dy = (-1, 1, 0, 0)
dx = (0, 0, -1, 1)


def bfs(y, x):
    queue = deque()
    queue.append((y, x, 0))

    visited = {(y, x)} 

    while queue:
        y, x, cnt = queue.popleft()

        for d in range(4):
            ny = y + dy[d]
            nx = x + dx[d]
            if 0 <= ny < R and 0 <= nx < C and _map[ny][nx] == 'L' and (ny, nx) not in visited:
                visited.add((ny, nx))
                queue.append((ny, nx, cnt + 1))
    
    return cnt

R, C = map(int, input().split())
_map = [[x for x in  input().rstrip()] for _ in range(R)]
mx = 0

for i in range(R):
    for j in range(C):
        if _map[i][j] == 'L':
            tmp = bfs(i, j)
            if tmp > mx:
                mx = tmp

print(mx)