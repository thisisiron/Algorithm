from collections import deque


UP: list = [-1, 0]
DOWN: list = [1, 0]
LEFT: list = [0, -1]
RIGHT: list = [0, 1]


def solution(board: list) -> int:
    answer: list = [] 

    bfs(board,'R', answer)
    bfs(board,'D', answer)

    return min(answer)


def bfs(board: list, direction: str, answer: list):
    queue: deque = deque()
    cost: int = 0
    visited: list = [[0] * len(board[0]) for _ in range(len(board))]
    queue.append([[0, 0], direction, cost])

    while queue:
        (cur_y, cur_x), direction, cost = queue.popleft()

        if cur_y == len(board) - 1 and cur_x == len(board[0]) - 1:
            answer.append(cost)
            continue

        for move_y, move_x in [UP, DOWN, LEFT, RIGHT]:
            next_y: int = cur_y + move_y
            next_x: int = cur_x + move_x

            if not (0 <= next_y < len(board) and 0 <= next_x < len(board[0])):
                continue

            if board[next_y][next_x] == 0:
                next_direction: str = pos2dir([move_y, move_x])
                next_cost: int = cal_cost(direction, next_direction, cost)
                if not visited[next_y][next_x] or visited[next_y][next_x] > next_cost: 
                    visited[next_y][next_x] = next_cost
                    queue.append([[next_y, next_x], next_direction, next_cost])


def cal_cost(cur_dir: str, next_dir: str, cost) -> int:
    if (cur_dir == 'U' or cur_dir == 'D') and (next_dir == 'U' or next_dir == 'D'):
        return cost + 100
    elif (cur_dir == 'U' or cur_dir == 'D') and (next_dir == 'L' or next_dir == 'R'):
        return cost + 600
    elif (cur_dir == 'L' or cur_dir == 'R') and (next_dir == 'L' or next_dir == 'R'):
        return cost + 100
    elif (cur_dir == 'L' or cur_dir == 'R') and (next_dir == 'U' or next_dir == 'D'):
        return cost + 600
    

def pos2dir(direction: list) -> str:
    if direction == UP:
        return 'U' 
    elif direction == DOWN:
        return 'D'
    elif direction == LEFT:
        return 'L'
    elif direction == RIGHT:
        return 'R'


def print_board(board: list):
    for x in board:
        print(x, sep="")
    print()


if __name__ == '__main__':
    print(solution([[0,0,0],[0,0,0],[0,0,0]]))
    print(solution([[0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0],[0,0,0,0,0,1,0,0],[0,0,0,0,1,0,0,0],[0,0,0,1,0,0,0,1],[0,0,1,0,0,0,1,0],[0,1,0,0,0,1,0,0],[1,0,0,0,0,0,0,0]]))