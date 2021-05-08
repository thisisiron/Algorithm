import sys
input = sys.stdin.readline


D, N = map(int, input().split())
oven = []
for x in map(int, input().split()):
    if len(oven) > 0:
        if oven[-1] > x:
            oven.append(x)
        else:
            oven.append(oven[-1])
    else:
        oven.append(x)
pizza = [int(x) for x in input().split()]

ans = 0
j = 0
for i in range(D - 1, -1, -1):
    if oven[i] < pizza[j]:
        continue

    j += 1
    if j == N:
        ans = i
        break

if j == N:
    print(ans + 1)
else:
    print(0)