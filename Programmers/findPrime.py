#
# From : https://programmers.co.kr/learn/courses/30/lessons/12921?language=python3
#

def solution(n):
    n+=1
    primes = [True] * n
    primes[0], primes[1] = [None] * 2

    for i, value in enumerate(primes):
        if value==True and i>n**0.5:
            primes[i] = True
        if value==True:
            primes[i*2::i] = [False] * ((n-1)//i -1)
            len([False] * ((n-1)//i))
    
    return primes.count(True)


print(solution(10))
print(solution(5))