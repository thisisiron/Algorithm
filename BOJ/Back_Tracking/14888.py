import sys
input = sys.stdin.readline


def add(x, y):
    return x + y


def minus(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x , y):
    if x < 0:
        return -(-x // y)
    return x // y


OPS = [add, minus, multiply, divide]


def back(idx, cur, ops):
    global mx, mn
    if idx == N:
        if mx < int(cur):
            mx = int(cur)
        if mn > int(cur):
            mn = int(cur)
    else:
        for o, cnt in enumerate(ops):
            if cnt == 0:
                continue
            val = OPS[o](cur, arr[idx])
            ops[o] -= 1
            back(idx + 1, val, ops)
            ops[o] += 1


N = int(input())
arr = [int(x) for x in input().split()]
ops = [int(x) for x in input().split()]

mx = -float('inf')
mn = float('inf')
back(1, arr[0], ops)
print(mx)
print(mn)