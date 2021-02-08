import sys
input = sys.stdin.readline


N, H = map(int, input().split())
up = [0] * (H + 1)
down = [0] * (H + 1)

for i in range(N):
    if i % 2:
        up[int(input())] += 1
    else:
        down[H - int(input()) + 1] += 1

for i in range(H - 1, 0, -1):
    up[i] += up[i + 1]

for i in range(2, H + 1):
    down[i] += down[i - 1]

total = [0] * (H + 1)
mn = N
cnt = 0
for i in range(1, H + 1):
    total[i] = up[i] + down[i]
    if mn > total[i]:
        mn = total[i]
        cnt = 1
    elif mn == total[i]:
        cnt += 1
print(mn, cnt)
