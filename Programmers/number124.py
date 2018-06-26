# 124 나라의 숫자
# From: https://programmers.co.kr/learn/courses/30/lessons/12899?language=python3#
#

def solution(n):
    answer = ''
    while(n>0):
        answer = "124"[(n-1)%3] + answer
        n = (n-1)//3
    return answer

print(solution(1))
print(solution(4))
print(solution(10))