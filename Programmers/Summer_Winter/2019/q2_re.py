from collections import deque 
from collections import defaultdict
import math


UP: list = [-1, 0]
DOWN: list = [1, 0]
LEFT: list = [0, -1]
RIGHT: list = [0, 1]


def find(x: int, groups: dict):
    if x == groups[x]:
        return x
    else:
        p = find(groups[x], groups)
        groups[x] = p
        return p


def union_find(x: int, y: int, groups: dict):
    x = find(x, groups)
    y = find(y, groups)
    if x != y:
        groups[y] = x


def bfs(land: list, visited: list, height: int, group: int, y: int, x: int):
    queue: deque = deque()
    queue.append([y, x])
    visited[y][x] = group

    while queue:
        y, x = queue.popleft()
        
        for move_y, move_x in [UP, DOWN, LEFT, RIGHT]:
            if y + move_y >= 0 and y + move_y < len(land) and x + move_x >= 0 and x + move_x < len(land[0]) and \
            abs(land[y][x] - land[y + move_y][x + move_x]) <= height:
                if visited[y + move_y][x + move_x] == 0:
                    visited[y + move_y][x + move_x] = group
                    queue.append([y + move_y, x + move_x])


def solution(land: list, height: int) -> int:
    answer: int = 0

    visited: list = [[0] * len(land[0]) for _ in range(len(land))]

    group: int = 1
    i: int
    j: int
    for i in range(len(land)):
        for j in range(len(land[0])):
            if visited[i][j] == 0:
                bfs(land, visited, height, group, i, j)
                group += 1

    min_dist: dict = defaultdict(lambda: math.inf) 
    for i in range(len(visited)):
        for j in range(len(visited[0])):
            if j + 1 < len(visited[0]) and visited[i][j] != visited[i][j + 1]:
                a: int = min(visited[i][j], visited[i][j + 1])
                b: int = max(visited[i][j], visited[i][j + 1])
                min_dist[(a, b)] = min(min_dist[(a, b)], abs(land[i][j] - land[i][j + 1]))
        
            if i + 1 < len(visited) and visited[i][j] != visited[i + 1][j]:
                a: int = min(visited[i][j], visited[i + 1][j])
                b: int = max(visited[i][j], visited[i + 1][j])
                min_dist[(a, b)] = min(min_dist[(a, b)], abs(land[i][j] - land[i + 1][j]))
    
    groups: dict = {i: i for i in range(1, group)}
    for a, b in sorted(min_dist, key=min_dist.get):
        if find(a, groups) != find(b, groups):
            union_find(a, b, groups)
            answer += min_dist[(a, b)]

    return answer


def print_land(land: list):
    for x in land:
        print(x, sep="")
    print()

if __name__ == '__main__':
    print(solution([[1, 4, 8, 10], [5, 5, 5, 5], [10, 10, 10, 10], [10, 10, 10, 20]],3))
    print(solution([[10, 11, 10, 11], [2, 21, 20, 10], [1, 20, 21, 11], [2, 1, 2, 1]],1))