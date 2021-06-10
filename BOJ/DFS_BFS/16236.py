import sys
import heapq
from collections import deque
input = sys.stdin.readline


dy = (-1, 1, 0, 0)
dx = (0, 0, -1, 1)


def find_min_dist(cur, sea, level):
    q = deque()
    q.append(cur)

    y, x, t = cur

    sea[y][x] = 0
    min_dists = []

    visited = [[0] * N for _ in range(N)]
    visited[y][x] = 1
    
    while q:
        y, x, t = q.popleft()

        for i in range(4):
            ny = dy[i] + y
            nx = dx[i] + x

            if ny < 0 or ny >= N or nx < 0 or nx >= N:
                continue

            if not visited[ny][nx]:
                visited[ny][nx] = 1

                if sea[ny][nx] == 0 or sea[ny][nx] == level:
                    q.append((ny, nx, t + 1))
                    continue
                
                if sea[ny][nx] > level:
                    continue
                else:
                    heapq.heappush(min_dists, (t + 1, ny, nx))

    return min_dists[0] if min_dists else None


N = int(input())
sea = []
for i in range(N):
    row = [int(x) for x in input().split()]
    for j in range(N):
        if row[j] == 9:
            cur = (i, j, 0)
        
    sea.append(row)

total_t = 0
level = 2
num_eat = 0

while True:
    min_dist = find_min_dist(cur, sea, level)
    if min_dist is None:
        break

    t, target_y, target_x = min_dist
    total_t += t
    num_eat += 1

    if num_eat == level:
        level += 1
        num_eat = 0

    cur = (target_y, target_x, 0)
print(total_t)