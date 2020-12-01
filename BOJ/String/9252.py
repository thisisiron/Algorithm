import sys
input = sys.stdin.readline


s1 = input().rstrip()
s2 = input().rstrip()

dp = [[0] * (len(s1) + 1) for _ in range(len(s2) + 1)]

for i in range(1, len(s2) + 1):
    for j in range(1, len(s1) + 1):
        if s2[i - 1] == s1[j - 1]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

print(dp[-1][-1])

mx = dp[-1][-1]
j_start = len(s1)
ans = ''

for i in range(len(s2), -1, -1):
    for j in range(j_start, -1, -1):
        if dp[i - 1][j - 1] < mx and dp[i - 1][j] < mx and dp[i][j - 1] < mx and dp[i][j] == mx:
            mx -= 1
            ans += s2[i - 1]
            j_start = j
            break

print(ans[::-1])