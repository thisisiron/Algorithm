import sys
input = sys.stdin.readline


tetromino = [
    [(0,0), (0,1), (1,0), (1,1)],
    [(0,0), (0,1), (0,2), (0,3)],
    [(0,0), (1,0), (2,0), (3,0)],
    [(0,0), (0,1), (0,2), (1,0)],
    [(1,0), (1,1), (1,2), (0,2)],
    [(0,0), (1,0), (1,1), (1,2)],
    [(0,0), (0,1), (0,2), (1,2)],
    [(0,0), (1,0), (2,0), (2,1)],
    [(2,0), (2,1), (1,1), (0,1)],
    [(0,0), (0,1), (1,0), (2,0)],
    [(0,0), (0,1), (1,1), (2,1)],
    [(0,0), (0,1), (0,2), (1,1)],
    [(1,0), (1,1), (1,2), (0,1)],
    [(0,0), (1,0), (2,0), (1,1)],
    [(1,0), (0,1), (1,1), (2,1)],
    [(1,0), (2,0), (0,1), (1,1)],
    [(0,0), (1,0), (1,1), (2,1)],
    [(1,0), (0,1), (1,1), (0,2)],
    [(0,0), (0,1), (1,1), (1,2)]
]


def check(_map, y, x):
    global mx
    for fig in range(19):
        res = 0
        for i in range(4):
            try:
                fy = y + tetromino[fig][i][1]
                fx = x + tetromino[fig][i][0]
                res += _map[fy][fx]
            except IndexError:
                continue
        mx = max(mx, res) 


N, M = map(int, input().split())

_map = []
for _ in range(N):
    _map.append(list(map(int, input().split())))

mx = 0
for i in range(N):
    for j in range(M):
        check(_map, i, j)

print(mx)