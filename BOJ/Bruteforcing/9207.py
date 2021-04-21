import sys
input = sys.stdin.readline


dy = (1, -1, 0, 0)
dx = (0, 0, -1, 1)


def dfs(y, x, num_pins, depth):
    global min_pins, cnt
    if num_pins <= min_pins:
        if num_pins == min_pins:
            cnt = depth if cnt > depth else cnt
        else:
            min_pins = num_pins
            cnt = depth

    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if ny < 0 or ny >= R or nx < 0 or nx >= C or board[ny][nx] != 'o':
            continue
        
        nny = ny + dy[i]
        nnx = nx + dx[i]

        if nny < 0 or nny >= R or nnx < 0 or nnx >= C or board[nny][nnx] != '.':
            continue
            
        board[y][x] = board[ny][nx] = '.'
        board[nny][nnx] = 'o'

        for r in range(R):
            for c in range(C):
                if board[r][c] == 'o':
                    dfs(r, c, num_pins - 1, depth + 1)

        board[y][x] = board[ny][nx] = 'o'
        board[nny][nnx] = '.'

R = 5
C = 9
N = int(input())

for t in range(N):
    board = []
    num_pins = 0
    for r in range(R):
        tmp = [x for x in input().rstrip()]
        for c in range(C):
            if tmp[c] == 'o':
                num_pins += 1
        board.append(tmp)
    if t != N - 1: 
        input()
    
    min_pins = cnt = float('inf') 
    
    for r in range(R):
        for c in range(C):
            if board[r][c] == 'o':
                dfs(r, c, num_pins, 0)
    print(min_pins, cnt) 