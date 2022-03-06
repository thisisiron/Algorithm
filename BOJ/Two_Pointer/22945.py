import sys
input = sys.stdin.readline


N = int(input())
D = [int(x) for x in input().split()]

left, right = 0, N - 1
ans = 0

while left + 1 < right:
    res = (right - left - 1) * min(D[left], D[right])
    if ans < res:
        ans = res
    
    if D[left] < D[right]:
        left += 1
    else:
        right -= 1

print(ans)