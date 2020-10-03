#
# From : https://programmers.co.kr/learn/challenge_codes/83
#

def string_middle(str):
    # 함수를 완성하세요
    middle = int(len(str)/2)
    if len(str) % 2 == 1:
        return str[middle]
    else:
        return str[middle-1] + str[middle] 


# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(string_middle("power"))


# 모범 답안
#
# def string_middle(str):
#     # 함수를 완성하세요
#     return(str[(len(str)-1)//2 : len(str)//2 + 1])

# # 아래는 테스트로 출력해 보기 위한 코드입니다.
# print(string_middle("test"))