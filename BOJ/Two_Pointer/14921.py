import sys
input = sys.stdin.readline


N = int(input())
arr = [int(x) for x in input().split()]

left, right = 0, N - 1
mn = arr[-2] + arr[-1]
ans = mn
while left < right:
    res = arr[left] + arr[right]

    if abs(res) < mn:
        mn = abs(res)
        ans = res 

    if res < 0:
        left += 1
    elif res > 0:
        right -= 1
    else:
        break

print(ans)