#
# From : https://programmers.co.kr/learn/challenge_codes/102
#

def printTriangle(num):
    #함수를 완성하세요
    s = ""
    for i in range(1, num+1):
        s += ('*' * int(i) + '\n')
    return s

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print( printTriangle(3) )
