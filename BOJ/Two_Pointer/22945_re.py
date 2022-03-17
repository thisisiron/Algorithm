import sys
input = sys.stdin.readline


N = int(input())
arr = [int(x) for x in input().split()]
ans = 0
left, right = 0, N - 1

while left + 1 < right:

    res = 0
    num = right - left - 1
    if arr[left] < arr[right]:
        res = arr[left] * num
        left += 1
    else:
        res = arr[right] * num
        right -= 1

    if ans < res:
        ans = res
print(ans)