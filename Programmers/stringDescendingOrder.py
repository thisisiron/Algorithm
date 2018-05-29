#
# From : https://programmers.co.kr/learn/courses/30/lessons/12917?language=python3
#

def solution(s):
    return "".join(sorted(list(s), reverse=True))

print(solution("Zbcdefg"))