# 정수 제곱근 판별
# From : https://programmers.co.kr/learn/courses/30/lessons/12934?language=python3
#

def solution(n):
    if (n**0.5).is_integer():
        return (int(n**0.5)+1)**2
    else:
        return -1

# is_integer 함수를 통해서 정수인지 아닌지 판별하였다.
print(solution(3))
print(solution(121))