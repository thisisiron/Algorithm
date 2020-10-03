# 줄 서는 방법
# From: https://programmers.co.kr/learn/courses/30/lessons/12936?language=python3#
#

def solution(n,k):
    answer = []
    x_list = [x for x in range(1,n+1)]

    for _ in range(n):
        f = fact(n)
        answer.append(x_list.pop(int((k-1)//(f/n))))
        n, k = n-1, k % (f/n)
    return answer

def fact(n):
    if n<=1:
        return 1
    else:
        return n * fact(n-1)

# [3,1,2]
print(solution(3,5))
# [1, 3, 2, 4]
print(solution(4,3))