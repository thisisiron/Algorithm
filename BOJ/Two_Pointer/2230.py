import sys
input = sys.stdin.readline


N, M = map(int, input().split())
arr = [int(input()) for _ in range(N)]
arr.sort()

left = 0
right = 0
mn = 2000000000
while left <= right and right < N:
    res = arr[right] - arr[left]
    if res >= M:
        if mn > res:
            mn = res
        left += 1
    else:
        right += 1
    
print(mn)