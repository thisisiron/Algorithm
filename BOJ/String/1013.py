import sys
import re
input = sys.stdin.readline


T = int(input())
for _ in range(T):
    s = input().rstrip()
    vega = re.compile('(100+1+|01)+')
    res = vega.fullmatch(s)
    print('YES' if res is not None else 'NO')