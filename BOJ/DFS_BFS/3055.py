import sys
from collections import deque
input = sys.stdin.readline


move = ((1, 0), (-1, 0), (0, 1), (0, -1))


R, C = map(int, input().split())
forest = []
water = []
for i in range(R):
    row = [x for x in input().rstrip()]
    for j in range(C):
        if row[j] == 'S':
            start = (i, j)
        elif row[j] == 'D':
            goal = (i, j)
        elif row[j] == '*':
            water.append((i, j))
    forest.append(row)

cnt = 0
queue = deque()
queue.append((*start, cnt))
visited = [[0] * C for _ in range(R)]
visited[start[0]][start[1]] = 1


def bfs(water):
    while queue:
        new = []
        for wi, wj in water:
            for mi, mj in move:
                nwi = wi + mi
                nwj = wj + mj
                if 0 <= nwi < R and 0 <= nwj < C:
                    if forest[nwi][nwj] == '.':
                        forest[nwi][nwj] = '*'
                        new.append((nwi, nwj))
        water = new 

        q_len = len(queue)
        while q_len:
            di, dj, cnt = queue.popleft()

            for mi, mj in move:
                ni = di + mi
                nj = dj + mj
                if 0 <= ni < R and 0 <= nj < C and not visited[ni][nj]:
                    if forest[ni][nj] == '.':
                        queue.append((ni, nj, cnt + 1))
                        visited[ni][nj] = 1
                    elif forest[ni][nj] == 'D':
                        cnt += 1
                        print(cnt)
                        return
            q_len -= 1
    print('KAKTUS')
    return


bfs(water)