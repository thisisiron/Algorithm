# 시저암호
# From: https://programmers.co.kr/learn/courses/30/lessons/12926?language=python3
#


def solution(s, n):
    answer = ''
    for c in s:
        if ' ' == c:
            answer += c
        else:
            if c.islower():
                answer += chr((ord(c) - ord('a') + n) % 26 + ord('a') ) 
            elif c.isupper():
                answer += chr((ord(c) - ord('A') + n) % 26 + ord('A') ) 
                
    return answer
            
# AB	  1    BC
# z	      1    a
# a B z   4	  e F d
print(solution('AB', 1))
print(solution('z', 1))
print(solution('a B z', 4))

# 다른 사람 풀이
import string
def caesar(s, n):
    result = ""
    base = ""
    for c in s:
        if c in string.ascii_lowercase:
            base = string.ascii_lowercase
        elif c in string.ascii_uppercase:
            base = string.ascii_uppercase
        else:
            result += c
            continue
        a = base.index(c) + n
        result += base[a % len(base)]
    return result

print(caesar('AB', 1))
print(caesar('z', 1))
print(caesar('a B z', 4))