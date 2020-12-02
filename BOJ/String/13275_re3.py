# Time excess method

import sys
input = sys.stdin.readline


def palind(s):
    for cut in range(len(s), 1, -1):
        for start in range(len(s)):
            if start + cut > len(s):
                break
            check = True
            for i in range(cut // 2):
                if s[start + i] != s[start + cut - i - 1]:
                    check = False
                    break
            if check:
                return cut 
    return 1


s = input().rstrip()
print(palind(s))