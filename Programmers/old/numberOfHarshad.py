# 하샤드 수
# From : https://programmers.co.kr/learn/courses/30/lessons/12947?language=python3
#

def solution(x):
    if x % sum([int(a) for a in str(x)])==0:
        return True
    return False


print(solution(11))
print(solution(10))