import sys
input = sys.stdin.readline


N = int(input())
arr = [int(x) for x in input().split()]
arr.sort()

cnt = 0
for i in range(N):
    tmp = arr[:i] + arr[i + 1:]
    left = 0
    right = N - 2 

    while left < right:
        res = tmp[left] + tmp[right]

        if arr[i] > res:
            left += 1
        elif arr[i] < res:
            right -= 1
        else:
            cnt += 1
            break
print(cnt)