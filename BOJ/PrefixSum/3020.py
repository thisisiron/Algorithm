# WRONG ANSWER

import sys
input = sys.stdin.readline


N, H = map(int, input().split())
dp = [0] * H

cnt = {}
for i in range(N):
    h = int(input())

    if i % 2 == 1:
        for j in range(H - 1, H - 1 - h, -1):
            dp[j] += 1
            cnt.setdefault(dp[j], 0)
            cnt[dp[j]] += 1
            if dp[j] - 1 in cnt:
                cnt[dp[j] - 1] -= 1
                if cnt[dp[j] - 1] < 1:
                    del cnt[dp[j] - 1]
    
    else:
        for j in range(h):
            dp[j] += 1
            cnt.setdefault(dp[j], 0)
            cnt[dp[j]] += 1
            if dp[j] - 1 in cnt:
                cnt[dp[j] - 1] -= 1
                if cnt[dp[j] - 1] < 1:
                    del cnt[dp[j] - 1]
mn = min(dp)
print(mn, cnt[mn])