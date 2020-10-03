# 야근 지수
# From: https://programmers.co.kr/learn/courses/30/lessons/12927?language=python3
#

# 시간 초과
def solution(n, works):
    if n >= sum(works): return 0
    while n>0:
        # sorting을 이용하는 방법은 시간이 오래 걸린다.
        works[works.index(max(works))] -= 1
        n = n - 1
    
    return sum([x**2 for x in works])
    # 계산(ex. +,-*,/)을 이용할 때, map함수를 이용하는 것은 성능이 더 안 좋다.
    # return sum(map(lambda x: x**2, works))

# def solution(n, works):
#     for i in range(n):
#         works[works.index(max(works))] -= 1
#     return sum([x**2 if x>=0 else 0 for x in works])

print(solution(4, [4, 3, 3]))