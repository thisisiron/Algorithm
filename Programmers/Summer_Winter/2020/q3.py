from collections import deque 


UP = [-1, 0]
DOWN = [1, 0]
LEFT = [0, -1]
RIGHT = [0, 1]


def bfs(land, visited, group, y, x):
    queue: deque = deque()
    queue.append([y, x])
    visited[y][x] = group

    while queue:
        y, x = queue.popleft()
        
        for move_y, move_x in [UP, DOWN, LEFT, RIGHT]:
            if y + move_y >= 0 and y + move_y < len(land) and x + move_x >= 0 and x + move_x < len(land[0]) and \
            abs(land[y][x] - land[y + move_y][x + move_x]) == 0:
                if visited[y + move_y][x + move_x] == 0:
                    visited[y + move_y][x + move_x] = group
                    queue.append([y + move_y, x + move_x])


def solution(v):
    visited = [[0] * len(v[0]) for _ in range(len(v))]

    group = 1
    for i in range(len(v)):
        for j in range(len(v[0])):
            if visited[i][j] == 0:
                bfs(v, visited, group, i, j)
                group += 1
    
    res = {i: set() for i in range(3)} 
    for i in range(len(v)):
        for j in range(len(v[0])):
            res[v[i][j]].add(visited[i][j])
    return [len(res[i]) for i in range(3)] 

print(solution([[0,0,1,1],[1,1,1,1],[2,2,2,1],[0,0,0,2]]))