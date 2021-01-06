import sys
input = sys.stdin.readline


N = int(input())
booked = []
for _ in range(N):
    s, e = map(int, input().split())
    booked.append([s, e])

booked.sort(key=lambda x: (x[1], x[0]))

decision = [booked[0]]
prev = booked[0][1]
for s, e in booked[1:]:
    if prev > s:
        continue
    decision.append([s, e])
    prev = e

print(len(decision))