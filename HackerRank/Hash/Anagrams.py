# Time Limit

def sherlockAndAnagrams(s):
    cnt = 0
    
    for k in range(1, le:w
    n(s)):
        for i in range(len(s) - k):
            for j in range(i + 1, len(s) - k + 1):
                res = comp(s[i:i + k], s[j: j + k])
                if res:
                    cnt += 1
    return cnt
                
from collections import Counter
def comp(s1, s2):
    if len(s1) != len(s2):
        return False
    elif s1 == s2:
        return True
    else:
        s1_cnt = Counter(s1)
        s2_cnt = Counter(s2)
        if s1_cnt == s2_cnt:
            return True
        else:
            return False