import sys
input = sys.stdin.readline


def backtracking(y):
    global cnt
    if y == N:
        cnt += 1
    else:
        for x in range(N):
            if not row[x] and not diag1[y + x] and not diag2[y - x + N - 1]:
                row[x] = diag1[y + x] = diag2[y - x + N - 1] = 1
                backtracking(y + 1)
                row[x] = diag1[y + x] = diag2[y - x + N - 1] = 0
    

N = int(input())
row, diag1, diag2 = [0] * N, [0] * (2 * N - 1), [0] * (2 * N - 1)
cnt = 0
backtracking(0)
print(cnt)