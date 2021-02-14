import sys
input = sys.stdin.readline


N, M = map(int, input().split())
K = int(input())
checkboard = [[[0, 0, 0] for _ in range(M + 1)] for _ in range(N + 1)]

for r in range(1, N + 1):
    for c, x in enumerate(input().rstrip(), 1):
        checkboard[r][c][0] = checkboard[r - 1][c][0] + checkboard[r][c - 1][0] - checkboard[r - 1][c - 1][0]
        checkboard[r][c][1] = checkboard[r - 1][c][1] + checkboard[r][c - 1][1] - checkboard[r - 1][c - 1][1]
        checkboard[r][c][2] = checkboard[r - 1][c][2] + checkboard[r][c - 1][2] - checkboard[r - 1][c - 1][2]
        if x == 'J':
            checkboard[r][c][0] += 1 
        elif x == 'O':
            checkboard[r][c][1] += 1 
        elif x == 'I':
            checkboard[r][c][2] += 1

for _ in range(K):
    y1, x1, y2, x2 = map(int, input().split())
    print(checkboard[y2][x2][0] - checkboard[y2][x1 - 1][0] - checkboard[y1 - 1][x2][0] + checkboard[y1 - 1][x1 - 1][0], end=' ')
    print(checkboard[y2][x2][1] - checkboard[y2][x1 - 1][1] - checkboard[y1 - 1][x2][1] + checkboard[y1 - 1][x1 - 1][1], end=' ')
    print(checkboard[y2][x2][2] - checkboard[y2][x1 - 1][2] - checkboard[y1 - 1][x2][2] + checkboard[y1 - 1][x1 - 1][2])