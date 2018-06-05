# 야근 지수
# From: https://programmers.co.kr/learn/courses/30/lessons/12927?language=python3
#

# 시간 초과
def solution(n, works):
    if n >= sum(works): return 0
    while n>0:
        works[works.index(max(works))] -= 1
        n = n - 1
    
    return sum([x**2 for x in works])


print(solution(4, [4, 3, 3]))