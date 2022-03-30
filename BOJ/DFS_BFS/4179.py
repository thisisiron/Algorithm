import sys
from collections import deque

input = sys.stdin.readline


dy = (0, 0, -1, 1)
dx = (1, -1, 0, 0)


R, C = map(int, input().split())
maze = [[] for _ in range(R)]
visited = [[0] * C for _ in range(R)]

loc_fire = []

for r in range(R):
    for c, state in enumerate(input().rstrip()):
        maze[r].append(state)
        if state == 'F':
            loc_fire.append((r, c))
        elif state == 'J':
            start = (r, c, 0)
            visited[r][c] = 1

queue = deque()
queue.append(start)

flag = False
while queue:

    tmp = []
    for f_y, f_x in loc_fire:
        for i in range(4):
            nf_y = f_y + dy[i]
            nf_x = f_x + dx[i]
            if nf_y < 0 or nf_y >= R or nf_x < 0 or nf_x >= C or maze[nf_y][nf_x] == '#' or maze[nf_y][nf_x] == 'F':
                continue
            maze[nf_y][nf_x] = 'F'
            tmp.append((nf_y, nf_x))
    loc_fire = tmp

    nxt_queue = deque()
    while queue:
        y, x, c = queue.popleft()
        if y == R - 1 or x == C - 1 or y == 0 or x == 0:
            flag = True
            break

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            
            if ny < 0 or ny >= R or nx < 0 or nx >= C or maze[ny][nx] == '#' or maze[ny][nx] == 'F' or visited[ny][nx]:
                continue
            visited[ny][nx] = 1
            nxt_queue.append((ny, nx, c + 1))
    if flag:
        break
    queue = nxt_queue

print(c + 1 if flag else 'IMPOSSIBLE')