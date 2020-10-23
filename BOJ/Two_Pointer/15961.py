import sys 
input = sys.stdin.readline


N, d, k, c = map(int, input().split())
arr = [int(input()) for _ in range(N)]

counts = [0] * (d + 1)
counts[c] += 1

tmp = 1
for i in range(k):
    if counts[arr[i]] < 1:
        tmp += 1
    counts[arr[i]] += 1

mx = tmp
for i in list(range(k, N)) + list(range(k - 1)):
    counts[arr[i - k]] -= 1
    if counts[arr[i - k]] < 1:
        tmp -= 1
    
    counts[arr[i]] += 1
    if counts[arr[i]] < 2:
        tmp += 1
    mx = max(mx, tmp)

print(mx)