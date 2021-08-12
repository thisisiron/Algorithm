import sys
input = sys.stdin.readline


n, m = map(int, input().split())
days = list(map(int, input().split()))

left = 0
right = m

cur = sum(days[:m])
mx = cur
while left < right < n:
    cur -= days[left]
    cur += days[right]
    if mx < cur:
        mx = cur
    left += 1
    right += 1
print(mx)