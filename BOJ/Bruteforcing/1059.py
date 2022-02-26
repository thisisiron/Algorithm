import sys
import bisect
input = sys.stdin.readline


L = int(input())
S = [int(x) for x in map(int, input().split())]
n = int(input())

S.sort()
idx = bisect.bisect(S, n)
total = 0
if S[idx - 1] == n:
    print(total)
else:
    if idx == 0:
        mn, mx = 1, S[0] - 1
    elif L == 1 and S[0] < n:
        mn, mx = S[0] + 1, 1000
    else:
        mn, mx = S[idx - 1] + 1, S[idx] - 1
    
    for cur in range(mn, n + 1):
        if cur < n:
            total += (mx - n + 1)
        else:
            total += (mx - cur)
    print(total)