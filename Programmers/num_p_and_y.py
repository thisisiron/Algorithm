#
# https://programmers.co.kr/learn/courses/30/lessons/12916?language=python3
#


def solution(s):
    p = len([x for x in s if x=='p' or x=='P'])
    y = len([x for x in s if x=='y' or x=="Y"])
    return p==y

print(solution("Hello Python"))

# 모범 답안
# count 함수를 활용해서 문제를 해결하였다.
# lower을 이용해서 모두 소문자로 만들었다.
# def numPY(s):
#     return s.lower().count('p') == s.lower().count('y')