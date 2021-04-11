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
        
        if arr[i] < open_a:
            backtracking(i + 1, cnt + open_a - arr[i], arr[i], open_b)
        elif arr[i] > open_b:
            backtracking(i + 1, cnt + arr[i] - open_b, open_a, arr[i])
        else:
            backtracking(i + 1, cnt + arr[i] - open_a, arr[i], open_b)
            backtracking(i + 1, cnt + open_b - arr[i], open_a, arr[i])


N = int(input())
open_a, open_b = map(int, input().split())
if open_b < open_a:
    open_a, open_b = open_b, open_a

num_used = int(input())
arr = []
for _ in range(num_used):
    arr.append(int(input()))

mn = float('inf')
backtracking(0, 0, open_a, open_b)
print(mn)