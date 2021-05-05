import sys
input = sys.stdin.readline


N = int(input())
arr = []

for i in range(N):
    arr.append((int(input().rstrip()), i))

arr.sort()

ans = 0
for i in range(N):
    if arr[i][1] - i >= 0:
        if ans < abs(i - arr[i][1]):
            ans = abs(i - arr[i][1])

print(ans + 1)