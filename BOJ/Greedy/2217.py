import sys
input = sys.stdin.readline


N = int(input())
L = []
for _ in range(N):
    L.append(int(input()))

L.sort(reverse=True)

mx = 0 
for i in range(1, len(L) + 1):
    mx = max(mx, i * L[i - 1])

print(mx)