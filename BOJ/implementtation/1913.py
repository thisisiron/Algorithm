import sys
input = sys.stdin.readline


LEFT = 0
TOP = 1
RIGHT = 2
DOWN = 3


N = int(input())
number = int(input())


board = [[0] * N for _ in range(N)]
y = (N - 1) // 2
x = (N - 1) // 2
val = 1
board[y][x] = val

direc = TOP
count = 1

while val != N**2:
    if direc == TOP:
        for i in range(count):
            val += 1
            y -= 1
            board[y][x] = val
            if val == N**2:
                break
        direc = RIGHT
    
    elif direc == RIGHT:
        for i in range(count):
            val += 1
            x += 1
            board[y][x] = val
        count += 1
        direc = DOWN
    
    elif direc == DOWN:
        for i in range(count):
            val += 1
            y += 1
            board[y][x] = val
        direc = LEFT
    
    elif direc == LEFT:
        for i in range(count):
            val += 1
            x -= 1
            board[y][x] = val
        count += 1
        direc = TOP

for i in range(N):
    for j in range(N):
        print(board[i][j], end=' ')
        if board[i][j] == number:
            y = i + 1
            x = j + 1
    print()
print(y, x)