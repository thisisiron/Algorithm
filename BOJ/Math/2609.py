import sys
input = sys.stdin.readline


def gcd(x, y):
    while x % y != 0:
        tmp = x % y
        x = y
        y = tmp
    return y


a, b = map(int, input().split())
c = gcd(a, b)
print(c)
print(int((a/c) * (b/c) * c))