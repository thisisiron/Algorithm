import sys
input = sys.stdin.readline


def backtracking(a, pre_cur, cnt):
    global move

    mx, mn = -1, 1100

    if cnt > move:
        return
    if a > ord('z'):
        if cnt < move:
            move = cnt
        return

    mx = alpha[a - 97][0]
    mn = alpha[a - 97][1]

    if mx == mn:
        backtracking(a + 1, mx, cnt + abs(pre_cur - mn) + abs(mx - mn))
    elif mx != -1:
        backtracking(a + 1, mx, cnt + abs(pre_cur - mn) + abs(mx - mn))
        backtracking(a + 1, mn, cnt + abs(pre_cur - mx) + abs(mx - mn))
    else:
        backtracking(a + 1, pre_cur, cnt)


move = float('inf') 
S = input().rstrip()
N = len(S)

alpha = [[0, 0] for _ in range(26)]

for i in range(26):
    mx, mn = -1, 1100
    for j in range(N):
        if S[j] == chr(97 + i):
            mx = j if mx < j else mx
            mn = j if mn > j else mn
    alpha[i][0] = mx
    alpha[i][1] = mn

backtracking(ord('a'), 0, 0)
move += N
print(move)