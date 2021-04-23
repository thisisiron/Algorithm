import sys
input = sys.stdin.readline


def back(depth):
    if depth == N:
        if check():
            print(*perm)
            exit()
    else:
        for i in range(N): 
            if not visited[i]:
                visited[i] = 1
                perm[depth] = i + 1
                back(depth + 1)
                perm[depth] = 0
                visited[i] = 0
    return False


def check():
    for i in range(N):
        arr[0][i] = perm[i]
    for i in range(1, N):
        for j in range(N - i):
            arr[i][j] = arr[i - 1][j] + arr[i - 1][j + 1]
    if arr[N - 1][0] == F:
        return True
    return False


N, F = map(int, input().split())
visited = [0] * N 
perm = [0] * N
arr = [[0] * N for _ in range(N)]
back(0)