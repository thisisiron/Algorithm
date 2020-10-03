# 다음 큰 숫자
# From: https://programmers.co.kr/learn/courses/30/lessons/12911?language=python3
#

def solution(n):
    num_one = str(bin(n)).count('1')
    for x in range(n+1,1000000):
        if num_one==str(bin(x)).count('1'):
            return x

print(solution(78))

# bin을 활용해서 문제를 해결할 수 있었다.
# bin함수는 주어진 정수를 2진수로 바꿔서 표현한다.