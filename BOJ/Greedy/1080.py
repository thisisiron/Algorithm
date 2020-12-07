import sys
input = sys.stdin.readline


def flip(r_start, c_start):
    for i in range(r_start, r_start + 3):
        for j in range(c_start, c_start + 3):
            A[i][j] = 1 - A[i][j]


N, M = map(int, input().split())
A = [[int(x) for x in input().rstrip()] for _ in range(N)]
B = [[int(x) for x in input().rstrip()] for _ in range(N)]

cnt = 0 
for i in range(N - 2):
    for j in range(M - 2):
        if A[i][j] != B[i][j]:
            flip(i, j)
            cnt += 1

flag = True
for A_row, B_row in zip(A, B):
    for a, b in zip(A_row, B_row):
        if a != b:
            flag = False

print(cnt if flag else -1)