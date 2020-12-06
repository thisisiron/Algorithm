import sys
input = sys.stdin.readline


N = int(input())
arr = list(map(int, input().split()))

ans = []
i = len(arr)
for a in arr[::-1]:
    ans.insert(a, i)
    i -= 1
print(*ans)