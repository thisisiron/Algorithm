import sys 
from math import inf
input = sys.stdin.readline


N = int(input())
arr = list(map(int, input().split()))
arr.sort()

start = 0
left = 1
right = N - 1
ans = [0, 0, 0]
mn = inf 

while True:
    if start == N - 3:
        break
    if left == right:
        start += 1
        left = start + 1
        right = N - 1
    
    result = arr[start] + arr[left] + arr[right]

    if abs(result) < mn:
        mn = abs(result)
        ans[0] = arr[start]
        ans[1] = arr[left]
        ans[2] = arr[right]
        if mn == 0:
            break

    if result < 0:
        left += 1
    elif result > 0:
        right -= 1
    else:
        left += 1
        right -= 1
    
print(*ans)