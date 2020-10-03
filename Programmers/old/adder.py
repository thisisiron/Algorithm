#
# From : https://programmers.co.kr/learn/courses/30/lessons/12912?language=python3
# 

def solution(a, b):
    answer = 0
    if a>b:
        a, b = b, a
    for i in range(a,b+1):
        answer += i
    return answer

print(solution(5,3))


# 모범 답안
# range와 sum만 이용해서 해결하였다.
# def adder(a, b):
#     if a > b: a, b = b, a
#     return sum(range(a,b+1))