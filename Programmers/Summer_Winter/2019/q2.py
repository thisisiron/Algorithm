from collections import deque 


UP: list = [-1, 0]
DOWN: list = [1, 0]
LEFT: list = [0, -1]
RIGHT: list = [0, 1]


def solution(land: list, height: int) -> int:
    answer: int = 0
    num_to_go: int = len(land) * len(land[0]) - 1
    visited: list = [[0] * (len(land[0]) + 2) for _ in range(len(land) + 2)]

    i: int
    j: int
    for i in range(len(visited)):
        for j in range(len(visited[0])):
            if i == 0 or i == len(visited) - 1:
                visited[i][j] = 1
            if j == 0 or j == len(visited[0]) - 1:
                visited[i][j] = 1

    i: int
    for i in range(len(land)):
        land[i] = [0] + land[i] + [0]
    land.insert(0, [0] * len(land[0]))
    land.append([0] * len(land[0]))

    stack: deque = deque()
    stack.append([1,1])
    visited[1][1] = 1

    while num_to_go > 0:
        min_vals: list = [] 
        min_pos: list = []
        while stack:
            y: int
            x: int
            y, x = stack.pop()

            for move_y, move_x in [UP, DOWN, LEFT, RIGHT]:
                if abs(land[y + move_y][x + move_x] - land[y][x]) <= height:
                    if visited[y + move_y][x + move_x] == 0:
                        stack.append([y + move_y, x + move_x])
                        visited[y + move_y][x + move_x] = 1
                        num_to_go -= 1
                else:
                    # if (y == 4 and x == 3) or (y==3 and x == 4):
                    #     import pdb;pdb.set_trace()
                    if visited[y + move_y][x + move_x] == 0:
                        diff: int = abs(land[y + move_y][x + move_x] - land[y][x])
                        min_vals.append(diff)
                        min_pos.append([y + move_y, x + move_x])

        min_val: int = 20000
        next_y: int = 1
        next_x: int = 1
        # print(min_pos)
        # print(min_vals)
        for idx, (min_y, min_x) in enumerate(min_pos):
            if visited[min_y][min_x] == 0:
                if min_val > min_vals[idx]:
                    min_val = min_vals[idx]
                    next_y, next_x = min_y, min_x

        stack.append([next_y, next_x])
        visited[next_y][next_x] = 1
        answer += min_val
        num_to_go -= 1
        print(next_y, next_x)
        print(answer, num_to_go)
        print_land(visited)

    return answer


def print_land(land: list):
    for x in land:
        print(x, sep="")
    print()

if __name__ == '__main__':
    # print(solution([[1, 4, 8, 10], [5, 5, 5, 5], [10, 10, 10, 10], [10, 10, 10, 20]],3))
    print(solution([[10, 11, 10, 11], [2, 21, 20, 10], [1, 20, 21, 11], [2, 1, 2, 1]],1))