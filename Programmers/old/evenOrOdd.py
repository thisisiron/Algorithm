#
# From : https://programmers.co.kr/learn/challenge_codes/124
#

def evenOrOdd(num):
    #함수를 완성하세요
    if num%2==1:
        return "Odd"
    else:
        return "Even"


#아래는 테스트로 출력해 보기 위한 코드입니다.
print("결과 : " + evenOrOdd(3))
print("결과 : " + evenOrOdd(2))


# 모범 답안
#
# def evenOrOdd(num):
#     return num % 2 and "Odd" or "Even"

# #아래는 테스트로 출력해 보기 위한 코드입니다.
# print("결과 : " + evenOrOdd(3))
# print("결과 : " + evenOrOdd(2))