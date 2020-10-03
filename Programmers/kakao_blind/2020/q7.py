from collections import deque

UP = (-1, 0)
LEFT = (0, -1) 
DOWN = (1, 0)
RIGHT = (0, 1) 


def solution(board: list):
    new_board = [[1] * len(board[0])] + board + [[1] * len(board[0])]
    for i in range(len(new_board)):
        new_board[i] = [1] + new_board[i] + [1] 

    # print_board(new_board)

    answer: int = 0
    dron_pos: list = [1, 1, RIGHT]  # (y, x)

    queue = deque()
    visited = []
    queue.append([dron_pos, 0])
    visited.append(dron_pos)

    while len(queue) != 0:
        dron, dist = queue.popleft()
        dist += 1

        for m in move(dron, new_board):
            if (len(board), len(board)) in ((m[0], m[1]), (m[0] + m[2][0], m[1] + m[2][1])):
                return dist
            
            if not m in visited:
                queue.append([m, dist])
                visited.append(m)

    return 0 


def move(dron, board):
    move = [UP, RIGHT, DOWN, LEFT]
    result = []
    for m in move:
        if board[dron[0] + m[0]][dron[1] + m[1]] == 0 and \
           board[dron[0] + m[0] + dron[2][0]][dron[1] + m[1] + dron[2][1]] == 0:
           result.append([dron[0] + m[0], dron[1] + m[1], dron[2]])
           
    rotate = [1, -1]
    if dron[2] in (LEFT, RIGHT):
        for r in rotate:
            if board[dron[0] + r][dron[1]] == 0 and board[dron[0] + r + dron[2][0]][dron[1] + dron[2][1]] == 0:
                if r == 1:
                    result.append([dron[0], dron[1], DOWN])
                    result.append([dron[0], dron[1] + dron[2][1], DOWN])
                elif r == -1:
                    result.append([dron[0], dron[1], UP])
                    result.append([dron[0], dron[1] + dron[2][1], UP])
    else:
        for r in rotate:
            if board[dron[0]][dron[1] + r] == 0 and board[dron[0] + dron[2][0]][dron[1] + r + dron[2][1]] == 0:
                if r == 1:
                    result.append([dron[0], dron[1], RIGHT])
                    result.append([dron[0] + dron[2][0], dron[1], RIGHT])
                elif r == -1:
                    result.append([dron[0], dron[1], LEFT])
                    result.append([dron[0] + dron[2][0], dron[1], LEFT])

    return result


def print_board(board: list):
    for x in board:
        print(x, sep=" ")
    print()


if __name__ == '__main__':
    print(solution([[0, 0, 0, 1, 1],[0, 0, 0, 1, 0],[0, 1, 0, 1, 1],[1, 1, 0, 0, 1],[0, 0, 0, 0, 0]]))