import sys
ipnut = sys.stdin.readline


N = int(input())
pos = []
neg = []
for _ in range(N):
    x = int(input())
    if x <= 0:
        neg.append(x)
    else:
        pos.append(x)

pos.sort(reverse=True)
neg.sort()

total = 0

for i in range(0, len(pos) - 1, 2):
    if pos[i] > 1 and pos[i + 1] > 1:
        total += pos[i] * pos[i + 1]
    else:
        total += pos[i]
        total += pos[i + 1]
if len(pos) % 2 != 0:
    total += pos[len(pos) - 1]

for i in range(0, len(neg) - 1, 2):
    total += neg[i] * neg[i + 1]

if len(neg) % 2 != 0:
    total += neg[len(neg) - 1]

print(total)