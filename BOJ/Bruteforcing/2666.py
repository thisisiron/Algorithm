import sys
input = sys.stdin.readline


def backtracking(i, cnt, open_a, open_b):
    global mn
    if i == num_used:
        if cnt < mn:
            mn = cnt
    else:
        if arr[i] == open_b or arr[i] == open_a:
            backtracking(i + 1, cnt, open_a, open_b)
        else:
            diff_a = abs(arr[i] - open_a)
            diff_b = abs(arr[i] - open_b)

            backtracking(i + 1, cnt + diff_a, arr[i], open_b)
            backtracking(i + 1, cnt + diff_b, open_a, arr[i])


N = int(input())
open_a, open_b = map(int, input().split())

num_used = int(input())
arr = []
for _ in range(num_used):
    arr.append(int(input()))

mn = float('inf')
backtracking(0, 0, open_a, open_b)
print(mn)