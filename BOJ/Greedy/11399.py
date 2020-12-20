import sys
from itertools import accumulate
input = sys.stdin.readline


N = int(input())

atm = [(p, i) for i, p in enumerate(map(int, input().split()))]
atm.sort(key=lambda x: x[0])

money = accumulate([x[0] for x in atm])
print(sum(money))