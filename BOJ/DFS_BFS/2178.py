from collections import deque 


UP: tuple = (1,0)
DOWN: tuple = (-1, 0)
LEFT: tuple = (0, -1)
RIGHT: tuple = (0, 1)


def print_matrix(m):
    for x in m:
        print(x, sep="")
    print()


if __name__ == '__main__':
    n, m = map(int, input().split())
    matrix: list = [[0] * (m + 2) for _ in range(n + 2)]

    for i in range(1, n + 1):
        cols = input()
        for j, col in enumerate(cols, 1):
            matrix[i][j] = int(col)
    
    queue: deque = deque()
    cnt: int = 1
    queue.append([[1, 1], cnt])
    matrix[1][1] = 0
    
    while queue:
        (cur_y, cur_x), cnt = queue.popleft()
        if cur_y == n and cur_x == m:
            break
        for y, x in [UP, DOWN, LEFT, RIGHT]:
            if matrix[cur_y + y][cur_x + x] == 0:
                continue
            else:
                tmp: int = cnt + 1
                queue.append([[cur_y + y, cur_x + x], tmp])
                matrix[cur_y + y][cur_x + x] = 0
        # print_matrix(matrix)
    print(cnt)