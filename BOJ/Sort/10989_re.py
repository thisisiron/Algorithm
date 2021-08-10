import sys
import itertools
from collections import Counter
input = sys.stdin.readline


N = int(input())
a = Counter(int(input()) for _ in range(N))

for i in range(10001):
    if a[i] != 0:
        for _ in range(a[i]):
            print(i)
