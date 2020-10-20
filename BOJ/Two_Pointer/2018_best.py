import sys 
input = sys.stdin.readline


N = int(input())
cnt = 0

for i in range(1, N + 1):
    s = i * (i + 1) // 2
    if s > N:
        break
    if (N - s) % i == 0:
        cnt += 1

print(cnt)