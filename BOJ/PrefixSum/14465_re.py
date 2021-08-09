import sys
input = sys.stdin.readline


N, K, B = map(int, input().split())

lights = [0] * (N + 1)
for _ in range(B):
    lights[int(input())] = 1
mn = sum(lights[1:K + 1])  # 1부터 K까지 합
now = mn
for i in range(1, N - K + 1):
    now -= lights[i] - lights[i + K]
    if now < mn:
        mn = now
print(mn)