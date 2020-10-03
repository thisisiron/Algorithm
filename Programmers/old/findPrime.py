#
# From : https://programmers.co.kr/learn/courses/30/lessons/12921?language=python3
#

def solution(n):
    n+=1
    primes = [True] * n
    primes[0], primes[1] = [None] * 2
    for idx, value in enumerate(primes):
        if value == True:
            primes[idx*2::idx] = [False] * ((n-1) // idx -1)
    return primes.count(True)


print(solution(10))
print(solution(5))