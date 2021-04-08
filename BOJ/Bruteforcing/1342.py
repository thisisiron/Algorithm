import sys
from collections import Counter
from math import factorial
input = sys.stdin.readline


def backtracking(counter, new_S):
    global cnt
    if len(new_S) == len(S):
        cnt += 1
    else:
        for key, val in counter.items():
            if val == 0:
                continue
            if not new_S or new_S[-1] != key:
                counter[key] -= 1
                backtracking(counter, new_S + key)
                counter[key] += 1

S = input().rstrip()
counter = Counter(S)
uniq_len = len(counter)

if len(S) == uniq_len:
    print(factorial(uniq_len))
else:
    cnt = 0
    backtracking(counter, '')
    print(cnt)