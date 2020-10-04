import sys
input = sys.stdin.readline

h, m = map(int, input().split())

if m >= 45:
    print(h, m - 45)
else:
    print(h - 1 if h - 1 >= 0 else 23, m + 15)