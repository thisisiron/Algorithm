import sys
input = sys.stdin.readline


N, C = map(int, input().split())
arr = []
for _ in range(N):
    arr.append(int(input().rstrip()))
arr.sort()

left = 1
right = arr[-1] - arr[0]
ans = 0

while left <= right:
    mid = (left + right) // 2
    start = arr[0]
    cnt = 1

    for i in range(1, N):
        d = arr[i] - start
        if mid <= d:
            cnt += 1
            start = arr[i]
    
    if cnt >= C:
        ans = mid
        left = mid + 1
    else:
        right = mid - 1
print(ans)