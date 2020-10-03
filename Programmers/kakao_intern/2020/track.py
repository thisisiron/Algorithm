from collections import deque

UP: list = [-1, 0]
DOWN: list = [1, 0]
LEFT: list = [0, -1]
RIGHT: list = [0, 1]


def solution(board: list) -> int:
    answer: list = [] 

    queue: deque = deque()
    cost: int = 100 
    visited: list = [[0] * len(board[0]) for _ in range(len(board))]
    visited[0][0] = 1 
    visited[0][1] = 100 
    queue.append([[0, 1], RIGHT, cost])
    bfs(queue, visited, board, answer)

    queue: deque = deque()
    cost: int = 100 
    visited: list = [[0] * len(board[0]) for _ in range(len(board))]
    visited[0][0] = 1 
    visited[1][0] = 100 
    queue.append([[1, 0], DOWN, cost])
    bfs(queue, visited, board, answer)

    return min(answer)


def bfs(queue: deque, visited: list, board: list, answer: list):
    while queue:
        cur_y: int
        cur_x: int
        direction: list
        (cur_y, cur_x), direction, cost = queue.popleft()

        if cur_y == len(board) - 1 and cur_x == len(board[0]) - 1:
            answer.append(cost)
            continue

        move_y: int
        move_x: int
        for move_y, move_x in [UP, DOWN, LEFT, RIGHT]:
            next_y: int = cur_y + move_y
            next_x: int = cur_x + move_x

            if not (0 <= next_y < len(board) and 0 <= next_x < len(board[0])):
                continue

            if board[next_y][next_x] == 0:
                next_cost: int = cal_cost(direction, [move_y, move_x], cost)
                # print(cur_y, cur_x, '->', next_y, next_x, ':', next_cost, '|',direction, [move_y, move_x])
                if visited[next_y][next_x] > next_cost or not visited[next_y][next_x]:
                    visited[next_y][next_x] = next_cost 
                    # print_board(visited)
                    queue.append([[next_y, next_x], [move_y, move_x], next_cost])


def cal_cost(cur_dir: list, next_dir: list, cost) -> int:
    if (cur_dir == UP or cur_dir == DOWN) and (next_dir == UP or next_dir == DOWN):
        return cost + 100
    elif (cur_dir == UP or cur_dir == DOWN) and (next_dir == LEFT or next_dir == RIGHT):
        return cost + 600
    elif (cur_dir == LEFT or cur_dir == RIGHT) and (next_dir == LEFT or next_dir == RIGHT):
        return cost + 100
    elif (cur_dir == LEFT or cur_dir == RIGHT) and (next_dir == UP or next_dir == DOWN):
        return cost + 600


def print_board(board: list):
    for x in board:
        print(x, sep="")
    print()


if __name__ == '__main__':
    # print(solution([[0,0,0],[0,0,0],[0,0,0]]))
    print(solution([[0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0],[0,0,0,0,0,1,0,0],[0,0,0,0,1,0,0,0],[0,0,0,1,0,0,0,1],[0,0,1,0,0,0,1,0],[0,1,0,0,0,1,0,0],[1,0,0,0,0,0,0,0]]))