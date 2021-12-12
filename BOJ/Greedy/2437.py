import sys
input = sys.stdin.readline


N = int(input())
weights = [int(x) for x in input().split()]
weights.sort()

goal = 1
for w in weights:
    if goal < w:
        break
    goal += w
print(goal)