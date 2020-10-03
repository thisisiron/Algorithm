# 약수의 합
# From : https://programmers.co.kr/learn/courses/30/lessons/12928?language=python3
# 


def solution(n):
    return sum([i for i in range(1,n+1) if n%i==0])

print(solution(12))

# 모범 답안
# def sumDivisor(num):
#     # num / 2 의 수들만 검사하면 성능 약 2배 향상
#     return num + sum([i for i in range(1, (num // 2) + 1) if num % i == 0])