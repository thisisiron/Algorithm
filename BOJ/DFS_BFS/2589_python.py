import sys
from collections import deque
input = sys.stdin.readline


dy = (-1, 1, 0, 0)
dx = (0, 0, -1, 1)


def bfs(y, x):
    queue = deque()
    queue.append((y, x))

    visited = [[0] * C for _ in range(R)] 
    visited[y][x] = 1
    
    cnt = 0

    while queue:
        y, x = queue.popleft()

        for d in range(4):
            ny = y + dy[d]
            nx = x + dx[d]
            if 0 > ny or ny >= R or 0 > nx or nx >= C: continue
            if _map[ny][nx] == 'L' and not visited[ny][nx]:
                visited[ny][nx] = visited[y][x] + 1
                queue.append((ny, nx))
                if visited[ny][nx] > cnt:
                    cnt = visited[ny][nx]
    
    return cnt - 1


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