# Time excess method

import sys
input = sys.stdin.readline


def check(s):
    if len(s) <= 1:
        return True
    
    if s[0] == s[-1]:
        return check(s[1:-1])
    else:
        return False


s = input().rstrip()
res = ''

for cut in range(len(s), 0, -1):
    for start in range(len(s)):
        cutted = s[start:start + cut]
        if check(cutted):
            res = len(cutted)
            break
        
        if start + cut >= len(s):
            break
    if res:
        break
print(res)