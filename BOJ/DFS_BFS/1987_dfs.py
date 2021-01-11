import sys
from collections import deque
input = sys.stdin.readline


def dfs(y, x, cnt):
    global max_val
    max_val = max(max_val, cnt)

    for my, mx in zip(dy, dx):
        ny = my + y
        nx = mx + x
        if 0 <= ny < R and 0 <= nx < C and not alphabet[board[ny][nx]]:
            alphabet[board[ny][nx]] = 1
            dfs(ny, nx, cnt + 1)
            alphabet[board[ny][nx]] = 0


dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]


R, C = map(int, input().split())
board = [list(map(lambda x: ord(x) - 65, input().rstrip())) for _ in range(R)]

max_val = 1 
alphabet = [0] * 26
alphabet[board[0][0]] = 1

dfs(0, 0, max_val)

print(max_val)