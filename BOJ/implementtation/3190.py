import sys
from collections import  deque
from pprint import pprint
input = sys.stdin.readline


direc = {
    'U': [-1, 0],
    'D': [1, 0],
    'R': [0, 1],
    'L': [0, -1]
}


def rotate(d, new_d):
    if d == 'R':
        if new_d == 'L':
            return 'U'
        else:
            return 'D'
    elif d == 'L':
        if new_d == 'D':
            return 'U'
        else:
            return 'D'
    elif d == 'U':
        if new_d == 'L':
            return 'L'
        else:
            return 'R'
    elif d == 'D':
        if new_d == 'D':
            return 'L'
        else:
            return 'R'


def game(board, times):
    d = 'R'
    sec = 1
    y, x = 0, 0
    snake = deque()
    snake.append([y, x])
    board[y][x] = 1

    while True:
        y, x = y + direc[d][0], x + direc[d][1]

        if 0 <= y < len(board) and 0 <= x < len(board[0]) and board[y][x] != 1:
            if not board[y][x] == 2:
                tail_y, tail_x = snake.popleft()
                board[tail_y][tail_x] = 0
            board[y][x] = 1
            snake.append([y, x])
            pprint(board)
            print()
            if sec in times:
                d = rotate(d, times[sec])
            sec += 1
        else:
            return sec


N = int(input())
K = int(input())
board = [[0] * N for _ in range(N)]

for _ in range(K):
    r, c = map(int, input().split())
    board[r - 1][c - 1] = 2

L = int(input())
times = {} 
for _ in range(L):
    X, C = input().split()
    times[int(X)] = C
print(game(board, times))