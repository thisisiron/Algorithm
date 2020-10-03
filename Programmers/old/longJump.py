# 멀리 뛰기
# From: https://programmers.co.kr/learn/courses/30/lessons/12914?language=python3#
#


def solution(n):
    a=0
    b=1
    for i in range(n):
        a,b=b,a+b
    return b%1234567

print(solution(5))

# 피보나치 개념을 사용하여 해결하는 문제이다.
# 문제에서 "1234567를 나눈 나머지를 리턴하는 함수, solution을 완성하세요."
# 문장을 제대로 확인하지 않아 오래 걸림.