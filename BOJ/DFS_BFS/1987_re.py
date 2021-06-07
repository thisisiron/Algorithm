import sys
input = sys.stdin.readline


dy = (0, 0, -1, 1)
dx = (1, -1, 0, 0)

R, C = map(int, input().split())
board = []
for _ in range(R):
    board.append(list(input().rstrip()))

q = set() 
q.add((0, 0, board[0][0]))
mx = 0

while q:
    y, x, string = q.pop()

    if mx < len(string):
        mx = len(string)
    
    if mx == 26:
        break

    for i in range(4):
        ny = dy[i] + y
        nx = dx[i] + x
        if ny < 0 or ny >= R or nx < 0 or nx >= C:
            continue

        if board[ny][nx] not in string:
            q.add((ny, nx, string + board[ny][nx]))

print(mx)