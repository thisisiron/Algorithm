import sys
import copy
from itertools import combinations
from collections import deque
input = sys.stdin.readline


dx = (-1, 1, 0, 0)
dy = (0, 0, 1, -1)


def bfs(virus):
    copied = copy.deepcopy(lab)
    q = deque(virus)
    for y, x, t in virus:
        copied[y][x] = 0

    while q:
        y, x, t = q.popleft()

        for i in range(4):
            ny = dy[i] + y
            nx = dx[i] + x
            if ny >= N or ny < 0 or nx >= N or nx < 0:
                continue

            if copied[ny][nx] == -1:
                continue                   
            
            if copied[ny][nx] == float('inf') or copied[ny][nx] > t + 1:
                copied[ny][nx] = t + 1
                q.append((ny, nx, t + 1))
    for row in copied:
        for x in row:
            if x == float('inf'):
                return float('inf') 
    return t


N, M = map(int, input().split())
lab = []
virus = []
for i in range(N):
    row = [int(x) for x in input().split()]
    tmp = []
    for j in range(N):
        if row[j] == 2:
            virus.append((i, j, 0))
            tmp.append(float('inf'))
        elif row[j] == 1:
            tmp.append(-1)
        else:
            tmp.append(float('inf'))
    lab.append(tmp)

combs = tuple(combinations(virus, M))
mn = float('inf') 
for comb in combs:
    res = bfs(comb)
    if res < mn:
        mn = res
print(mn if mn != float('inf') else -1)