# Memory excess method

import sys
input = sys.stdin.readline


s = input().rstrip()

dp =[[0] * len(s) for _ in range(len(s))]

for i in range(len(s)):
    dp[i][i] = 1

for i in range(len(s) - 1):
    if s[i] == s[i + 1]:
        dp[i][i + 1] = 1

for i in range(2, len(s)):
    for j in range(2, i + 1):
        if s[i] == s[i - j] and dp[i - j + 1][i - 1]:
            dp[i - j][i] = 1

mx = 0 
for i in range(len(s) - 1):
    start = i
    end = 0
    for j in range(len(s) - 1, i - 1, -1):
        if dp[i][j]:
            end = j
            break
    mx = max(mx, end - start + 1)
print(mx)