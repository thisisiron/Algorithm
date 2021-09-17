import sys
input = sys.stdin.readline


def back(lotto, start):
    if len(lotto) == 6:
        print(*lotto)
    else:
        for i in range(start, N):
            lotto.append(arr[i])
            back(lotto, i + 1)
            lotto.pop()


while True:
    N, *arr = list(map(int, input().split()))
    if N == 0:
        break
    back([], 0)
    print()