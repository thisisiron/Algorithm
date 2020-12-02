import sys
input = sys.stdin.readline


s = input().rstrip()
new_s = '#'
for c in s:
    new_s += c
    new_s += '#'

pal = [0] * len(new_s)
center = 0
right = 0

for i in range(len(new_s)):
    left = 2 * center - i
    if i < right:
        pal[i] = min(right - i, pal[left])
    while i - pal[i] > 0 and i + pal[i]  + 1 < len(new_s) and new_s[i - pal[i] - 1] == new_s[i + pal[i] + 1]:
        pal[i] += 1
    if pal[i] + i > right:
        right = pal[i] + i
        center = i

res = 0
for i in range(len(new_s)):
    cur = pal[i]
    if i % 2 == 0 and pal[i] % 2 == 1:
        cur += 1
    res = max(res, cur)
print(res)