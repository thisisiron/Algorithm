import sys
input = sys.stdin.readline


di = (0, 0, -1, 1, 1, -1, -1, 1)
dj = (1, -1, 0, 0, 1, -1, 1, -1)

n = int(input())
board = [[0] * n for _ in range(n)]
mine = [[] for _ in range(n)]
for i in range(n):
    for j, x in enumerate(input().rstrip()):
        mine[i].append(x)
        if x == '*':
            for d in range(8):
                ni = i + di[d]
                nj = j + dj[d]
                if ni >= n or ni < 0 or nj >= n or nj < 0:
                    continue
                board[ni][nj] += 1

flag = False
answer = [[] for _ in range(n)]
for i in range(n):
    for j, x in enumerate(input().rstrip()):
        if x == 'x':
            if mine[i][j] == '*':
                flag = True
            answer[i].append(board[i][j])
        else:
            answer[i].append('.')

if flag:
    for i in range(n):
        for j in range(n):
            if mine[i][j] == '*':
                answer[i][j] = '*'

for row in answer:
    print(*row, sep='')