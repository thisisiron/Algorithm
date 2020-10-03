#
# From : https://programmers.co.kr/learn/challenge_codes/5/solutions
#

def fibonacci(num):
    answer = 0
    a=0
    b=1
    for i in range(num-1):
        answer = a + b
        a = b
        b = answer
    return answer

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(fibonacci(3))

# 모범답안
#
# def fibonacci(num):
#     a, b = 0, 1
#     for i in range(num):
#         a, b = b, a+b
#     return a

# # 아래는 테스트로 출력해 보기 위한 코드입니다.
# print(fibonacci(3))