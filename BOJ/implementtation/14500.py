import sys
input = sys.stdin.readline


fig1 = [[1, 1], [1, 1]]
fig2 = [[1], [1], [1], [1]]
fig3 = [[1, 0], [1, 1], [0, 1]]
fig4 = [[1, 0], [1, 0], [1, 1]]
fig5 = [[1, 1, 1], [0, 1, 0]]


def rotate_matrix(m):
    return [[m[j][i] for j in range(len(m))] for i in range(len(m[0])-1,-1,-1)]


def check_fig(fig, _map, y, x):
    _sum = 0
    for fy in range(len(fig)):
        for fx in range(len(fig[0])):
            if fig[fy][fx]:
                if 0 <= y + fy < len(_map) and 0 <= x + fx < len(_map[0]):
                    _sum += _map[y + fy][x + fx]
                else:
                    return 0
    return _sum


N, M = map(int, input().split())

_map = []
for _ in range(N):
    _map.append(list(map(int, input().split())))


mx = 0
for i in range(N):
    for j in range(M):
        res = check_fig(fig1, _map, i, j)
        mx = max(mx, res)

        for fig in [fig2, fig3]:
            res = check_fig(fig, _map, i, j)
            mx = max(mx, res)

            fig = rotate_matrix(fig)
            res = check_fig(fig, _map, i, j)
            mx = max(mx, res)

        for fig in [fig4, fig5]:
            fig = rotate_matrix(fig)
            res = check_fig(fig, _map, i, j)
            mx = max(mx, res)

            for r in range(3):
                fig = rotate_matrix(fig)
                res = check_fig(fig, _map, i, j)
                mx = max(mx, res)

print(mx)