import sys
input = sys.stdin.readline


dy = (1, -1, -1, 1)
dx = (-1, -1, 1, 1)


def back(y, x, strength):
    global ans
    if x == M:
        x = 0
        y += 1
    
    if y == N:
        if ans < strength:
            ans = strength
        return

    if not used[y][x]:
        for i in range(4):
            by = y + dy[i]
            bx = x + dx[i]

            if by < 0 or by >= N or bx < 0 or bx >= M:
                continue

            if used[y][x] or used[by][x] or used[y][bx]:
                continue

            used[y][x] = 1
            used[by][x] = 1
            used[y][bx] = 1

            back(y, x + 1, strength + (wood[y][x] * 2) + wood[by][x] + wood[y][bx])
            
            used[y][x] = 0
            used[by][x] = 0
            used[y][bx] = 0

    back(y, x + 1, strength)

N, M = map(int, input().split())
wood = [[int(x) for x in input().split()] for _ in range(N)]
used = [[0] * M for _ in range(N)]
ans = 0
back(0, 0, 0)
print(ans)