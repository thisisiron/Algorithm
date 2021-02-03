import sys
from collections import deque
input = sys.stdin.readline


dy = (-1, 1, 0, 0)
dx = (0, 0, -1, 1) 


def bfs(y, x, num):
    q = deque()
    q.append((y, x))
    island[y][x] = num
    side = []
    
    while q:
        y, x = q.popleft()
        is_side = False

        for i in range(4):
            ny = y + dy[i] 
            nx = x + dx[i]
            if ny >= N or ny < 0 or nx >= N or nx < 0: continue
            if not island[ny][nx]:
                is_side = True 
            elif island[ny][nx] == 1:
                island[ny][nx] = num
                q.append((ny, nx))
        
        if is_side:
            side.append((y, x))
    total_side.append(side)


def cal_dist(y1, x1, y2, x2):
    return abs(y2 - y1) + abs(x2 - x1)


N = int(input())
island = [list(map(int, input().split())) for _ in range(N)]
total_side = [[], []]
visited = [[0] * N for _ in range(N)]

num = 2
for i in range(N):
    for j in range(N):
        if island[i][j] == 1:
            bfs(i, j, num)
            num += 1

mn = float('inf')
for start in range(2, num - 1):
    for end in range(start + 1, num):
        for sy, sx in total_side[start]:
            for ey, ex in total_side[end]:
                dist = cal_dist(sy, sx, ey, ex)
                if mn > dist:
                    mn = dist 

print(mn - 1)