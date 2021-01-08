import sys
input = sys.stdin.readline


right = 0
down = 1
left = 2
up = 3
dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]


def watch(y, x, direction):
    checked = set()
    for d in direction:
        ny = y
        nx = x
        while True:
            ny += dy[d]
            nx += dx[d]
            if not(0 <= ny < N and 0 <= nx < M):
                break
            if room[ny][nx] == 6:
                break
            if room[ny][nx] == 0:
                checked.add((ny, nx))
    return checked


def dfs(n, union):
    global mx
    if n == len(cameras):
        if mx < len(union):
            mx = len(union)
        return
    for checked in cameras[n]:
        dfs(n + 1, union | checked)


N, M = map(int, input().split())
area = N * M
cameras = [] 
camera5 = []
room = [list(map(int, input().split())) for _ in range(N)]
for y in range(N):
    for x in range(M):
        if room[y][x] == 0:
            continue
        if room[y][x] == 1:
            cameras.append([watch(y, x, [up]), watch(y, x, [down]), watch(y, x, [left]), watch(y, x, [right])])
        elif room[y][x] == 2:
            cameras.append([watch(y, x, [up, down]), watch(y, x, [left, right])])
        elif room[y][x] == 3:
            cameras.append([watch(y, x, [up, right]), watch(y, x, [right, down]), watch(y, x, [down, left]), watch(y, x, [left, up])])
        elif room[y][x] == 4:
            cameras.append([watch(y, x, [left, up, right]), watch(y, x, [up, right, down]), watch(y, x, [right, down, left]), watch(y, x, [down, left, up])])
        elif room[y][x] == 5:
            cameras.append([watch(y, x, [up, down, left, right])])
        area -= 1

mx = 0
dfs(0, set())
print(area - mx)