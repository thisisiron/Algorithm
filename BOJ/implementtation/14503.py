import sys
from collections import deque
input = sys.stdin.readline


def check(_map, y, x):
    if 0 <= y < len(_map) and 0 <= x < len(_map[0]):
        if _map[y][x] == 1:
            return False 
        return True
    else:
        return False


N, M = map(int, input().split())
r, c, d = map(int, input().split())

_map = [list(map(int, input().split())) for _ in range(N)]

cnt = 0

stack = deque()
stack.append([r, c, d])

while stack:
    r, c, d = stack.pop()
    if _map[r][c] == 0:
        cnt += 1
    _map[r][c] = 2

    i = 4
    while i > 0:
        if d == 0:
            if check(_map, r, c - 1) and _map[r][c - 1] == 0:
                stack.append([r, c - 1, 3])
                break
            else:
                d = 3
                i -= 1
                continue
        elif d == 1:
            if check(_map, r - 1, c) and _map[r - 1][c] == 0:
                stack.append([r - 1, c, 0])
                break
            else:
                d = 0
                i -= 1
                continue
        elif d == 2:
            if check(_map, r, c + 1) and _map[r][c + 1] == 0:
                stack.append([r, c + 1, 1])
                break
            else:
                d = 1
                i -= 1
                continue
        elif d == 3:
            if check(_map, r + 1, c) and _map[r + 1][c] == 0:
                stack.append([r + 1, c, 2])
                break
            else:
                d = 2
                i -= 1
                continue
    
    if i == 0:
        if d == 0:
            if check(_map, r + 1, c):
                stack.append([r + 1, c, d])
            else:
                break
        elif d == 1: 
            if check(_map, r, c - 1):
                stack.append([r, c - 1, d])
            else:
                break
        elif d == 2:
            if check(_map, r - 1, c):
                stack.append([r - 1, c, d])
            else:
                break
        elif d == 3:
            if check(_map, r, c + 1):
                stack.append([r, c + 1, d])
            else:
                break
print(cnt)