import sys
input = sys.stdin.readline


N = int(input())
arr = []
for _ in range(N):
    idx, name = input().split()
    arr.append((int(idx), name))

arr.sort(key=lambda x: x[0])

for a in arr:
    print(*a, sep=' ')