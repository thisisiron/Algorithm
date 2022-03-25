import sys
input = sys.stdin.readline


def back(S, start, k):
    if k == M:
        print(*S, sep=' ')
    else:
        for i in range(start, len(arr)):
            S.append(arr[i])
            back(S, i, k + 1)
            S.pop()


N, M = map(int, input().split())
arr = sorted({int(x) for x in input().split()})

back([], 0, 0)
