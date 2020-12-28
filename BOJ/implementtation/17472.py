import sys
import bisect
from collections import deque
input = sys.stdin.readline


dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

total_edge = [[], []]  # start 2 index


def dfs(_map, i, j, number):
    stack = deque()
    stack.append([i, j])
    edge = []
    _map[i][j] = number

    while stack:
        y, x = stack.pop()
        is_edge = False

        for d in range(4):
            new_y = y + dy[d]
            new_x = x + dx[d] 
            if 0 <= new_x < M and 0 <= new_y < N:
                if _map[new_y][new_x] == 1:
                    stack.append([new_y, new_x])
                    _map[new_y][new_x] = number
                elif _map[new_y][new_x] == 0:
                    is_edge = True
        if is_edge:
            edge.append((y, x))

    total_edge.append(edge)


def find(x, parent):
    if parent[x] == x:
        return x
    parent[x] = find(parent[x], parent)
    return parent[x]


def union(x, y, parent):
    x = find(x, parent)
    y = find(y, parent)
    parent[x] = y


N, M = map(int, input().split())
_map = []
for _ in range(N):
    _map.append(list(map(int, input().split())))

number = 2
for i in range(N):
    for j in range(M):
        if _map[i][j] == 1:
            dfs(_map, i, j, number)
            number += 1

bridge_table = [[0] * number for _ in range(number)]

for idx in range(2, number):
    for y, x in total_edge[idx]:
        for d in range(4):
            new_y = y + dy[d] 
            new_x = x + dx[d] 
            if 0 <= new_y < N and 0 <= new_x < M:
                cnt = 0
                while _map[new_y][new_x] == 0:
                    cnt += 1
                    new_y += dy[d]
                    new_x += dx[d]
                    
                    if not 0 <= new_y < N or not 0 <= new_x < M:
                        cnt = 0
                        break
                
                if cnt >= 2:
                    if bridge_table[idx][_map[new_y][new_x]]:
                        bridge_table[idx][_map[new_y][new_x]] = min(bridge_table[idx][_map[new_y][new_x]], cnt)
                        bridge_table[_map[new_y][new_x]][idx] = bridge_table[idx][_map[new_y][new_x]]
                    else:
                        bridge_table[idx][_map[new_y][new_x]] = cnt
                        bridge_table[_map[new_y][new_x]][idx] = cnt

bridge = [] 
for i in range(2, number):
    for j in range(i + 1, number):
        if bridge_table[i][j]:
            bisect.insort(bridge, (bridge_table[i][j], (i - 2, j - 2)))

check = list(range(number - 2))

total = 0
is_right = False
for length, (a, b) in bridge:
    if find(a, check) != find(b, check):
        union(a, b, check)
        total += length

    if len(set([find(i, check) for i in check])) == 1:
        is_right = True
        break

print(total if is_right else -1)