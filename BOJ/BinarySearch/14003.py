import sys
import bisect
input = sys.stdin.readline


N = int(input())
nums = list(map(int, input().split()))
pos = [0] * N

ans = []

for i in range(N):
    x = nums[i]
    index = bisect.bisect_left(ans, x)
    if index == len(ans):
        ans.append(x)
    else:
        ans[index] = x
    pos[i] = index

print(len(ans))

lis = []
cur = len(ans) - 1
for i in range(N - 1, -1, -1):
    if pos[i] == cur:
        lis.append(nums[i])
        cur -= 1
        
        if cur < 0:
            break

print(*reversed(lis))
