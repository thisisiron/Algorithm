from collections import deque


def solution(maps: list) -> int:
    N: int = len(maps)
    M: int = len(maps[0])

    queue: deque = deque()
    cnt: int = 1
    queue.append((0, 0, cnt))

    while queue:
        y, x, cnt = queue.popleft()

        if y == N - 1 and x == M - 1:
            return cnt

        maps[y][x] = 0

        for move_y, move_x in zip((-1, 1, 0, 0), (0, 0, -1, 1)):
            next_y: int = y + move_y
            next_x: int = x + move_x

            if not (0 <= next_y < N and 0 <= next_x < M):
                continue

            if maps[next_y][next_x] == 1:
                maps[next_y][next_x] = 0
                queue.append((next_y, next_x, cnt + 1))
        
    return -1


def print_maps(maps: list):
    for x in maps:
        print(x, sep=" ")
    print()


if __name__ == '__main__':
    print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]))
    print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]]))
    print(solution([[1,1],[1,1]]))
    print(solution([[1,1],[1,1],[0,1]]))