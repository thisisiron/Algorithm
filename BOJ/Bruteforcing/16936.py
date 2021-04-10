import sys
from collections import Counter
input = sys.stdin.readline


def backtracking(arr, counter):
    if len(arr) == N:
        print(*arr)
        exit()
    else:
        two_mul = arr[-1] * 2
        three_div, check = divmod(arr[-1], 3)
        if counter[two_mul]:
            counter[two_mul] -= 1
            arr.append(two_mul)
            backtracking(arr, counter)
            counter[two_mul] += 1
            arr.pop()
        elif not check and counter[three_div]:
            counter[three_div] -= 1
            arr.append(three_div)
            backtracking(arr, counter)
            counter[three_div] += 1
            arr.pop()


N = int(input())
B = [int(x) for x in input().split()]
counter = Counter(B)
for i in range(N):
    backtracking([B[i]], counter)