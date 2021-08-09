import sys
input = sys.stdin.readline

cows = [[] for _ in range(26)]
for i, x in enumerate(input().rstrip()):
    cows[ord(x) - 65].append(i)

cnt = 0
prev = cows[0][1]
for i in range(26):
    s, e = cows[i]
    for j in range(i + 1, 26):
        s2, e2 = cows[j]
        if s < s2 < e < e2:
            cnt += 1
        elif s2 < s < e2 < e:
            cnt += 1

print(cnt)
