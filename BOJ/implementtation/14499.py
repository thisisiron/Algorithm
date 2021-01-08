import sys
input = sys.stdin.readline


dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

N, M, x, y, K = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(N)]

commands = list(map(int, input().split()))

direction = [
    (2, 0, 5, 3, 4, 1), # east 
    (1, 5, 0, 3, 4, 2), # west 
    (4, 1, 2, 0, 5, 3), # north 
    (3, 1, 2, 5, 0, 4) # south
]

dice = [0] * 6
temp = [0] * 6

for c in commands:
    c -= 1
    direction[c]
    ny = y + dy[c]
    nx = x + dx[c] 
    
    if 0 <= ny < M and 0 <= nx < N:
        y = ny
        x = nx
        temp = dice.copy()
        for i in range(6):
            dice[i] = temp[direction[c][i]]
        
        if board[x][y]:
            dice[5] = board[x][y]
            board[x][y] = 0
        else:
            board[x][y] = dice[5]
        print(dice[0])