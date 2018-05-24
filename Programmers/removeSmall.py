#
# From : https://programmers.co.kr/learn/challenge_codes/121
#

def rm_small(mylist):
    # 함수를 완성하세요
    mylist = [x for x in mylist if min(mylist)!=x]

    return mylist


# 아래는 테스트로 출력해 보기 위한 코드입니다.
my_list = [10, 8, 22]
print("결과 {} ".format(rm_small(my_list)))


# sort와 sorted의 차이
# sort는 값을 반환하지 않음.
# sorted는 값을 반환함. (원본은 sorting 되어있지않음.)