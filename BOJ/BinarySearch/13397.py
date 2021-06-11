import sys
input = sys.stdin.readline


def split(x):
    mx = mn = arr[0]
    cnt = 1
    for i in range(1, N):
        if mx < arr[i]:
            mx = arr[i]
        
        if mn > arr[i]:
            mn = arr[i]
        
        if mx - mn > x:
            cnt += 1
            mx = arr[i]
            mn = arr[i]
    return cnt


N, M = map(int, input().split())
arr = [int(x) for x in input().split()]

left, right = 0, max(arr)
ans = 0
while left <= right:
    mid = (left + right) // 2
    if split(mid) <= M:
        right = mid - 1
        ans = mid
    else:
        left = mid + 1

print(ans)