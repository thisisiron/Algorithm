# 콜라츠 추측
# From : https://programmers.co.kr/learn/courses/30/lessons/12943?language=python3
#


def solution(num):
    for i in range(500):
        if num == 1:
            return i
        elif num%2==0:
            num /= 2
        elif num%2==1:
            num = num*3 + 1
    return -1

# Answer : 8
print(solution(6))
