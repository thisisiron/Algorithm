import sys
ipnut = sys.stdin.readline


N, K, B = map(int, input().split())

lights = [1] * (N + 1)
for i in range(B):
    lights[int(input())] = 0

prefix = [0] * (N + 1)
for i in range(1, N + 1):
    prefix[i] = prefix[i - 1]
    prefix[i] += lights[i]

mx = 0
for i in range(K, N + 1):
    if mx < prefix[i] - prefix[i - K]:
        mx = prefix[i] - prefix[i - K]

print(K - mx)