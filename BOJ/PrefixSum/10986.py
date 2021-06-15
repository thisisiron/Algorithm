import sys
input = sys.stdin.readline


N, M = map(int, input().split())
arr = [0] * 1000001

total_sum = 0
for x in input().split():
    total_sum += int(x)
    arr[total_sum % M] += 1

ans = arr[0]
for i in range(M):
    ans += (arr[i] * (arr[i] -  1)) // 2

print(ans)