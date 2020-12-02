import sys
import re
input = sys.stdin.readline


s1 = input().rstrip()
s2 = input().rstrip()

res = re.findall(s2, s1)
print(len(res))