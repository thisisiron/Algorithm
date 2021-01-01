import sys
import heapq
from collections import deque
input = sys.stdin.readline


dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]


def find_min_dist(cur, _map, baby):
    q = deque()
    q.append(cur)

    cnt, cur_y, cur_x = cur

    _map[cur_y][cur_x] = 0
    min_dist = []
    visited = [[0] * len(_map) for _ in range(len(_map))]
    visited[cur_y][cur_x] = 1

    while q:
        cnt, cur_y, cur_x = q.popleft()

        for mv_y, mv_x in zip(dy, dx):
            nxt_y, nxt_x = cur_y + mv_y, cur_x + mv_x

            if 0 <= nxt_y < len(_map) and 0 <= nxt_x < len(_map) and not visited[nxt_y][nxt_x]:
                visited[nxt_y][nxt_x] = 1
                
                if _map[nxt_y][nxt_x] == 0 or _map[nxt_y][nxt_x] == baby:
                    q.append((cnt + 1, nxt_y, nxt_x))
                    continue
                
                if _map[nxt_y][nxt_x] > baby:
                    continue
                else:
                    heapq.heappush(min_dist, (cnt + 1, nxt_y, nxt_x))

    return min_dist[0] if min_dist else None


N = int(input())
_map = []
for y in range(N):
    m = list(map(int, input().split()))
    for x in range(len(m)):
        if m[x] == 9:
            cur = (0, y, x)
    _map.append(m)

sec = 0
baby = 2
ate = baby

while True:
    cur = find_min_dist(cur, _map, baby)
    if cur is None:
        break

    sec = cur[0]
    ate -= 1

    if ate == 0:
        baby += 1
        ate = baby

print(sec)