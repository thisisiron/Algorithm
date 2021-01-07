import sys
input = sys.stdin.readline


N = int(input())
arrow = {}
for _ in range(N):
    x, y = map(int, input().split())
    d = ''
    if x > 0 and y > 0:
        d = '1'
        a = y / x
        arrow.setdefault((a, d), 0)
        arrow[(a, d)] += 1
    elif x < 0 and y > 0:
        d = '2'
        a = y / x
        arrow.setdefault((a, d), 0)
        arrow[(a, d)] += 1
    elif x < 0 and y < 0:
        d = '3'
        a = y / x
        arrow.setdefault((a, d), 0)
        arrow[(a, d)] += 1
    elif x > 0 and y < 0:
        d = '4'
        a = y / x
        arrow.setdefault((a, d), 0)
        arrow[(a, d)] += 1
    elif x == 0:
        if y > 0:
            d = '+y'
        else:
            d = '-y'
        arrow.setdefault(d, 0)
        arrow[d] += 1
    elif y == 0:
        if x > 0:
            d = '+x'
        else:
            d = '-x'
        arrow.setdefault(d, 0)
        arrow[d] += 1

print(max(arrow.values()))