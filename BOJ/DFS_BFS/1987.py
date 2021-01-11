import sys
from collections import deque
input = sys.stdin.readline


dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]


R, C = map(int, input().split())
board = [[c for c in input().rstrip()] for _ in range(R)]

max_val = 0
q = set()
q.add((0, 0, board[0][0]))

while q:
    y, x, alphabet = q.pop()
    
    if max_val < len(alphabet):
        max_val = len(alphabet)

    if max_val == 26:
        max_val = 26
        break

    for my, mx in zip(dy, dx):
        ny = my + y
        nx = mx + x
        if 0 <= ny < R and 0 <= nx < C and board[ny][nx] not in alphabet:
            q.add((ny, nx, alphabet + board[ny][nx]))

print(max_val)